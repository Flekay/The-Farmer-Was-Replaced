clear()
betterStackDicts()
def betterStackDicts():
	move(North)
	move(East)
	move(East)
	move(North)
	change_hat(Hats.Dinosaur_Hat)

	apple_dict = {0: measure()}
	length_dict = {0: 0}

	def mowe(dir):
		measurement = measure()
		if measurement:
			length_dict[0] += 1
			apple_dict[0] = measurement
		return move(dir)


	ALMIGHTY = [
		North, East, East, North, West, West, North, East, East, North,
		West, West, North, East, East, East, East, North, West, West,
		West, West, North, North, North, East, South, South, East, North,
		North, East, South, South, East, North, North, East, South, South,
		South, South, East, North, North, North, North, East, East, East,
		South, West, West, South, East, East, South, West, West, South,
		East, East, South, West, West, West, West, South, East, East,
		East, East, South, South, South, West, North, North, West, South,
		South, West, North, North, West, South, South, West, North, North,
		North, North, West, South, South, South, South, West, West, West
	]
	position_function_dict = {
		# extended
		# West 1
		(0, 2): x2y2, (0, 3): x2y2, (1, 2): x2y2, (1, 3): x2y2,
		# West 2
		(0, 4): x2y4, (0, 5): x2y4, (1, 4): x2y4, (1, 5): x2y4,
		# Inner top left
		(3, 5): x2y5, (3, 6): x2y5, (4, 5): x2y5, (4, 6): x2y5,
		# North West
		(0, 6): x2y6, (0, 7): x2y6, (0, 8): x2y6, (0, 9): x2y6,
		(1, 6): x2y6, (1, 7): x2y6, (1, 8): x2y6, (1, 9): x2y6,
		# North 1
		(2, 8): x2y7, (2, 9): x2y7, (3, 8): x2y7, (3, 9): x2y7,
		# North 2
		(4, 8): x4y7, (4, 9): x4y7, (5, 8): x4y7, (5, 9): x4y7,
		# Inner top right
		(5, 6): x5y7, (5, 5): x5y7, (6, 6): x5y7, (6, 5): x5y7,
		# North East
		(6, 8): x6y7, (6, 9): x6y7, (7, 8): x6y7, (7, 9): x6y7,
		(8, 8): x6y7, (8, 9): x6y7, (9, 8): x6y7, (9, 9): x6y7,
		# East 1
		(8, 6): x7y7, (8, 7): x7y7, (9, 6): x7y7, (9, 7): x7y7,
		# East 2
		(8, 4): x7y5, (8, 5): x7y5, (9, 4): x7y5, (9, 5): x7y5,
		# Inner bottom right
		(6, 4): x7y4, (6, 3): x7y4, (5, 4): x7y4, (5, 3): x7y4,
		# South East
		(8, 3): x7y3, (9, 3): x7y3, (8, 2): x7y3, (9, 2): x7y3,
		(8, 1): x7y3, (9, 1): x7y3, (8, 0): x7y3, (9, 0): x7y3,
		# South 1
		(6, 0): x7y2, (6, 1): x7y2, (7, 0): x7y2, (7, 1): x7y2,
		# South 2
		(4, 0): x5y2, (4, 1): x5y2, (5, 0): x5y2, (5, 1): x5y2,
		# Inner bottom left
		(4, 3): x4y2, (4, 4): x4y2, (3, 3): x4y2, (3, 4): x4y2,
		# South West
		(0, 0): x3y2, (0, 1): x3y2, (1, 0): x3y2, (1, 1): x3y2,
		(2, 0): x3y2, (2, 1):x3y2, (3, 0): x3y2, (3, 1): x3y2,

		# shortcut
		(2, 2): x2y2, (2, 3): x2y3, (2, 4): x2y4, (2, 5): x2y5,
		(2, 6): x2y6, (2, 7): x2y7, (3, 7): x3y7, (4, 7): x4y7,
		(5, 7): x5y7, (6, 7): x6y7, (7, 7): x7y7, (7, 6): x7y6,
		(7, 5): x7y5, (7, 4): x7y4, (7, 3): x7y3, (7, 2): x7y2,
		(6, 2): x6y2, (5, 2): x5y2, (4, 2): x4y2, (3, 2): x3y2,
	}

	current_func = x2y2
	while length_dict[0] < 38:
		extend_func = position_function_dict[apple_dict[0]]
		while current_func != extend_func:
			current_func = current_func()
		current_func = current_func(mowe, True)

	while current_func != x3y2:
		current_func = current_func(move, True)
	move(South)
	move(South)
	move(West)
	move(West)
	move(West)

	breaker = True
	while breaker:
		for direction in ALMIGHTY:
			if not move(direction):
				breaker = False
				break
	clear()
	