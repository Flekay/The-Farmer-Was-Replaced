clear()
change_hat(Hats.Dinosaur_Hat)
apple = measure()
DD = {
	North: 1,
	East: 1,
	South: -1,
	West: -1
}
# snake_body = [(0, 0)]
# length = 0

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


# print(movable_directions(7,1))
while True:
	directions = movable_directions()
	# move the first direction that moves in the direction of the apple
	# pos = (get_pos_x(), get_pos_y())
	# distanceX = manhatten_distance((pos[0] + DD[directions[0]], pos[1]), apple)
	# distanceY = manhatten_distance((pos[0], pos[1] + DD[directions[1]]), apple)
	distanceX = abs(DD[directions[0]] + get_pos_x() - apple[0])
	distanceY = abs(DD[directions[1]] + get_pos_y() - apple[1])
	# if distanceX < distanceY:
	# 	move(directions[0])
	# else:
	# 	move(directions[1])
	if distanceX > distanceY and not move(directions[0]):
		move(directions[1])
	elif not move(directions[1]):
		move(directions[0])
