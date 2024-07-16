# Constants (as provided)
BASE = (4, 4)
OPP = {North: South, East: West, South: North, West: East}
DX = {North: 0, South: 0, East: 1, West: -1}
DY = {North: 1, South: -1, East: 0, West: 0}
BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer
TREASURE = Entities.Treasure
WALLS = init_walls()
PRE_WALLS_REVERSE_POS = init_walls_reverse()
PRE_WALLS = init_walls_reverse()
PRE_WALLS_REVERSE = init_walls_reverse()
TREASURE_POS = {0: (0, 0)}
TILE_NORTH = tile_north()
TILE_EAST = tile_east()
TILE_SOUTH = tile_south()
TILE_WEST = tile_west()
def bfs_north():
	pass
def bfs_east():
	pass
def bfs_south():
	pass
def bfs_west():
	pass

def tile_north():
	pos = {}
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			pos[(x, y)] = (x, y+1)
	return pos

def tile_east():
	pos = {}
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			pos[(x, y)] = (x+1, y)
	return pos

def tile_south():
	pos = {}
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			pos[(x, y)] = (x, y-1)
	return pos

def tile_west():
	pos = {}
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			pos[(x, y)] = (x-1, y)
	return pos




# Initialize walls with empty sets
def init_walls():
	ws = get_world_size()
	WALLS = {}
	for x in range(ws):
		for y in range(ws):
			WALLS[(x, y)] = set()
	return WALLS

# Initialize walls with full sets
def init_walls_reverse():
	ws = get_world_size()
	WALLS = {}
	for x in range(ws):
		for y in range(ws):
			# WALLS[(x, y)] = {bfs_north, bfs_east, bfs_south, bfs_west}
			WALLS[(x, y)] = {North, East, South, West}
	return WALLS

# Benchmark function
def benchmark_scan(scan_function, name):
	time = get_op_count()
	scan_function()
	quick_print(name + ":", get_op_count() - time)
	# return_to_start()
	# quick_print(TREASURE_POS)

# Helper recursive function returning to the start
def return_to_start(back=None):
	if get_pos_x() == 0 and get_pos_y() == 0:
		return
	for dir in [North, East, South, West]:
		if dir != back:
			if move(dir):
				return_to_start(OPP[dir])
				move(OPP[dir])

# create the maze
clear()
plant(BUSH)
while get_entity_type() == BUSH:
	use_item(FERTILIZER)

# Run benchmarks
# benchmark_scan(vehn_scan, "Vehn")
# benchmark_scan(vehn_scan_prewalls_four_directions_treasure, "vehn_scan_prewalls_four_directions_treasure")
benchmark_scan(vehn_scan_prewalls_four_directions_treasure_reversed_walls, "vehn_scan_prewalls_four_directions_treasure_reversed_walls")
benchmark_scan(vehn_scan_prewalls_four_directions_treasure_reversed_walls_pos, "vehn_scan_prewalls_four_directions_treasure_reversed_walls_pos")


def gen_reverse_walls():
	wllz = {}
	for pos in PRE_WALLS_REVERSE_POS:
		wllz[pos] = []
		for dir in [North, East, South, West]:
			if dir not in PRE_WALLS_REVERSE_POS[pos]:
				wllz[pos].append(dir)
	return wllz
op = get_op_count()
WALL_FUNC = gen_reverse_walls()
quick_print("gen_reverse_walls:", get_op_count() - op)
# results:
# Vehn: 45734 ops
# vehn_scan_prewalls_four_directions_treasure: 43343 ops
# vehn_scan_prewalls_four_directions_treasure_reversed_walls: 43299 ops
# vehn_scan_prewalls_four_directions_treasure_reversed_walls_pos: 44309 ops

# quick_print(WALLS == WALL_FUNC, "WALLS == WALL_FUNC")
# quick_print(PRE_WALLS_REVERSE_POS == PRE_WALLS_REVERSE, "PRE_WALLS_REVERSE_POS == PRE_WALLS_REVERSE")

# for pos in WALLS:
	# quick_print(pos, PRE_WALLS_REVERSE[pos], PRE_WALLS[pos])
	# if WALLS[pos] != PRE_WALLS[pos]:
	# 	quick_print(pos, WALLS[pos], PRE_WALLS[pos])










# 45734 ops
def vehn_scan():
	# Mapping information
	# WALLS = {}
	# TREASURE_POS = []
	# Helper recursive function to find walls and treasure
	def vehn_scan_maze(back=None):
		if measure():
			# TREASURE_POS.append((get_pos_x(), get_pos_y()))
			TREASURE_POS[0] = measure()
		# WALLS[(get_pos_x(), get_pos_y())] = set()
		for dir in [North, East, South, West]:
			if dir != back:
				if move(dir):
					vehn_scan_maze(OPP[dir])
					move(OPP[dir])
				else:
					WALLS[(get_pos_x(), get_pos_y())].add(dir)
	# Map the maze
	vehn_scan_maze()





