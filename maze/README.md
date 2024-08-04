# Maze
This is a small competition to find the fastest script to solve a maze. The goal is to collect all treasures as fast as possible. The maze is generated randomly, and the treasures are placed randomly. The maze is solved by moving around the grid and collecting treasures

## Rules
### DO'S
1. You can reset variables outside the timer.
2. You can preload functions and variables outside the timer.
3. You can print debug information outside the timer.
4. You can split the code into multiple files for better organization.
5. You can use your own `str`, `insort`, `sorted`, `median`, `average` functions. but they must be included in the submission. Consider making a pull request if your functions are faster than then ones in the `general` folder.
6. You don't have to use the example code, but it's recommended to use it as it is easy to use and understand.
7. You can edit your save file to speed up the process.
8. You can edit your save file to have infinite `Fertilizer` and `Sunflower/Power`
9. Check twice if everything included in the submission.

### DON'TS
1. You do not talk about the maze code.
2. You do NOT talk about the maze code.
3. The first action after the timer starts must be the `clear()` function.
4. The last action before the timer ends must be the `harvest()` function.
5. The time must have a precision of 4 digits; missing digits will be counted as 9's.
6. You must verify the collected gold (this can be done outside the timer).
7. You must use `get_time()` or `get_op_count()` for time measurement.
8. Your code must be public for verification.
9. Your file or folder must include all functions used in the maze.
10. You are only allowed to analyze the source code of mazes that are slower than yours.
11. Your submission must include the following: `minimum`, `maximum`, `median`, `average` and the number of runs.
12. The minimum number of runs in a submission is 100.
13. Do not cheat. Have fun! Good luck!

## Example
The functions used in this example (str, insort, sorted, median, average) are available in the `general` folder.
a working template is available in `example.py`. Or you can copy the `maze-savefile` that includes common functions, the template script and a 100x speedup.
short pseudocode example:
```python

// Initialize configurations and constants
Set CATEGORY, MAZE_COUNT, TRIM, ONLY_PRINT_HIGHSCORE, PRINT_CURRENT_LAPS
Initialize maze_stats, lap_count, runtime

// Main loop
For i = 1 to MAZE_COUNT:
	// Reset before each maze
	Reset_code()

	// Solve maze
	gold_at_start = current_gold
	timer_start = current_op_count
	clear()
	do_maze(CHEST_COUNT)

	// Calculate and store results
	harvest()
	lap_time = (current_op_count - timer_start) / OPS
	actual_gold = current_gold - gold_at_start

	If actual_gold != EXPECTED_GOLD:
		Print error message
		Break
	Else:
		Update maze_stats
		If new_highscore or (lap_count == MAZE_COUNT):
			Print statistics

	// Optional reset or custom statistics code
	Post_maze_code()

// End of script

```


## Early Maze Leaderboard 1x20 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 20 treasures.
| # | file            | min       | max       | median    | avg       |
| - | --------------- | --------- | --------- | --------- | --------- |
| 0 | /pro-max        | 8.5139s   | 18.1323s  | 11.2679s  | 11.2679s  |
| 0 | meorin.py       |           |           |           |           |
| 0 | vehn.py         | 10.3037s  | 20.7707s  | 12.8393s  | 12.9266s  |
| 0 | dfs.py          | 14.9768s  | 42.6155s  | 27.4407s  | 27.1052s  |
| 0 | farm-gold.py    |           |           |           |           |
| 0 | hugger.py       |           |           |           |           |
| 0 | tiny-hugger.py  |           |           |           |           |
| 0 | random.py       |           |           |           |           |
| 0 | kuga.py         | 26.9105s  | 37.0566s  | 30.9114s  | 31.0826s  |


