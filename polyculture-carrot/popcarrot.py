MOVES = generate_moves()
MOVES_ONE_MIN = generate_moves(2500)
PUMPKIN = Entities.Pumpkin
CARROT = Entities.Carrots
FERTILIZER = Items.Fertilizer
WATER = Items.Water_Tank
BUSH = Entities.Bush
BUSH_LOCATIONS = [(1,1),(3,6),(6,3),(9,6),(6,9)]

def poly_carrots():
	clear()
	companions = {(1,1):BUSH, (3,6):BUSH, (6,3):BUSH, (9,6):BUSH, (6,9):BUSH}
	def preplant():
		for dir in MOVES:
			till()
			if (get_pos_x(), get_pos_y()) in BUSH_LOCATIONS:
				plant(BUSH)
			else:
				plant(CARROT)
				companion, x, y = get_companion()
				while not (x, y) in BUSH_LOCATIONS:
					harvest()
					plant(CARROT)
					companion, x, y = get_companion()
			use_item(WATER)
			use_item(WATER)
			use_item(WATER)
			use_item(WATER)
			move(dir)

	def tillall():
		for dir in MOVES:
			till()
			move(dir)
	def prewater():
		for dir in MOVES:
			use_item(WATER)
			use_item(WATER)
			move(dir)

	preplant()
	# tillall()
	# prewater()
	prewater()

	# start = get_time()
	for dir in MOVES_ONE_MIN:
		coords = (get_pos_x(), get_pos_y())
		if coords in companions:
			if get_entity_type() == companions[coords]:
				move(dir)
			else:
				harvest()
				plant(companions.pop(coords))
				move(dir)
		else:

			harvest()
			plant(CARROT)
			companion, x, y = get_companion()
			# while (x,y) in companions:
			# 	harvest()
			# 	plant(CARROT)
			# 	companion, x, y = get_companion()

			companions[(x,y)] = companion
			move(dir)
	# quick_print("Time taken: " + str(get_time() - start))

	for dir in MOVES:
		if get_entity_type() == CARROT:
			harvest()
		move(dir)

for i in range(0,1,0):
	poly_carrots()
