clear()
change_hat(Hats.Dinosaur_Hat)
apple_pos = measure()
length = 0

while True:
	apple_x, apple_y = apple_pos
	x=get_pos_x()
	y=get_pos_y()

	if x % 2 == 0:
		if y % 2 == 0:
			if apple_y < y:
				move(North)
			elif apple_y > y:
				move(South)
			else:
				if apple_x < x:
					move(West)
				elif apple_x > x:
					move(East)
		else:
			if apple_x < x:
				move(West)
			elif apple_x > x:
				move(East)
			else:
				if apple_y < y:
					move(North)
				elif apple_y > y:
					move(South)
	else:
		if y % 2 == 0:
			if apple_y < y:
				move(North)
			elif apple_y > y:
				move(South)
			else:
				if apple_x < x:
					move(West)
				elif apple_x > x:
					move(East)
		else:
			if apple_x < x:
				move(West)
			elif apple_x > x:
				move(East)
			else:
				if apple_y < y:
					move(North)
				elif apple_y > y:
					move(South)

	m = measure()
	if m:
		apple_x, apple_y = measure()
		length += 1
		quick_print(length)


def movable_directions(x=get_pos_x(), y=get_pos_y()):
	directions = []
	if x % 2:
		directions.append(North)
	else:
		directions.append(South)
	if y % 2:
		directions.append(West)
	else:
		directions.append(East)
	return directions
