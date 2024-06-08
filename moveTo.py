def moveTo(x, y):
    # move to a specific tile
    if x >= get_world_size():
        x = 0
    if y >= get_world_size():
        y = 0
        
    while get_pos_x() < x:
        move(East)
    while get_pos_x() > x:
        move(West)
    while get_pos_y() < y:
        move(North)
    while get_pos_y() > y:
        move(South)