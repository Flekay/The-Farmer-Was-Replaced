# globals path
DX = {North: 0, South: 0, East: 1, West: -1}
DY = {North: 1, South: -1, East: 0, West: 0}

# Helper to compute the path to a base
def pro_max_path(x, y):
	path = []
	dir = DIR_TO_BASE[x, y]
	while dir:
		path.append(dir)
		x += DX[dir]
		y += DY[dir]
		dir = DIR_TO_BASE[x, y]
	return path
