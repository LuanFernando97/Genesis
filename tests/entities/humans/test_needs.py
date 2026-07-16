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
