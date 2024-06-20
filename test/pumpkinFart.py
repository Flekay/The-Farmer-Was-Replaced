ws = get_world_size()**2

# wthout water
# op: 84636  | time: 5.0431  | netto: 8200
# with water
# op: 80105  | time: 4.7621  | netto: 8520

def fart():
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
fart()
nettoPumpkins = num_items(Items.Pumpkin) - pumpkins - fertilizerCost * (fertilizers - num_items(Items.Fertilizer))
nettoPumpkins = nettoPumpkins / (get_time() - startTime) * 60
quick_print("op:", get_op_count() - startOp - 8,
" | time:", str(get_time() - startTime),
" | netto:", nettoPumpkins)