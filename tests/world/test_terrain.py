from genesis.world.terrain import Terrain, TerrainType


def test_terrain_types_exist():
    assert TerrainType.FOREST
    assert TerrainType.MOUNTAIN


def test_create_terrain():
    forest = Terrain(TerrainType.FOREST, movement_cost=2, resources={"wood": 100})

    assert forest.type == TerrainType.FOREST
    assert forest.movement_cost == 2


def test_water_has_high_movement_cost():
    water = Terrain(TerrainType.WATER, movement_cost=999, resources={})

    assert water.movement_cost == 999
