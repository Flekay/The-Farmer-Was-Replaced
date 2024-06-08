def buyTanks():
    while (num_items(Items.Empty_Tank) +
            num_items(Items.Water_Tank)) < (get_world_size() * get_world_size()) * 8:
        trade(Items.Empty_Tank)