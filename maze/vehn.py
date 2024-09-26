# This is not Vehn's code, but implements the core idea.
def vehn(iterations=100):
	AMOUNT = get_world_size() * num_unlocked(Unlocks.Mazes)
	BASE = (4, 4)

	# Geometry tables
	OPP = {North: South, East: West,
		   South: North, West: East}
	DX = {North: 0, South: 0, East: 1, West: -1}
	DY = {North: 1, South: -1, East: 0, West: 0}

	# Mapping information
	WALLS = {}
	DIST_TO_BASE = {BASE: 0}
	DIR_TO_BASE = {BASE: None}
	TREASURE_POS = []

	# Helper recursive function to find walls and treasure
	def scan_maze(back=None):
		if get_entity_type() == Entities.Treasure:
			TREASURE_POS.append((get_pos_x(), get_pos_y()))
		WALLS[(get_pos_x(), get_pos_y())] = set()
		for dir in [North, East, South, West]:
			if dir != back:
				if move(dir):
					scan_maze(OPP[dir])
					move(OPP[dir])
				else:
					WALLS[(get_pos_x(), get_pos_y())].add(dir)

	# Helper to populate the flowfield
	def do_bfs(x, y):
		queue = [(x, y, DIST_TO_BASE[x, y])]
		while queue:
			old_x, old_y, dist = queue.pop(0)
			for dir in [North, South, East, West]:
				if dir not in WALLS[old_x, old_y]:
					new_x = old_x + DX[dir]
					new_y = old_y + DY[dir]
					if ((new_x, new_y) not in DIST_TO_BASE
							or DIST_TO_BASE[new_x, new_y]
													> dist + 1):
						DIST_TO_BASE[new_x, new_y] = dist + 1
						DIR_TO_BASE[new_x, new_y] = OPP[dir]
						queue.append((new_x, new_y, dist + 1))

	# Helper to compute the path to a base
	def get_path_to_base(x, y):
		path = []
		dir = DIR_TO_BASE[x, y]
		while dir:
			path.append(dir)
			x += DX[dir]
			y += DY[dir]
			dir = DIR_TO_BASE[x, y]
		return path

	# Helper to look for missing walls
	def move_and_break_walls(step):
		move(step)
		for dir in list(WALLS[get_pos_x(), get_pos_y()]):
			if move(dir):
				new_x = get_pos_x()
				new_y = get_pos_y()
				move(OPP[dir])
				# Remove both sides of the wall
				WALLS[get_pos_x(), get_pos_y()].remove(dir)
				WALLS[new_x, new_y].remove(OPP[dir])
				# Update the flowfield
				do_bfs(get_pos_x(), get_pos_y())
				do_bfs(new_x, new_y)


	# Start the maze!
	clear()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, AMOUNT)

	# Map the maze
	scan_maze()
	do_bfs(BASE[0], BASE[1])

	# Solve the maze
	goal = TREASURE_POS[0]
	while True:
		# Recycle or harvest treasure if it's here
		while get_entity_type() == Entities.Treasure:
			goal = measure()
			iterations -= 1
			if iterations == 0:
				harvest()
				return
			use_item(Items.Weird_Substance, AMOUNT)

		# Compute paths from drone and goal to base
		dpath = get_path_to_base(get_pos_x(), get_pos_y())
		gpath = get_path_to_base(goal[0], goal[1])
		# Cancel the final moves if they're the same
		while dpath and gpath and dpath[-1] == gpath[-1]:
			gpath.pop()
			dpath.pop()
		# Follow the drone path forward
		for step in dpath:
			move_and_break_walls(step)
		# Follow the goal path backward
		for step in gpath[::-1]:
			move_and_break_walls(OPP[step])


timings = []
for i in range(10000):
	time = get_time()
	vehn()
	time = get_time() - time
	insort(timings, time)
	quick_print("#", i, "min:", timings[0], "max:", timings[-1], "median:", median(timings), "avg:", average(timings), "time:", time)
