clear()
betterStackDicts()
def betterStackDicts():
	move(North)
	move(East)
	move(East)
	move(North)
	change_hat(Hats.Dinosaur_Hat)

	apple_dict = {0: measure()}
	# quick_print(measure())
	length_dict = {0: 0}

	def mowe(dir):
		measurement = measure()
		if measurement:
			# quick_print(measurement)
			# extend_func, extend, extend_index = position_function_dict[apple_dict[0]]
			# quick_print(extend_func, extend, extend_index)
			length_dict[0] += 1
			apple_dict[0] = measurement
		return move(dir)

	path_to_apple = []



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
	SHORTCUT = [
		North, North, North, North, North,
		East, East, East, East, East,
		South, South, South, South, South,
		West, West, West, West, West
	]
	SHORTCUT_POS = [
		(2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
		(2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
		(7, 7), (7, 6), (7, 5), (7, 4), (7, 3),
		(7, 2), (6, 2), (5, 2), (4, 2), (3, 2),
	]
	EXTEND_LENGTH = {
		x2y2: 4, x2y4: 4, x2y5: 4, x2y6: 8,
		x2y7: 4, x4y7: 4, x5y7: 4, x6y7: 8,
		x7y7: 4, x7y5: 4, x7y4: 4, x7y3: 8,
		x7y2: 4, x5y2: 4, x4y2: 4, x3y2: 8,
		x2y3: 0, x3y7: 0, x7y6: 0, x6y2: 0,
	}
	SHORTCUT_FUNC = [
		x2y2, x2y3, x2y4, x2y5, x2y6,
		x2y7, x3y7, x4y7, x5y7, x6y7,
		x7y7, x7y6, x7y5, x7y4, x7y3,
		x7y2, x6y2, x5y2, x4y2, x3y2,
	]
	position_function_dict = {
		# extended
		# West 1
		(0, 2): (x2y2, True, 0), (0, 3): (x2y2, True, 0), (1, 2): (x2y2, True, 0), (1, 3): (x2y2, True, 0),
		# West 2
		(0, 4): (x2y4, True, 2), (0, 5): (x2y4, True, 2), (1, 4): (x2y4, True, 2), (1, 5): (x2y4, True, 2),
		# Inner top left
		(3, 5): (x2y5, True, 3), (3, 6): (x2y5, True, 3), (4, 5): (x2y5, True, 3), (4, 6): (x2y5, True, 3),
		# North West
		(0, 6): (x2y6, True, 4), (0, 7): (x2y6, True, 4), (0, 8): (x2y6, True, 4), (0, 9): (x2y6, True, 4),
		(1, 6): (x2y6, True, 4), (1, 7): (x2y6, True, 4), (1, 8): (x2y6, True, 4), (1, 9): (x2y6, True, 4),
		# North 1
		(2, 8): (x2y7, True, 5), (2, 9): (x2y7, True, 5), (3, 8): (x2y7, True, 5), (3, 9): (x2y7, True, 5),
		# North 2
		(4, 8): (x4y7, True, 7), (4, 9): (x4y7, True, 7), (5, 8): (x4y7, True, 7), (5, 9): (x4y7, True, 7),
		# Inner top right
		(5, 6): (x5y7, True, 8), (5, 5): (x5y7, True, 8), (6, 6): (x5y7, True, 8), (6, 5): (x5y7, True, 8),
		# North East
		(6, 8): (x6y7, True, 9), (6, 9): (x6y7, True, 9), (7, 8): (x6y7, True, 9), (7, 9): (x6y7, True, 9),
		(8, 8): (x6y7, True, 9), (8, 9): (x6y7, True, 9), (9, 8): (x6y7, True, 9), (9, 9): (x6y7, True, 9),
		# East 1
		(8, 6): (x7y7, True, 10), (8, 7): (x7y7, True, 10), (9, 6): (x7y7, True, 10), (9, 7): (x7y7, True, 10),
		# East 2
		(8, 4): (x7y5, True, 12), (8, 5): (x7y5, True, 12), (9, 4): (x7y5, True, 12), (9, 5): (x7y5, True, 12),
		# Inner bottom right
		(6, 4): (x7y4, True, 13), (6, 3): (x7y4, True, 13), (5, 4): (x7y4, True, 13), (5, 3): (x7y4, True, 13),
		# South East
		(8, 3): (x7y3, True, 14), (9, 3): (x7y3, True, 14), (8, 2): (x7y3, True, 14), (9, 2): (x7y3, True, 14),
		(8, 1): (x7y3, True, 14), (9, 1): (x7y3, True, 14), (8, 0): (x7y3, True, 14), (9, 0): (x7y3, True, 14),
		# South 1
		(6, 0): (x7y2, True, 15), (6, 1): (x7y2, True, 15), (7, 0): (x7y2, True, 15), (7, 1): (x7y2, True, 15),
		# South 2
		(4, 0): (x5y2, True, 17), (4, 1): (x5y2, True, 17), (5, 0): (x5y2, True, 17), (5, 1): (x5y2, True, 17),
		# Inner bottom left
		(4, 3): (x4y2, True, 18), (4, 4): (x4y2, True, 18), (3, 3): (x4y2, True, 18), (3, 4): (x4y2, True, 18),
		# South West
		(0, 0): (x3y2, True, 19), (0, 1): (x3y2, True, 19), (1, 0): (x3y2, True, 19), (1, 1): (x3y2, True, 19),
		(2, 0): (x3y2, True, 19), (2, 1): (x3y2, True, 19), (3, 0): (x3y2, True, 19), (3, 1): (x3y2, True, 19),

		# shortcut
		(2, 2): (x2y2, False, 0), (2, 3): (x2y3, False, 1),
		(2, 4): (x2y4, False, 2), (2, 5): (x2y5, False, 3),
		(2, 6): (x2y6, False, 4), (2, 7): (x2y7, False, 5),
		(3, 7): (x3y7, False, 6), (4, 7): (x4y7, False, 7),
		(5, 7): (x5y7, False, 8), (6, 7): (x6y7, False, 9),
		(7, 7): (x7y7, False, 10), (7, 6): (x7y6, False, 11),
		(7, 5): (x7y5, False, 12), (7, 4): (x7y4, False, 13),
		(7, 3): (x7y3, False, 14), (7, 2): (x7y2, False, 15),
		(6, 2): (x6y2, False, 16), (5, 2): (x5y2, False, 17),
		(4, 2): (x4y2, False, 18), (3, 2): (x3y2, False, 19),
	}

	current_func = x2y2
	while length_dict[0] < 50:
		mmv = measure()
		if mmv:
			extend_func, extend, extend_index = position_function_dict[mmv]
			length_dict[0] += 1
		else:
			extend_func, extend, extend_index = position_function_dict[apple_dict[0]]

		length = length_dict[0]
		# quick_print(length)
		while length > 25:
			func = SHORTCUT_FUNC[extend_index - 1]
			if current_func == func:
				break
			path_to_apple.append(func)
			length -= EXTEND_LENGTH[func]
			extend_index -= 1

		if path_to_apple:
			first_func = path_to_apple.pop()
			while current_func != first_func:
				current_func = current_func()
			current_func = first_func(move, True)

			while path_to_apple:
				current_func = path_to_apple.pop()(move, True)
		else:
			while current_func != extend_func:
				current_func = current_func()

		current_func = current_func(mowe, extend)

	while current_func != x4y2:
		current_func = current_func(mowe, True)
	move(South)
	move(South)
	move(West)
	move(West)

	breaker = True
	while breaker:
		for direction in ALMIGHTY:
			if not move(direction):
				breaker = False
				break
	clear()
