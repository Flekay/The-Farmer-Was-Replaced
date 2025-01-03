# manhatten distance on a self wrapping 10x10 grid
def distance(point1, point2, ws=get_world_size()):
	p1x, p1y = point1
	p2x, p2y = point2
	dx = abs(p1x - p2x)
	dy = abs(p1y - p2y)
	return min(dx, ws - dx) + min(dy, ws - dy)
