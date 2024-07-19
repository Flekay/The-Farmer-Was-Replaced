# Maze

## Rules
1. You do not talk about the maze code.
2. You do NOT talk about the maze code.
3. The first line after the timer starts must be the `clear()` function.
4. The last line before the timer ends must be the `harvest()` function.
5. The time must have a precision of 4 digits; missing digits will be counted as 9's.
6. You must verify the collected gold (this can be done outside the timer).
7. You must use `get_time()` or `get_op_count()` for time measurement.
8. Preloading and variable resetting is allowed outside the timer.
9. Your code must be public for verification.
10. Your file or folder must include all functions used in the maze.
11. You are only allowed to analyze the source code of mazes that are slower than yours.
12. Your submission must include the following: `minimum`, `maximum`, `median`, `average` and the number of runs.
13. The minimum number of runs in a submission is 100.
14. You are only allowed to submit one script per category.
15. Do not cheat. Have fun! Good luck!

## Example
The functions used in this example (str, insort, sorted, median, average) are available in the `general` folder.
```python
# init code here
BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer

gold_at_start = num_items(Items.Gold)
clear()
timer_start = get_time()

# start maze
plant(BUSH)
while get_entity_type() == BUSH:
    use_item(FERTILIZER)

# your function here
maze_solver(300)

harvest()
lap_time = get_time() - timer_start
if num_items(Items.Gold) - gold_at_start != 150000:
    quick_print("Insufficient Gold, better luck next time :)")
insort(timings, time)
quick_print(
    "#", i,
    "min:", str(timings[0]),
    "max:", str(timings[-1]),
    "median:", str(median(timings)),
    "avg:", str(average(timings)),
    "time:", str(time)
)

# reset code or statistics code can go here
```


## Early Maze Leaderboard 100x20 (10x10)
| # | file            | min      | max      | median   | avg      |
| - | --------------- | -------- | -------- | -------- | -------- |
| 1 | /pro-max        | 29.4016s | 45.6599s | 37.5599s | 37.6999s |
| 2 | meorin.py       | 34.0199s |          |          |          |
| 3 | vehn.py         | 35.1144s | 56.3899s | 40.9699s | 41.5299s |
| 4 | dfs.py          | 78.5699s |          |          |          |
| 5 | farm-gold.py    | 58.1799s |          |          |          |
| 0 | hugger.py       |          |          |          |          |
| 0 | tiny-hugger.py  |          |          |          |          |
| 0 | random.py       |          |          |          |          |

## Mid Maze Leaderboard 1x100 (10x10)
| # | file            | min      | max      | median   | avg      |
| - | --------------- | -------- | -------- | -------- | -------- |
| 0 | /pro-max        |          |          |          |          |
| 0 | meorin.py       |          |          |          |          |
| 0 | vehn.py         |          |          |          |          |
| 0 | dfs.py          |          |          |          |          |
| 0 | farm-gold.py    |          |          |          |          |
| 0 | hugger.py       |          |          |          |          |
| 0 | tiny-hugger.py  |          |          |          |          |
| 0 | random.py       |          |          |          |          |

## Late Maze Leaderboard 1x300 (10x10)
| # | file            | min      | max      | median   | avg      |
| - | --------------- | -------- | -------- | -------- | -------- |
| 0 | /pro-max        |          |          |          |          |
| 0 | meorin.py       |          |          |          |          |
| 0 | vehn.py         |          |          |          |          |
| 0 | dfs.py          |          |          |          |          |
| 0 | farm-gold.py    |          |          |          |          |
| 0 | hugger.py       |          |          |          |          |
| 0 | tiny-hugger.py  |          |          |          |          |
| 0 | random.py       |          |          |          |          |

## Speedrun Leaderboard 1x151 (8x8)
| # | file            | min      | max      | median   | avg      |
| - | --------------- | -------- | -------- | -------- | -------- |
| 0 | /pro-max        |          |          |          |          |
| 0 | meorin.py       |          |          |          |          |
| 0 | vehn.py         |          |          |          |          |
| 0 | dfs.py          |          |          |          |          |
| 0 | farm-gold.py    |          |          |          |          |
| 0 | hugger.py       |          |          |          |          |
| 0 | tiny-hugger.py  |          |          |          |          |
| 0 | random.py       |          |          |          |          |


## farm-gold.py
dont know how this works. just copyed it from the internet.

## hugger.py
Old script that was used to farm gold befor fertilizer was a thing. Huggs the wall until the tresure is found.

## vehn.py
code by @Zapakh strat by @Vehn.
This uses the same logic as the current leaderboard #1 but some optimizations missing.\

## dfs.py
This script uses a depth first search algorithm to find the tresure.

## random.py
This script moves randomly until the tresure is found.

## pro-max.py
This is an optimized version of the vehn.py script. It uses the same logic. pro-max/pro-max.py is the main script. The rest is just helper code.

## meorin.py
The code employs a hybrid strategy that combines DFS for initial exploration and BFS for efficient pathfinding. This approach allows for thorough exploration of the maze while ensuring the shortest path is found to the goal. The integration of backtracking ensures that dead ends are handled gracefully, allowing the algorithm to find valid paths through the maze.
