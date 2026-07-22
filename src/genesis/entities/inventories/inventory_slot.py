from genesis.items.item import Item


class InventorySlot:
    def __init__(
        self,
        item: Item,
        quantity: int = 0,
    ) -> None:
        if not isinstance(item, Item):
            raise TypeError("Item must be an instance of Item.")

        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self._item = item
        self._quantity = quantity

    @property
    def item(self) -> Item:
        return self._item

    @property
    def quantity(self) -> int:
        return self._quantity

    def add(self, quantity: int) -> None:
        if quantity < 1:
            raise ValueError("Quantity must be greater than zero.")

        self._quantity += quantity

    def remove(self, quantity: int) -> None:
        if quantity < 1:
            raise ValueError("Quantity must be greater than zero.")

        if quantity > self._quantity:
            raise ValueError("Cannot remove more items than available.")

        self._quantity -= quantity
