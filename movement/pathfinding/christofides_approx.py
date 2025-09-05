distances = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1)

# Cheapest insertion - often better than nearest neighbor
def christofides_approx(points, start_pos=None):
	if start_pos:
		cur_x, cur_y = start_pos
	else:
		cur_x = get_pos_x()
		cur_y = get_pos_y()

	if not points:
		return []

	# Start with closest point
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

	# For each remaining point, find cheapest insertion
	while points:
		best_cost = 200
		best_point = None
		best_pos = 0

		for point in points:
			px, py = point
			
			# Try inserting at each position
			for i in range(len(path) + 1):
				if i == 0:
					prev_pos = (cur_x, cur_y)
				else:
					prev_pos = path[i-1]
				
				if i == len(path):
					# Insert at end
					cost = distances[px - prev_pos[0]] + distances[py - prev_pos[1]]
				else:
					next_pos = path[i]
					# Cost = new edges - old edge
					old_cost = distances[next_pos[0] - prev_pos[0]] + distances[next_pos[1] - prev_pos[1]]
					new_cost = (distances[px - prev_pos[0]] + distances[py - prev_pos[1]] +
							   distances[next_pos[0] - px] + distances[next_pos[1] - py])
					cost = new_cost - old_cost

				if cost < best_cost:
					best_cost = cost
					best_point = point
					best_pos = i

		points.remove(best_point)
		path.insert(best_pos, best_point)

	return path
