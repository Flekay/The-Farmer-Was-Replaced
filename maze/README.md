# Maze
This is a small competition to find the fastest script to solve a maze. The goal is to collect all treasures as fast as possible. The maze is generated randomly, and the treasures are placed randomly. The maze is solved by moving around the grid and collecting treasures

## Functions

### `hugger.py`
This a super short hugger script. It can only be used for mapping or reaching the first treasure. It will get stuck after the first treasure is found.

### `vehn.py`
code by @Zapakh strategy first implemented by @Vehn.
This uses the same logic as the current leaderboard #1 but some optimizations missing.

### `random.py`
This script moves randomly until the tresure is found. Its more of a joke than a real script. But it works.

### `nogo.py`
This script never even tries to solve the maze it just counts on your luck to spawn above the teasure. stupid but works.

### `astar.py`
Work in progress.

### `dfs.py`
Work in progress.

### `bfs.py`
Work in progress.

### `bi-bfs.py`
Work in progress.

### `zero_tick_maze_runner.py`
This abomination from @kalpyy uses dynamic functions as logic gates to solve the maze for "free". Has been patched and is no longer free. Quite laggy and slow.


## Benchmarks
The gold stat is currently a bit broken. So the stats might be a off.

| file             |  gold/min  |
| ---------------- | ---------- |
| nogo.py          |  53k       |
| pro-max.py       | 351k       |
| hugger.py        |  50k       |


## Early Maze Leaderboard 1x20 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 20 treasures.
| # | file            | min       | max       | avg       |
| - | --------------- | --------- | --------- | --------- |
| 0 | vehn.py         |   7.0707s |  13.4355s |   9.6710s |


## Mid Maze Leaderboard 1x100 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 100 treasures.
| # | file            | min       | max       | avg       |
| - | --------------- | --------- | --------- | --------- |
| 0 | vehn.py         |  20.3616s |  34.4092s |  25.9778s |

## Late Maze Leaderboard 1x300 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 300 treasures.
| # | file                     | min       | max       | avg       |
| - | ------------------------ | --------- | --------- | --------- |
| 0 | vehn.py                  |  47.1636s |  65.3409s |  54.2558s |
| 0 | zero_tick_maze_runner.py |  2315.71s |  2315.71s |  2315.71s |


## Important Notes
- Currently known best strategy is to use recursive dfs to scan the map than use a flowfield (vehn.py) for about 40-50 treasures. After that use recursive Astar to collect the rest of the treasures.
- `pro-max.py`, `dfs.py`, `bi-bfs.py`, `astar.py` are all outdated and need to be updated.
