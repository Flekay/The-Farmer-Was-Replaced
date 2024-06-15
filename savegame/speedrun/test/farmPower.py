# test script to farm sunflowers with only level 15 petals
def farmPower(batches=999999):
    # move_x2,move_y2 = loadData()
    size = get_world_size()**2
    # powers = {
    #     15: [],
    #     14: [],
    #     13: [],
    #     12: [],
    #     11: [],
    #     10: [],
    #     9: [],
    #     8: [],
    #     7: [],
    #     6: []
    # }
    # clear()
    
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

    # testing setup
    if get_ground_type() != Grounds.Soil:
        for i in range(size):
            while get_water() < 0.76:
                use_item(Items.Water_Tank)
            till()
            moveToNextTile()
    naviTo(0,0)


    # subsequent batches
    while 1:
        for b in range(size):
            trade(Items.Sunflower_Seed, size)

            for i in range(size):
                while get_water() < 0.76:
                    use_item(Items.Water_Tank)
                plant(Entities.Sunflower)
                powers[measure()].append((get_pos_x(), get_pos_y()))
                moveToNextTile()


            # harvest sunflowers highest petals to lowest
            for i in range(15, 6, -1):
                # if i == 0:
                #     naviTo(powers[i-1][0])
                #     while not can_harvest():
                #         continue
                #     harvest()
                #     break
                for x in range(len(powers[i])):
                    next_x, next_y = powers[i][x]
                    naviTo(next_x, next_y)
                    while not can_harvest():
                        continue
                    harvest()
                powers[i] = []

start = get_time()
move_x2,move_y2 = loadData()
farmPower(1)
quick_print("Total Time taken:", get_time() - start, "seconds")