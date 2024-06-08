def farmPumpkin(farmAmount):
    # only harvest if all pumpkins are ready
    clear()
    grownPumpkins = 0
    while num_items(Items.Pumpkin) < farmAmount:
        if get_pos_x() == 0 and get_pos_y() == 0:
            grownPumpkins = 0
        if can_harvest():
            grownPumpkins += 1
            if grownPumpkins == get_world_size() * get_world_size():
                harvest()
                grownPumpkins = 0
        if num_items(Items.Pumpkin_Seed) < 1:
            trade(Items.Pumpkin_Seed)
        if get_ground_type() == Grounds.Turf:
            till()
        plant(Entities.Pumpkin)
        tryWatering()
        moveToNextTile()