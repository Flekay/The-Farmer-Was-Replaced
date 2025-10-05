def heuristic(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(goal, snake_body):
	start = get_pos_x(), get_pos_y()
	open_list = [(0, start, snake_body)]
	came_from = {}
	g_score = {start: 0}
	f_score = {start: heuristic(start, goal)}
	ws = get_world_size() - 1

	while open_list:
		# Find the node with the lowest f_score
		current_index = 0
		for i in range(len(open_list)):
			if open_list[i][0] < open_list[current_index][0]:
				current_index = i
		current_f, current, current_snake_body = open_list.pop(current_index)

		if current == goal:
			path = []
			while current in came_from:
				prev = came_from[current]
				if current[0] > prev[0]:
					path.append(East)
				elif current[0] < prev[0]:
					path.append(West)
				elif current[1] > prev[1]:
					path.append(North)
				elif current[1] < prev[1]:
					path.append(South)
				current = prev
			return path[::-1], [goal] + current_snake_body

		neighbors = [
			(current[0] + 1, current[1]),  # East
			(current[0] - 1, current[1]),  # West
			(current[0], current[1] + 1),  # North
			(current[0], current[1] - 1)   # South
		]

		for neighbor in neighbors:
			if neighbor in current_snake_body:
				continue  # Skip if the neighbor is part of the snake's body
			if neighbor[0] < 0 or neighbor[0] > ws or neighbor[1] < 0 or neighbor[1] > ws:
				continue

			tentative_g_score = g_score[current] + 1
			if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = tentative_g_score
				f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

				# Update the snake's body positions
				new_snake_body = list(current_snake_body)
				new_snake_body.pop(0)  # Remove the tail
				new_snake_body.append(current)  # Add the new head position

				in_open_list = False
				for item in open_list:
					if neighbor == item[1]:
						in_open_list = True
						break
				if not in_open_list:
					open_list.append((f_score[neighbor], neighbor, new_snake_body))

	return [], []

clear()
bone()
def bone():
	change_hat(Hats.Dinosaur_Hat)
	cur_x, cur_y = measure()
	for _ in range(cur_x):
		move(East)
	if not cur_y:
		snake_body = [(cur_x, cur_y), (cur_x - 1, cur_y)]
	else:
		for _ in range(cur_y):
			move(North)
		snake_body = [(cur_x, cur_y), (cur_x, cur_y - 1)]

	while True:
		path, snake_body = a_star(measure(), snake_body)
		if not path:
			break
		for step in path:
			move(step)
	clear()
