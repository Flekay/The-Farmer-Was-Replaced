# manhatten distance on a self wrapping 10x10 grid
def distance(point1, point2, ws=get_world_size()):
    dx = abs(point1[0] - point2[0])
    dy = abs(point1[1] - point2[1])
    return min(dx, ws - dx) + min(dy, ws - dy)
