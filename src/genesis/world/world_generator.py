import random

from genesis.infrastructure.logger import get_logger
from genesis.infrastructure.position import Position
from genesis.world.grid import Grid
from genesis.world.resource import Resource
from genesis.world.resource_distribution import ResourceDistribution
from genesis.world.terrain import TerrainType
from genesis.world.tile import Tile
from genesis.world.world import World

WORLD_LOGGER_LEVEL = "debug"


class WorldGenerator:
    def __init__(self, seed: int | None = None):
        self.logger = get_logger(
            "world_generator",
            level=WORLD_LOGGER_LEVEL,
        )
        if seed is not None:
            if not isinstance(seed, int):
                raise TypeError("Seed must be an integer.")

            if seed < 0:
                raise ValueError("Seed must be a non-negative integer.")
        self.seed = seed if seed is not None else random.randint(0, 2**32 - 1)
        self.random = random.Random(self.seed)

    def generate(
        self,
        width: int,
        height: int,
    ) -> World:
        world = World(
            width=width,
            height=height,
            seed=self.seed,
        )

        world.grid = Grid(
            width,
            height,
        )

        for y in range(height):
            for x in range(width):
                position = Position(x, y)

                tile = Tile(position)

                tile.terrain = self.generate_terrain()
                tile.resources = self.generate_resources(tile.terrain)

                world.grid.set(
                    position,
                    tile,
                )

        self.logger.info(f"World generated: world={world}")
        return world

    def generate_value(self, range_start: int = 0, range_end: int = 100) -> int:
        return self.random.randint(range_start, range_end)

    def generate_terrain(self) -> TerrainType:
        terrains = [
            TerrainType.PLAIN,
            TerrainType.FOREST,
            TerrainType.MOUNTAIN,
            TerrainType.WATER,
            TerrainType.DESERT,
        ]

        return self.random.choice(terrains)

    def generate_resources(self, terrain: TerrainType):
        resources = []

        rules = ResourceDistribution.RULES.get(terrain, {})

        for resource_type, probability in rules.items():
            if self.random.random() <= probability:
                resources.append(Resource(resource_type, self.random.randint(10, 100)))

        return resources
