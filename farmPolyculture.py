def farmPolyculture():
    planted = []
    while True:
        watersq(.7)
        plant(Entities.Grass)
        comp = get_companion()
        planted.append((get_pos_x(), get_pos_y()))
        goto(comp[1], comp[2])
        if get_entity_type() == None:
            plant(comp[0])
        else:
            for pos in planted:
                goto(pos[0], pos[1])
                while not can_harvest():
                    watersq(.70)
                    trade(Items.Fertilizer)
                    use_item(Items.Fertilizer)
                harvest()
            planted = []