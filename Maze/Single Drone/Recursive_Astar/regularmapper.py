def mapper(wall_dict, invert, pos_add, ws, ws_square):
	rot = {}
	rot[North] = (West, North, East, South)
	rot[East] = (North, East, South, West)
	rot[South] = (East, South, West, North)
	rot[West] = (South, West, North, East)
	
	coord = get_pos_x() + (get_pos_y() * ws)
	
	visited = {coord}
	
	if measure():
		tgt = coord
	
	dir = North
	while len(visited) != ws_square:
		for dir in rot[dir]:
			if move(dir):
				walls = wall_dict[coord]
				if dir in walls:
					walls.remove(dir)
				coord += pos_add[dir]
				if measure():
					tgt = coord
				walls = wall_dict[coord]
				inverted_dir = invert[dir]
				if inverted_dir in walls:
					walls.remove(inverted_dir)
				visited.add(coord)
				break
	return tgt