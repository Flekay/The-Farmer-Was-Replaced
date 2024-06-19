# ⌀ Items harvested per second: 995
# max Over the last 60s you farmed 60.8k Power
def powerFart():
    size = get_world_size()**2
    start = get_time()

    for i in range(size):
        while True:
            if num_items(Items.Sunflower_Seed) < size:
                trade(Items.Sunflower_Seed, size)
            if get_ground_type() != Grounds.Soil:
                till()
            # while get_water() < 0.76:
            #     use_item(Items.Water_Tank)
                
            plant(Entities.Sunflower)
            
            if measure() != 7:
                till()
            else:
                break
        moveToNextTile()

    while get_time() - start < 80:
        harvest()
        plant(Entities.Sunflower)
        use_item(Items.Fertilizer)
        use_item(Items.Fertilizer)
        use_item(Items.Fertilizer)

    while get_entity_type() == Entities.Sunflower:
        harvest()
        moveToNextTile()
powerFart()