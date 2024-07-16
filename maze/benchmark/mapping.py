# Constants
BASE = (4, 4)
OPP = {North: South, East: West, South: North, West: East}
DX = {North: 0, South: 0, East: 1, West: -1}
DY = {North: 1, South: -1, East: 0, West: 0}
DIST_TO_BASE = {BASE: 0}
DIST_TO_BASE_2 = init_dist_to_base()
DIR_TO_BASE = {BASE: None}
DIR_TO_BASE_2 = {BASE: None}
BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer
TREASURE = Entities.Treasure
WALLS = init_walls()
TREASURE_POS = {0: (0, 0)}
BFG = {North: bfs_north, East: bfs_east, South: bfs_south, West: bfs_west}
queuex = []


# Initialize walls with empty sets
def init_walls():
	ws = get_world_size()
	WALLS = {}
	for x in range(ws):
		for y in range(ws):
			WALLS[(x, y)] = set()
	return WALLS

# Initialize walls with empty sets
def init_dist_to_base():
	ws = get_world_size()
	DIST_TO_BASE = {}
	for x in range(ws):
		for y in range(ws):
			if (x, y) == BASE:
				DIST_TO_BASE[(x, y)] = 0
			else:
				DIST_TO_BASE[(x, y)] = 999
	return DIST_TO_BASE

# scan maze
def maze_scan():
	def vehn_scan_maze(back=None):
		if measure():
			TREASURE_POS[0] = measure()
		# WALLS[(get_pos_x(), get_pos_y())] = set()
		for dir in [North, East, South, West]:
			if dir != back:
				if move(dir):
					vehn_scan_maze(OPP[dir])
					move(OPP[dir])
				else:
					WALLS[(get_pos_x(), get_pos_y())].add(dir)
					# WALL_FUNC[(get_pos_x(), get_pos_y())].add(BFG[dir])
	vehn_scan_maze()

def gen_reverse_walls():
	wllz = {}
	for pos in WALLS:
		wllz[pos] = []
		for dir in [North, East, South, West]:
			if dir not in WALLS[pos]:
				wllz[pos].append(BFG[dir])
	return wllz




# Benchmark function
def benchmark_mapping(scan_function, name):
	time = get_op_count()
	scan_function(BASE[0], BASE[1])
	quick_print(name + ":", get_op_count() - time)

# create the maze
clear()
plant(BUSH)
while get_entity_type() == BUSH:
	use_item(FERTILIZER)
maze_scan()
WALL_FUNC = gen_reverse_walls()

# Run benchmarks
benchmark_mapping(do_bfs, "do_bfs")
benchmark_mapping(do_bfs_four_directions_optimized, "do_bfs_four_directions_optimized")
DIST_TO_BASE_2 = init_dist_to_base()
DIR_TO_BASE_2 = {BASE: None}
benchmark_mapping(do_bfs_four_directions_optimized_func, "do_bfs_four_directions_optimized_func")
quick_print(DIST_TO_BASE == DIST_TO_BASE_2, "DIST_TO_BASE")
quick_print(DIR_TO_BASE == DIR_TO_BASE_2, "DIR_TO_BASE")













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














def do_bfs_four_directions_optimized(start_x, start_y):
	queue = [(start_x, start_y, DIST_TO_BASE_2[start_x, start_y])]

	while queue:
		x, y, d = queue.pop(0)
		nd = d + 1

		if North not in WALLS[x, y]:
			ny = y + 1
			if nd < DIST_TO_BASE_2[(x, ny)]:
				DIST_TO_BASE_2[(x, ny)] = nd
				DIR_TO_BASE_2[(x, ny)] = South
				queue.append((x, ny, nd))

		if South not in WALLS[x, y]:
			ny = y - 1
			if nd < DIST_TO_BASE_2[(x, ny)]:
				DIST_TO_BASE_2[(x, ny)] = nd
				DIR_TO_BASE_2[(x, ny)] = North
				queue.append((x, ny, nd))

		if East not in WALLS[x, y]:
			nx = x + 1
			if nd < DIST_TO_BASE_2[(nx, y)]:
				DIST_TO_BASE_2[(nx, y)] = nd
				DIR_TO_BASE_2[(nx, y)] = West
				queue.append((nx, y, nd))

		if West not in WALLS[x, y]:
			nx = x - 1
			if nd < DIST_TO_BASE_2[(nx, y)]:
				DIST_TO_BASE_2[(nx, y)] = nd
				DIR_TO_BASE_2[(nx, y)] = East
				queue.append((nx, y, nd))













def bfs_north(x, y, d):
	y += 1
	if d < DIST_TO_BASE_2[(x, y)]:
		DIST_TO_BASE_2[(x, y)] = d
		DIR_TO_BASE_2[(x, y)] = South
		queuex.append((x, y, d))

def bfs_south(x, y, d):
	y -= 1
	if d < DIST_TO_BASE_2[(x, y)]:
		DIST_TO_BASE_2[(x, y)] = d
		DIR_TO_BASE_2[(x, y)] = North
		queuex.append((x, y, d))

def bfs_east(x, y, d):
	x += 1
	if d < DIST_TO_BASE_2[(x, y)]:
		DIST_TO_BASE_2[(x, y)] = d
		DIR_TO_BASE_2[(x, y)] = West
		queuex.append((x, y, d))

def bfs_west(x, y, d):
	x -= 1
	if d < DIST_TO_BASE_2[(x, y)]:
		DIST_TO_BASE_2[(x, y)] = d
		DIR_TO_BASE_2[(x, y)] = East
		queuex.append((x, y, d))

def do_bfs_four_directions_optimized_func(start_x, start_y):
	queuex.append((start_x, start_y, DIST_TO_BASE_2[start_x, start_y]))
	while queuex:
		x, y, d = queuex.pop(0)
		for func in WALL_FUNC[(x, y)]:
			func(x, y, d + 1)
