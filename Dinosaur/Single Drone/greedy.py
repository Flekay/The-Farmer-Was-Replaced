clear()
greedy()
def greedy():
	change_hat(Hats.Dinosaur_Hat)
	can_move = True
	apple_x, apple_y = measure()
	for _ in range(apple_x):
		move(East)
	for _ in range(apple_y):
		move(North)

	while can_move:
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
	clear()
