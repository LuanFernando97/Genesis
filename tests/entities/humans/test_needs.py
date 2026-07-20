import pytest

from genesis.entities.humans.needs import Needs


def test_can_create_needs():
    needs = Needs()

    assert isinstance(needs, Needs)


def test_default_energy():
    needs = Needs()

    assert needs.energy == 100


def test_default_hunger():
    needs = Needs()

    assert needs.hunger == 0


def test_default_thirst():
    needs = Needs()

    assert needs.thirst == 0


def test_default_health():
    needs = Needs()

    assert needs.health == 100


def test_can_create_custom_needs():
    needs = Needs(
        energy=80,
        hunger=20,
        thirst=15,
        health=90,
    )

    assert needs.energy == 80
    assert needs.hunger == 20
    assert needs.thirst == 15
    assert needs.health == 90


@pytest.mark.parametrize("value", [-1, 101])
def test_invalid_energy(value):
    with pytest.raises(ValueError):
        Needs(energy=value)


@pytest.mark.parametrize("value", [-1, 101])
def test_invalid_hunger(value):
    with pytest.raises(ValueError):
        Needs(hunger=value)


@pytest.mark.parametrize("value", [-1, 101])
def test_invalid_thirst(value):
    with pytest.raises(ValueError):
        Needs(thirst=value)


@pytest.mark.parametrize("value", [-1, 101])
def test_invalid_health(value):
    with pytest.raises(ValueError):
        Needs(health=value)


def test_increase_energy():
    needs = Needs(energy=50)

    needs.increase_energy(10)

    assert needs.energy == 60


def test_decrease_energy():
    needs = Needs(energy=50)

    needs.decrease_energy(10)

    assert needs.energy == 40


def test_energy_cannot_exceed_maximum():
    needs = Needs(energy=95)

    needs.increase_energy(10)

    assert needs.energy == 100


def test_energy_cannot_be_negative():
    needs = Needs(energy=5)

    needs.decrease_energy(10)

    assert needs.energy == 0


def test_increase_hunger():
    needs = Needs(hunger=50)

    needs.increase_hunger(10)

    assert needs.hunger == 60


def test_decrease_hunger():
    needs = Needs(hunger=50)

    needs.decrease_hunger(10)

    assert needs.hunger == 40


def test_hunger_cannot_exceed_maximum():
    needs = Needs(hunger=95)

    needs.increase_hunger(10)

    assert needs.hunger == 100


def test_hunger_cannot_be_negative():
    needs = Needs(hunger=5)

    needs.decrease_hunger(10)

    assert needs.hunger == 0


def test_increase_thirst():
    needs = Needs(thirst=50)

    needs.increase_thirst(10)

    assert needs.thirst == 60


def test_decrease_thirst():
    needs = Needs(thirst=50)

    needs.decrease_thirst(10)

    assert needs.thirst == 40


def test_thirst_cannot_exceed_maximum():
    needs = Needs(thirst=95)

    needs.increase_thirst(10)

    assert needs.thirst == 100


def test_thirst_cannot_be_negative():
    needs = Needs(thirst=5)

    needs.decrease_thirst(10)

    assert needs.thirst == 0


def test_increase_health():
    needs = Needs(health=50)

    needs.increase_health(10)

    assert needs.health == 60


def test_decrease_health():
    needs = Needs(health=50)

    needs.decrease_health(10)

    assert needs.health == 40


def test_health_cannot_exceed_maximum():
    needs = Needs(health=95)

    needs.increase_health(10)

    assert needs.health == 100


def test_health_cannot_be_negative():
    needs = Needs(health=5)

    needs.decrease_health(10)

    assert needs.health == 0
