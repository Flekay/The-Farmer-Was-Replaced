# Pathfinding Algorithms

This folder contains various pathfinding algorithm implementations for visiting multiple points efficiently. These algorithms solve the Traveling Salesman Problem (TSP) for the game's constrained environment where every tick counts.

## Functions

### `nearest-neighbor.py`
Implements the nearest neighbor heuristic algorithm. This greedy algorithm selects the closest unvisited node to the current node and moves to it. Highly optimized for the game's constraints.

**Optimization Hints:**
1. It might be beneficial to break the for loop early if you find a point with distance 0 or 1 (adjacent positions)
2. Depending on your movement function, you might want to return a list of delta values (movement directions) instead of absolute positions

### `greedy_insertion.py`
Builds a tour by inserting each remaining point at the position that causes minimum tour length increase. Often better than nearest neighbor but more expensive.

### `two_opt.py`
Improves an existing tour using 2-opt swaps. Takes a nearest neighbor tour and iteratively improves it with limited iterations to keep it fast.

### `farthest_insertion.py`
Alternative insertion heuristic that starts with the farthest point and inserts remaining points. Sometimes finds better solutions than nearest neighbor for clustered points.

### `christofides_approx.py`
Simplified approximation of Christofides algorithm using farthest insertion. Better quality than nearest neighbor while remaining computationally efficient.

## Benchmark
To benchmark the pathfinding algorithms, run the `benchmark.py` script. This will test each algorithm on various point sets and measure both speed and path quality.

### Benchmark Results from `benchmark.py`

#### Small (5 points)
| Algorithm             | Gen Ticks | Move Ticks | Total Ticks |
| --------------------- | --------- | ---------- | ----------- |
| no_pathfinding        |         1 |       5701 |        5702 |
| nearest_neighbor      |       129 |       4901 |        5030 |
| greedy_insertion      |       768 |       4901 |        5669 |
| farthest_insertion    |       643 |       4901 |        5544 |
| two_opt              |       368 |       4901 |        5269 |
| christofides_approx   |       959 |       4901 |        5860 |
| divinepath           |       162 |       4816 |        4978 |

#### Medium (20 points)
| Algorithm             | Gen Ticks | Move Ticks | Total Ticks |
| --------------------- | --------- | ---------- | ----------- |
| no_pathfinding        |         1 |      11801 |       11802 |
| nearest_neighbor      |      1554 |       8601 |       10155 |
| greedy_insertion      |     39194 |       8001 |       47195 |
| farthest_insertion    |     16999 |       8601 |       25600 |
| two_opt              |     12113 |       8601 |       20714 |
| christofides_approx   |     50405 |       8001 |       58406 |
| divinepath           |      1501 |       8261 |        9762 |

#### Large (60 points)
| Algorithm             | Gen Ticks | Move Ticks | Total Ticks |
| --------------------- | --------- | ---------- | ----------- |
| no_pathfinding        |         1 |      21601 |       21602 |
| nearest_neighbor      |     13054 |      17801 |       30855 |
| greedy_insertion      |   1001638 |      16001 |     1017639 |
| farthest_insertion    |    319971 |      17801 |      337772 |
| two_opt              |    124911 |      16201 |      141112 |
| christofides_approx   |   1294869 |      16001 |     1310870 |
| divinepath           |      2483 |      17581 |       20064 |

## Important Notes
- All algorithms are hyper-optimized for the game's tick-based execution model
- `nearest-neighbor.py` remains the fastest and most reliable choice for most scenarios
- More sophisticated algorithms provide better path quality at the cost of increased computation time
- The `two_opt.py` algorithm can be combined with other algorithms as a post-processing step
- All algorithms avoid tuple unpacking and unnecessary operations for maximum performance
- Consider the trade-off between path optimality and computation time when choosing an algorithm
- `nearest-neighbor.py` remains the fastest and most practical for most scenarios
- More complex algorithms may provide better paths but cost more ticks
- The `distances` tuple uses the game's wrapping distance calculation
- Consider tick cost vs path quality trade-off when choosing algorithms
- All algorithms modify the input `points` list - make a copy if you need to preserve it
