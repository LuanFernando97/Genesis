import pytest

from genesis.items.item import Item


class MockItem(Item):
    def __init__(self, name: str, description: str = "") -> None:
        super().__init__(name, description)


def test_can_create_item():
    item = MockItem(name="Wood")

    assert isinstance(item, Item)


def test_can_create_item_with_description():
    item = MockItem(
        name="Wood",
        description="A piece of wood.",
    )

    assert item.description == "A piece of wood."


def test_name_is_required():
    with pytest.raises(ValueError):
        MockItem(name="")


def test_name_property():
    item = MockItem(name="Stone")

    assert item.name == "Stone"


def test_description_property():
    item = MockItem(
        name="Stone",
        description="A rock.",
    )

    assert item.description == "A rock."
