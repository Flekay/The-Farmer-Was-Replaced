def stage0():
    while not can_harvest():
        pass
    for i in range(50):
        harvest()
    unlock(Unlocks.Speed)
    unlock(Unlocks.Expand)