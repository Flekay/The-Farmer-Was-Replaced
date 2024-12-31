# globals bfs
BASE = (4, 4)
PATH = init_path()
DIR_TO_BASE = {BASE: None}
DIST_TO_BASE = init_dist_to_base()
queuepos = []
queued = {}

# Initialize walls with empty sets
def init_dist_to_base():
	ws = get_world_size()+1
	DIST_TO_BASE = []
	for x in range(ws):
		DIST_TO_BASE.append([])
		for y in range(ws):
			if (x, y) == BASE:
				# DIST_TO_BASE[(x, y)] = 0
				DIST_TO_BASE[x].append(0)
			else:
				# DIST_TO_BASE[(x, y)] = 999
				DIST_TO_BASE[x].append(999)
	return DIST_TO_BASE




# def bfs_north(pos, dist):
	# pos = TILE_NORTH[pos]
	# if dist < DIST_TO_BASE[pos]:
	# 	DIST_TO_BASE[pos] = dist
	# 	DIR_TO_BASE[pos] = South
	# 	pro_max_bfs(pos, dist)
def bfs_north(x, y, dist):
	y += 1
	if dist < DIST_TO_BASE[x][y]:
		DIST_TO_BASE[x][y] = dist
		DIR_TO_BASE[x,y] = South
		pro_max_bfs(x, y, dist)

# def bfs_east(pos, dist):
# 	pos = TILE_EAST[pos]
# 	if dist < DIST_TO_BASE[pos]:
# 		DIST_TO_BASE[pos] = dist
# 		DIR_TO_BASE[pos] = West
# 		pro_max_bfs(pos, dist)
def bfs_east(x, y, dist):
	x += 1
	if dist < DIST_TO_BASE[x][y]:
		DIST_TO_BASE[x][y] = dist
		DIR_TO_BASE[x,y] = West
		pro_max_bfs(x, y, dist)


# def bfs_south(pos, dist):
# 	pos = TILE_SOUTH[pos]
# 	if dist < DIST_TO_BASE[pos]:
# 		DIST_TO_BASE[pos] = dist
# 		DIR_TO_BASE[pos] = North
# 		pro_max_bfs(pos, dist)
def bfs_south(x, y, dist):
	y -= 1
	if dist < DIST_TO_BASE[x][y]:
		DIST_TO_BASE[x][y] = dist
		DIR_TO_BASE[x,y] = North
		pro_max_bfs(x, y, dist)

# def bfs_west(pos, dist):
# 	pos = TILE_WEST[pos]
# 	if dist < DIST_TO_BASE[pos]:
# 		DIST_TO_BASE[pos] = dist
# 		DIR_TO_BASE[pos] = East
# 		pro_max_bfs(pos, dist)
def bfs_west(x, y, dist):
	x -= 1
	if dist < DIST_TO_BASE[x][y]:
		DIST_TO_BASE[x][y] = dist
		DIR_TO_BASE[x,y] = East
		pro_max_bfs(x, y, dist)

# def pro_max_bfs(pos, dist):
# 	for func in PATH[pos[0]][pos[1]]:
# 		func(pos, dist+1)

def pro_max_bfs(x, y, dist):
	for func in PATH[x][y]:
		func(x, y, dist+1)
		