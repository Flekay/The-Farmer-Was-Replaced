def move_to(x, y, ws = get_world_size()):
	hws = ws // 2
	# Calculate the shortest x direction
	dx = (x - get_pos_x() + hws) % ws - hws
	# Calculate the shortest y direction
	dy = (y - get_pos_y() + hws) % ws - hws
	
	# Move in x direction
	for i in range(dx):
		move(East)
	for i in range(-dx):
		move(West)
	
	# Move in y direction
	for i in range(dy):
		move(North)
	for i in range(-dy):
		move(South)
		
		
def move_to_pos(pos, ws = get_world_size()):
	hws = ws // 2
	
	dx = (pos[0] - get_pos_x() + hws) % ws - hws
	dy = (pos[1] - get_pos_y() + hws) % ws - hws
	
	for i in range(dx):
		move(East)
	for i in range(-dx):
		move(West)
	for i in range(dy):
		move(North)
	for i in range(-dy):
		move(South)