# 43343 ops
def vehn_scan_prewalls_four_directions_treasure():
	def scan_north():
		if move(North):
			if measure():
				# TREASURE_POS[0] = measure()
				# while not use_item(FERTILIZER):
				# 	pass
				TREASURE_POS[0] = (get_pos_x(), get_pos_y())
			scan_north()
			scan_east()
			scan_west()
			move(South)
		else:
			PRE_WALLS[(get_pos_x(), get_pos_y())].add(North)

	def scan_east():
		if move(East):
			if measure():
				# TREASURE_POS[0] = measure()
				# while not use_item(FERTILIZER):
				# 	pass
				TREASURE_POS[0] = (get_pos_x(), get_pos_y())
			scan_east()
			scan_north()
			scan_south()
			move(West)
		else:
			PRE_WALLS[(get_pos_x(), get_pos_y())].add(East)

	def scan_south():
		if move(South):
			if measure():
				# TREASURE_POS[0] = measure()
				# while not use_item(FERTILIZER):
				# 	pass
				TREASURE_POS[0] = (get_pos_x(), get_pos_y())
			scan_south()
			scan_east()
			scan_west()
			move(North)
		else:
			PRE_WALLS[(get_pos_x(), get_pos_y())].add(South)

	def scan_west():
		if move(West):
			if measure():
				# TREASURE_POS[0] = measure()
				# while not use_item(FERTILIZER):
				# 	pass
				TREASURE_POS[0] = (get_pos_x(), get_pos_y())
			scan_west()
			scan_north()
			scan_south()
			move(East)
		else:
			PRE_WALLS[(get_pos_x(), get_pos_y())].add(West)

	# Start the maze mapping
	scan_north()
	scan_east()
	scan_south()
	scan_west()





# 45477 ops
def vehn_scan_prewalls_four_directions_treasure_reversed_walls():
	def scan_north():
		if move(North):
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE[pos].remove(South)
			PRE_WALLS[pos].remove(North)
			if measure():
				TREASURE_POS[0] = pos
			scan_north()
			scan_east()
			scan_west()
			move(South)
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE[pos].remove(North)
			PRE_WALLS[pos].remove(South)
		# else:
		# 	PRE_WALLS[(get_pos_x(), get_pos_y())].remove(North)

	def scan_east():
		if move(East):
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE[pos].remove(West)
			PRE_WALLS[pos].remove(East)
			if measure():
				TREASURE_POS[0] = pos
			scan_east()
			scan_north()
			scan_south()
			move(West)
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE[pos].remove(East)
			PRE_WALLS[pos].remove(West)
		# else:
		# 	PRE_WALLS[(get_pos_x(), get_pos_y())].remove(East)

	def scan_south():
		if move(South):
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE[pos].remove(North)
			PRE_WALLS[pos].remove(South)
			if measure():
				TREASURE_POS[0] = pos
			scan_south()
			scan_east()
			scan_west()
			move(North)
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE[pos].remove(South)
			PRE_WALLS[pos].remove(North)
		# else:
		# 	PRE_WALLS[(get_pos_x(), get_pos_y())].remove(South)

	def scan_west():
		if move(West):
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE[pos].remove(East)
			PRE_WALLS[pos].remove(West)
			if measure():
				TREASURE_POS[0] = pos
			scan_west()
			scan_north()
			scan_south()
			move(East)
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE[pos].remove(West)
			PRE_WALLS[pos].remove(East)
		# else:
		# 	PRE_WALLS[(get_pos_x(), get_pos_y())].remove(West)

	# Start the maze mapping
	scan_north()
	scan_east()
	scan_south()
	scan_west()









# 44879 ops
def vehn_scan_prewalls_four_directions_treasure_reversed_walls_pos():
	def scan_north():
		if move(North):
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE_POS[pos].remove(South)
			PRE_WALLS_REVERSE_POS[TILE_SOUTH[pos]].remove(North)
			WALLS[pos].add(South)
			WALLS[TILE_SOUTH[pos]].add(North)
			if measure():
				TREASURE_POS[0] = pos
			scan_north()
			scan_east()
			scan_west()
			move(South)

	def scan_east():
		if move(East):
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE_POS[pos].remove(West)
			PRE_WALLS_REVERSE_POS[TILE_WEST[pos]].remove(East)
			WALLS[pos].add(West)
			WALLS[TILE_WEST[pos]].add(East)
			if measure():
				TREASURE_POS[0] = pos
			scan_east()
			scan_north()
			scan_south()
			move(West)

	def scan_south():
		if move(South):
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE_POS[pos].remove(North)
			PRE_WALLS_REVERSE_POS[TILE_NORTH[pos]].remove(South)
			WALLS[pos].add(North)
			WALLS[TILE_NORTH[pos]].add(South)
			if measure():
				TREASURE_POS[0] = pos
			scan_south()
			scan_east()
			scan_west()
			move(North)

	def scan_west():
		if move(West):
			pos = (get_pos_x(), get_pos_y())
			PRE_WALLS_REVERSE_POS[pos].remove(East)
			PRE_WALLS_REVERSE_POS[TILE_EAST[pos]].remove(West)
			WALLS[pos].add(East)
			WALLS[TILE_EAST[pos]].add(West)
			if measure():
				TREASURE_POS[0] = pos
			scan_west()
			scan_north()
			scan_south()
			move(East)

	scan_north()
	scan_east()
	scan_south()
	scan_west()
