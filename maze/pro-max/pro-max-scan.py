# globals scan
PATH = init_path()
WALL = init_wall()
TREASURE_POS = {0: (0, 0)}
AMOUNT = {0: get_world_size() * num_unlocked(Unlocks.Mazes)}
TILE_NORTH = tile_north()
TILE_EAST = tile_east()
TILE_SOUTH = tile_south()
TILE_WEST = tile_west()
VISITED = set()
MISSING = init_missing()

def init_missing():
	ws = get_world_size()
	MISSING = set()
	for x in range(ws):
		for y in range(ws):
			MISSING.add((x, y))
	return MISSING

# Initialize WALL with empty sets
def init_path():
	ws = get_world_size()
	PATHH = {}
	for x in range(ws):
		for y in range(ws):
			PATHH[(x, y)] = set()
	return PATHH

# Initialize WALL with full sets
def init_wall():
	ws = get_world_size()
	WALLL = {}
	for x in range(ws):
		for y in range(ws):
			WALLL[(x, y)] = {mnb_north, mnb_east, mnb_south, mnb_west}
	return WALLL

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






def scan_north():
	if move(North):
		pos = (get_pos_x(), get_pos_y())
		WALL[pos].remove(mnb_south)
		WALL[TILE_SOUTH[pos]].remove(mnb_north)
		PATH[pos].add(bfs_south)
		PATH[TILE_SOUTH[pos]].add(bfs_north)
		if measure():
			# option 1
			# explore the maze first
			TREASURE_POS[0] = pos

			# option 2
			# harvest treasure immediately
			# fails 1/3 of the time
			# because i dont have a list of visited tiles
			# TREASURE_POS[0] = measure()
			# use_item(Items.Weird_Substance, AMOUNT[0])
		scan_north()
		scan_east()
		scan_west()
		move(South)

def scan_east():
	if move(East):
		pos = (get_pos_x(), get_pos_y())
		WALL[pos].remove(mnb_west)
		WALL[TILE_WEST[pos]].remove(mnb_east)
		PATH[pos].add(bfs_west)
		PATH[TILE_WEST[pos]].add(bfs_east)
		if measure():
			TREASURE_POS[0] = pos
			# TREASURE_POS[0] = measure()
			# use_item(Items.Weird_Substance, AMOUNT[0])
		scan_east()
		scan_north()
		scan_south()
		move(West)

def scan_south():
	if move(South):
		pos = (get_pos_x(), get_pos_y())
		WALL[pos].remove(mnb_north)
		WALL[TILE_NORTH[pos]].remove(mnb_south)
		PATH[pos].add(bfs_north)
		PATH[TILE_NORTH[pos]].add(bfs_south)
		if measure():
			TREASURE_POS[0] = pos
			# TREASURE_POS[0] = measure()
			# use_item(Items.Weird_Substance, AMOUNT[0])
		scan_south()
		scan_east()
		scan_west()
		move(North)

def scan_west():
	if move(West):
		pos = (get_pos_x(), get_pos_y())
		WALL[pos].remove(mnb_east)
		WALL[TILE_EAST[pos]].remove(mnb_west)
		PATH[pos].add(bfs_east)
		PATH[TILE_EAST[pos]].add(bfs_west)
		if measure():
			TREASURE_POS[0] = pos
			# TREASURE_POS[0] = measure()
			# use_item(Items.Weird_Substance, AMOUNT[0])
		scan_west()
		scan_north()
		scan_south()
		move(East)
