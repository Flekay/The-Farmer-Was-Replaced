def expand0():
    i = 0
    while i < 30:
        if can_harvest():
            harvest()
            i += 1
    unlock(Unlocks.Expand)