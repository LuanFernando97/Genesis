import pytest

from genesis.entities.entity import Entity
from genesis.entities.humans.human import Human
from genesis.entities.humans.sex import Sex


def test_human_is_entity():
    assert issubclass(Human, Entity)


def test_can_create_human(simulation):
    human = Human(
        simulation=simulation,
        name="John",
        sex=Sex.MALE,
        age=25,
    )

    assert isinstance(human, Human)
    assert human.is_alive


def test_human_name(simulation):
    human = Human(
        simulation=simulation,
        name="John",
        sex=Sex.MALE,
        age=25,
    )

    assert human.name == "John"


def test_human_sex(simulation):
    human = Human(
        simulation=simulation,
        name="John",
        sex=Sex.MALE,
        age=25,
    )

    assert human.sex == Sex.MALE


def test_human_age(simulation):
    human = Human(
        simulation=simulation,
        name="John",
        sex=Sex.MALE,
        age=25,
    )

    assert human.age == 25


def test_name_is_required(simulation):
    with pytest.raises(ValueError):
        Human(
            simulation=simulation,
            name="",
            sex=Sex.MALE,
            age=25,
        )


def test_age_cannot_be_negative(simulation):
    with pytest.raises(ValueError):
        Human(
            simulation=simulation,
            name="John",
            sex=Sex.MALE,
            age=-1,
        )
