def mnb_north():
	if move(North):
		x,y = get_pos_x(), get_pos_y()
		ys = y-1
		move(South)
		# Remove both sides of the wall
		WALL[x][ys].remove(mnb_north)
		WALL[x][y].remove(mnb_south)
		# Add path
		PATH[x][ys].add(bfs_north)
		PATH[x][y].add(bfs_south)

		# Update the flowfield
		# pro_max_bfs((x, ys), DIST_TO_BASE[(x, ys)])
		# pro_max_bfs((x, y), DIST_TO_BASE[(x, y)])
		pro_max_bfs(x, ys, DIST_TO_BASE[x][ys])
		pro_max_bfs(x, y, DIST_TO_BASE[x][y])

def mnb_east():
	if move(East):
		x,y = get_pos_x(), get_pos_y()
		xs = x-1
		move(West)
		# Remove both sides of the wall
		WALL[xs][y].remove(mnb_east)
		WALL[x][y].remove(mnb_west)
		# Add path
		PATH[xs][y].add(bfs_east)
		PATH[x][y].add(bfs_west)

		# Update the flowfield
		# pro_max_bfs((xs, y), DIST_TO_BASE[(xs, y)])
		# pro_max_bfs((x, y), DIST_TO_BASE[(x, y)])
		pro_max_bfs(xs, y, DIST_TO_BASE[xs][y])
		pro_max_bfs(x, y, DIST_TO_BASE[x][y])

def mnb_south():
	if move(South):
		x,y = get_pos_x(), get_pos_y()
		ys = y+1
		move(North)
		# Remove both sides of the wall
		WALL[x][ys].remove(mnb_south)
		WALL[x][y].remove(mnb_north)
		# Add path
		PATH[x][ys].add(bfs_south)
		PATH[x][y].add(bfs_north)

		# Update the flowfield
		# pro_max_bfs((x, ys), DIST_TO_BASE[(x, ys)])
		# pro_max_bfs((x, y), DIST_TO_BASE[(x, y)])
		pro_max_bfs(x, ys, DIST_TO_BASE[x][ys])
		pro_max_bfs(x, y, DIST_TO_BASE[x][y])

def mnb_west():
	if move(West):
		x,y = get_pos_x(), get_pos_y()
		xs = x+1
		move(East)
		# Remove both sides of the wall
		WALL[xs][y].remove(mnb_west)
		WALL[x][y].remove(mnb_east)
		# Add path
		PATH[xs][y].add(bfs_west)
		PATH[x][y].add(bfs_east)

		# Update the flowfield
		# pro_max_bfs((xs, y), DIST_TO_BASE[(xs, y)])
		# pro_max_bfs((x, y), DIST_TO_BASE[(x, y)])
		pro_max_bfs(xs, y, DIST_TO_BASE[xs][y])
		pro_max_bfs(x, y, DIST_TO_BASE[x][y])
		