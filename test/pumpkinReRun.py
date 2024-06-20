ws = get_world_size()**2

# wthout water
# op: 80368  | time: 4.7876  | netto: 9680
# preWaterd
# op: 73180  | time: 4.3573  | netto: 9810

def reRun():
    for i in range(ws):
        plant(Entities.Pumpkin)
        if get_water() <= 0.0:
            use_item(Items.Water_Tank)
        moveToNextTileEven()
    for i in range(ws):
        for b in range(0, 1, 0):
            plant(Entities.Pumpkin)
            if not can_harvest():
                use_item(Items.Fertilizer)
            else:
                break
        moveToNextTileEven()
    harvest()

def setupPumpkin():
    clear()
    for i in range(ws):
        till()
        moveToNextTileEven()

def preWater():
    for i in range(ws):
        while get_water() <= 0.75:
            use_item(Items.Water_Tank)
        moveToNextTileEven()

setupPumpkin()
# preWater() # toggle water

pumpkins = num_items(Items.Pumpkin)
fertilizers = num_items(Items.Fertilizer)
# fertilizerCost = get_cost(Items.Fertilizer) # 10 pumpkins
fertilizerCost = 10 # 10 pumpkins
startOp = get_op_count()
startTime = get_time()
reRun()
nettoPumpkins = num_items(Items.Pumpkin) - pumpkins - fertilizerCost * (fertilizers - num_items(Items.Fertilizer))
nettoPumpkins = nettoPumpkins / (get_time() - startTime) * 60
quick_print("op:", get_op_count() - startOp - 8,
" | time:", str(get_time() - startTime),
" | netto:", nettoPumpkins)