def farmBones(numBones=2000):

    dinos = [0, 0, 0, 0]

    bones = num_items(Items.Bones)
    egg = Items.Egg

    # Functions for black dino
    def swap_black():
        swap(North)
        dinos[0] += 1

    def shuffle_black():
        move(North)
        swap(North)
        swap(South)
        swap(East)
        move(South)
        dinos[0] += 1

    def harvest_black():
        harvest()
        dinos[0] = 0

    # Functions for brown dino
    def swap_brown():
        swap(East)
        dinos[1] += 1

    def shuffle_brown():
        move(East)
        swap(East)
        swap(West)
        swap(South)
        move(West)
        dinos[1] += 1

    def harvest_brown():
        harvest()
        dinos[1] = 0

    # Functions for white dino
    def swap_white():
        swap(South)
        dinos[2] += 1

    def shuffle_white():
        move(South)
        swap(South)
        swap(North)
        swap(West)
        move(North)
        dinos[2] += 1

    def harvest_white():
        harvest()
        dinos[2] = 0

    # Functions for grey dino
    def swap_grey():
        swap(West)
        dinos[3] += 1

    def shuffle_grey():
        move(West)
        swap(West)
        swap(East)
        swap(North)
        move(East)
        dinos[3] += 1

    def harvest_grey():
        harvest()
        dinos[3] = 0

    # Operations dictionary for each dino type
    operations = {
        0: {0: swap_black, 1: shuffle_black, 2: swap_black, 3: harvest_black},
        1: {0: swap_brown, 1: shuffle_brown, 2: swap_brown, 3: harvest_brown},
        2: {0: swap_white, 1: shuffle_white, 2: swap_white, 3: harvest_white},
        3: {0: swap_grey, 1: shuffle_grey, 2: swap_grey, 3: harvest_grey},
    }

    # Setup 
    setupBones()
    # setupBlackCocks()
    # setupMixedCocks()
    # harvestMixedCocks()
    # harvest()

    # Main loop
    # for inf in range(0, 1, 0):
    while num_items(Items.Bones) < numBones + bones:
        use_item(egg)
        dino_type = measure()
        operations[dino_type][dinos[dino_type]]()

def setupBones():
    clear()
    moveTo(2, 2)
    till()
    move(North)
    move(North)
    till()
    move(South)
    till()
    move(East)
    till()
    move(South)
    move(East)
    till()
    move(West)
    till()
    move(South)
    till()
    move(West)
    move(South)
    till()
    move(North)
    till()
    move(West)
    till()
    move(North)
    move(West)
    till()
    move(East)
    till()
    move(North)
    till()
    move(East)
    move(South)

def setupBlackCocks():
    clear()
    for tile in range(get_world_size()**2):
        till()
        for inf in range(0, 1, 0):
            use_item(Items.Egg)
            if measure() != 0:
                till()
                till()
            else:
                break

        moveToNextTile()
    moveTo(2, 2)

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
            (0, 6), (0, 7), (0, 8), (0, 9),
            (1, 6), (1, 7), (1, 8), (1, 9),
            (2, 6), (2, 7), (2, 8), (2, 9),
            (3, 6), (3, 7), (3, 8), (3, 9),
            (4, 6), (4, 7), (4, 8), (4, 9),
        ],
        2: [
            (6, 0), (6, 1), (6, 2), (6, 3), (6, 4),
            (7, 0), (7, 1), (7, 2), (7, 3), (7, 4),
            (8, 0), (8, 1), (8, 2), (8, 3), (8, 4),
            (9, 0), (9, 1), (9, 2), (9, 3), (9, 4),
        ],
        3: [
            (6, 6), (6, 7), (6, 8), (6, 9),
            (7, 6), (7, 7), (7, 8), (7, 9),
            (8, 6), (8, 7), (8, 8), (8, 9),
            (9, 6), (9, 7), (9, 8), (9, 9),
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

start = get_time()
farmBones()
quick_print(get_time() - start)
