from genesis.infrastructure.position import Position


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cells = self._create_grid()

    def _create_grid(self):
        return [[None for _ in range(self.width)] for _ in range(self.height)]

    def contains(self, position: Position) -> bool:
        return 0 <= position.x < self.width and 0 <= position.y < self.height

    def get(self, position: Position):
        if not self.contains(position):
            raise ValueError("Position is outside grid boundaries.")

        return self.cells[position.y][position.x]

    def set(self, position: Position, value) -> None:
        if not self.contains(position):
            raise ValueError("Position is outside grid boundaries.")

        self.cells[position.y][position.x] = value

    def neighbors(self, position: Position) -> list[Position]:
        directions = [
            Position(-1, -1),
            Position(0, -1),
            Position(1, -1),
            Position(-1, 0),
            Position(1, 0),
            Position(-1, 1),
            Position(0, 1),
            Position(1, 1),
        ]

        neighbors = []

        for direction in directions:
            neighbor = position + direction

            if self.contains(neighbor):
                neighbors.append(neighbor)

        return neighbors
