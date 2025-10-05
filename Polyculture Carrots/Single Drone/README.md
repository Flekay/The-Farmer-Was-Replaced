# Polyculture Carrot
This is a collection of scripts that are used to farm carrots using polyculture.

## functions

### `popcarrot.py`
This script is the same as `pophay.py` but for carrots.

### `strip.py`
This plants and harvests a single strip of carrots over and over again.

### `gridpop.py`
Simular to `popcarrot.py`, but instead of the entire field, it focuses on a checkerboard pattern.

### `brick.py`
This plants multiple strips of carrots.

## Benchmarks
benchmarks with "-" have a less than 100% success rate and are therefore not able to compete in leaderboard runs.

### Benchmark Results
| file         | leaderboard time |
| -----------  | ---------------- |
| gridpop.py   |         0:58.191 |
| popcarrot.py |         1:01.991 |
| brick.py     |         1:23.603 |
| strip.py     |         1:34.172 |

## Important Notes
- Polyculture leaderboards usually requires you to split the code into 3 distinct phases: initial planting, main loop, and cleanup. These scripts only contain the main loop because initial planting and cleanup are not necessary and almost identical to the main loop and make it easier to focus on the core algorithm.
