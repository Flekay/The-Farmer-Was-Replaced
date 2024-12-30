# Wrapping Shortest Path

This folder contains functions related to calculating the shortest wrapping path for movement. These functions determine the most efficient way to move the player to a specific position on a wrapped map, where the edges loop around.

## Functions

### `gen-move-to.py`
Generates a dynamic `move_to` function based on the world size. This script only exists because @ThatMerlinGuy insisted on having a not completely hard-coded version of move-to.py.

### `move-to.py`
Calculates the moves to a specific position on the fly. It wraps around the map if a shorter path exists by moving east or west and north or south accordingly.

### `navi-pos-to-pos-func.py`
Slighly modified version of けろびー code.
This script pre-calculates the moves form each position to each position. Similar to navi-pos-to-pos.py but uses functions instead of a dictionary. You can also dump the compiled functions to a file which will reduce the setup time to ~2.4s.

### `navi-pos-to-pos.py`
Generates a comprehensive map of paths between all possible position pairs. It stores these paths in a dictionary for quick lookup and execution.

### `navi-to-list.py`
Similar to `navi-to-tuple.py`, but utilizes lists instead of dictionaries to store movement data. This can potentially reduce setup time by using a generator method.

### `navi-to-tuple.py`
Pre-calculates the moves from each x,y coordinate to every other x,y coordinate. This approach reduces computation time during execution by using precomputed paths.


## Benchmark
To benchmark the movement functions, run the `benchmark.py` script. This will execute each movement method against a predefined set of target positions and report the setup time and operations performed.

### Benchmark Results from `benchmark.py`

| File                       | Setup Time | Operations per Benchmark |
| -------------------------- | ---------- | ------------------------ |
| move-to.py                 |          - |                      660 |
| navi-to-tuple.py           |    0.0915s |                      360 |
| navi-to-list.py            |    0.0303s |                      300 |
| navi-pos-to-pos.py         |    6.6732s |                      240 |
| navi-pos-to-pos-func.py    |    4.8067s |                      241 |
| gen-move-to.py             |    0.0049s |                      450 |


## Important Notes
- The `navi-pos-to-pos.py` and `navi-pos-to-pos-func.py` currently have no real use case in the game, because of the high setup time compared to the other methods.
- The `gen-move-to.py` is technically a `navi` method, because it hardcodes the world size.
- The `move-to.py` and `gen-move-to.py` are most likely be used in quick testing and debugging scenarios.
- The `navi-to-list.py` is currently never a good choice, because it performs worse than `navi-to-list.py` in every aspect.
- The `navi-to-list.py` is the best choice for most scenarios, because it has a low setup time and a good performance.