def generate_path_map(ws=get_world_size()):
	hws = ws // 2
	ranges = range(ws)
	x_paths = {}
	y_paths = {}
	map_paths = {}

	for i in ranges:
		x_paths[i] = {}
		y_paths[i] = {}
		for j in ranges:
			x_paths[i][j] = []
			y_paths[i][j] = []
			map_paths[(i, j)] = {}
			delta = (j - i + hws) % ws - hws
			for k in range(delta):
				x_paths[i][j].append(East)
				y_paths[i][j].append(North)
			for k in range(-delta):
				x_paths[i][j].append(West)
				y_paths[i][j].append(South)

	for start_pos in map_paths:
		sx, sy = start_pos
		x_path_start = x_paths[sx]
		y_path_start = y_paths[sy]

		for end_pos in map_paths:
			ex, ey = end_pos
			map_paths[start_pos][end_pos] = x_path_start[ex] + y_path_start[ey]
	return map_paths
