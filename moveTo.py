# bench()
# op: 35019  | time: 2.0837
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



# Setup for your function
ws = get_world_size()

def bench():
    clear()
    # True Random Number Generator
    # https://www.random.org/
    spots = [
        (5,0),(2,0),(3,5),(8,9),(6,6),(6,6),
        (3,0),(4,7),(9,7),(5,3),(7,9),(9,4),
        (6,7),(4,4),(2,6),(1,5),(6,8),(2,0),
        (0,1),(4,2),(8,7),(4,7),(8,2),(6,4),
        (2,7),(5,8),(0,2),(8,0),(0,8),(6,6)
    ]
    startOp = get_op_count()
    startTime = get_time()
    for pos in spots:

        # Call your moveTo function here
        moveToPos(pos)

        if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
            quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
            break
    quick_print("@username | op:", get_op_count() - startOp - 8, " | time:", str(get_time() - startTime))
bench()