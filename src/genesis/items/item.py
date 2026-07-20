from abc import ABC


class Item(ABC):
    def __init__(
        self,
        name: str,
        description: str = "",
    ) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        self._name = name
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description
