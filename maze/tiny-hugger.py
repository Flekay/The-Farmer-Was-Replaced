DIRECTION = [West,South,East,North]
TREASURE = Entities.Treasure
BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer
dir=0
clear()

for i in range(0,1,0):
	plant(BUSH)
	while get_entity_type() == BUSH:
		use_item(FERTILIZER)
	while not measure():
		dir = (dir + 2 * move(DIRECTION[dir]) - 1) % 4
	harvest()
