MOVES = [
	West, South, East, South, East, North, North, North, West, West,
	West, South, South, South, East, South, West, West, North, North,
	North, North, North, East, East, East, East, East, South, South,
	South, South, South, West, West, South, East, East, East, North,
	North, North, North, North, North, North, West, West, West, West,
	West, West, West, South, South, South, South, South, South, South,
	East, East, East, South, West, West, West, West, North, North, North,
	North, North, North, North, North, North, East, East, East, East,
	East, East, East, East, East, South, South, South, South, South, South,
	South, South, South, West, West, West, West
]

clear()
for dir in MOVES:
	till()
	move(dir)