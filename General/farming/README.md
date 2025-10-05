# Farming Functions

This folder contains functions that help you automate farming tasks.

## Scripts

### `batch_func.py`
Runs a user-defined function on every tile in the world.
```python
def custom_func():
	...
batch_func(custom_func)
```

### `batch_harvest.py`
Harvests every tile in the field.
```python
batch_harvest()
```

### `batch_plant.py`
Plants the specified entity on every tile.
```python
batch_plant(Entities.Carrot)
```

### `batch_till.py`
Tills each tile in the field.
```python
batch_till()
```

### `batch_water.py`
Waters each tile up to a given threshold.
```python
batch_water(0.5)
```
