ALMIGHTY_MOVES = almighty()
while True:
	clear()
	mighty = True
	pos = greedy2()
	if pos:
		stack2(pos)
		while mighty:
			for dir in ALMIGHTY_MOVES:
				if not move(dir):
					mighty = False
					break

def greedy2():
	change_hat(Hats.Dinosaur_Hat)
	can_move = True
	length = 1
	apple_x, apple_y = measure()
	for _ in range(apple_x):
		move(East)
	for _ in range(apple_y):
		move(North)

	while can_move and length < 18:
		length += 1
		apple_x, apple_y = measure()
		while not measure() or measure() == (apple_x, apple_y):
			while apple_x > get_pos_x() and move(East):
				pass
			while apple_x < get_pos_x() and move(West):
				pass
			while apple_y > get_pos_y() and move(North):
				pass
			while apple_y < get_pos_y() and move(South):
				pass

			if not measure() or measure() == (apple_x, apple_y):
				if not move(North):
					if not move(South):
						if not move(West):
							if not move(East):
								can_move = False
								break
	if can_move:
		return measure()



def stack2(pos):
	apple_x, apple_y = pos
	apple_y = apple_y + (not apple_y % 2)
	forbidden_moves = {(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9)}
	move_order = [West, South, East]
	length = 1

	while True:
		direction_found = False
		for dir in move_order:
			if dir == West and (get_pos_x(), get_pos_y()) in forbidden_moves:
				pass
			elif move(dir):
				direction_found = True
				break
		if direction_found:
			if measure():
				apple_x, apple_y = measure()
				apple_y = apple_y + (not apple_y % 2)
				length += 1
			if get_pos_y() == apple_y:
				for _ in range(apple_x - 1):
					move(East)
					if measure():
						apple_x, apple_y = measure()
						apple_y = apple_y + (not apple_y % 2)
						length += 1
		else:
			if length > 34: # 34 seems to be the fastest
				break
			stuck = True
			while move(North):
				stuck = False
				if measure():
					apple_x, apple_y = measure()
					apple_y = apple_y + (not apple_y % 2)
					length += 1
			if move(East):
				stuck = False
				if measure():
					apple_x, apple_y = measure()
					apple_y = apple_y + (not apple_y % 2)
					length += 1
				if get_pos_y() == apple_y:
					for _ in range(apple_x - 1):
						move(East)
						if measure():
							apple_x, apple_y = measure()
							apple_y = apple_y + (not apple_y % 2)
							length += 1
			if stuck:
				break
