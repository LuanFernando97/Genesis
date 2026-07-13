from dataclasses import dataclass, field

from genesis.infrastructure.position import Position
from genesis.world.resource import Resource
from genesis.world.terrain import TerrainType


@dataclass
class Tile:
    position: Position
    terrain: TerrainType | None = None
    resources: list[Resource] = field(default_factory=list)

    def __repr__(self):
        return (
            f"Tile("
            f"position={self.position}, "
            f"terrain={self.terrain}, "
            f"resources={self.resources})"
        )
