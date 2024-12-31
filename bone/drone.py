# for dinos it turns out the other rules aren't really worth it anyway
# the idea was to split the grid into 2x2 cells
# always drive on the right side of cells
# only enter a cell you're in from the same side you entered it
# but it was faster to only do the valid directions and fail slightly more

# video
# https://discord.com/channels/988081966035402783/1241469488919220316/1323107367419777025



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

# manhatten distance
def manhatten_distance(point1, point2, ws=get_world_size()):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


# print(movable_directions(7,1))
while True:
	directions = movable_directions()
	# move the first direction that moves in the direction of the apple
	pos = (get_pos_x(), get_pos_y())
	distanceX = manhatten_distance((pos[0] + DD[directions[0]], pos[1]), apple)
	distanceY = manhatten_distance((pos[0], pos[1] + DD[directions[1]]), apple)
	# if distanceX < distanceY:
	# 	move(directions[0])
	# else:
	# 	move(directions[1])
	if distanceX > distanceY and not move(directions[0]):
		move(directions[1])
	elif not move(directions[1]):
		move(directions[0])
