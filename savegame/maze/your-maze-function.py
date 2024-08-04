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