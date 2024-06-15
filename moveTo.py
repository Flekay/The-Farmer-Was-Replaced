# 0.1036s
# 1661 op
def moveTo(x, y, ws = get_world_size()):
    # move to a specific tile, taking advantage of connected edges
    # this expects the world to be square so world_size >= 3 only
    # this is such a beautiful solution its a shame that naviTo(x,y) is 2% faster
    hws = ws // 2
    
    # Calculate the shortest x direction
    dx = (x - get_pos_x() + hws) % ws - hws
    # Calculate the shortest y direction
    dy = (y - get_pos_y() + hws) % ws - hws
    
    # Move in x direction
    for i in range(dx):
        move(East)
    for i in range(-dx):
        move(West)
    
    # Move in y direction
    for i in range(dy):
        move(North)
    for i in range(-dy):
        move(South)
        
def moveToPos(pos, ws = get_world_size()):
    hws = ws // 2
    
    dx = (pos[0] - get_pos_x() + hws) % ws - hws
    dy = (pos[1] - get_pos_y() + hws) % ws - hws
    
    for i in range(dx):
        move(East)
    for i in range(-dx):
        move(West)
    for i in range(dy):
        move(North)
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
