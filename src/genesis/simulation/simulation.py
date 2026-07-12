from enum import Enum
from threading import Thread
from time import sleep

from genesis.infrastructure.logger import get_logger
from genesis.simulation.clock import Clock
from genesis.simulation.scheduler import Scheduler


class SimulationState(Enum):
    CREATED = "created"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPED = "stopped"


SIMULATION_LOGGER_LEVEL = "debug"
MIN_SPEED = 1
MAX_SPEED = 100


class Simulation:
    def __init__(self):
        self.logger = get_logger("simulation", level=SIMULATION_LOGGER_LEVEL)
        self.state = SimulationState.CREATED

        self.clock = Clock()
        self.scheduler = Scheduler()
        self.executed_ticks = 0
        self.speed = MIN_SPEED
        self.thread = None

    def start(self):
        if self.state != SimulationState.CREATED:
            raise RuntimeError("Simulation has already been started.")

        self.state = SimulationState.RUNNING
        self.thread = Thread(target=self.run, daemon=True)

        self.thread.start()

    def pause(self):
        if self.state != SimulationState.RUNNING:
            raise RuntimeError("Simulation is not running.")
        self.state = SimulationState.PAUSED

    def resume(self):
        if self.state != SimulationState.PAUSED:
            raise RuntimeError("Simulation is not paused.")

        self.state = SimulationState.RUNNING

    def stop(self):
        if self.state not in (
            SimulationState.RUNNING,
            SimulationState.PAUSED,
        ):
            raise RuntimeError("Simulation cannot be stopped.")

        self.state = SimulationState.STOPPED

        if self.thread:
            self.thread.join()

    def set_speed(self, speed: int):
        if speed < MIN_SPEED:
            self.logger.warning(
                "Speed %s below minimum. Setting to %s.",
                speed,
                MIN_SPEED,
            )
            speed = MIN_SPEED

        elif speed > MAX_SPEED:
            self.logger.warning(
                "Speed %s above maximum. Setting to %s.",
                speed,
                MAX_SPEED,
            )
            speed = MAX_SPEED

        self.speed = speed

    def _wait(self):
        interval = 1 / self.speed
        sleep(interval)

    def tick(self):
        if self.state != SimulationState.RUNNING:
            return

        self.clock.tick()
        self.executed_ticks += 1

        try:
            self.scheduler.execute(self.clock.current_tick)
        except Exception as e:
            self.logger.error(
                f"Error executing events at tick {self.clock.current_tick}: {e}"
            )

        self.logger.debug(self)

    def run(self):
        self.logger.debug("Simulation loop started")
        while self.state != SimulationState.STOPPED:
            if self.state == SimulationState.RUNNING:
                try:
                    self.tick()
                except Exception as e:
                    self.logger.error(f"Error occurred while executing tick: {e}")

            self._wait()

        self.logger.debug("Simulation loop finished")

    def __repr__(self):
        return (
            f"<Simulation "
            f"state={self.state.value}, "
            f"tick={self.executed_ticks}, "
            f"time={self.clock.current_tick}, "
            f"speed={self.speed}x>"
        )
