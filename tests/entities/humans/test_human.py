import pytest

from genesis.entities.entity import Entity
from genesis.entities.humans.human import Human
from genesis.entities.humans.human_state import HumanState
from genesis.entities.humans.needs import Needs
from genesis.entities.humans.sex import Sex
from genesis.entities.inventories.inventory import Inventory
from genesis.infrastructure.position import Position


def test_human_is_entity():
    assert issubclass(Human, Entity)


def test_can_create_human(position):
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=position,
    )

    assert isinstance(human, Human)
    assert human.is_alive
    assert human.position is position


def test_human_name(position):
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=position,
    )

    assert human.name == "John"


def test_human_sex(position):
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=position,
    )

    assert human.sex == Sex.MALE


def test_human_age(position):
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=position,
    )

    assert human.age == 25


def test_human_creates_default_needs(position):
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=position,
    )

    assert isinstance(human.needs, Needs)


def test_human_accepts_custom_needs(position):
    needs = Needs(
        energy=50,
        hunger=25,
        thirst=10,
        health=80,
    )

    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=position,
        needs=needs,
    )

    assert human.needs is needs


def test_name_is_required(position):
    with pytest.raises(ValueError):
        Human(
            name="",
            sex=Sex.MALE,
            age=25,
            position=position,
        )


def test_age_cannot_be_negative(position):
    with pytest.raises(ValueError):
        Human(
            name="John",
            sex=Sex.MALE,
            age=-1,
            position=position,
        )


@pytest.mark.parametrize(
    ("field", "kwargs"),
    [
        ("energy", {"energy": -1}),
        ("energy", {"energy": 101}),
        ("hunger", {"hunger": -1}),
        ("hunger", {"hunger": 101}),
        ("thirst", {"thirst": -1}),
        ("thirst", {"thirst": 101}),
        ("health", {"health": -1}),
        ("health", {"health": 101}),
    ],
)
def test_invalid_needs_values(field, kwargs):
    with pytest.raises(ValueError):
        Needs(**kwargs)


def test_can_change_position(position):
    human = Human(name="John", sex=Sex.MALE, age=25, position=position)

    new_position = Position(10, 20)

    human.position = new_position

    assert human.position is new_position


def test_position_must_be_position():
    with pytest.raises(TypeError):
        Human(
            name="John",
            sex=Sex.MALE,
            age=25,
            position=(0, 0),
        )


def test_cannot_assign_invalid_position():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=Position(0, 0),
    )

    with pytest.raises(TypeError):
        human.position = (5, 5)


def test_default_state_is_idle():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=Position(0, 0),
    )

    assert human.state == HumanState.IDLE


def test_can_create_human_with_custom_state():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=Position(0, 0),
        state=HumanState.SLEEPING,
    )

    assert human.state == HumanState.SLEEPING


def test_can_change_state():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=Position(0, 0),
    )

    human.state = HumanState.WALKING

    assert human.state == HumanState.WALKING


def test_invalid_state():
    with pytest.raises(TypeError):
        Human(
            name="John",
            sex=Sex.MALE,
            age=25,
            position=Position(0, 0),
            state="walking",
        )


def test_cannot_assign_invalid_state():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=Position(0, 0),
    )

    with pytest.raises(TypeError):
        human.state = "sleeping"


def test_human_creates_default_inventory():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=Position(0, 0),
    )

    assert isinstance(human.inventory, Inventory)


def test_human_accepts_custom_inventory():
    inventory = Inventory()

    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=Position(0, 0),
        inventory=inventory,
    )

    assert human.inventory is inventory


def test_human_always_has_valid_inventory():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=25,
        position=Position(0, 0),
    )

    assert human.inventory is not None
    assert isinstance(human.inventory, Inventory)


def test_update_decreases_energy():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=Position(0, 0),
        needs=Needs(energy=50),
    )

    human.update()

    assert human.needs.energy == 49


def test_update_increases_hunger():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=Position(0, 0),
        needs=Needs(hunger=50),
    )

    human.update()

    assert human.needs.hunger == 51


def test_update_increases_thirst():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=Position(0, 0),
        needs=Needs(thirst=50),
    )

    human.update()

    assert human.needs.thirst == 51


def test_update_updates_all_needs():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=Position(0, 0),
        needs=Needs(
            energy=50,
            hunger=50,
            thirst=50,
            health=100,
        ),
    )

    human.update()

    assert human.needs.energy == 49
    assert human.needs.hunger == 51
    assert human.needs.thirst == 51
    assert human.needs.health == 100


def test_update_respects_needs_limits():
    human = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=Position(0, 0),
        needs=Needs(
            energy=0,
            hunger=100,
            thirst=100,
        ),
    )

    human.update()

    assert human.needs.energy == 0
    assert human.needs.hunger == 100
    assert human.needs.thirst == 100


def test_update_does_not_change_identity_or_state():
    position = Position(5, 10)

    human = Human(
        name="John",
        sex=Sex.MALE,
        age=20,
        position=position,
        state=HumanState.IDLE,
    )

    human.update()

    assert human.name == "John"
    assert human.age == 20
    assert human.sex == Sex.MALE
    assert human.position is position
    assert human.state == HumanState.IDLE
