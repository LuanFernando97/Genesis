# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [0.1.0] - 2026-07-10

### Added

- Initial project structure
- Python virtual environment configuration
- `pyproject.toml` configuration
- Development tools setup
- Basic project documentation
- Initial repository configuration

### Documentation

- Created initial README
- Defined project goals and learning objectives
- Documented development principles

---

## [0.1.1] - 2026-07-10

### Added

- Implemented the core simulation engine.
- Added `Simulation` class responsible for controlling the simulation lifecycle.
- Added simulation states:
  - CREATED
  - RUNNING
  - PAUSED
  - STOPPED
- Added `Clock` system for internal simulation time management.
- Added tick-based simulation progression.
- Added `Scheduler` system for future event execution.
- Added event scheduling and execution support.
- Added simulation lifecycle controls:
  - Start
  - Pause
  - Resume
  - Stop
- Added simulation speed control with configurable limits.
- Added main simulation loop running on a dedicated thread.
- Added logging support for simulation execution cycles.

### Changed

- Expanded project architecture with a simulation execution layer.
- Added core runtime components under `genesis.core`.


### Testing

- Added unit tests for:
  - Simulation lifecycle
  - Clock
  - Tick execution
  - Scheduler
  - Event execution
  - Speed control
- Added test coverage for the simulation engine flow.

### Documentation

- Added simulation engine documentation.
- Added Clock architecture documentation.
- Added Scheduler documentation.
- Updated README with simulation execution instructions.

---

## [0.2.0] - 2026-07-13

### Added

- Implemented the world system.
- Added `World` class representing the simulation environment.
- Added `Grid` structure for storing world tiles.
- Added immutable `Position` coordinate system.
- Added `Tile` class representing individual map cells.
- Added terrain system with the following terrain types:
  - Plain
  - Forest
  - Mountain
  - Water
  - Desert
- Added natural resource system with:
  - Wood
  - Stone
  - Water
  - Food
  - Ore
- Added procedural world generation through `WorldGenerator`.
- Added deterministic world generation using configurable seeds.
- Added resource distribution rules based on terrain types.
- Integrated the world system into the simulation engine.
- Added world update execution during simulation ticks.
- Added world generation and update logging.

### Changed

- Expanded the project architecture with a dedicated world module.
- Updated the simulation initialization flow to automatically generate the world.
- Improved project structure by introducing infrastructure components shared across systems.

### Testing

- Added unit tests for:
  - World
  - Grid
  - Position
  - Tile
  - Terrain
  - Resource
  - WorldGenerator
- Added integration tests between `Simulation` and `World`.
- Improved overall test coverage for the world system.

### Documentation

- Added world system documentation.
- Documented the Grid architecture.
- Documented the coordinate system.
- Documented procedural world generation.
- Updated the project architecture documentation.
- Updated README with world generation examples.

---

## [0.3.0] - 2026-07-14

### Added

- Implemented the entity infrastructure.
- Added abstract `Entity` base class.
- Added entity lifecycle management through `spawn()` and `despawn()`.
- Added `EntityRegistry` for managing active entities.
- Added `EntityIdGenerator` for automatic entity identification.
- Added globally unique UUID generation for entities.
- Added incremental display IDs for each entity type.
- Added automatic entity registration during spawn.
- Added automatic entity removal during despawn.
- Added entity state tracking through `is_alive`.

### Changed

- Expanded the project architecture with a dedicated entity module.
- Introduced a centralized entity lifecycle management model.
- Improved the foundation for future autonomous entity implementations.

### Testing

- Added unit tests for:
  - Entity
  - EntityRegistry
  - EntityIdGenerator
- Added lifecycle tests covering entity spawning and despawning.
- Added tests for UUID generation and incremental display IDs.
- Improved overall test coverage for the entity infrastructure.

### Documentation

- Added entity infrastructure documentation.
- Documented the entity lifecycle.
- Documented the entity identification strategy.
- Updated the project architecture documentation.
- Updated README with the entity system.
  
---

## [0.4.0] - 2026-07-21

### Added

- Implemented the first autonomous agent: `Human`.
- Added immutable human identity:
  - Name
  - Sex
  - Age
- Added `Sex` enumeration.
- Added `HumanState` enumeration with initial behavior states.
- Added the `Needs` system:
  - Energy
  - Hunger
  - Thirst
  - Health
- Added configurable human positioning through `Position`.
- Added reusable inventory system.
- Added abstract `Item` class.
- Added `InventorySlot` for stack management.
- Added `Inventory` for storing multiple item stacks.
- Added automatic inventory creation for humans.
- Added configurable inventory injection through the constructor.
- Added automatic human updates through the simulation.
- Added recurring entity update events managed by the `Scheduler`.
- Added logging for human update cycles.

### Changed

- Expanded the project architecture with the first autonomous agent implementation.
- Simulation now updates registered entities through recurring scheduled events.
- Improved the separation between the simulation engine and entity behavior.
- Refactored entity updates to be fully event-driven.

### Testing

- Added unit tests for:
  - Human
  - Needs
  - HumanState
  - Item
  - InventorySlot
  - Inventory
- Added integration tests covering:
  - Human updates during simulation.
  - Multiple human updates.
  - Scheduler-driven entity updates.
  - Entity lifecycle integration with the simulation.
- Improved overall test coverage for the agent system.

### Documentation

- Added Human documentation.
- Added Needs documentation.
- Added HumanState documentation.
- Added Item documentation.
- Added InventorySlot documentation.
- Added Inventory documentation.
- Updated Simulation documentation.
- Updated Scheduler documentation.
- Updated project architecture documentation.
