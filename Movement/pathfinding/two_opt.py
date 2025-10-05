distances = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1)

# Simple 2-opt on nearest neighbor - fast improvement
def two_opt(points, start_pos=None):
	if start_pos:
		cur_x, cur_y = start_pos
	else:
		cur_x = get_pos_x()
		cur_y = get_pos_y()

	# Build nearest neighbor tour first
	tour = []
	while points:
		closest_dis = 20
		closest = None
		for pos in points:
			x, y = pos
			dis = distances[x - cur_x] + distances[y - cur_y]
			if dis < closest_dis:
				closest = pos
				closest_dis = dis
		tour.append(closest)
		points.remove(closest)
		cur_x, cur_y = closest

	# Only do 1 pass of 2-opt for speed
	for i in range(len(tour)):
		for j in range(i + 2, len(tour)):
			if j == len(tour) - 1:
				continue  # Skip wrap around for simplicity
			
			# Check if swapping edges improves
			curr_dist = (distances[tour[i+1][0] - tour[i][0]] + distances[tour[i+1][1] - tour[i][1]] +
						 distances[tour[j+1][0] - tour[j][0]] + distances[tour[j+1][1] - tour[j][1]])
			
			new_dist = (distances[tour[j][0] - tour[i][0]] + distances[tour[j][1] - tour[i][1]] +
					   distances[tour[j+1][0] - tour[i+1][0]] + distances[tour[j+1][1] - tour[i+1][1]])
			
			if new_dist < curr_dist:
				# Reverse segment
				while i + 1 < j:
					tour[i + 1], tour[j] = tour[j], tour[i + 1]
					i += 1
					j -= 1
				break

	return tour
