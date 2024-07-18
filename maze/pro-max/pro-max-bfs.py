# globals bfs
BASE = (4, 4)
PATH = init_path()
DIR_TO_BASE = {BASE: None}
DIST_TO_BASE = init_dist_to_base()
queuepos = []
queued = {}

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





def bfs_north(pos, dist):
	pos = TILE_NORTH[pos]
	if dist < DIST_TO_BASE[pos]:
		DIST_TO_BASE[pos] = dist
		DIR_TO_BASE[pos] = South
		queuepos.append((pos, dist))

def bfs_east(pos, dist):
	pos = TILE_EAST[pos]
	if dist < DIST_TO_BASE[pos]:
		DIST_TO_BASE[pos] = dist
		DIR_TO_BASE[pos] = West
		queuepos.append((pos, dist))

def bfs_south(pos, dist):
	pos = TILE_SOUTH[pos]
	if dist < DIST_TO_BASE[pos]:
		DIST_TO_BASE[pos] = dist
		DIR_TO_BASE[pos] = North
		queuepos.append((pos, dist))

def bfs_west(pos, dist):
	pos = TILE_WEST[pos]
	if dist < DIST_TO_BASE[pos]:
		DIST_TO_BASE[pos] = dist
		DIR_TO_BASE[pos] = East
		queuepos.append((pos, dist))

def pro_max_bfs(pos):
	queuepos.append((pos, DIST_TO_BASE[pos]))
	while queuepos:
		pos, dist = queuepos.pop(0)
		for func in PATH[pos]:
			func(pos, dist+1)
