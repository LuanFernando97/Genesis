import pytest

from genesis.world.resource import Resource, ResourceType


def test_resource_type_exists():
    assert ResourceType.WOOD


def test_create_resource():
    resource = Resource(ResourceType.WOOD, 100)

    assert resource.type == ResourceType.WOOD
    assert resource.amount == 100


def test_consume_resource():
    resource = Resource(ResourceType.WOOD, 100)

    resource.consume(30)

    assert resource.amount == 70


def test_cannot_consume_more_than_available():
    resource = Resource(ResourceType.WOOD, 10)

    with pytest.raises(ValueError):
        resource.consume(20)


def test_resource_cannot_have_negative_amount():
    with pytest.raises(ValueError):
        Resource(ResourceType.WOOD, -10)


def test_consume_all_resource():
    resource = Resource(ResourceType.WOOD, 100)

    resource.consume(100)

    assert resource.amount == 0
