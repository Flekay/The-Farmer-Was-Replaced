# Bone / Snake
This will be a collection of snake scripts that are used to farm bone.

## Benchmarks
| file         | items/min |
| -----------  | --------- |
| greedy.py    |    55 000 |
| almighty.py  |   196 000 |
| timon.py     |   294 280 |
| hybrid.py    |   304 000 |
| astar.py     |    39 900 |
| rando.py     |     1 810 |
| stack.py     |   196 000 |
| brainlet.py  |     8 590 |


## greedy.py
This Script tries to move to the apple in a straight line.

## almighty.py
Almighty makes the snake move in a circular pattern around the board

## timon.py
This is a recreation of Timon's script shown in the first snake video. It is a switches at length 34 from the stack.py script to the almighty.py script.

## hybrid.py
This script switches from greedy.py to stack.py at length 20 and switches to almighty.py at length 34.

## astar.py
This script uses the A* algorithm to find the shortest path to the goal.

## rando.py
This script moves in a random direction until it gets stuck.

## stack.py
This script is a modified version of the almighty.py script. It moves in a circular pattern around the board and tries make shortcuts when possible.

## brainlet.py
This script is the simplest script that possible. It only harvest one apple before restarting.
