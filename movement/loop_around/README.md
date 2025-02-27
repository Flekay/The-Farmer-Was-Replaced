# Loop Around Movement

This directory contains functions and scripts designed to facilitate seamless looping movements within the game world. These utilities enable the player to traverse the map efficiently, handling edge cases where the map wraps around its boundaries.

## Functions

### `map_adv.py`
Generates movement sequences based on the current world size and player position. Utilizes recursive logic to handle large maps by breaking them down into manageable segments. Support for custom path lengths and custom starting positions.

### `map_inline.py`
Provides inline generation of move sequences reducing the need for precomputed data. Adapts dynamically to different world sizes, ensuring consistent performance.

### `map_light.py`
A streamlined version of `map_adv.py` with reduced functionality. Focuses on essential movement without support for custom path lengths or starting positions to optimize setup time.

### `map_pos.py`
Simular to `map_adv.py` but returns a tuple with direction and current position.

### `map_local.py`
I forgot what this does.

### `move_to_next_tile.py`
Calculates the immediate next move required to advance the player to the adjacent tile based on the current position. Utilizes simple conditional logic for quick execution.

### `navi_to_next_tile.py`
Precomputed movement sequences for each tile to the next tile. Ensures consistent and predictable traversal paths across the map.

### `world_adv.py`
This script pre-calculates the moves to the next tile for each tile. Without using world wrapping. Currently only works for even-sized maps.

## Benchmarking

To assess the performance of the movement functions, execute the `benchmark.py` script. This will evaluate each movement method's setup time and operational efficiency, providing insights into their suitability for different scenarios.

### Benchmark Results from `benchmark.py`

| File                        | Setup Ticks | Ticks per Benchmark |
| --------------------------- | ----------- | ------------------- |
| map_adv.py                  |         610 |                   1 |
| map_light.py                |         117 |                   1 |
| map_inline.py               |          15 |                  12 |
| map_pos.py                  |         517 |                   1 |
| move_to_next_tile.py        |           1 |                 402 |
| navi_to_next_tile.py        |          16 |                 402 |

## Important Notes
- The `map_light.py` is the best choice for most scenarios, because it has a low setup time and a good performance.
- The `map_adv.py` and `map_inline.py` only have some niche use cases.
- The `world_adv.py` was created for in the previous version of the game to fit a non full field pumpkin in the 60s best stats time window. It is currently not used in the game.
- The `navi_to_next_tile.py` and `move_to_next_tile.py` currently don't have a real use case in the game.
