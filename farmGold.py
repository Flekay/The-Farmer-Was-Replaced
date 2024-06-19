def farmGold():
    start = get_time()
    n = get_world_size() 
    
    plant(Entities.Bush)
    nextChestPos = (0, 0)

    moveTable = (
        (East, North, South, West),
        (West, South, North, East),
        (South, East, West, North),
        (North, West, East, South)
    )
    
    opposite = {
        North: South,
        East:  West,
        South: North,
        West:  East
    }

    for x in range(300):
        while get_entity_type() in [Entities.Treasure, Entities.Bush]:
            use_item(Items.Fertilizer)
        
        x, y = get_pos_x(), get_pos_y()
        stack = []
        visited = set([(x, y)])
        
        while get_entity_type() != Entities.Treasure:
            moves = moveTable[getMovesOpt(x, y, nextChestPos)]
            moved = False
            for dir in moves:
                nextCoord = mazeCoordAdd(x, y, dir)
                if nextCoord in visited:
                    continue
                if move(dir):
                    visited.add(nextCoord)
                    x, y = nextCoord
                    stack.append(dir)
                    moved = True
                    break
            
            if moved:
                continue
            
            move(opposite[stack.pop()])
            x, y = get_pos_x(), get_pos_y()
        
        nextChestPos = measure()
        
    harvest()
    quick_print(get_time() - start)


def mazeCoordAdd(x, y, dir):
    if dir == North:
        return (x, y + 1)
    if dir == East:
        return (x + 1, y)
    if dir == South:
        return (x, y - 1)
    return (x - 1, y)


def getMovesOpt(x, y, chestPos):
    tx, ty = chestPos
    if x < tx and y <= ty:
        return 0
    if x > tx and y >= ty:
        return 1
    if y > ty:
        return 2
    return 3


farmGold()