# Dinosaur / Snake

Strategies for farming bone using snake-like movement patterns.

## [Single Drone](./Single%20Drone/)
- [Drone](./Single%20Drone/drone.py): Simple rules to reach apple, switches to circle pattern at length 50
- [Circle](./Single%20Drone/circle/): Circular pattern movement with shortcuts
- [Timon](./Single%20Drone/timon.py): Switches from stack to almighty strategy at length 34
- [Almighty](./Single%20Drone/almighty.py): Circular pattern movement around board
- [Hybrid](./Single%20Drone/hybrid.py): Progressive strategy switching from greedy to stack to almighty
- [Stack](./Single%20Drone/stack.py): Modified almighty with shortcut optimization
- [Greedy](./Single%20Drone/greedy.py): Straight line movement to apple
- [A-star](./Single%20Drone/astar.py): A* pathfinding algorithm implementation
- [Brainlet](./Single%20Drone/brainlet.py): Harvest one apple then restart
- [Rando](./Single%20Drone/rando.py): Random movement until stuck

## [Multi Drone](./Multi%20Drone/)
Currently no strategies available.

Refer to each subfolder for detailed information and benchmarks.
