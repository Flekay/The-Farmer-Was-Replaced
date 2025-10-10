# Multi Drone Pumpkins
This will be a collection of multi-drone scripts that are used to farm pumpkins efficiently with coordinated drone strategies.

## Functions

### `devil.py`
This script operates on a 27x27 grid with 16 x 6x6 sections (you know, 1666... devil). Each tiny 6x6 pumpkin area is handled by 2 drones working in coordination.

### `mega_line.py`
Just calls `movement/line_formation` to run over the grid until the big pumpkin is formed. Uses line formation movement patterns for systematic coverage.

### `mega_chunk.py`
Same concept as `mega_line.py` but uses `movement/chunk_positioning` instead. Operates with 32 drones where each drone has its own 8x4 chunk on a 32x32 field.

### `mega_swarm.py`
The individual drones don't have a fixed path - they use swarm intelligence to build a big pumpkin. Constantly spawning and despawning drones based on dynamic conditions and requirements.

### `tiny_line.py`
Just harvests small (2x2) pumpkins. Each drone operates independently with no communication between the drones at all. Simple parallel farming approach.

## Benchmarks
Benchmarks with "-" have a less than 100% success rate and are therefore not able to compete in leaderboard runs.

### Benchmark Results
| file         | leaderboard time |
| -----------  | ---------------- |
| devil.py     |              TBD |
| mega_line.py |        08:54.836 |
| mega_chunk.py|              TBD |
| mega_swarm.py|              TBD |
| tiny_line.py |        09:48.730 |
