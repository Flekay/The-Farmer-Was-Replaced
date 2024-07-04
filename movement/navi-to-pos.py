def wrap_around_distance(start, end, size):
	# Calculate the wrap-around distance between two points in one dimension.
	return min(abs(start - end), size - abs(start - end))

def get_shortest_path(start, end, size):
	# Get the shortest path directions from start to end in a wrap-around map.
	x1, y1 = start
	x2, y2 = end
	path = []

	# Calculate shortest x distance
	x_distance = wrap_around_distance(x1, x2, size)
	if (x1 + x_distance) % size == x2:
		for i in range(x_distance):
			path.append(East)
	else:
		for i in range(x_distance):
			path.append(West)

	# Calculate shortest y distance
	y_distance = wrap_around_distance(y1, y2, size)
	if (y1 + y_distance) % size == y2:
		for i in range(y_distance):
			path.append(North)
	else:
		for i in range(y_distance):
			path.append(South)

	return path

def generate_path_map(size=get_world_size()):
	# Generate a dictionary of dictionaries containing shortest paths in a wrap-around map.
	map_paths = {}

	for x in range(size):
		for y in range(size):
			start = (x, y)
			map_paths[start] = {}
			for i in range(size):
				for j in range(size):
					end = (i, j)
					if start == end:
						map_paths[start][end] = []
					else:
						map_paths[start][end] = get_shortest_path(start, end, size)

	return map_paths