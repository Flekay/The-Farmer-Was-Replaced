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
7. You must use `get_time()` or `get_tick_count()` for time measurement.
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


## Benchmarks
The gold stat is currently a bit broken. So the stats might be a off.

| file             |  gold/min  |
| ---------------- | ---------- |
| nogo.py          |  53k       |
| pro-max.py       | 351k       |
| tiny-hugger.py   |  50k       |


## Early Maze Leaderboard 1x20 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 20 treasures.
| # | file            | min       | max       | median    | avg       |
| - | --------------- | --------- | --------- | --------- | --------- |
| 0 | /pro-max        |   6.8815s |  13.8376s |   9.0502s |   9.2787s |
| 0 | vehn.py         |   8.6299s |  14.6499s |  10.9099s |  10.9299s |
| 0 | dfs.py          |           |           |           |           |
| 0 | farm-gold.py    |           |           |           |           |
| 0 | random.py       |           |           |           |           |


## Mid Maze Leaderboard 1x100 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 100 treasures.
| # | file            | min       | max       | median    | avg       |
| - | --------------- | --------- | --------- | --------- | --------- |
| 0 | /pro-max        |  19.2318s |  37.0693s |  24.9337s |  25.5051s |
| 0 | vehn.py         |  23.3799s |  40.3199s |  28.5699s |  28.5399s |
| 0 | dfs.py          |           |           |           |           |
| 0 | farm-gold.py    |           |           |           |           |
| 0 | random.py       |           |           |           |           |

## Late Maze Leaderboard 1x300 (10x10)
This leaderboard aims to show the fastest scripts for a 10x10 maze with 300 treasures.
| # | file            | min       | max       | median    | avg       |
| - | --------------- | --------- | --------- | --------- | --------- |
| 0 | /pro-max        |  47.5013s |  69.6955s |  53.6171s |  53.8510s |
| 0 | vehn.py         |  50.9299s |  73.5099s |  59.7399s |  59.9699s |
| 0 | dfs.py          |           |           |           |           |
| 0 | farm-gold.py    |           |           |           |           |
| 0 | random.py       |           |           |           |           |

## Speedrun Maze Leaderboard 1x151 (8x8)
This leaderboard changes over time based on the current meta for timed resets.
| # | file            | min       | max       | median    | avg       |
| - | --------------- | --------- | --------- | --------- | --------- |
| 0 | /pro-max        |  20.1024s |  32.2629s |  24.5705s |  24.7239s |
| 0 | vehn.py         |  22.6899s |  34.8999s |  26.4699s |  26.7899s |
| 0 | dfs.py          |           |           |           |           |
| 0 | farm-gold.py    |           |           |           |           |
| 0 | random.py       |           |           |           |           |


## farm-gold.py
dont know how this works. just copyed it from the internet.

## hugger.py
This a super short hugger script.

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

## nogo.py
This script never even tries to solve the maze it just counts on your luck to spawn above the teasure. stupid but works.
