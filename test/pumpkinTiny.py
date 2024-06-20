ws = get_world_size()**2

# wthout water
# @justHarvest() | op: 71869  | time: 4.2790  | pumpkins: 1460
# with water
# @justHarvest() | op: 72864  | time: 4.3376  | pumpkins: 1390

def pumpkinTiny():
    for i in range(ws):
        plant(Entities.Pumpkin)
        if get_water() <= 0.5:
            use_item(Items.Water_Tank)
        moveToNextTileEven()
    for i in range(ws):
        harvest()
        moveToNextTileEven()

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
pumpkinTiny()
nettoPumpkins = num_items(Items.Pumpkin) - pumpkins - fertilizerCost * (fertilizers - num_items(Items.Fertilizer))
nettoPumpkins = nettoPumpkins / (get_time() - startTime) * 60
quick_print("op:", get_op_count() - startOp - 8,
" | time:", str(get_time() - startTime),
" | netto:", nettoPumpkins)