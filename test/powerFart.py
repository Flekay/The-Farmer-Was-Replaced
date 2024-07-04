naviToNextTile = loadNaviToNextTile()
moves = generate_moves()

def powerFart():
    size = get_world_size()**2
    waterTank = Items.Water_Tank
    fertilizer = Items.Fertilizer
    sunflower = Entities.Sunflower

    def plant7s():
        for i in range(size):
            for i in range(0, 1, 0):
                if get_ground_type() != Grounds.Soil:
                    till()
                plant(sunflower)
                
                if measure() != 7:
                    till()
                else:
                    break
            move(naviToNextTile[get_pos_x()][get_pos_y()])

    def water():
        for i in range(size):
            use_item(waterTank)
            use_item(waterTank)
            use_item(waterTank)
            use_item(waterTank)
            move(naviToNextTile[get_pos_x()][get_pos_y()])
        for i in range(size):
            use_item(waterTank)
            move(naviToNextTile[get_pos_x()][get_pos_y()])


    plant7s()
    water()

    for i in range(1067):
        harvest()
        plant(sunflower)
        if measure() == 7:
            move(naviToNextTile[get_pos_x()][get_pos_y()])
        elif get_water():
            use_item(fertilizer)
        else:
            use_item(waterTank)
            use_item(waterTank)
            use_item(fertilizer)

    for dir in moves:
        harvest()
        move(dir)


for i in range(0, 1, 0):
    powerFart()