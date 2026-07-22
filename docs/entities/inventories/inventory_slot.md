# InventorySlot

## Overview

`InventorySlot` represents a stack of identical items inside an inventory.

Each slot stores a single `Item` instance together with its current quantity.

---

# Responsibilities

The class is responsible for:

- Storing one item.
- Storing its quantity.
- Increasing quantity.
- Decreasing quantity.
- Validating stack operations.

---

# Structure

```
InventorySlot
│
├── Item
└── Quantity
```

---

# Construction

A slot requires an item.

```python
slot = InventorySlot(item)
```

A custom quantity may also be provided.

```python
slot = InventorySlot(item, quantity=10)
```

---

# Validation

InventorySlot enforces the following rules.

| Validation | Behavior |
|------------|----------|
| Missing item | Raises `TypeError` |
| Quantity ≤ 0 | Raises `ValueError` |
| Add quantity ≤ 0 | Raises `ValueError` |
| Remove quantity ≤ 0 | Raises `ValueError` |
| Remove more than available | Raises `ValueError` |

---

# Operations

Increase quantity.

```python
slot.add(5)
```

Decrease quantity.

```python
slot.remove(2)
```

The slot never allows invalid quantities.

---

# Integration

Slots are managed exclusively by `Inventory`.

```
Inventory
    │
    ├── InventorySlot
    ├── InventorySlot
    └── InventorySlot
```

Users of the inventory normally interact with the inventory itself rather than individual slots.