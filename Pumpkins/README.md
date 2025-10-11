# Pumpkins

Strategies for farming pumpkins.

## [Single Drone](./Single%20Drone/)
- [Oneshot](./Single%20Drone/oneshot.py): Plants and harvests pumpkins in a single run with fertilizer
- [Schindler](./Single%20Drone/schindler.py): Keeps planting until every tile is filled using position tracking
- [Tiny](./Single%20Drone/tiny.py): Simple approach that alternates between planting and harvesting

## [Multi Drone](./Multi%20Drone/)
- [Devil](./Multi%20Drone/devil.py): 16 coordinated drones on 27x27 grid with 6x6 sections
- [Jarvan](./Multi%20Drone/jarvan.py): Advanced hierarchical drone spawning on 29x29 world
- [Mega Chunk](./Multi%20Drone/mega_chunk.py): 32 drones each managing 8x4 chunks on 32x32 field
- [Mega Line](./Multi%20Drone/mega_line.py): Line formation movement for systematic coverage
- [Mega Swarm](./Multi%20Drone/mega_swarm.py): Dynamic swarm intelligence with spawning/despawning
- [Tiny Line](./Multi%20Drone/tiny_line.py): Independent drones harvesting small pumpkins

Refer to each subfolder for detailed information and benchmarks.
