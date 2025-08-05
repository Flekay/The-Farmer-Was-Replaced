# Polyculture Hay
These polyculture hay scripts are designed to teach you the core concepts of each algorithm. They are not optimized for speed or efficiency, but rather to provide a clear understanding of how each method works.

## functions

### `static.py`
This script just spams fertilizer and harvest in the middle of a bush field. Very luck based.

### `preplant.py` + `harvest_polyhay.py`
Implementation of preplanting/harvesting with a lower max but more stable average.

### `pophay.py`
This script is the same as `popwood.py` but for hay.

### `corners.py`
This script plants a 5x5 grid of bushes and harvests 4 grass tiles in the corners.

### `strip.py`
This plants and harvests a single strip of hay over and over again.

## Benchmarks
Benchmarks with "-" have a less than 100% success rate and are therefore not able to compete in leaderboard runs.

### Benchmark Results
| file         | items/min | leaderboard time |
| -----------  | --------- | ---------------- |
| pophay.py    |   218 000 |         0:29.770 |
| corners.py   |   250 000 |         0:28.947 |
| strip.py     |   216 000 |         0:30.891 |
| preplant.py  |   246 000 |                - |
| static.py    |   236 000 |                - |


## Important Notes
- `preplant.py` and `static.py` are not able to compete in leaderboard runs due to their high fertilizer usage.
