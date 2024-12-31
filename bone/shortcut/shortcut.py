clear()
snake_body = []
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
	(0, 0): 0, (0, 1): 1, (1, 1): 2, (2, 1): 3, (2, 2): 4,
	(1, 2): 5, (0, 2): 6, (0, 3): 7, (1, 3): 8, (2, 3): 9,
	(2, 4): 10, (1, 4): 11, (0, 4): 12, (0, 5): 13, (1, 5): 14,
	(2, 5): 15, (3, 5): 16, (4, 5): 17, (4, 6): 18, (3, 6): 19,
	(2, 6): 20, (1, 6): 21, (0, 6): 22, (0, 7): 23, (0, 8): 24,
	(0, 9): 25, (1, 9): 26, (1, 8): 27, (1, 7): 28, (2, 7): 29,
	(2, 8): 30, (2, 9): 31, (3, 9): 32, (3, 8): 33, (3, 7): 34,
	(4, 7): 35, (4, 8): 36, (4, 9): 37, (5, 9): 38, (5, 8): 39,
	(5, 7): 40, (5, 6): 41, (5, 5): 42, (6, 5): 43, (6, 6): 44,
	(6, 7): 45, (6, 8): 46, (6, 9): 47, (7, 9): 48, (8, 9): 49,
	(9, 9): 50, (9, 8): 51, (8, 8): 52, (7, 8): 53, (7, 7): 54,
	(8, 7): 55, (9, 7): 56, (9, 6): 57, (8, 6): 58, (7, 6): 59,
	(7, 5): 60, (8, 5): 61, (9, 5): 62, (9, 4): 63, (8, 4): 64,
	(7, 4): 65, (6, 4): 66, (5, 4): 67, (5, 3): 68, (6, 3): 69,
	(7, 3): 70, (8, 3): 71, (9, 3): 72, (9, 2): 73, (9, 1): 74,
	(9, 0): 75, (8, 0): 76, (8, 1): 77, (8, 2): 78, (7, 2): 79,
	(7, 1): 80, (7, 0): 81, (6, 0): 82, (6, 1): 83, (6, 2): 84,
	(5, 2): 85, (5, 1): 86, (5, 0): 87, (4, 0): 88, (4, 1): 89,
	(4, 2): 90, (4, 3): 91, (4, 4): 92, (3, 4): 93, (3, 3): 94,
	(3, 2): 95, (3, 1): 96, (3, 0): 97, (2, 0): 98, (1, 0): 99,
}

snakeMachine()
def snakeMachine():
	change_hat(Hats.Dinosaur_Hat)
	snake_body = [(0, 0)]
	current_func = SMx0y0
	length = 0
	# while length != 99:
	# 	# quick_print(length, snake_body)
	# 	if measure():
	# 		length += 1
	# 		apple = position_function_dict[measure()]
	# 	else:
	# 		snake_body.pop(0)
	# 	current_func = current_func(apple, length, snake_body, position_function_dict)
	# clear()


	current_func = SMx0y0a
	ticks = get_tick_count()
	while True:
		if measure():
			length += 1
			# quick_print(length)
			apple = position_function_dict[measure()]
			quick_print((get_tick_count()-ticks)/ops())
			ticks = get_tick_count()
		if length < 37:
			current_func = current_func(apple, length, snake_body, position_function_dict)
		elif current_func == SMx0y0a:
			break
		else:
			current_func = current_func(0, length, snake_body, position_function_dict)

	breaker = True
	while breaker:
		for direction in ALMIGHTY:
			if not move(direction):
				breaker = False
				break
	clear()
	