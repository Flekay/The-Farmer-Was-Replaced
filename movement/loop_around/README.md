# Loop Around Movement

This directory contains functions and scripts designed to facilitate seamless looping movements within the game world. These utilities enable the player to traverse the map efficiently, handling edge cases where the map wraps around its boundaries.

## Functions

### `navi-world.py`
Precomputes movement paths for the entire world. Currently optimized for even-sized maps, this script generates a comprehensive set of moves to navigate the player across the entire map seamlessly.

### `navi-map.py`
Generates movement sequences based on the current world size and player position. Utilizes recursive logic to handle large maps by breaking them down into manageable segments.

### `navi-map-light.py`
A streamlined version of `navi-map.py` with reduced functionality. Focuses on essential movement without support for custom path lengths, offering faster setup times.

### `navi-map-inline.py`
Provides inline generation of move sequences, enhancing flexibility and reducing the need for precomputed data. Adapts dynamically to different world sizes, ensuring consistent performance.

### `navi-to-next-tile.py`
Precomputes the necessary moves to transition the player to the next tile. Ensures consistent and predictable traversal paths across the map.

### `move-to-next-tile.py`
Calculates the immediate next move required to advance the player to the adjacent tile based on the current position. Utilizes simple conditional logic for quick execution.

### `navi-world.py`
Handles the generation of movement paths for the entire world, ensuring that the player can navigate from any position to any other position without encountering boundaries.

## Benchmarking

To assess the performance of the movement functions, execute the `benchmark.py` script. This will evaluate each movement method's setup time and operational efficiency, providing insights into their suitability for different scenarios.

### Benchmark Results from `benchmark.py`

| File                  | Setup Time | Operations per Benchmark |
| --------------------- | ---------- | ------------------------ |
| navi-map.py           |    0.0915s |                      360 |
| navi-map-light.py     |    0.0303s |                      300 |
| navi-map-inline.py    |    0.0049s |                      450 |
| move-to-next-tile.py  |          - |                      402 |
| navi-to-next-tile.py  |    0.127s  |                      402 |
