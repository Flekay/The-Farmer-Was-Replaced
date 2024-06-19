# 1.2845s
# 21656 op
def moveToNextTileEven():
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

def moveToNextTileOdd():
    if get_pos_x() % 2 == 0:
        if get_pos_y() == get_world_size() - 1:
            if get_pos_x() == get_world_size() - 1:
                move(North)
            move(East)
        else:
            move(North)
    else:
        if get_pos_y() == 0:
            move(East)
        else:
            move(South)

def moveToNextTile():
    if get_world_size() == 2:
        move(North)
        return
    if get_pos_x() % 2 == 0:
        if get_pos_y() == get_world_size() - 1:
            if get_pos_x() == get_world_size() - 1:
                move(North)
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
        # moveToNextTileOdd()
        # moveToNextTileEven()
        moveToNextTile()
    quick_print(str(get_time()-start))

    clear()
    start = get_op_count()
    for i in range(get_world_size()**2):
        moveToNextTile()
        # moveToNextTileEven()
    quick_print(get_op_count()-start-4)
bench()