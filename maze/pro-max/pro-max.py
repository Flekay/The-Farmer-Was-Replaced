# globals scan
WALL = init_wall()
PATH = init_path()
TREASURE_POS = {0: (0, 0)}
FERTILIZER = Items.Fertilizer
TILE_NORTH = tile_north()
TILE_EAST = tile_east()
TILE_SOUTH = tile_south()
TILE_WEST = tile_west()

# globals bfs
BASE = (4, 4)
# PATH = init_path()
DIR_TO_BASE = {BASE: None}
DIST_TO_BASE = init_dist_to_base()
queuex = []

# globals path
DX = {North: 0, South: 0, East: 1, West: -1}
DY = {North: 1, South: -1, East: 0, West: 0}

# globals pro-max
OPP = {North: South, East: West, South: North, West: East}
BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer
TREASURE = Entities.Treasure




# This is not Vehn's code, but implements the core idea.
def pro_max(iterations=300):
	# Map the maze
	pro_max_scan()
	pro_max_bfs(BASE[0], BASE[1])

	# Solve the maze
	goal = TREASURE_POS[0]
	while True:
		# Recycle or harvest treasure if it's here
		while get_entity_type() == TREASURE:
			goal = measure()
			iterations -= 1
			if iterations == 0:
				harvest()
				return
			while not use_item(FERTILIZER):
				pass

		# Compute paths from drone and goal to base
		dpath = pro_max_path(get_pos_x(), get_pos_y())
		gpath = pro_max_path(goal[0], goal[1])
		# Cancel the final moves if they're the same
		while dpath and gpath and dpath[-1] == gpath[-1]:
			gpath.pop()
			dpath.pop()
		# Follow the drone path forward
		for step in dpath:
			move_n_break(step)
		# Follow the goal path backward
		for step in gpath[::-1]:
			move_n_break(OPP[step])


timings = []
for i in range(10000):
	# setup the maze!
	clear()
	plant(BUSH)
	while get_entity_type() == BUSH:
		use_item(FERTILIZER)
	# run the timed pro-max algorithm
	time = get_time()
	pro_max()
	time = get_time() - time
	insort(timings, time)
	quick_print("#", i, "min:", timings[0], "max:", timings[-1], "median:", median(timings), "avg:", average(timings), "time:", time)
	# reset
	PATH = init_path()
	WALL = init_wall()
	DIST_TO_BASE = init_dist_to_base()
	DIR_TO_BASE = {BASE: None}
