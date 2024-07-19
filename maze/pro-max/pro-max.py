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
PATH = init_path()
DIR_TO_BASE = {BASE: None}
DIST_TO_BASE = init_dist_to_base()
queuepos = []
queued = {}

# globals path
DPOS = generate_dpos()

def generate_dpos():
	dpos = {}
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			dpos[(x, y)] = {North: (x, y + 1), South: (x, y - 1), East: (x + 1, y), West: (x - 1, y)}
	return dpos

# globals pro-max
OPP = {North: South, East: West, South: North, West: East}
BUSH = Entities.Bush




def pro_max(iterations):
	# scan the maze
	scan_north()
	scan_east()
	scan_south()
	scan_west()

	# map the map
	pro_max_bfs(BASE)


	# get_path_to_base
	# only works if you move to BASE befor the maze is initialized
	goal = TREASURE_POS[0]
	gpath = []
	ddpath = []
	dir = DIR_TO_BASE[goal]
	while dir:
		gpath.insert(0, OPP[dir])
		ddpath.append(dir)
		goal = DPOS[goal][dir]
		dir = DIR_TO_BASE[goal]

	# Follow the goal path backward
	for step in gpath:
		move(step)



	for i in range(iterations - 2):
		# Compute paths from drone to base
		dpath = ddpath
		# Recycle treasure
		goal = measure()
		while measure():
			use_item(FERTILIZER)
		# Compute paths from goal to base
		gpath = []
		dir = DIR_TO_BASE[goal]
		while dir:
			gpath.append(dir)
			goal = DPOS[goal][dir]
			dir = DIR_TO_BASE[goal]
		ddpath = gpath + []
		# Cancel the final moves if they're the same
		while dpath and gpath and dpath[-1] == gpath[-1]:
			gpath.pop()
			dpath.pop()
		# Follow the drone path forward
		for step in dpath:
			move(step)
			for func in WALL[get_pos_x(), get_pos_y()]:
				func()
		# Follow the goal path backward
		for step in gpath[::-1]:
			move(OPP[step])
			for func in WALL[get_pos_x(), get_pos_y()]:
				func()


timings = []
for i in range(133337):
	clear()
	time = get_op_count()
	# setup the maze!
	move_to(BASE)
	plant(BUSH)
	while get_entity_type() == BUSH:
		use_item(FERTILIZER)
	# run the timed pro-max algorithm
	pro_max(300)
	# Harvest the treasure
	harvest()
	time = (get_op_count() - time)/16800
	insort(timings, time)
	quick_print("#", i, "min:", str(timings[0]), "max:", timings[-1], "median:", median(timings), "avg:", average(timings), "time:", time)
	# reset
	PATH = init_path()
	WALL = init_wall()
	DIST_TO_BASE = init_dist_to_base()
	DIR_TO_BASE = {BASE: None}
