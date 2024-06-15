# test script to farm sunflowers with only level 15 petals

# Total Time taken: ~50 seconds | 44 - 52s
# Items harvested: ~5870 | 5863 - 5875
# Items harvested per second: ~120 | 114 - 133
def powerTill():
    size = get_world_size()**2

    # testing setup
    if get_ground_type() != Grounds.Soil:
        for i in range(size):
            while get_water() < 0.76:
                use_item(Items.Water_Tank)
            till()
            moveToNextTile()
    naviTo(0,0)
    for i in range(size):
        while measure() != 15:
            till()
            while num_items(Items.Sunflower_Seed) < 1:
                trade(Items.Sunflower_Seed, 1)
            plant(Entities.Sunflower)
        moveToNextTile()

    # subsequent batches
    while 1:
        # items = num_items(Items.Power)
        # starts = get_time()
        for b in range(size):
            harvest()
            while measure() != 15:
                till()
                while num_items(Items.Sunflower_Seed) < 1:
                    trade(Items.Sunflower_Seed, 1)
                plant(Entities.Sunflower)
            moveToNextTile()
        
        # quick_print("Total Time taken:", get_time() - starts, "seconds")
        # quick_print("Items harvested:", num_items(Items.Power) - items)
        # quick_print("Items harvested per second:", (num_items(Items.Power) - items) / (get_time() - starts) )



cPower = num_items(Items.Power)
batches = 5
move_x2,move_y2 = loadData()
start = get_time()
powerTill(batches)
# quick_print("Total Time taken:", get_time() - start, "seconds")
quick_print("⌀ time per batch:", (get_time() - start) / batches)
# quick_print("Total Items harvested:", num_items(Items.Power) - cPower)
# quick_print("⌀ items per batch:", (num_items(Items.Power) - cPower) / batches)
quick_print("⌀ Items harvested per second:", (num_items(Items.Power) - cPower) / (get_time() - start) )