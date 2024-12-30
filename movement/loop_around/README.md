# Loop Around Movement

This directory contains functions and scripts designed to facilitate seamless looping movements within the game world. These utilities enable the player to traverse the map efficiently, handling edge cases where the map wraps around its boundaries.

## Functions

### `map-adv.py`
Generates movement sequences based on the current world size and player position. Utilizes recursive logic to handle large maps by breaking them down into manageable segments. Support for custom path lengths and custom starting positions.

### `map-inline.py`
Provides inline generation of move sequences reducing the need for precomputed data. Adapts dynamically to different world sizes, ensuring consistent performance.

### `map-light.py`
A streamlined version of `map-adv.py` with reduced functionality. Focuses on essential movement without support for custom path lengths or starting positions to optimize setup time.

### `map-local.py`
I forgot what this does.

### `move-to-next-tile.py`
Calculates the immediate next move required to advance the player to the adjacent tile based on the current position. Utilizes simple conditional logic for quick execution.

### `navi-to-next-tile.py`
Precomputes the necessary moves to transition the player to the next tile. Ensures consistent and predictable traversal paths across the map.

### `world-adv.py`
This script pre-calculates the moves to the next tile for each tile. Withouth using world wraping. Currently only works for even sized maps.

## Benchmarking

To assess the performance of the movement functions, execute the `benchmark.py` script. This will evaluate each movement method's setup time and operational efficiency, providing insights into their suitability for different scenarios.

### Benchmark Results from `benchmark.py`

| File                        | Setup Time | Operations per Benchmark |
| --------------------------- | ---------- | ------------------------ |
| map-adv.py                  |        609 |                        1 |
| map-light.py                |        116 |                        1 |
| map-inline.py               |         14 |                       12 |
| move-to-next-tile.py        |          - |                      402 |
| navi-to-next-tile.py        |        127 |                      402 |

## Important Notes
- The `map-light.py` is the best choice for most scenarios, because it has a low setup time and a good performance.
- The `map-adv.py` and `map-inline.py` only have some niche use cases.
- The `world-adv.py` was created for in the previous version of the game to fit a non full field pumpking in the 60s best stats time window. It is currently not used in the game.
- The `navi-to-next-tile.py` and `move-to-next-tile.py` currently dont have a real use case in the game.
