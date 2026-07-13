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
