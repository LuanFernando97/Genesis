from genesis.infrastructure.logger import get_logger

WORLD_LOGGER_LEVEL = "debug"


class World:
    def __init__(
        self,
        seed: int,
        width: int = 100,
        height: int = 100,
    ) -> None:
        self.logger = get_logger(
            "world",
            level=WORLD_LOGGER_LEVEL,
        )
        self.width = width
        self.height = height
        self.seed = seed

        self.grid = None

        self._validate()

    @property
    def size(self) -> tuple[int, int]:
        return self.width, self.height

    def update(self, tick: int | None = None):
        self.logger.debug(f"Updating world in tick {tick}: {self}")

    def _validate(self) -> None:
        if self.width <= 0:
            raise ValueError("World width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("World height must be greater than zero.")

    def __repr__(self) -> str:
        return f"World(width={self.width}, height={self.height}, seed={self.seed})"
