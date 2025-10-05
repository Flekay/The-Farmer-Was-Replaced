clear()
AMOUNT = get_world_size() * num_unlocked(Unlocks.Mazes)
while True:
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, AMOUNT)
	harvest()
