clear()
stack()
def stack():
	change_hat(Hats.Dinosaur_Hat)
	goto_pos(measure(), (0, 0))
	apple_x, apple_y = measure()
	move_order = [West, South, East]
	apple_y = apple_y + (not apple_y % 2)
	forbidden_moves = {(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9)}
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
			if length > 100:
				break
			while move(North):
				if measure():
					apple_x, apple_y = measure()
					apple_y = apple_y + (not apple_y % 2)
					length += 1
			if move(East):
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
				break
	clear()
