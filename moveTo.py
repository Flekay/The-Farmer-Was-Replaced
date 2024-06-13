def moveTo(x, y):
    # move to a specific tile, taking advantage of connected edges
    # this expects the world to be square so world_size >= 3 only
    n = get_world_size()
    dx = x - get_pos_x()
    if dx > n / 2:
        dx -= n
    elif dx < -(n / 2):
        dx += n
    if dx > 0:
        for m in range(dx):
            move(East)
    elif dx < 0:
        for m in range(-dx):
            move(West)
    dy = y - get_pos_y()
    if dy > n / 2:
        dy -= n
    elif dy < -(n / 2):
        dy += n
    if dy > 0:
        for m in range(dy):
            move(North)
    elif dy < 0:
        for m in range(-dy):
            move(South)
