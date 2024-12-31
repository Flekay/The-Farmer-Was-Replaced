moves = [
	North, West, South, West, North, East, North, East, North, West,
	South, West, South, West, South, West, North, East, North, East,
	North, East, North, East, North, West, South, West, South, West,
	South, West, South, West, South, West, North, East, North, East,
	North, East, North, East, North, East, North, East, North, West,
	South, West, South, West, South, West, South, West, South, West,
	South, West, North, East, North, East, North, East, North, East,
	North, East, North, West, South, West, South, West, South, West,
	South, West, North, East, North, East, North, East, North, West,
	South, West, South, West, North, East, North, West
]
init5()
def init5():
	clear()
	# till plant and sort
	current_function = cacti_move_0
	while current_function:
		current_function = current_function()

	move(West)
	move(West)
	move(North)
	# measure and sort
	for dir in moves:
		simple_swap()
		move(dir)
	harvest()
