# 0.1623s
# 1676 op
def moveTo(x, y):
    # move to a specific tile, taking advantage of connected edges
    # this expects the world to be square so world_size >= 3 only
    # this is such a beautiful solution its a shame that naviTo(x,y) is 2% faster
    n = get_world_size()
    
    # Calculate the shortest x direction
    dx = (x - get_pos_x() + n // 2) % n - n // 2
    # Calculate the shortest y direction
    dy = (y - get_pos_y() + n // 2) % n - n // 2
    
    # Move in x direction
    if dx > 0:
        for i in range(dx):
            move(East)
    elif dx < 0:
        for i in range(-dx):
            move(West)
    
    # Move in y direction
    if dy > 0:
        for i in range(dy):
            move(North)
    elif dy < 0:
        for i in range(-dy):
            move(South)
            
def bench():
    clear()
    #set_execution_speed(1)
    start = get_time()
    moveTo(6,6)
    quick_print(str(get_time()-start))
    
    clear()
    start = get_op_count()
    moveTo(6,6)
    quick_print(get_op_count()-start-4)
bench()
