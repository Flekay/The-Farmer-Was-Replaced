def plant0():
    while not can_harvest():
        pass
    for i in range(49):
        harvest()
        move(North)
    harvest()
    unlock(Unlocks.Plant)
    plant(Entities.Bush)