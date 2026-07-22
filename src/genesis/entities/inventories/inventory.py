from genesis.entities.inventories.inventory_slot import InventorySlot
from genesis.items.item import Item


class Inventory:
    def __init__(self) -> None:
        self._slots: list[InventorySlot] = []

    @property
    def slots(self) -> tuple[InventorySlot, ...]:
        return tuple(self._slots)

    def add(self, item: Item, quantity: int = 1) -> None:
        if quantity < 1:
            raise ValueError("Quantity must be greater than zero.")

        slot = self._find_slot(item)

        if slot is None:
            self._slots.append(InventorySlot(item, quantity))
            return

        slot.add(quantity)

    def remove(self, item: Item, quantity: int = 1) -> None:
        if quantity < 1:
            raise ValueError("Quantity must be greater than zero.")

        slot = self._find_slot(item)

        if slot is None:
            raise ValueError("Item not found.")

        slot.remove(quantity)

        if slot.quantity == 0:
            self._slots.remove(slot)

    def quantity(self, item: Item) -> int:
        slot = self._find_slot(item)

        if slot is None:
            return 0

        return slot.quantity

    def contains(self, item: Item) -> bool:
        return self._find_slot(item) is not None

    def _find_slot(self, item: Item) -> InventorySlot | None:
        for slot in self._slots:
            if slot.item == item:
                return slot

        return None
