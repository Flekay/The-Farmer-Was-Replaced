MOVES = generate_moves()
MOVES_ONE_MIN = generate_moves(2500)
PUMPKIN = Entities.Pumpkin
CARROT = Entities.Carrot
FERTILIZER = Items.Fertilizer
WATER = Items.Water
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
				companion, pos = get_companion()
				while not pos in BUSH_LOCATIONS:
					harvest()
					plant(CARROT)
					companion, pos = get_companion()
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
			companion, pos = get_companion()
			# while pos in companions:
			# 	harvest()
			# 	plant(CARROT)
			# 	companion, pos = get_companion()

			companions[pos] = companion
			move(dir)
	# quick_print("Time taken: " + str(get_time() - start))

	for dir in MOVES:
		if get_entity_type() == CARROT:
			harvest()
		move(dir)

while True:
	poly_carrots()
