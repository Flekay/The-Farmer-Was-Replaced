# Snake
This will be a collection of pumpkin scripts that are used to farm snakes.

## Benchmarks
| file         | items/min |
| -----------  | --------- |
| greedy.py    | ?         |
| almighty.py  | ?         |
| timon.py     | ?         |
| hybrid.py    | ?         |
| checkered.py | ?         |


## greedy.py
This Greedy Best-First Search algorithm has a one-move horizon and only considers moving the snake to the position on the board that appears to be closest to the goal

## almighty.py
Almighty makes the snake move in a circular pattern around the board

## timon.py
Timon uses a stack based almighty algorithm to move the snake in a circular pattern around the board with some shortcuts.

## hybrid.py
This script is a combination of greedy.py and almighty.py. It uses the Greedy Best-First Search algorithm to move the snake to the position on the board that appears to be closest to the goal until the snake reaches a certain length, then it switches to the circular pattern around the board.

## checkered.py
This checks for dead ends before moving the snake. If there is a dead end, it will move the snake in a different direction.
