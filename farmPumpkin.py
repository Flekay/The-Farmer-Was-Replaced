def farmPumpkin(farmAmount):
    clear()
    pumpkins = []
    world_size = get_world_size()
    while num_items(Items.Pumpkin) < farmAmount:
        for i in range(0, (world_size * world_size)):
            pumpkins.append(i)
        while len(pumpkins) > 0:
            for pumpkin in pumpkins:
                posY = pumpkin % world_size
                posX = (pumpkin / world_size) + 0.01
                i = 0
                for i in range(0, posX):
                    pass
                moveTo(i, posY)
                if can_harvest() and get_entity_type() == Entities.Pumpkin:
                    pumpkins.remove(pumpkin)
                if num_items(Items.Pumpkin_Seed) < 1:
                    trade(Items.Pumpkin_Seed)
                if get_ground_type() == Grounds.Turf:
                    till()
                plant(Entities.Pumpkin)
                tryWatering()
        harvest()