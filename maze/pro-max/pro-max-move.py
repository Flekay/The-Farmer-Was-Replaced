def mnb_north():
	if move(North):
		pos = get_pos_x(), get_pos_y()
		pos_south = TILE_SOUTH[pos]
		move(South)
		# Remove both sides of the wall
		WALL[pos_south].remove(mnb_north)
		WALL[pos].remove(mnb_south)
		# Add path
		PATH[pos_south].add(bfs_north)
		PATH[pos].add(bfs_south)

		# Update the flowfield
		pro_max_bfs(pos_south, DIST_TO_BASE[pos_south])
		pro_max_bfs(pos, DIST_TO_BASE[pos])

def mnb_east():
	if move(East):
		pos = get_pos_x(), get_pos_y()
		pos_west = TILE_WEST[pos]
		move(West)
		# Remove both sides of the wall
		WALL[pos_west].remove(mnb_east)
		WALL[pos].remove(mnb_west)
		# Add path
		PATH[pos_west].add(bfs_east)
		PATH[pos].add(bfs_west)

		# Update the flowfield
		pro_max_bfs(pos_west, DIST_TO_BASE[pos_west])
		pro_max_bfs(pos, DIST_TO_BASE[pos])

def mnb_south():
	if move(South):
		pos = get_pos_x(), get_pos_y()
		pos_north = TILE_NORTH[pos]
		move(North)
		# Remove both sides of the wall
		WALL[pos_north].remove(mnb_south)
		WALL[pos].remove(mnb_north)
		# Add path
		PATH[pos_north].add(bfs_south)
		PATH[pos].add(bfs_north)

		# Update the flowfield
		pro_max_bfs(pos_north, DIST_TO_BASE[pos_north])
		pro_max_bfs(pos, DIST_TO_BASE[pos])

def mnb_west():
	if move(West):
		pos = get_pos_x(), get_pos_y()
		pos_east = TILE_EAST[pos]
		move(East)
		# Remove both sides of the wall
		WALL[pos_east].remove(mnb_west)
		WALL[pos].remove(mnb_east)
		# Add path
		PATH[pos_east].add(bfs_west)
		PATH[pos].add(bfs_east)

		# Update the flowfield
		pro_max_bfs(pos_east, DIST_TO_BASE[pos_east])
		pro_max_bfs(pos, DIST_TO_BASE[pos])
