def get_random_unlock():
    unlocks = []
    for unlockn in unlock_cost:
        if not len(unlock_cost[unlockn]):
            continue
        for resource in unlock_cost[unlockn][0]:
            if available_resources[resource]:
                unlocks.append(unlockn)
    if unlocks:
        unlockn = unlocks[randint(0, len(unlocks) - 1)]
        return unlockn, unlock_cost[unlockn].pop(0)
    return None
    