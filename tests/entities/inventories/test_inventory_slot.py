import pytest

from genesis.entities.inventories.inventory_slot import InventorySlot
from genesis.items.item import Item


class MockItem(Item):
    def __init__(self, name: str, description: str = "") -> None:
        super().__init__(name, description)


def test_can_create_inventory_slot():
    slot = InventorySlot(MockItem("Wood"))

    assert isinstance(slot, InventorySlot)


def test_default_quantity_is_zero():
    slot = InventorySlot(MockItem("Wood"))

    assert slot.quantity == 0


def test_can_create_slot_with_custom_quantity():
    slot = InventorySlot(
        MockItem("Wood"),
        quantity=10,
    )

    assert slot.quantity == 10


def test_item_must_be_item():
    with pytest.raises(TypeError):
        InventorySlot("Wood")


@pytest.mark.parametrize("quantity", [-1])
def test_invalid_initial_quantity(quantity):
    with pytest.raises(ValueError):
        InventorySlot(
            MockItem("Wood"),
            quantity=quantity,
        )


def test_add_quantity():
    slot = InventorySlot(MockItem("Wood"))

    slot.add(5)

    assert slot.quantity == 5


@pytest.mark.parametrize("quantity", [-1])
def test_invalid_add_quantity(quantity):
    slot = InventorySlot(MockItem("Wood"))

    with pytest.raises(ValueError):
        slot.add(quantity)


def test_remove_quantity():
    slot = InventorySlot(
        MockItem("Wood"),
        quantity=10,
    )

    slot.remove(3)

    assert slot.quantity == 7


@pytest.mark.parametrize("quantity", [-1])
def test_invalid_remove_quantity(quantity):
    slot = InventorySlot(MockItem("Wood"))

    with pytest.raises(ValueError):
        slot.remove(quantity)


def test_cannot_remove_more_than_available():
    slot = InventorySlot(
        MockItem("Wood"),
        quantity=5,
    )

    with pytest.raises(ValueError):
        slot.remove(6)


def test_item_property():
    item = MockItem("Stone")

    slot = InventorySlot(item)

    assert slot.item is item


def test_quantity_property():
    slot = InventorySlot(
        MockItem("Stone"),
        quantity=3,
    )

    assert slot.quantity == 3
