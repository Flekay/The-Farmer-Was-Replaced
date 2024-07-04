DIRECTION = [North, South, West, East]
TREASURE = Entities.Treasure
BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer
clear()

for i in range(0,1,0):
	till()
	plant(BUSH)
	while get_entity_type() == BUSH:
		use_item(FERTILIZER)
	while get_entity_type() != TREASURE:
		move(DIRECTION[random()*4])
	harvest()