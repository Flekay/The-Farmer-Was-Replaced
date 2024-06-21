def moveToNextTile():
    if get_pos_x() == get_pos_y():
        move(West)
    else:
        move(North)

def moveToNextTileMirror():
    if get_pos_x() == get_pos_y():
        move(South)
    else:
        move(East)

        
# set_farm_size(3)
# set_execution_speed(7)

def bench():
    clear()
    startOp = get_op_count()
    startTime = get_time()
    for i in range(get_world_size()**2):
        till()

        # inline is faster than function call
        if get_pos_x() == get_pos_y():
            move(West)
        else:
            move(North)

    quick_print("@username | op:", get_op_count() - startOp - 8,
                " | time:", str(get_time() - startTime - 0.0008))
bench()