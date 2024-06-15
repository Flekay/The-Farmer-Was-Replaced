start = get_time()

timed_reset()
getUnlocks([
    Unlocks.Speed0, # 20 hay
    Unlocks.Expand0, # 30 hay
    Unlocks.Plant, # 50 hay
    Unlocks.Speed1, # 10 wood
    Unlocks.Expand1, # 20 wood
    Unlocks.Grass, # 100 hay
    Unlocks.Carrots # 100 wood
])

for i in range(10):
    getTanks(1)

getUnlocks([
    Unlocks.Expand2,
    Unlocks.Trees, # 50 wood, 200 carrots
    Unlocks.Speed2
])

for i in range(4):
    getTanks(10)

getUnlocks([
    Unlocks.Grass,
    Unlocks.Grass,
    Unlocks.Trees,
    Unlocks.Trees
])

getSeeds(Items.Carrot_Seed, 100)

getUnlocks([
    Unlocks.Carrots,
    Unlocks.Speed
])

for i in range(3):
    getTanks(10)
    
getUnlocks([
    Unlocks.Grass,
    Unlocks.Trees
])

getSeeds(Items.Carrot_Seed, 300)

getUnlocks([
    Unlocks.Carrots,
    Unlocks.Speed,
    Unlocks.Carrots,
    Unlocks.Speed,
    Unlocks.Speed,
    Unlocks.Pumpkins, # 500 wood, 1000 carrots
    Unlocks.Polyculture # 3000 hay, 3000 wood, 3000 carrots
])


getTanks(200)
getSeeds(Items.Pumpkin_Seed, 450)

getUnlocks([
    Unlocks.Pumpkins,
    Unlocks.Expand3
])

for i in range(7):
    getTanks(10)

getUnlocks([
    Unlocks.Speed,
    Unlocks.Speed
])

getSeeds(Items.Pumpkin_Seed, 350)

getUnlocks([
    Unlocks.Pumpkins,
    Unlocks.Expand4,
    Unlocks.Fertilizer, # 1000 pumpkins
    Unlocks.Sunflowers, # 500 carrots
])

getPower(500)
    
getUnlocks([
    Unlocks.Grass,
    Unlocks.Speed,
    Unlocks.Grass,
    Unlocks.Speed,
    Unlocks.Speed,
    Unlocks.Expand5,
    Unlocks.Expand6
])

getPower(1300)

getUnlocks([
    Unlocks.Mazes, # 2000 carrots, 3000 pumpkins
    Unlocks.Mazes
])

quick_print("Endgame split ", 
    get_time() - start)

getGold(15000 + 8320)
unlock(Unlocks.Cactus) # 5000 gold
trade(Items.Cactus_Seed, 832)
unlock(Unlocks.Cactus)
getCacti(13)
unlock(Unlocks.Dinosaurs) # 5000 cacti
trade(Items.Egg, 365)
unlock(Unlocks.Dinosaurs)
getBones(2000)
unlock(Unlocks.Leaderboard) # 2000 bones
timed_reset()