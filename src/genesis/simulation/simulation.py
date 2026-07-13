from enum import Enum
from threading import Thread
from time import sleep

from genesis.infrastructure.logger import get_logger
from genesis.simulation.clock import Clock
from genesis.simulation.scheduler import Scheduler
from genesis.world.world_generator import WorldGenerator


class SimulationState(Enum):
    CREATED = "created"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPED = "stopped"


class SimulationMode(Enum):
    REALTIME = "realtime"
    STEP = "step"


SIMULATION_LOGGER_LEVEL = "debug"
MIN_SPEED = 1
MAX_SPEED = 100
WORLD_WIDTH = 100
WORLD_HEIGHT = 100


class Simulation:
    def __init__(
        self,
        world_width: int = WORLD_WIDTH,
        world_height: int = WORLD_HEIGHT,
        seed: int | None = None,
        mode: SimulationMode = SimulationMode.REALTIME,
    ):
        self.logger = get_logger("simulation", level=SIMULATION_LOGGER_LEVEL)
        self.state = SimulationState.CREATED
        self.mode = mode

        self.clock = Clock()
        self.scheduler = Scheduler()
        self.executed_ticks = 0
        self.speed = MIN_SPEED
        self.thread = None

        self.world_width = world_width
        self.world_height = world_height
        self.seed = seed

        self.world_generator = WorldGenerator(seed)
        self.world = None

    def start(self):
        if self.state != SimulationState.CREATED:
            raise RuntimeError("Simulation has already been started.")

        self.logger.debug("Starting simulation")
        self.state = SimulationState.RUNNING
        self._initialize_world()

        self.thread = Thread(target=self.run, daemon=True)
        if self.mode == SimulationMode.REALTIME:
            self.thread.start()

    def pause(self):
        if self.state != SimulationState.RUNNING:
            raise RuntimeError("Simulation is not running.")
        self.logger.debug("Pausing simulation")
        self.state = SimulationState.PAUSED

    def resume(self):
        if self.state != SimulationState.PAUSED:
            raise RuntimeError("Simulation is not paused.")

        self.logger.debug("Resuming simulation")
        self.state = SimulationState.RUNNING

    def stop(self):
        if self.state not in (
            SimulationState.RUNNING,
            SimulationState.PAUSED,
        ):
            raise RuntimeError("Simulation cannot be stopped.")

        self.logger.debug("Stopping simulation")
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
        self._update_world()

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

    def _initialize_world(self) -> None:
        self.world = self.world_generator.generate(
            width=self.world_width,
            height=self.world_height,
        )

    def _update_world(self) -> None:
        if self.world is None:
            raise RuntimeError("World has not been initialized.")
        self.world.update(self.clock.current_tick)

    def __repr__(self):
        return (
            f"<Simulation "
            f"state={self.state.value}, "
            f"tick={self.executed_ticks}, "
            f"time={self.clock.current_tick}, "
            f"world_size={self.world.size if self.world else None}, "
            f"speed={self.speed}x>"
        )
