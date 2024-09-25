DIRECTION = [West,South,East,North]
AMOUNT = get_world_size() * num_unlocked(Unlocks.Mazes)
dir=0
clear()

while True:
	plant(Entities.Bush)
	use_item(Items.Fertilizer)
	use_item(Items.Weird_Substance, AMOUNT)
	while not measure():
		dir = (dir + 2 * move(DIRECTION[dir]) - 1) % 4
	harvest()
