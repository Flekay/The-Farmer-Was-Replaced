# Wrapping Shortest Path

This folder contains functions related to calculating the shortest wrapping path for movement. These functions determine the most efficient way to move the player to a specific position on a wrapped map, where the edges loop around.

## Functions

### `gen_move_to.py`
Generates a dynamic `move_to` function based on the world size. This script only exists because @ThatMerlinGuy insisted on having a not completely hardcoded version of `move_to.py`.

### `move_to.py`
Calculates the moves to a specific position on the fly. It wraps around the map if a shorter path exists by moving east or west and north or south accordingly.

### `navi_pos_to_pos_func.py`
Slighly modified version of けろびー code.
This script pre-calculates the moves form each position to each position. Similar to `navi_pos_to_pos.py` but uses functions instead of a dictionary. You can also dump the compiled functions to a file which will reduce the setup time to ~2.4s.

### `navi_pos_to_pos.py`
Generates a comprehensive map of paths between all possible position pairs. It stores these paths in a dictionary for quick lookup and execution.

### `navi_to_list.py`
Similar to `navi_to_dict.py`, but utilizes ~~lists~~ tuples instead of dictionaries to store movement data. Changed from 2d Lists to 1d Tuples to increased setup time. Setup time can be reduced even further by directly assaining the variable instead of using the function. e.g. `navi_to_list.py _ known positions`

### `navi_to_deltalist.py`
Similar to `navi_to_list.py`, but uses 2d tuples to store delta moves

### `navi_to_dict.py`
Pre-calculates the moves from each x,y coordinate to every other x,y coordinate. This approach reduces computation time during execution by using precomputed paths.


## Benchmark
To benchmark the movement functions, run the `benchmark.py` script. This will execute each movement method against a predefined set of target positions and report the setup time and operations performed.

### Benchmark Results from `benchmark.py`

| File                              | Setup Time | Ticks per Benchmark |
| --------------------------------- | ---------- | ------------------- |
| gen_move_to.py                    |    0.0049s |                 450 |
| move_to.py                        |    0.0001s |                 630 |
| navi_pos_to_pos_func.py           |    4.8068s |                 271 |
| navi_pos_to_pos.py                |    6.6757s |                 270 |
| navi_to_deltalist.py              |    0.0069s |                 240 |
| navi_to_dict.py                   |    0.0917s |                 330 |
| navi_to_list.py                   |    0.0017s |                 270 |


## Important Notes
- `navi_pos_to_pos.py` and `navi_pos_to_pos_func.py` are not recommended anymore due to their high setup times compared to other methods.
- `gen_move_to.py` is considered a `navi` method as it hardcodes the world size.
- `move_to.py` is primarily used for debugging and testing purposes.
- `navi_to_dict.py` is generally not recommended anymore due to the increased cost of using dictionaries.
- `navi_to_deltalist.py` is currently the most efficient choice for most scenarios.
- Most functions allow you to pass current position as an argument to increase performance even more.
