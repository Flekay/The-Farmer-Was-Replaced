# 4.1579s
# 21656 op
def moveToNextTile():
    # move to a next tile in a zigzag pattern
    # this expects the world to be square so world_size >= 3 only
    # if get_world_size() == 2:
    #     move(North)
    #     return
    if get_pos_x() % 2 == 0:
        if get_pos_y() == get_world_size() - 1:
            move(East)
        else:
            move(North)
    else:
        if get_pos_y() == 0:
            move(East)
        else:
            move(South)
            
def bench():
    clear()
    start = get_time()
    for i in range(get_world_size()**2):
        moveToNextTile()
    quick_print(str(get_time()-start))

    clear()
    start = get_op_count()
    for i in range(get_world_size()**2):
        moveToNextTile()
    quick_print(get_op_count()-start-4)
bench()