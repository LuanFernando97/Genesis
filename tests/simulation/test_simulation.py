from unittest.mock import MagicMock

import pytest

from genesis.simulation.scheduler import Event
from genesis.simulation.simulation import (
    MAX_SPEED,
    MIN_SPEED,
    Simulation,
    SimulationState,
)


def test_tick_advances_clock():
    simulation = Simulation()

    simulation.state = SimulationState.RUNNING
    simulation.tick()

    assert simulation.clock.current_tick == 1


def test_tick_increments_counter():
    simulation = Simulation()

    simulation.state = SimulationState.RUNNING

    simulation.tick()
    simulation.tick()

    assert simulation.executed_ticks == 2


def test_tick_does_nothing_when_not_running():
    simulation = Simulation()

    simulation.tick()

    assert simulation.clock.current_tick == 0
    assert simulation.executed_ticks == 0


def test_start():
    simulation = Simulation()

    simulation.start()

    assert simulation.state is SimulationState.RUNNING
    simulation.stop()


def test_pause():
    simulation = Simulation()

    simulation.start()
    simulation.pause()

    assert simulation.state is SimulationState.PAUSED
    simulation.stop()


def test_resume():
    simulation = Simulation()

    simulation.start()
    simulation.pause()
    simulation.resume()

    assert simulation.state is SimulationState.RUNNING
    simulation.stop()


def test_stop():
    simulation = Simulation()

    simulation.start()
    simulation.stop()

    assert simulation.state is SimulationState.STOPPED


def test_cannot_pause_before_start():
    simulation = Simulation()

    with pytest.raises(RuntimeError):
        simulation.pause()


def test_cannot_resume_without_pause():
    simulation = Simulation()

    simulation.start()

    with pytest.raises(RuntimeError):
        simulation.resume()


def test_cannot_start_twice():
    simulation = Simulation()

    simulation.start()

    with pytest.raises(RuntimeError):
        simulation.start()


def test_cannot_resume_after_stop():
    simulation = Simulation()

    simulation.start()
    simulation.stop()

    with pytest.raises(RuntimeError):
        simulation.resume()


def test_default_speed():
    simulation = Simulation()

    assert simulation.speed == MIN_SPEED


def test_set_valid_speed():
    simulation = Simulation()

    simulation.set_speed(10)

    assert simulation.speed == 10


def test_speed_below_minimum_sets_minimum():
    simulation = Simulation()

    simulation.set_speed(0)

    assert simulation.speed == MIN_SPEED


def test_speed_above_maximum_sets_maximum():
    simulation = Simulation()

    simulation.set_speed(200)

    assert simulation.speed == MAX_SPEED


def test_speed_minimum_boundary():
    simulation = Simulation()

    simulation.set_speed(MIN_SPEED)

    assert simulation.speed == MIN_SPEED


def test_speed_maximum_boundary():
    simulation = Simulation()

    simulation.set_speed(MAX_SPEED)

    assert simulation.speed == MAX_SPEED


def test_speed_interval():
    simulation = Simulation()

    simulation.set_speed(10)

    assert 1 / simulation.speed == 0.1


def test_run_executes_tick():
    simulation = Simulation()

    simulation.state = SimulationState.RUNNING

    simulation.tick = MagicMock(side_effect=simulation.stop)

    simulation.run()

    simulation.tick.assert_called_once()


def test_run_stops():
    simulation = Simulation()

    simulation.state = SimulationState.RUNNING
    simulation.tick = MagicMock(side_effect=simulation.stop)

    simulation.run()

    assert simulation.state == SimulationState.STOPPED


def test_tick_executes_scheduled_event():
    simulation = Simulation()

    executed = False

    def callback():
        nonlocal executed
        executed = True

    simulation.scheduler.schedule(Event(tick=1, callback=callback))

    simulation.state = SimulationState.RUNNING

    simulation.tick()

    assert executed
