# Simulation Engine

## Overview

The Simulation Engine is the core responsible for controlling the execution of the simulated world.

Its main responsibilities are:

- Managing the simulation lifecycle;
- Advancing simulation time;
- Processing scheduled events;
- Controlling simulation speed;
- Running the continuous execution loop.

The main class responsible for the engine is:

```python
Simulation
```

---

# Architecture

The engine is composed of the following components:

```
Simulation

 ├── Clock
 │     └── Internal time management
 │
 ├── Scheduler
 │     └── Future event management
 │
 ├── Tick System
 │     └── Simulation advancement unit
 │
 ├── State Machine
 │     └── Lifecycle management
 │
 └── Main Loop
       └── Continuous execution
```

---

# Simulation States

The simulation lifecycle is controlled through four states.

## CREATED

Initial state.

The simulation object has been created but execution has not started yet.

---

## RUNNING

The simulation is actively executing.

While running:

- The Clock advances;
- Scheduled events are processed;
- Simulation systems are updated.

---

## PAUSED

The simulation execution is temporarily suspended.

The current state is preserved.

No ticks are executed until the simulation is resumed.

---

## STOPPED

The simulation execution has finished.

The execution thread is terminated and the simulation cannot continue.

---

# Lifecycle Flow

The expected lifecycle is:

```
CREATED

   |
   v

start()

   |
   v

RUNNING

   |
   +----------+
   |          |
   v          |
PAUSED        |
   |          |
resume()      |
   |          |
   +----------+

   |
   v

STOPPED
```

---

# Simulation Speed

Simulation speed defines how many simulation ticks are executed per second of real time.

Example:

```
Speed 1x

1 second in real time
=
1 simulation tick
```

```
Speed 10x

1 second in real time
=
10 simulation ticks
```

The engine uses speed limits:

```python
MIN_SPEED = 1
MAX_SPEED = 100
```

Values outside this range are automatically adjusted.

---

# Thread Execution

The simulation loop runs in its own execution thread.

Flow:

```
Main Thread

     |
     v

Simulation Thread

     |
     v

run()

     |
     v

tick()
```

This architecture allows future features such as:

- Graphical interfaces;
- External controls;
- Real-time visualization;
- Multiple simulation environments.