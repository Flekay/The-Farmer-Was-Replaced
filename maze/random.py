DIRECTION = [North, South, West, East]
AMOUNT = get_world_size() * num_unlocked(Unlocks.Mazes)
clear()

while True:
	plant(Entities.Bush)
	use_item(Items.Fertilizer)
	use_item(Items.Weird_Substance, AMOUNT)
	while not measure():
		move(DIRECTION[random()*4])
	harvest()
