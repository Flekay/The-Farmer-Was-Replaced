DIRECTION = [West,South,East,North]
TREASURE = Entities.Treasure
BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer
current_dir=0
clear()

for i in range(0,1,0):
	plant(BUSH)
	while get_entity_type() == BUSH:
		use_item(FERTILIZER)
	while not measure():
		if move(DIRECTION[current_dir]):
			current_dir=(current_dir-1)%4
		else:
			current_dir=(current_dir+1)%4
	harvest()
