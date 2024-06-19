def cactuser():
    reset_position()
    sweeper = get_sweeper_single()
    size = get_world_size()
    clockwise_dict = clockwise_factory()
    cactuscending = cactuscending_factory()
    while True:
        if num_items(Items.Cactus_Seed) <= size*size:
            trade(Items.Cactus_Seed, size*size)
        sweeper(plant, Entities.Cactus)
        bubble_cactus_dir(East, size, clockwise_dict, cactuscending)
        bubble_cactus_dir(North, size, clockwise_dict, cactuscending)
        bubble_cactus_dir(East, size, clockwise_dict, cactuscending)
        bubble_cactus_dir(North, size, clockwise_dict, cactuscending)
        harvest()

def bubble_cactus_swap_j(dir, nitems, size, clockwise_dict, cactuscending):
    iter_dir = clockwise_dict[dir]
    nearside_dir = clockwise_dict[iter_dir]
    ascending = cactuscending[dir]
    if nitems < 2:
        # just go home honestly
        return
    if not nitems % 2:
        # even -> odd
        for i in range(size):
            if (measure() > measure(dir)) == ascending:
                swap(dir)
            move(iter_dir)
        move(dir)
        bubble_cactus_swap_j(dir, nitems-1, size, clockwise_dict, cactuscending)
    else:
        # odd code
        for j in range(nitems//2):
            move(dir)
            # scan in iter_dir
            for k in range(size):
                if (measure(nearside_dir) > measure()) == ascending:
                    swap(nearside_dir)
                if (measure() > measure(dir)) == ascending:
                    swap(dir)
                move(iter_dir)
            move(dir)
            
            
def bubble_cactus_dir(dir, size, clockwise_dict, cactuscending):
    return_dir = clockwise_dict[clockwise_dict[dir]]
    for i in range(size, 0, -2):
        bubble_cactus_swap_j(dir, i, size, clockwise_dict, cactuscending)
        move(return_dir)
        bubble_cactus_swap_j(return_dir, i-1, size, clockwise_dict, cactuscending)



def cactuscending_factory():
    return {
        North: True,
        West: False,
        South: False,
        East: True,
    }

def clockwise_factory():
    return {
        North: East,
        West: North,
        South: West,
        East: South,
    }