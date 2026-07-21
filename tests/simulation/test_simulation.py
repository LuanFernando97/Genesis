from unittest.mock import MagicMock

import pytest

from genesis.entities.entity import Entity
from genesis.entities.humans.human import Human
from genesis.entities.humans.needs import Needs
from genesis.entities.humans.sex import Sex
from genesis.infrastructure.position import Position
from genesis.simulation.scheduler import Event
from genesis.simulation.simulation import (
    MAX_SPEED,
    MIN_SPEED,
    Simulation,
    SimulationMode,
    SimulationState,
)

# =============================================================================
# Initialization
# =============================================================================


def test_simulation_has_world_configuration():
    simulation = Simulation(
        world_width=50,
        world_height=30,
        seed=123,
        mode=SimulationMode.STEP,
    )

    assert simulation.world is None
    assert simulation.world_width == 50
    assert simulation.world_height == 30
    assert simulation.seed == 123
    assert simulation.mode is SimulationMode.STEP


# =============================================================================
# World Integration
# =============================================================================


def test_start_creates_world():
    simulation = Simulation(
        world_width=20,
        world_height=10,
        seed=123,
        mode=SimulationMode.STEP,
    )

    assert simulation.world is None

    simulation.start()

    assert simulation.world is not None
    assert simulation.world.width == 20
    assert simulation.world.height == 10
    assert simulation.world.seed == 123


def test_tick_updates_world():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    simulation.start()

    simulation.world.update = MagicMock()

    simulation.tick()

    simulation.world.update.assert_called_once()


# =============================================================================
# Lifecycle
# =============================================================================


def test_start():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    simulation.start()

    assert simulation.state is SimulationState.RUNNING


def test_pause():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    simulation.start()
    simulation.pause()

    assert simulation.state is SimulationState.PAUSED


def test_resume():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    simulation.start()
    simulation.pause()
    simulation.resume()

    assert simulation.state is SimulationState.RUNNING


def test_stop():
    simulation = Simulation(
        mode=SimulationMode.REALTIME,
    )

    simulation.start()
    simulation.stop()

    assert simulation.state is SimulationState.STOPPED


def test_cannot_pause_before_start():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    with pytest.raises(RuntimeError):
        simulation.pause()


def test_cannot_resume_without_pause():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    simulation.start()

    with pytest.raises(RuntimeError):
        simulation.resume()


def test_cannot_start_twice():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    simulation.start()

    with pytest.raises(RuntimeError):
        simulation.start()


def test_cannot_resume_after_stop():
    simulation = Simulation(
        mode=SimulationMode.REALTIME,
    )

    simulation.start()
    simulation.stop()

    with pytest.raises(RuntimeError):
        simulation.resume()


# =============================================================================
# Tick
# =============================================================================


def test_tick_advances_clock():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    simulation.start()

    simulation.tick()

    assert simulation.clock.current_tick == 1


def test_tick_increments_counter():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    simulation.start()

    simulation.tick()
    simulation.tick()

    assert simulation.executed_ticks == 2


def test_tick_does_nothing_when_not_running():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    simulation.tick()

    assert simulation.clock.current_tick == 0
    assert simulation.executed_ticks == 0


# =============================================================================
# Scheduler
# =============================================================================


def test_tick_executes_scheduled_event():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    executed = False

    def callback():
        nonlocal executed
        executed = True

    simulation.scheduler.schedule(
        Event(
            tick=1,
            callback=callback,
        )
    )

    simulation.start()

    simulation.tick()

    assert executed


# =============================================================================
# Speed Control
# =============================================================================


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


# =============================================================================
# Execution Mode
# =============================================================================


def test_step_mode_does_not_create_running_thread():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    simulation.start()

    assert simulation.thread is not None
    assert not simulation.thread.is_alive()


def test_realtime_mode_starts_thread():
    simulation = Simulation(
        mode=SimulationMode.REALTIME,
    )

    simulation.start()

    assert simulation.thread is not None
    assert simulation.thread.is_alive()

    simulation.stop()


# =============================================================================
# Entity Integration
# =============================================================================


def test_simulation_updates_entities():
    simulation = Simulation(
        mode=SimulationMode.STEP,
    )

    Entity._reset()

    human = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=Position(0, 0),
        needs=Needs(
            energy=50,
            hunger=50,
            thirst=50,
        ),
    )
    human.spawn()
    simulation.start()

    simulation.tick()

    assert human.needs.energy == 49
    assert human.needs.hunger == 51
    assert human.needs.thirst == 51


def test_simulation_schedules_entity_update():
    simulation = Simulation(mode=SimulationMode.STEP)

    Entity._reset()

    human = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=Position(0, 0),
    )
    human.spawn()
    simulation.start()

    assert len(simulation.scheduler.events) == 1
    assert simulation.scheduler.events[0].name == "Update Entities"


def test_simulation_updates_multiple_humans():
    simulation = Simulation(mode=SimulationMode.STEP)

    Entity._reset()

    human1 = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=Position(0, 0),
    )

    human2 = Human(
        name="Jane",
        sex=Sex.FEMALE,
        age=22,
        position=Position(1, 1),
    )

    human1.spawn()
    human2.spawn()

    simulation.start()

    simulation.tick()

    assert human1.needs.energy == 99
    assert human1.needs.hunger == 1
    assert human1.needs.thirst == 1

    assert human2.needs.energy == 99
    assert human2.needs.hunger == 1
    assert human2.needs.thirst == 1


def test_dead_entities_are_not_updated():
    simulation = Simulation(mode=SimulationMode.STEP)

    Entity._reset()

    human = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=Position(0, 0),
    )

    human.spawn()
    human.despawn()

    simulation.start()

    simulation.tick()

    assert human.needs.energy == 100
    assert human.needs.hunger == 0
    assert human.needs.thirst == 0


def test_scheduler_executes_entity_update():
    simulation = Simulation(mode=SimulationMode.STEP)

    Entity._reset()

    human = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=Position(0, 0),
    )

    human.spawn()

    human.update = MagicMock()

    simulation.start()

    simulation.tick()

    human.update.assert_called_once()
