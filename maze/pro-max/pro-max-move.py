def mnb_north():
	if move(North):
		x = get_pos_x()
		new_y = get_pos_y()
		move(South)
		y = new_y - 1
		# Remove both sides of the wall
		WALL[x, y].remove(mnb_north)
		WALL[x, new_y].remove(mnb_south)
		#
		PATH[x, y].add(bfs_north)
		PATH[x, new_y].add(bfs_south)
		# Update the flowfield
		pro_max_bfs(x, y)
		pro_max_bfs(x, new_y)

def mnb_east():
	if move(East):
		new_x = get_pos_x()
		y = get_pos_y()
		move(West)
		x = new_x - 1
		# Remove both sides of the wall
		WALL[x, y].remove(mnb_east)
		WALL[new_x, y].remove(mnb_west)
		#
		PATH[x, y].add(bfs_east)
		PATH[new_x, y].add(bfs_west)
		# Update the flowfield
		pro_max_bfs(x, y)
		pro_max_bfs(new_x, y)

def mnb_south():
	if move(South):
		x = get_pos_x()
		new_y = get_pos_y()
		move(North)
		y = new_y + 1
		# Remove both sides of the wall
		WALL[x, y].remove(mnb_south)
		WALL[x, new_y].remove(mnb_north)
		#
		PATH[x, y].add(bfs_south)
		PATH[x, new_y].add(bfs_north)
		# Update the flowfield
		pro_max_bfs(x, y)
		pro_max_bfs(x, new_y)

def mnb_west():
	if move(West):
		new_x = get_pos_x()
		y = get_pos_y()
		move(East)
		x = new_x + 1
		# Remove both sides of the wall
		WALL[x, y].remove(mnb_west)
		WALL[new_x, y].remove(mnb_east)
		#
		PATH[x, y].add(bfs_west)
		PATH[new_x, y].add(bfs_east)
		# Update the flowfield
		pro_max_bfs(x, y)
		pro_max_bfs(new_x, y)

# Helper to look for missing WALL
def move_n_break(step):
	move(step)
	for func in WALL[get_pos_x(), get_pos_y()]:
		func()
