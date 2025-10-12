# Line Formation

This directory contains multi-drone coordination functions that execute a given function across the entire grid using different spawning strategies.

## Functions

### `for_all.py`
The standard multi-drone implementation from the ingame documentation. Spawns drones in a line formation moving east, with each drone executing the provided function while moving north across the grid.

#### How to use:
```python
from for_all import for_all

def my_function():
    # Your farming logic here
    harvest()

for_all(my_function)
```

### `for_all_sync_col.py` and `for_all_sync_row.py`
Two synchronized versions where all drones are spawned first, then move in a coordinated pattern ensuring all drones stop at the same time. Hardcoded for maximum world size for leaderboard optimization. These files are functionally identical - the only difference is the movement direction (East/West vs South/North).

#### How to use:
```python
from for_all_sync_col import for_all_sync_col
# OR
from for_all_sync_row import for_all_sync_row

def my_function():
    # Your farming logic here
    harvest()

for_all_sync_col(my_function)
# OR
for_all_sync_row(my_function)
```

### `for_all_dual.py`
Uses two spawner drones positioned strategically. Both spawners remain stationary at their starting positions while the worker drones move to their assigned positions before executing the function. Provides better coverage and reduced movement overhead by dividing the work between two spawners.

**Implementation details:**
- Main spawner (at position 0,0) spawns worker drones for the left half of the grid
- Second spawner (spawned by main) stays at origin and spawns worker drones for the right half
- Each worker drone moves to its assigned column position before executing the row function
- Main spawner executes the first column (position 0)
- Second spawner moves once at the end to execute the last column (rightmost position)
- Worker drones handle all intermediate columns

#### How to use:
```python
from for_all_dual import for_all

def my_function():
    # Your farming logic here
    harvest()

for_all(my_function)
```


## Benchmarking

To assess the performance of the movement functions, execute the `benchmark.py` script. This will evaluate each movement method's runtime and wait time, providing insights into their execution efficiency and coordination overhead.

### Benchmark Results from `benchmark.py`

| File                        | Runtime Ticks | Wait Time Ticks |
| --------------------------- | ------------- | --------------- |
| for_all.py                  |         25006 |               3 |
| for_all_dual.py             |         16224 |               5 |
| for_all_sync_col/row.py     |         16224 |               5 |
