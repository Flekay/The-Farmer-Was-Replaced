DIRECTION = [West,South,East,North]
AMOUNT = get_world_size() * num_unlocked(Unlocks.Mazes)
dir=0
clear()

while True:
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, AMOUNT)
	while get_entity_type() != Entities.Treasure:
		dir = (dir + 2 * move(DIRECTION[dir]) - 1) % 4
	harvest()
