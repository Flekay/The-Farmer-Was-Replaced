def speed0():
    while not can_harvest():
        pass
    for i in range(20):
        harvest()
    unlock(Unlocks.Speed)