# globals bfs
BASE = (4, 4)
PATH = init_path()
DIR_TO_BASE = {BASE: None}
DIST_TO_BASE = init_dist_to_base()
queuex = []

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





def bfs_north(x, y, d):
	y += 1
	if d < DIST_TO_BASE[(x, y)]:
		DIST_TO_BASE[(x, y)] = d
		DIR_TO_BASE[(x, y)] = South
		queuex.append((x, y, d))

def bfs_south(x, y, d):
	y -= 1
	if d < DIST_TO_BASE[(x, y)]:
		DIST_TO_BASE[(x, y)] = d
		DIR_TO_BASE[(x, y)] = North
		queuex.append((x, y, d))

def bfs_east(x, y, d):
	x += 1
	if d < DIST_TO_BASE[(x, y)]:
		DIST_TO_BASE[(x, y)] = d
		DIR_TO_BASE[(x, y)] = West
		queuex.append((x, y, d))

def bfs_west(x, y, d):
	x -= 1
	if d < DIST_TO_BASE[(x, y)]:
		DIST_TO_BASE[(x, y)] = d
		DIR_TO_BASE[(x, y)] = East
		queuex.append((x, y, d))

def pro_max_bfs(start_x, start_y):
	queuex.append((start_x, start_y, DIST_TO_BASE[start_x, start_y]))
	while queuex:
		x, y, d = queuex.pop(0)
		for func in PATH[(x, y)]:
			func(x, y, d + 1)
