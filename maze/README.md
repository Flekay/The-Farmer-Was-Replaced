# Maze
This is a small competition to find the fastest script to solve a maze. The goal is to collect all treasures as fast as possible. The maze is generated randomly, and the treasures are placed randomly. The maze is solved by moving around the grid and collecting treasures

## Functions

### `Left_Hand_Rule.py` ( LHR )
This is a simple and efficient variation of the left-hand rule. It follows the left wall of the maze until it reaches a dead end. It then backtracks and continues to follow the left wall until it finds the exit. This algorithm is particularly effective in mazes with a clear path to the exit. Its primary use is for `exploration` and `mapping` the maze.

### `Indexed_Left_Hand_Rule.py` ( iLHR )
Identical to the `Left_Hand_Rule.py` but uses an index to keep track of the current direction. Its a bit slower and harder to read.

### `Depth_First_Search.py` ( DFS )
This is a simple `depth-first search` algorithm. It uses a stack to keep track of the current path and backtracks when it reaches a dead end. Its primary use is for `exploration` and `mapping` the maze.

### `Recursive_Depth_First_Search.py` ( rDFS )
This is a simple, `recursive depth-first search` algorithm. It works exactly like normal DFS but uses recursion instead of a stack. Its faster and more popular than the normal DFS because of its simplicity and speed.

### `Shared_Vector_Flow_Field.py` ( vehn )
original code by @Zapakh strategy first implemented by @Vehn.
This is a simple implementation of a `shared vector flow field` algorithm commonly named after its pioneer, @Vehn. It uses a single vector field to guide the drone through the maze by using Intersection Stitching. This algorithm is particularly effective in early maze stage navigation where there are only a few available paths. For generating the flow field BFS is used.

### `random.py`
This script moves randomly until the tresure is found. Its more of a joke than a real script. But it works.

### `nogo.py`
This script never even tries to solve the maze it just counts on your luck to spawn above the teasure. stupid but works.

### `zero_tick_maze_runner.py`
This abomination from @kalpyy uses dynamic functions as logic gates to solve the maze for "free". Has been patched and is no longer free. Quite laggy and slow.

### `Recursive_Astar.py`
code by @kalpyy
can also be found on his [github](https://github.com/Kalpyy/The-Farmer-Was-Replaced/tree/main/maze/Simple-Astar) and [discord](https://discord.com/channels/988081966035402783/1344014508791697549)
This is kalpyys implementation of a optimized dual queue A* algorithm.


## Early Maze Leaderboard 1x20 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 20 treasures.
| # | file                                | min       | max       | avg       |
| - | ----------------------------------- | --------- | --------- | --------- |
| 0 | Shared_Vector_Flow_Field.py         |   7.0707s |  13.4355s |   9.6710s |


## Mid Maze Leaderboard 1x100 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 100 treasures.
| # | file                                | min       | max       | avg       |
| - | ----------------------------------- | --------- | --------- | --------- |
| 0 | Shared_Vector_Flow_Field.py         |  20.3616s |  34.4092s |  25.9778s |


## Late Maze Leaderboard 1x300 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 300 treasures.
| # | file                                | min       | max       | avg       |
| - | ----------------------------------- | --------- | --------- | --------- |
| 0 | Shared_Vector_Flow_Field.py         |  47.1636s |  65.3409s |  54.2558s |
| 0 | zero_tick_maze_runner.py            |  2315.71s |  2315.71s |  2315.71s |
