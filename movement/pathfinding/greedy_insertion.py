distances = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1)

# Simple insertion heuristic - minimal overhead
def greedy_insertion(points, start_pos=None):
	if start_pos:
		cur_x, cur_y = start_pos
	else:
		cur_x = get_pos_x()
		cur_y = get_pos_y()

	# Find closest point to start
	min_dis = 20
	first = None
	for pos in points:
		x, y = pos
		dis = distances[x - cur_x] + distances[y - cur_y]
		if dis < min_dis:
			min_dis = dis
			first = pos

	points.remove(first)
	path = [first]

	# Insert remaining points at best position
	while points:
		best_pos = 0
		best_point = None
		best_cost = 200  # High initial cost

		for point in points:
			px, py = point
			for i in range(len(path) + 1):
				# Calculate insertion cost
				if i == 0:
					prev_x = cur_x
					prev_y = cur_y
				else:
					prev_x, prev_y = path[i-1]

				if i == len(path):
					cost = distances[px - prev_x] + distances[py - prev_y]
				else:
					next_x, next_y = path[i]
					old_cost = distances[next_x - prev_x] + distances[next_y - prev_y]
					new_cost = distances[px - prev_x] + distances[py - prev_y] + distances[next_x - px] + distances[next_y - py]
					cost = new_cost - old_cost

				if cost < best_cost:
					best_cost = cost
					best_point = point
					best_pos = i

		path.insert(best_pos, best_point)
		points.remove(best_point)

	return path
