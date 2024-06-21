
def setupMixedCocks():
    clear()
    cocks = {
        0: [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
            (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
            (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
        ],
        1: [
            (0, 6), (0, 7), (0, 8), (0, 9), (0, 5),
            (1, 6), (1, 7), (1, 8), (1, 9), (1, 5),
            (2, 6), (2, 7), (2, 8), (2, 9), (2, 5),
            (3, 6), (3, 7), (3, 8), (3, 9), (3, 5),
            (4, 6), (4, 7), (4, 8), (4, 9), (4, 5),
        ],
        2: [
            (6, 0), (6, 1), (6, 2), (6, 3), (6, 4),
            (7, 0), (7, 1), (7, 2), (7, 3), (7, 4),
            (8, 0), (8, 1), (8, 2), (8, 3), (8, 4),
            (9, 0), (9, 1), (9, 2), (9, 3), (9, 4),
            (5, 0), (5, 1), (5, 2), (5, 3), (5, 4),
        ],
        3: [
            (6, 6), (6, 7), (6, 8), (6, 9), (6, 5),
            (7, 6), (7, 7), (7, 8), (7, 9), (7, 5),
            (8, 6), (8, 7), (8, 8), (8, 9), (8, 5),
            (9, 6), (9, 7), (9, 8), (9, 9), (9, 5),
            (5, 6), (5, 7), (5, 8), (5, 9), (5, 5),
        ],
    }
    for color in cocks:
        for pos in cocks[color]:
            moveToPos(pos)
            till()

            for inf in range(0, 1, 0):
                use_item(Items.Egg)
                if measure() != color:
                    till()
                    till()
                else:
                    break

    moveTo(9, 9)

def harvestMixedCocks():
    harvest()
    move(North)
    harvest()
    move(South)
    move(East)
    harvest()
    move(North)
    move(North)
    move(North)
    move(East)
    move(East)
    harvest()

def farmBones():
    egg = Items.Egg

    # Functions for black dino
    def swap_black():
        swap(North)
        operations[0] = shuffle_black

    def shuffle_black():
        move(North)
        swap(North)
        swap(South)
        swap(East)
        move(South)
        operations[0] = swap_black2
    
    def swap_black2():
        swap(North)
        operations[0] = harvest_black

    def harvest_black():
        harvest()
        operations[0] = swap_black

    # Functions for brown dino
    def swap_brown():
        swap(East)
        operations[1] = shuffle_brown

    def shuffle_brown():
        move(East)
        swap(East)
        swap(West)
        swap(South)
        move(West)
        operations[1] = swap_brown2
    
    def swap_brown2():  
        swap(East)
        operations[1] = harvest_brown

    def harvest_brown():
        harvest()
        operations[1] = swap_brown

    # Functions for white dino
    def swap_white():
        swap(South)
        operations[2] = shuffle_white

    def shuffle_white():
        move(South)
        swap(South)
        swap(North)
        swap(West)
        move(North)
        operations[2] = swap_white2
    
    def swap_white2():
        swap(South)
        operations[2] = harvest_white

    def harvest_white():
        harvest()
        operations[2] = swap_white

    # Functions for grey dino
    def swap_grey():
        swap(West)
        operations[3] = shuffle_grey

    def shuffle_grey():
        move(West)
        swap(West)
        swap(East)
        swap(North)
        move(East)
        operations[3] = swap_grey2
    
    def swap_grey2():
        swap(West)
        operations[3] = harvest_grey

    def harvest_grey():
        harvest()
        operations[3] = swap_grey

    operations = [swap_black, swap_brown, swap_white, swap_grey]

    # Setup 
    setupMixedCocks()
    harvestMixedCocks()

    # Main loop
    for i in range(0, 1, 0):
        use_item(egg)
        color = measure()
        operations[measure()]()

farmBones()