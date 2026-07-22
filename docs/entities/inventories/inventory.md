# Inventory

## Overview

`Inventory` is responsible for storing every item owned by a human.

Internally it manages a collection of `InventorySlot` objects and automatically groups identical items into the same slot.

---

# Responsibilities

The inventory is responsible for:

- Storing item stacks.
- Adding items.
- Removing items.
- Querying quantities.
- Checking item existence.
- Removing empty slots automatically.

---

# Internal Structure

```
Inventory
│
├── InventorySlot
│      ├── Item
│      └── Quantity
│
├── InventorySlot
│      ├── Item
│      └── Quantity
│
└── ...
```

---

# Construction

An inventory starts empty.

```python
inventory = Inventory()
```

---

# Adding Items

Items can be added with a quantity.

```python
inventory.add(item)
```

```python
inventory.add(item, quantity=10)
```

If the item already exists, its quantity is increased.

Otherwise a new slot is created.

---

# Removing Items

```python
inventory.remove(item)
```

```python
inventory.remove(item, quantity=5)
```

Removing the last item automatically removes the slot from the inventory.

---

# Querying

Check the quantity.

```python
inventory.quantity(item)
```

Check if an item exists.

```python
inventory.contains(item)
```

---

# Read-only Slots

The inventory exposes its slots through a read-only property.

```
Inventory
    │
    └── slots
```

Consumers may inspect the inventory but should not manipulate its internal collection directly.

---

# Validation

The inventory validates every operation.

| Validation | Behavior |
|------------|----------|
| Add quantity ≤ 0 | Raises `ValueError` |
| Remove quantity ≤ 0 | Raises `ValueError` |
| Item not found | Raises `ValueError` |
| Remove more than available | Raises `ValueError` |

---

# Integration

Every `Human` owns exactly one inventory.

```
Human
    │
    └── Inventory
            ├── InventorySlot
            ├── InventorySlot
            └── ...
```

If no inventory is provided during construction, an empty one is automatically created.

---

# Future Improvements

The inventory was designed to be expanded with features such as:

- Maximum capacity
- Weight system
- Equipment slots
- Stack limits
- Item categories
- Sorting
- Filters
- Serialization

The current implementation focuses on providing a simple and reusable inventory suitable for the first stages of the simulation.