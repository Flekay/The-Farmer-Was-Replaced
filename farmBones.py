# 60s stats 16.3k - 16.5k
def farmBone(count=2000):
    setupBones()
    opposite = {
        North: South,
        East:  West,
        South: North,
        West:  East
    }
    items = 0
    dinos = [0, 0, 0, 0]
    dirs = (North, East, South, West, North)
    egg = Items.Egg
    
    while items < count:
        if num_items(egg) < 1:
            trade(egg)
        use_item(egg)
        colour = measure()
        numDinos = dinos[colour]
        dinos[colour] += 1
        if numDinos == 0:
            swap(dirs[colour])
        elif numDinos == 1:
            dir = dirs[colour]
            move(dir)
            swap(dir)
            move(opposite[dir])
            swap(dir)
        elif numDinos == 2:
            dir = dirs[colour]
            move(dir)
            swap(dirs[colour+1])
            move(opposite[dir])
            swap(dir)
        else:
            harvest()
            dinos[colour] = 0
            items += 48


def setupBones():
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
farmBone()
quick_print(get_time() - start)
