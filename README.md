# Genesis

> **Genesis** is an experimental project focused on building a civilization simulation from scratch using autonomous agents and emergent behavior.

## About

Genesis is a personal learning project created to explore software engineering, artificial intelligence, concurrent programming, and simulation systems by developing a virtual world where autonomous agents interact and evolve over time.

The goal is **not** to build a game, but to understand how complex behaviors and societies can emerge from simple rules and interactions.

The project will be developed incrementally, starting from an empty simulation engine and gradually introducing new mechanics and systems.

---

# Learning Goals

Throughout the development of Genesis, the following topics will be explored:

- Software Architecture
- Object-Oriented Programming
- Concurrent Programming
- Agent-Based Simulation
- Artificial Intelligence
- Emergent Systems
- Data Structures
- Algorithms
- Design Patterns
- Automated Testing
- Performance Optimization

---

# Project Goals

Some of the questions this project aims to explore include:

- How can autonomous agents make decisions?
- How do societies emerge from simple interactions?
- How do limited resources affect behavior?
- How can simple rules generate complex systems?
- How can a large-scale simulation remain modular and maintainable?

---

# Current Status

> 🚧 Early development.

The simulation engine, procedural world generation, and entity infrastructure are implemented.
Future phases will introduce autonomous entities, behaviors, and civilizations.

---

# Development Principles

Genesis follows a few core principles:

- Simplicity before complexity
- Incremental development
- Modular architecture
- Low coupling
- High cohesion
- Testability
- Continuous documentation
- Learning over speed

---

# Installation

## Requirements

- Python 3.11+

---

## Clone repository

```bash
git clone https://github.com/LuanFernando97/Genesis.git

cd Genesis
```

---

## Create virtual environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install project

```bash
pip install -e .
```

---

## Install development dependencies

```bash
pip install -e ".[dev]"
```

---

# Development

## Code Quality

Genesis uses:

- pytest for automated tests
- ruff for linting, import organization and code formatting
- pre-commit for automated code quality checks

## Pre-commit

Install hooks:

```bash
pre-commit install
```
Run manually:
```bash
pre-commit run --all-files
```
Run tests:

```bash
pytest
```


---
# Logging

Genesis uses Python's built-in logging system.

The logging system is organized by simulation execution and context.

Each execution creates a unique log directory:

```
logs/
└── YYYY-MM-DD_HH-MM-SS/
    ├── genesis.simulation.log
    ├── genesis.world.log
    └── genesis.agent.log
```

Loggers are created dynamically by context:

```python
logger = get_logger("genesis.world")
```

Available log levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Generated log files are ignored by Git and are not versioned.
---
# Running

After installing the project dependencies, execute:

```bash
python -m genesis.main
```

The simulation initializes:

- Clock
- Scheduler
- Procedurally generated World
- Entity infrastructure

In realtime mode, the simulation automatically starts executing simulation ticks.

Example output:

```
Simulation loop started

tick=1
tick=2
tick=3

Simulation loop finished
```

---
# World Generation

The simulation now includes a deterministic procedural world generation system.

Example:

```python
from genesis.simulation.simulation import Simulation
from genesis.simulation.simulation import SimulationMode

simulation = Simulation(
    world_width=100,
    world_height=100,
    seed=12345,
    mode=SimulationMode.STEP,
)

simulation.start()

world = simulation.world
```

The same seed always generates the same world, ensuring deterministic simulations.

---

# Current Architecture

The current simulation engine contains:

```
Simulation
    │
    ├── Clock
    └── Scheduler

World
    ├── Grid
    ├── Tiles
    ├── Terrain
    ├── Resources
    └── WorldGenerator

Entity
│
├── EntityIdGenerator
└── EntityRegistry
```

The current implementation provides:

- Simulation lifecycle management
- Clock and Scheduler
- Tick execution system
- Procedural world generation
- Deterministic random seeds
- Grid-based world representation
- Terrain and natural resources
- Base entity infrastructure
- Automatic entity identification
- Entity lifecycle management (`spawn` / `despawn`)
- Centralized entity registry

Future phases will introduce concrete entity types (such as humans and animals), autonomous behaviors, civilizations, and environmental systems.

---

# Project Structure

```
Genesis/
│
├── docs/
│
├── examples/
│
├── logs/
│
├── src/
│   └── genesis/
│
├── tests/
│
├── CHANGELOG.md
├── README.md
├── TODO.md
└── pyproject.toml
```

---

# Contributing

Genesis is currently a personal experimental project.

The main objective is exploration, learning, and incremental development of simulation systems.

---

# Disclaimer

This is an **educational and experimental project**.

Many implementation decisions are intentionally made to explore concepts, experiment with different architectures, and learn new techniques rather than to produce the most optimized or production-ready solution.