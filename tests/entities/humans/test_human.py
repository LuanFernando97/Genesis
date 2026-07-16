from genesis.entities.entity import Entity
from genesis.entities.humans.human import Human


def test_human_is_entity():
    assert issubclass(Human, Entity)


def test_can_create_human(simulation):
    human = Human(simulation)

    assert isinstance(human, Human)
    assert human.is_alive
