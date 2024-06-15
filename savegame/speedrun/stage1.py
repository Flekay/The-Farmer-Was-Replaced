def stage1():
    i = 0
    while i < 50:
        if can_harvest():
            harvest()
            i += 1
    unlock(Unlocks.Plant)