# Bone / Snake
This will be a collection of snake scripts that are used to farm bone.

## functions

### `greedy.py`
This Script tries to move to the apple in a straight line.

### `almighty.py`
Almighty makes the snake move in a circular pattern around the board

### `timon.py`
This is a recreation of Timon's script shown in the first snake video. It is a switches at length 34 from the stack.py script to the almighty.py script.

### `hybrid.py`
This script switches from greedy.py to stack.py at length 20 and switches to almighty.py at length 34.

### `astar.py`
This script uses the A* algorithm to find the shortest path to the goal.

### `rando.py`
This script moves in a random direction until it gets stuck.

### `stack.py`
This script is a modified version of the almighty.py script. It moves in a circular pattern around the board and tries make shortcuts when possible.

### `brainlet.py`
This script is the simplest script that possible. It only harvest one apple before restarting.

### `circle.py`
This script moves in a circular pattern around the board. similar to almighty.py but with a different pattern and shortcuts.

### `drone.py`
Strategy by @drone.
This script just follows simple rules to move to the apple without without getting stuck.

## Benchmarks
benchmarks with "-" have a less than 100% success rate and are therefore not able to compete in leaderboard runs.

### Benchmark Results
| file         | items/min | leaderboard time |
| -----------  | --------- | ---------------- |
| drone.py     |   392 373 |         0:18.845 |
| /circle.py   |   294 280 |         0:23.924 |
| timon.py     |   294 280 |         0:27.889 |
| almighty.py  |   196 000 |         0:42.221 |
| hybrid.py    |   304 000 |                - |
| stack.py     |   196 000 |                - |
| greedy.py    |    55 000 |                - |
| astar.py     |    39 900 |                - |
| brainlet.py  |     8 590 |                - |
| rando.py     |     1 810 |                - |

## Important Notes
- The `drone.py` script is currently not working, but it uses the core concept of drones algorithm.
