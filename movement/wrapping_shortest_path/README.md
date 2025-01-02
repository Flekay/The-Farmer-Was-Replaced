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
Similar to `navi-to-dict.py`, but utilizes ~~lists~~ tuples instead of dictionaries to store movement data. Changed from 2d Lists to 1d Tuples to increased setup time. Setup time can be reduced even further by directly assaining the variable instead of using the function. e.g. `navi-to-list.py - known positions`

### `navi-to-dict.py`
Pre-calculates the moves from each x,y coordinate to every other x,y coordinate. This approach reduces computation time during execution by using precomputed paths.


## Benchmark
To benchmark the movement functions, run the `benchmark.py` script. This will execute each movement method against a predefined set of target positions and report the setup time and operations performed.

### Benchmark Results from `benchmark.py`

| File                              | Setup Time | Operations per Benchmark |
| --------------------------------- | ---------- | ------------------------ |
| move-to.py                        |          - |                      600 |
| navi-to-dict.py                   |    0.0915s |                      300 |
| navi-to-list.py                   |    0.0024s |                      240 |
| navi-to-list.py - known positions |    0.0013s |                      180 |
| navi-pos-to-pos.py                |    6.6732s |                      240 |
| navi-pos-to-pos-func.py           |    4.8067s |                      241 |
| gen-move-to.py                    |    0.0049s |                      450 |


## Important Notes
- `navi-pos-to-pos.py` and `navi-pos-to-pos-func.py` are not recommended for use in the game due to their high setup times compared to other methods.
- `gen-move-to.py` is considered a `navi` method as it hardcodes the world size.
- `move-to.py` is primarily used for debugging and testing purposes.
- `navi-to-dict.py` is generally not recommended anymore due to the increased cost of using dictionaries.
- `navi-to-list.py` is currently the most efficient choice for most scenarios.
- Most functions allow you to pass current position as an argument to increase performance even more. e.g. `navi-to-list.py - known positions`
