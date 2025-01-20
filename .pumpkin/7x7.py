MOVES = (
	North, East, South, South, West, West, North,
	West, South, South, East, East, East, East,
	North, North, North, North, West, West, West,
	West, West, North, East, East, East, East,
	East, East, South, South, South, South, South,
	South, West, West, West, West, West, West, North,
	North, North, North, East, East, East
)
clear()
move_to(3,3)
set_execution_speed(5)
for direction in MOVES:
	till()
	move(direction)

