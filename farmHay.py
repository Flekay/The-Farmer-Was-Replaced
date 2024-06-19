def farmHay(farmAmount):
    clear()
    while num_items(Items.Hay) < farmAmount:
        if can_harvest():
            harvest()
        moveToNextTile()