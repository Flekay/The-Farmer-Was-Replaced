ws = get_world_size()**2
# move_x2, move_y2 = loadData()

def farmPumpkin():
    def setupPumpkin():
        clear()
        for i in range(ws):
            till()
            moveToNextTile()
    def prePlant():
        for i in range(ws):
            for b in range(0, 1, 0):
                plant(Entities.Pumpkin)
                if not can_harvest():
                    use_item(Items.Fertilizer)
                else:
                    break
            moveToNextTile()
    def preWater():
        for i in range(ws):
            use_item(Items.Water_Tank)
            use_item(Items.Water_Tank)
            use_item(Items.Water_Tank)
            use_item(Items.Water_Tank)
            moveToNextTile()
            
    setupPumpkin()
    prePlant()
    preWater()
    harvest()

    for b in range(0, 15, 1):
        for i in range(ws):
            plant(Entities.Pumpkin)
            if get_water() == 0:
                use_item(Items.Water_Tank)
            moveToNextTile()
        for i in range(ws):
            for b in range(0, 1, 0):
                plant(Entities.Pumpkin)
                if not can_harvest():
                    use_item(Items.Fertilizer)
                else:
                    break
            moveToNextTile()
        harvest()



pumpkins = num_items(Items.Pumpkin)
fertilizers = num_items(Items.Fertilizer)
# fertilizerCost = get_cost(Items.Fertilizer) # 10 pumpkins
fertilizerCost = 10 # 10 pumpkins
startOp = get_op_count()
startTime = get_time()
farmPumpkin()
nettoPumpkins = num_items(Items.Pumpkin) - pumpkins - fertilizerCost * (fertilizers - num_items(Items.Fertilizer))
nettoPumpkins = nettoPumpkins / (get_time() - startTime) * 60
bruttoPumpkins = (num_items(Items.Pumpkin) - pumpkins) / (get_time() - startTime) * 60
quick_print("op:", get_op_count() - startOp - 8,
" | time:", str(get_time() - startTime),
" | netto:", nettoPumpkins, "brutto:", bruttoPumpkins)