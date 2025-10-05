distances = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1)

# Farthest insertion - sometimes better than nearest neighbor
def farthest_insertion(points, start_pos=None):
	if start_pos:
		cur_x, cur_y = start_pos
	else:
		cur_x = get_pos_x()
		cur_y = get_pos_y()

	# Find farthest point from start
	max_dis = 0
	first = None
	for pos in points:
		x, y = pos
		dis = distances[x - cur_x] + distances[y - cur_y]
		if dis > max_dis:
			max_dis = dis
			first = pos

	points.remove(first)
	path = [first]

	# Insert remaining points
	while points:
		# Find point farthest from current tour
		max_min_dis = 0
		farthest = None

		for point in points:
			px, py = point
			min_dis_to_tour = 20

			# Distance to start
			dis = distances[px - cur_x] + distances[py - cur_y]
			if dis < min_dis_to_tour:
				min_dis_to_tour = dis

			# Distance to tour points
			for tour_point in path:
				tx, ty = tour_point
				dis = distances[px - tx] + distances[py - ty]
				if dis < min_dis_to_tour:
					min_dis_to_tour = dis

			if min_dis_to_tour > max_min_dis:
				max_min_dis = min_dis_to_tour
				farthest = point

		# Find best insertion position for farthest point
		best_pos = 0
		best_cost = 200
		px, py = farthest

		for i in range(len(path) + 1):
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
				best_pos = i

		path.insert(best_pos, farthest)
		points.remove(farthest)

	return path
