def do_maze(iterations=100):
	opp = {North: South, East: West,
		   South: North, West: East}
	dx = {North: 0, East: 1, South: 0, West: -1}
	dy = {North: 1, East: 0, South: -1, West: 0}

	harvest()
	plant(Entities.Bush)
	while get_entity_type() == Entities.Bush:
		use_item(Items.Fertilizer)

	x, y = get_pos_x(), get_pos_y()
	goalx, goaly = None, None
	while iterations > 0:
		while get_entity_type() == Entities.Treasure:
			if measure() == None:
				iterations = 0
				break
			goalx, goaly = measure()
			iterations -= 1
			if iterations <= 0:
				break
			while not use_item(Items.Fertilizer):
				pass

		stack = [([North, East, South, West], None)]
		visited = {(get_pos_x(), get_pos_y())}

		while get_entity_type() != Entities.Treasure:
			dirs, back = stack[-1]  # stack peek
			oldx = x
			oldy = y
			dir = None
			while len(dirs) > 0:
				dir = dirs.pop()
				x = oldx + dx[dir]
				y = oldy + dy[dir]
				if (x, y) in visited or not move(dir):
					dir = None
					continue
				else:
					break
			if dir == None:
				stack.pop()   # Get rid of the node we peeked
				if back == None:
					print("I give up!")
					while True:
						do_a_flip()
				move(back)
				x = oldx + dx[back]
				y = oldy + dy[back]
			else:
				visited.add((x, y))
				stack.append(
					(get_ranked_dirs(x, y, goalx, goaly, opp[dir]),
					 opp[dir]))
	harvest()

def get_ranked_dirs(pos_x, pos_y, goal_x, goal_y, exclude=None):
	if goal_x == None:
		all_dirs = [(1, North), (2, East), (3, South), (4, West)]
	else:
		all_dirs = [
			(goal_y - pos_y + 0.1, North),
			(goal_x - pos_x + 0.2, East),
			(pos_y - goal_y + 0.3, South),
			(pos_x - goal_x + 0.4, West)]

	ranked_dirs = []
	for i in range(len(all_dirs)):
		worst_dir = min(all_dirs)
		all_dirs.remove(worst_dir)
		if worst_dir[1] != exclude:
			ranked_dirs.append(worst_dir[1])

	return ranked_dirs

# Example usage
start_time = get_time()
do_maze(300)
quick_print("Maze time:", get_time() - start_time)