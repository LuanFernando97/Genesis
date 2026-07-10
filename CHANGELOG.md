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