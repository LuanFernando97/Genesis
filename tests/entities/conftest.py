import pytest

from genesis.entities.entity import Entity
from genesis.infrastructure.position import Position
from genesis.simulation.simulation import Simulation


@pytest.fixture
def simulation() -> Simulation:
    return Simulation()


@pytest.fixture()
def position() -> Position:
    return Position(x=0, y=0)


@pytest.fixture(autouse=True)
def reset_entity_state() -> None:
    Entity._reset()
