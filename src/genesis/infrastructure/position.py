from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Position") -> "Position":
        if not isinstance(other, Position):
            return NotImplemented

        return Position(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: "Position") -> "Position":
        if not isinstance(other, Position):
            return NotImplemented

        return Position(
            self.x - other.x,
            self.y - other.y,
        )

    def __repr__(self) -> str:
        return f"Position(x={self.x}, y={self.y})"
