# 2k bones | time: 6.7922
def farmBones(numBones=2000):
    bones = num_items(Items.Bones)
    egg = Items.Egg

    # Functions for black dino
    def swap_black():
        swap(North)
        return shuffle_black

    def shuffle_black():
        move(North)
        swap(North)
        swap(South)
        swap(East)
        move(South)
        return swap_black2
    
    def swap_black2():
        swap(North)
        return harvest_black

    def harvest_black():
        harvest()
        return swap_black

    # Functions for brown dino
    def swap_brown():
        swap(East)
        return shuffle_brown

    def shuffle_brown():
        move(East)
        swap(East)
        swap(West)
        swap(South)
        move(West)
        return swap_brown2
    
    def swap_brown2():  
        swap(East)
        return harvest_brown

    def harvest_brown():
        harvest()
        return swap_brown

    # Functions for white dino
    def swap_white():
        swap(South)
        return shuffle_white

    def shuffle_white():
        move(South)
        swap(South)
        swap(North)
        swap(West)
        move(North)
        return swap_white2
    
    def swap_white2():
        swap(South)
        return harvest_white

    def harvest_white():
        harvest()
        return swap_white

    # Functions for grey dino
    def swap_grey():
        swap(West)
        return shuffle_grey

    def shuffle_grey():
        move(West)
        swap(West)
        swap(East)
        swap(North)
        move(East)
        return swap_grey2
    
    def swap_grey2():
        swap(West)
        return harvest_grey

    def harvest_grey():
        harvest()
        return swap_grey

    operations = [swap_black, swap_brown, swap_white, swap_grey]

    # Setup 
    setupBones()

    # Main loop
    while num_items(Items.Bones) < numBones + bones:
        use_item(egg)
        color = measure()
        operations[color] = operations[color]()

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
