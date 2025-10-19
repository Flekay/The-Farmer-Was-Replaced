DIRECTION = [North, South, West, East]
AMOUNT = get_world_size() * num_unlocked(Unlocks.Mazes)
clear()

while True:
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, AMOUNT)
	while get_entity_type() != Entities.Treasure:
		move(DIRECTION[random()*4])
	harvest()
