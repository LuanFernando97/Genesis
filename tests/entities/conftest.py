import pytest

from genesis.entities.entity import Entity
from genesis.simulation.simulation import Simulation


@pytest.fixture
def simulation() -> Simulation:
    return Simulation()


@pytest.fixture(autouse=True)
def reset_entity_state() -> None:
    Entity._reset()
