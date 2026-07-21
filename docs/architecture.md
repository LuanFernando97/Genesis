# Genesis Architecture

## Overview

Genesis is an experimental civilization simulation engine based on autonomous agents and emergent behavior.

The architecture is designed to support incremental development while maintaining:

- Modularity
- Testability
- Low coupling
- Clear separation of responsibilities

The simulation will evolve from simple rules and interactions into increasingly complex systems.

---

# Architectural Principles

## Incremental Development

Every development phase should result in a functional system.

New features should be added gradually without requiring future systems to exist.

---

## Modularity

Each component should have a clear responsibility.

Systems should be independent whenever possible.

Examples:

- Simulation engine
- World management
- Agents
- Resources
- Social systems
- Evolution systems

---

## Low Coupling

Components should communicate through well-defined interfaces.

Changes in one subsystem should have minimal impact on others.

---

## Testability

Core simulation logic should be designed to allow automated testing.

Important behaviors should be reproducible whenever possible.

---

# High-Level Architecture

The current architecture is organized around the simulation engine and the world system.

```
src/
└── genesis/
    │
    ├── simulation/
    │   ├── simulation.py
    │   ├── scheduler.py
    │   └── clock.py
    │
    ├── world/
    │   ├── world.py
    │   ├── world_generator.py
    │   ├── grid.py
    │   ├── tile.py
    │   ├── terrain.py
    │   └── resource.py
    │
    ├── entities/
    │   ├── entity.py
    │   ├── registry.py
    │   ├── id_generator.py
    │   │
    │   ├── humans/
    │   │   ├── human.py
    │   │   ├── human_state.py
    │   │   ├── needs.py
    │   │   └── sex.py
    │   │
    │   └── inventories/
    │       ├── inventory.py
    │       └── inventory_slot.py
    │
    ├── infrastructure/
    │   ├── position.py
    │   └── logger.py
    │
    ├── items/
    │   └── item.py
    │
    └── main.py
```

The architecture is intentionally modular so new simulation systems can be introduced without affecting existing components.

---

# Core Components

## Simulation Engine

Responsible for controlling the simulation lifecycle.

Responsibilities:

- Initialize simulation
- Advance simulation steps
- Manage execution order
- Control simulation time

---

## World

Represents the physical environment of the simulation.

The world is composed of:

- Grid
- Tiles
- Terrain
- Natural Resources

World generation is deterministic and performed through the WorldGenerator using a configurable random seed.

The World is updated once every simulation Tick.

---
## Entities

## Entities

Entities represent every object capable of existing within the simulation.

The entity infrastructure currently consists of:

- Entity
- EntityRegistry
- EntityIdGenerator

The first concrete entity implemented is `Human`.

Every human possesses:

- Identity
- Needs
- Position
- Inventory
- Current State

All entities are automatically registered through the `EntityRegistry` and updated once per simulation tick.

---

# Entity Lifecycle

Entities are responsible for managing their own lifecycle.

Each entity:

- Receives a globally unique UUID.
- Receives an incremental display identifier per entity type.
- Registers itself during `spawn()`.
- Removes itself from the registry during `despawn()`.

The entity registry maintains the set of active entities currently present in the simulation.
---

## Systems

Independent modules responsible for simulation mechanics.

Examples:

- Resource system
- Economy system
- Social system
- Evolution system
- Event system

---

# Data Flow

The simulation follows a cycle:

```
Entity Spawn
    |
    v
World State
    |
    v
Agent Perception
    |
    v
Decision Making
    |
    v
Actions
    |
    v
World Update
    |
    v
Next Simulation Step
```

This cycle repeats throughout the simulation lifecycle.

---

# Concurrency

Concurrency is an area of exploration in Genesis.

Possible approaches include:

- Independent agent execution
- Parallel system updates
- Event-driven processing
- Scheduled simulation steps

The final concurrency model will be defined after initial prototypes and performance analysis.

---

# Logging Strategy

The project will use Python's built-in logging system.

Goals:

- Debug simulation behavior
- Track execution flow
- Record important events
- Identify errors

Rules:

- Logs should not replace simulation data.
- Detailed information should use DEBUG level.
- Log configuration should remain centralized.
- Generated logs should not be committed to Git.

---
# Configuration Strategy

Genesis uses external configuration files to separate simulation parameters from source code.

Configuration files are stored in:
```
config/
└── default.yaml
```
he default configuration contains shared simulation parameters.

Local or environment-specific configurations should not replace the default configuration and should remain outside version control when necessary.

Examples of future configurable parameters:

- Simulation speed
- World dimensions
- Initial population
- Random seed
- Resource settings
---
# Future Architecture Considerations

Possible future components:

- Persistence system
- Save/load simulations
- Visualization layer
- Distributed simulation
- Autonomous agent behaviors
- Advanced AI models
- Performance optimization
- Large-scale world management

---

# Architectural Decisions

Important architecture decisions should be documented separately.

Future decisions should be stored in:

```
docs/decisions/
```

Example:

```
docs/decisions/
├── 0001-concurrency-model.md
├── 0002-agent-architecture.md
└── 0003-world-representation.md
```