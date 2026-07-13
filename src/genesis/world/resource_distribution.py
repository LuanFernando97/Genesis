from genesis.world.resource import ResourceType
from genesis.world.terrain import TerrainType


class ResourceDistribution:
    RULES = {
        TerrainType.PLAIN: {
            ResourceType.FOOD: 0.8,
            ResourceType.WATER: 0.3,
            ResourceType.WOOD: 0.2,
            ResourceType.STONE: 0.1,
        },
        TerrainType.FOREST: {
            ResourceType.WOOD: 0.9,
            ResourceType.FOOD: 0.5,
            ResourceType.WATER: 0.4,
            ResourceType.STONE: 0.1,
        },
        TerrainType.MOUNTAIN: {
            ResourceType.STONE: 0.9,
            ResourceType.MINERALS: 0.6,
            ResourceType.WATER: 0.2,
            ResourceType.WOOD: 0.05,
        },
        TerrainType.WATER: {
            ResourceType.WATER: 1.0,
            ResourceType.FOOD: 0.5,
            ResourceType.MINERALS: 0.1,
        },
        TerrainType.DESERT: {
            ResourceType.STONE: 0.4,
            ResourceType.MINERALS: 0.2,
            ResourceType.WATER: 0.05,
            ResourceType.FOOD: 0.05,
        },
    }
