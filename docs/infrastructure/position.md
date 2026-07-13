# Position

## Objective

The `Position` class represents a coordinate inside the simulation space.

It belongs to the infrastructure layer and provides a generic structure for representing locations, allowing it to be reused by different systems throughout the project.

At this stage, it will mainly be used by the world system (`World`), `Grid`, and `Tile`.

---

# Responsibilities

The `Position` class is responsible for:

* Storing X/Y coordinates
* Representing a location in space
* Comparing positions
* Performing mathematical operations between coordinates
* Providing a debug representation

The class is **not responsible for**:

* Validating world boundaries
* Searching elements inside the world
* Controlling movement
* Knowing about Tiles or entities

Those responsibilities belong to higher-level systems, such as `World` and `Grid`.

---

# Structure

A position is defined using two coordinates:

```python
position = Position(10, 5)
```

Representation:

```text
X = 10
Y = 5
```

---

# Operations

## Comparison

Allows checking whether two positions represent the same point.

Example:

```python
Position(10, 5) == Position(10, 5)

# True
```

---

## Addition

Allows combining coordinate offsets.

Example:

```python
Position(10, 5) + Position(2, 3)

# Position(x=12, y=8)
```

---

## Subtraction

Allows calculating the difference between coordinates.

Example:

```python
Position(10, 5) - Position(2, 3)

# Position(x=8, y=2)
```

---

# Usage Example

```python
player_position = Position(10, 5)

movement = Position(1, 0)

new_position = player_position + movement

# Position(x=11, y=5)
```

---

# Future Integrations

The `Position` class will be used by:

* `World`
* `Grid`
* `Tile`
* Simulation entities
* Movement systems
* Pathfinding systems

---

# Tests

The class contains tests covering:

* Position creation
* Coordinate storage
* Position comparison
* Position addition
* Position subtraction
* Debug representation

Test file:

```text
tests/
└── infrastructure/
    └── test_position.py
```
