# Polyculture Wood
These polyculture wood scripts are designed to teach you the core concepts of each algorithm. They are not optimized for speed or efficiency, but rather to provide a clear understanding of how each method works.

## functions

### `grid.py`
This is the most basic script that uses a grid-based approach to plant and harvest trees.

### `gridpop.py`
popwood and grid hybrid approach.

### `popwood.py`
This script is the same as `popcarrot.py` but for wood.

### `hypotenuse.py`
This script moves diagonally to plant and harvest trees.

## Benchmarks

### Benchmark Results
| file         | leaderboard time |
| -----------  | ---------------- |
| gridpop.py   |         0:24.058 |
| popwood.py   |         0:26.226 |
| grid.py      |         0:26.873 |
| hypotenuse.py|         0:31.015 |

## Important Notes
- Polyculture leaderboards usually requires you to split the code into 3 distinct phases: initial planting, main loop, and cleanup. These scripts only contain the main loop because initial planting and cleanup are not necessary and almost identical to the main loop and make it easier to focus on the core algorithm.
