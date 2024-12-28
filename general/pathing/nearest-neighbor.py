def nearest_neighbor(start_pos, points):
	path = [start_pos]

	while points:
		nearest = None
		nearest_dist = 999
		for point in points:
			dist = distance(path[-1], point)
			if dist < nearest_dist:
				nearest = point
				nearest_dist = dist

		path.append(nearest)
		points.remove(nearest)

	return path
