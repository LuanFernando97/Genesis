from enum import Enum


class TerrainType(Enum):
    PLAIN = "plain"
    FOREST = "forest"
    MOUNTAIN = "mountain"
    WATER = "water"
    DESERT = "desert"


class Terrain:
    def __init__(self, terrain_type: TerrainType, movement_cost: int, resources: dict):
        self.type = terrain_type
        self.movement_cost = movement_cost
        self.resources = resources
