# World System

## Overview

The World System is responsible for representing the physical environment where the simulation takes place.

It provides the spatial structure used by every future system, including entities, civilizations, resources, and environmental events.

The world is composed of a fixed-size grid of tiles. Each tile stores its position, terrain type, and the natural resources available at that location.

The world is generated procedurally from a seed, allowing deterministic world generation.

---

# Architecture

```text
Simulation
│
└── World
    │
    ├── Grid
    │   └── Tile
    │       ├── Position
    │       ├── Terrain
    │       └── Resources
    │
    └── WorldGenerator
```

---

# World

The `World` class represents the complete simulation environment.

Responsibilities:

- Store world dimensions
- Store the world seed
- Own the Grid
- Update the world every simulation tick

---

# Grid

The Grid is responsible for storing every Tile.

Coordinates follow a two-dimensional Cartesian system.

```text
(0,0) (1,0) (2,0)

(0,1) (1,1) (2,1)

(0,2) (1,2) (2,2)
```

The Grid provides:

- Tile lookup
- Tile replacement
- Neighbor search
- Coordinate validation

---

# Position

Positions identify locations inside the Grid.

Each Position contains:

- X coordinate
- Y coordinate

Positions are immutable and comparable.

Example:

```python
Position(10, 5)
```

---

# Tile

A Tile represents a single cell of the world.

Each Tile stores:

- Position
- Terrain
- Natural resources

Example:

```python
Tile(
    position=Position(5, 8),
    terrain=TerrainType.FOREST,
    resources=[
        Resource(ResourceType.WOOD, 120),
        Resource(ResourceType.FOOD, 40),
    ],
)
```

---

# Terrain

Currently supported terrain types:

- Plain
- Forest
- Mountain
- Water
- Desert

Each terrain defines which natural resources may appear on that tile.

---

# Resources

Resources represent materials available in the environment.

Current resource types:

- Wood
- Stone
- Water
- Food
- Ore

A Tile may contain multiple resources simultaneously.

---

# Procedural Generation

World generation is handled by the `WorldGenerator`.

Generation process:

```text
Seed
 │
 ▼
Create Grid
 │
 ▼
Generate Terrain
 │
 ▼
Distribute Resources
 │
 ▼
Create World
```

The same seed always generates the same world.

Different seeds generate different worlds.

---

# Integration with Simulation

The World is owned by the Simulation.

Initialization flow:

```text
Simulation.start()

        │
        ▼

WorldGenerator.generate()

        │
        ▼

World
```

Every simulation Tick updates the World.

```text
Tick

│

├── Clock

├── Scheduler

└── World.update()
```

---

# Future Extensions

The current implementation provides the foundation for future systems, including:

- Living entities
- Civilizations
- Climate
- Rivers
- Resource regeneration
- Biomes
- Environmental events