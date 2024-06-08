def tryWatering():
    if num_items(Items.Water_Tank) < 1:
        return
    if get_water() < 0.75:
        use_item(Items.Water_Tank)