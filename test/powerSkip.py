# ⌀ time per batch: 7.77
# ⌀ Items harvested per second: 465.45
def powerSkip(batches=999999):
    # move_x2,move_y2 = loadData()
    size = get_world_size()**2
    powers = {
        15: [],
        14: [],
        13: [],
        12: [],
        11: [],
        10: [],
        9: [],
        8: [],
        7: [],
        # 6: []
    }
    
    clear()
    
    # first batch
    # trade(Items.Sunflower_Seed, size)
    # for i in range(size):
    #     till()
    #     while get_water() < 0.76:
    #         use_item(Items.Water_Tank)
    #     plant(Entities.Sunflower)
    #     powers[measure()].append((get_pos_x(), get_pos_y()))
    #     moveToNextTile()
    # for i in range(15, 6, -1):
    #     for x in range(len(powers[i])):
    #         next_x, next_y = powers[i][x]
    #         naviTo(next_x, next_y)
    #         while not can_harvest():
    #             continue
    #         harvest()
    #     powers[i] = []

    # subsequent batches
    for b in range(batches):
        for i in range(size):
            # pedal = 0
            # while pedal < 10:
            if num_items(Items.Sunflower_Seed) < size:
                trade(Items.Sunflower_Seed, size)
            if get_ground_type() != Grounds.Soil:
                till()
            # while get_ground_type() != Grounds.Soil:
            # if get_entity_type() != Entities.Sunflower:
            # while get_entity_type() != Entities.Sunflower:
            plant(Entities.Sunflower)
            
            # if get_entity_type() == Entities.Sunflower:
                # pedal = measure()

            powers[measure()].append((get_pos_x(), get_pos_y()))
            if get_water() < 0.76:
                use_item(Items.Water_Tank)
            moveToNextTile()


        # harvest sunflowers highest petals to lowest
        for i in range(15, 6, -1):
            if i == 8:
                next_x, next_y = powers[i-1][0]
                naviTo(next_x, next_y)
                while not can_harvest():
                    continue
                harvest()
                break
            for x in range(len(powers[i])):
                next_x, next_y = powers[i][x]
                naviTo(next_x, next_y)
                while not can_harvest():
                    continue
                harvest()
            powers[i] = []
        powers[i] = []
        powers[i-1] = []

# set_farm_size(6) # 240p/s
# set_farm_size(8) # 334p/s
# set_farm_size(10) # 415p/s
cPower = num_items(Items.Power)
batches = 50
move_x2,move_y2 = loadData()
start = get_time()
powerSkip(batches)
# quick_print("Total Time taken:", get_time() - start, "seconds")
quick_print("⌀ time per batch:", (get_time() - start) / batches)
# quick_print("Total Items harvested:", num_items(Items.Power) - cPower)
# quick_print("⌀ items per batch:", (num_items(Items.Power) - cPower) / batches)
quick_print("⌀ Items harvested per second:", (num_items(Items.Power) - cPower) / (get_time() - start) )
