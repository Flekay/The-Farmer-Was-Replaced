def whatToFarm():
    # return the item with the lowest stock
    hay = num_items(Items.Hay)
    wood = num_items(Items.Wood)
    carrot = num_items(Items.Carrot)
    pumpkin = num_items(Items.Pumpkin)
    gold = num_items(Items.Gold)

    if hay <= wood and hay <= carrot and hay <= pumpkin and hay <= gold:
        return Items.Hay
    elif wood <= carrot and wood <= pumpkin and wood <= gold:
        return Items.Wood
    elif carrot <= pumpkin and carrot <= gold:
        return Items.Carrot
    elif pumpkin <= gold:
        return Items.Pumpkin
    else:
        return Items.Gold