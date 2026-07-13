from genesis.infrastructure.position import Position
from genesis.world.resource import Resource, ResourceType
from genesis.world.terrain import TerrainType
from genesis.world.tile import Tile


def test_create_tile():
    tile = Tile(Position(5, 10))

    assert tile.position == Position(5, 10)


def test_tile_initial_state():
    tile = Tile(Position(0, 0))

    assert tile.terrain is None
    assert tile.resources == []


def test_tile_repr():
    tile = Tile(Position(0, 0))

    assert repr(tile) == "Tile(position=Position(x=0, y=0), terrain=None, resources=[])"


def test_tile_can_have_terrain():
    tile = Tile(Position(0, 0))

    tile.terrain = TerrainType.FOREST

    assert tile.terrain == TerrainType.FOREST


def test_tile_can_have_multiple_resources():
    tile = Tile(Position(0, 0))

    tile.resources.append(Resource(ResourceType.WOOD, 100))

    tile.resources.append(Resource(ResourceType.FOOD, 50))

    assert len(tile.resources) == 2
    assert tile.resources[0].type == ResourceType.WOOD
    assert tile.resources[1].type == ResourceType.FOOD
