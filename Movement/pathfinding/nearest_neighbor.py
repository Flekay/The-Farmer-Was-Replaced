distances = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1)
# The nearest_neighbor function takes a list of points and finds the shortest path visiting all points
# using the nearest neighbor heuristic algorithm.
#
# Arguments:
#	points (list or set): a list or set of (x, y) coordinate tuples to visit
#	start_pos (tuple, optional): starting position as (x, y). If None, uses current position
#
# Returns:
#	list: ordered list of points representing the path to visit all locations
#
# Example:
#	points = [(1, 2), (3, 4), (0, 1)]
#	path = nearest_neighbor(points, (0, 0))
def nearest_neighbor(points, start_pos=None):
	path = []
	if start_pos:
		cur_x, cur_y = start_pos
	else:
		cur_x = get_pos_x()
		cur_y = get_pos_y()

	while points:
		closest_dis = 20
		closest = None
		for pos in points:
			x, y = pos
			dis = distances[x - cur_x] + distances[y - cur_y]
			if dis < closest_dis:
				closest = pos
				closest_dis = dis
		path.append(closest)
		points.remove(closest)
		cur_x, cur_y = closest
	return path
