# Non Wrapping Shortest Path

This folder contains functions related to calculating the shortest wrapping path for movement. These functions determine the most efficient way to move the player to a specific position on a non wrapped map.

## Functions

### `goto-local.py`
Similar to `navi-pos-to-pos.py`, but without wrapping around the map.

### `goto.py`
Calculates the moves to a specific position on the fly. It moves east or west and north or south accordingly.

### Benchmark Results from `benchmark.py`
This is the same benchmark as in the `wrapping_shortest_path` folder, but with the functions from this folder.

| File                       | Setup Time | Operations per Benchmark |
| -------------------------- | ---------- | ------------------------ |
| goto.py                    |          - |                     7560 |
| goto-local.py              |    7.7344s |                     7440 |
