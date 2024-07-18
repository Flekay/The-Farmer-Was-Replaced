# Maze

## Benchmarks
| file          | 1x100  | 10x20   | 1x300   | note |
| ------------- | ------ | ------- | ------- | ---- |
| leaderboard   | 31.66s | 100.48s | 78.03s  |      |
| farm-gold.py  | 58.17s | 193.09s | 127.67s |      |
| hugger.py     |        |         |         |      |
| vehn.py       | 38.64s | 132.33s | 87.92s  |      |
| dfs.py        | 78.56s | 275.09s | 191.06s |      |
| pro-max.py    | 29.40s | 999.99s | 999.99s |      |


## farm-gold.py
dont know how this works. just copyed it from the internet.

## hugger.py
Old script that was used to farm gold befor fertilizer was a thing. Huggs the wall until the tresure is found.

## vehn.py
code by @Zapakh strat by @Vehn.
This uses the same logic as the current leaderboard #1 but some optimizations missing.\
100 runs @ 1x300 | min: 87.92 max: 106.73 median: 95.33 avg: 95.95

## dfs.py
This script uses a depth first search algorithm to find the tresure.

## random.py
This script moves randomly until the tresure is found.

## pro-max.py
This is an optimized version of the vehn.py script. It uses the same logic. pro-max/pro-max.py is the main script. The rest is just helper code. Havn't tested 10x20, 1x300 yet.\
1x100 | min: 29.4016 max: 45.65 median: 37.55 avg: 37.69\
