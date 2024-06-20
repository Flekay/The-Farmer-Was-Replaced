# 2k bones | time: 6.9825
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

    # Main loop
    while num_items(Items.Bones) < numBones + bones:
        use_item(egg)
        dino_type = measure()
        operations[dino_type][dinos[dino_type]]()

# outside functions because probably not needed in a speedrun
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

start = get_time()
farmBones()
quick_print("2k bones | time:", str(get_time() - start))
