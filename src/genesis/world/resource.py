from dataclasses import dataclass
from enum import Enum


class ResourceType(Enum):
    WOOD = "wood"
    STONE = "stone"
    WATER = "water"
    FOOD = "food"
    MINERALS = "minerals"


@dataclass
class Resource:
    type: ResourceType
    amount: int

    def __post_init__(self):
        if not isinstance(self.amount, int):
            raise TypeError("Resource amount must be an integer.")
        if self.amount < 0:
            raise ValueError("Resource amount cannot be negative.")

    def consume(self, amount: int):
        if amount > self.amount:
            raise ValueError("Not enough resources to consume.")
        self.amount -= amount
