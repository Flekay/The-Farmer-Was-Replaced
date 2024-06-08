def main():
    farmItem = Items.Hay
    farmAmount = 0
    farmStep = 100 * get_world_size() * get_world_size()
    while True:
        farmItem = whatToFarm()
        farmAmount = num_items(farmItem) + farmStep
        if farmItem == Items.Hay:
            farmHay(farmAmount)
        elif farmItem == Items.Wood:
            farmWood(farmAmount)
        elif farmItem == Items.Carrot:
            farmCarrot(farmAmount)
        elif farmItem == Items.Pumpkin:
            farmPumpkin(farmAmount)
        elif farmItem == Items.Gold:
            farmMaze(farmAmount)