## Mid Maze Leaderboard 1x100 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 100 treasures.
| # | file            | min       | max       | median    | avg       |
| - | --------------- | --------- | --------- | --------- | --------- |
| 0 | /pro-max        | 29.1330s  | 49.9307s  | 32.5036s  | 32.5036s  |
| 0 | meorin.py       |           |           |           |           |
| 0 | vehn.py         | 35.0286s  | 51.9207s  | 39.7101s  | 39.5643s  |
| 0 | dfs.py          | 66.4129s  | 128.0101s | 83.6680s  | 86.5905s  |
| 0 | farm-gold.py    |           |           |           |           |
| 0 | hugger.py       |           |           |           |           |
| 0 | tiny-hugger.py  |           |           |           |           |
| 0 | random.py       |           |           |           |           |
| 0 | kuga.py         | 111.4583s | 123.6947s | 115.8458s | 116.0371s |

## Late Maze Leaderboard 1x300 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 300 treasures.
| # | file            | min       | max       | median    | avg       |
| - | --------------- | --------- | --------- | --------- | --------- |
| 0 | /pro-max        | 77.2243s  | 110.5291s | 87.8430s  | 88.4174s  |
| 0 | meorin.py       |           |           |           |           |
| 0 | vehn.py         | 86.2768s  | 110.0054s | 94.6180s  | 94.7839s  |
| 0 | dfs.py          | 131.7877s | 249.2588s | 163.0861s | 163.7300s |
| 0 | farm-gold.py    |           |           |           |           |
| 0 | hugger.py       |           |           |           |           |
| 0 | tiny-hugger.py  |           |           |           |           |
| 0 | random.py       |           |           |           |           |
| 0 | kuga.py         | 326.1511s | 343.9965s | 333.7336s | 333.4588s |

## Speedrun Maze Leaderboard 1x151 (8x8)
This leaderboard changes over time based on the current meta for timed resets.
| # | file            | min       | max       | median    | avg       |
| - | --------------- | --------- | --------- | --------- | --------- |
| 0 | /pro-max        | 34.4651s  | 53.0905s  | 40.6385s  | 40.6385s  |
| 0 | meorin.py       |           |           |           |           |
| 0 | vehn.py         | 38.1625s  | 55.3636s  | 41.9679s  | 43.1850s  |
| 0 | dfs.py          | 58.5108s  | 106.6305s | 72.6535s  | 73.4470s  |
| 0 | farm-gold.py    |           |           |           |           |
| 0 | hugger.py       |           |           |           |           |
| 0 | tiny-hugger.py  |           |           |           |           |
| 0 | random.py       |           |           |           |           |
| 0 | kuga.py         | 113.1489s | 124.3384s | 118.3982s | 118.9357s |


## farm-gold.py
dont know how this works. just copyed it from the internet.

## hugger.py
Old script that was used to farm gold befor fertilizer was a thing. Huggs the wall until the tresure is found.

## tiny-hugger.py
This script is a optimized version of the hugger.py script. It uses the same logic but is faster and way shorter.

## vehn.py
code by @Zapakh strat by @Vehn.
This uses the same logic as the current leaderboard #1 but some optimizations missing.

## dfs.py
This script uses a depth first search algorithm to find the tresure.

## random.py
This script moves randomly until the tresure is found. Its more of a joke than a real script. But it works.

## pro-max.py
Originally called "vehn-pro-max". This is an optimized version of the vehn.py script by @Zapakh. It uses the same logic. pro-max/pro-max.py is the main script. The rest is just helper code.
possible improvements:
- greedy pathfinding after x treasures
- collect treasures while phase 1 (maze exploration) WIP
- better wall/path data structure

## meorin.py
The code employs a hybrid strategy that combines DFS for initial exploration and BFS for efficient pathfinding. This approach allows for thorough exploration of the maze while ensuring the shortest path is found to the goal. The integration of backtracking ensures that dead ends are handled gracefully, allowing the algorithm to find valid paths through the maze.

## kuga.py
This script uses an astar algorithm to calculate the shortest path to the tresure.
