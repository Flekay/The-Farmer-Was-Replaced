def moveToNextTile():
    if get_world_size() == 2:
        move(North)
        return
    # move in a zigzag pattern
    if get_pos_x() % 2 == 0:
        if get_pos_y() == get_world_size() - 1:
            moveTo(get_pos_x() + 1, get_pos_y())
        else:
            moveTo(get_pos_x(), get_pos_y() + 1)
    else:
        if get_pos_y() == 0:
            moveTo(get_pos_x() + 1, get_pos_y())
        else:
            moveTo(get_pos_x(), get_pos_y() - 1)
