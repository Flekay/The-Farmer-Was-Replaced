def generate_path_map(ws=get_world_size()):
	def generate_paths(delta):
		if delta == 0:
			return [], []
		elif delta > 0:
			x_path, y_path = generate_paths(delta - 1)
			return x_path + [East], y_path + [North]
		else:
			x_path, y_path = generate_paths(delta + 1)
			return x_path + [West], y_path + [South]

	# Precompute paths for all possible delta values
	hws = ws // 2
	precomputed_paths = {}

	for delta in range(-hws, hws + 1):
		precomputed_paths[delta] = generate_paths(delta)

	ranges = range(ws)
	x_paths = {}
	y_paths = {}
	map_paths = {}

	for i in ranges:
		x_paths[i] = {}
		y_paths[i] = {}
		for j in ranges:
			delta = (j - i + hws) % ws - hws
			x_paths[i][j], y_paths[i][j] = precomputed_paths[delta]
			map_paths[(i, j)] = {}

	for start_pos in map_paths:
		sx, sy = start_pos
		x_path_start = x_paths[sx]
		y_path_start = y_paths[sy]

		for end_pos in map_paths:
			ex, ey = end_pos
			map_paths[start_pos][end_pos] = x_path_start[ex] + y_path_start[ey]
	return map_paths
