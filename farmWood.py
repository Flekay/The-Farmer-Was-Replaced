def farmWood(farmAmount):
    # plant trees in a chessboard pattern
    clear()
    while num_items(Items.Wood) < farmAmount:
        if can_harvest():
            harvest()
        if ((get_pos_x() + get_pos_y()) % 2 == 0) and num_unlocked(Unlocks.Trees) > 0:
            plant(Entities.Tree)
        else:
            plant(Entities.Bush)
        tryWatering()
        moveToNextTile()