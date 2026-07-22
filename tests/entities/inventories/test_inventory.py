import pytest

from genesis.entities.inventories.inventory import Inventory
from genesis.items.item import Item


class MockItem(Item):
    def __init__(self, name: str, description: str = "") -> None:
        super().__init__(name, description)


def test_inventory_starts_empty():
    inventory = Inventory()

    assert len(inventory.slots) == 0


def test_add_item():
    inventory = Inventory()
    wood = MockItem("Wood")

    inventory.add(wood)

    assert inventory.quantity(wood) == 1


def test_add_existing_item():
    inventory = Inventory()
    wood = MockItem("Wood")

    inventory.add(wood)
    inventory.add(wood, 3)

    assert inventory.quantity(wood) == 4


def test_add_different_items():
    inventory = Inventory()

    inventory.add(MockItem("Wood"))
    inventory.add(MockItem("Stone"))

    assert len(inventory.slots) == 2


def test_remove_partial_quantity():
    inventory = Inventory()
    wood = MockItem("Wood")

    inventory.add(wood, 5)
    inventory.remove(wood, 2)

    assert inventory.quantity(wood) == 3


def test_remove_all_quantity():
    inventory = Inventory()
    wood = MockItem("Wood")

    inventory.add(wood)

    inventory.remove(wood)

    assert inventory.quantity(wood) == 0


def test_remove_empty_slot():
    inventory = Inventory()
    wood = MockItem("Wood")

    inventory.add(wood)
    inventory.remove(wood)

    assert len(inventory.slots) == 0


def test_quantity_unknown_item():
    inventory = Inventory()

    assert inventory.quantity(MockItem("Wood")) == 0


def test_contains_existing_item():
    inventory = Inventory()
    wood = MockItem("Wood")

    inventory.add(wood)

    assert inventory.contains(wood)


def test_contains_unknown_item():
    inventory = Inventory()

    assert not inventory.contains(MockItem("Wood"))


@pytest.mark.parametrize("quantity", [0, -1])
def test_invalid_add_quantity(quantity):
    inventory = Inventory()

    with pytest.raises(ValueError):
        inventory.add(MockItem("Wood"), quantity)


@pytest.mark.parametrize("quantity", [0, -1])
def test_invalid_remove_quantity(quantity):
    inventory = Inventory()

    with pytest.raises(ValueError):
        inventory.remove(MockItem("Wood"), quantity)


def test_remove_unknown_item():
    inventory = Inventory()

    with pytest.raises(ValueError):
        inventory.remove(MockItem("Wood"))
