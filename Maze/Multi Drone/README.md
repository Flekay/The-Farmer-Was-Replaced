# Multi Drone Maze
This will be a collection of multi-drone scripts that are used to solve mazes efficiently with coordinated drone strategies.

## Functions

### `substance_spam.py`
A brute-force multi-drone maze strategy operating on a 5x5 grid. Spawns 25 drones (one per grid cell) that continuously spam weird substance to generate new mazes and harvest any treasures found. Each drone works independently using substance spamming until the gold goal is reached.

## Benchmarks
Benchmarks with "-" have a less than 100% success rate and are therefore not able to compete in leaderboard runs.

### Benchmark Results
| file              | leaderboard time |
| ----------------- | ---------------- |
| substance_spam.py |        01:07.107 |
