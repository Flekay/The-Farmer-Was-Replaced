MOVES = generate_moves()
MOVES_ONE_MIN = generate_moves(2500)
CARROT = Entities.Carrot
BUSH = Entities.Bush
GRASS = Entities.Grass
TREE = Entities.Tree
FERTILIZER = Items.Fertilizer
WATER = Items.Water
companions = {}

def pregrow():
	for dir in MOVES:
		till()
		use_item(WATER)
		use_item(WATER)
		use_item(WATER)
		use_item(WATER)
		move(dir)


def popit():
	for dir in MOVES_ONE_MIN:
		harvest()
		coords = (get_pos_x(), get_pos_y())
		if coords in companions:
			plant(companions.pop(coords))
		else:
			plant(GRASS)
		companion, pos = get_companion()
		companions[pos] = companion
		move(dir)



while True:
	clear()
	pregrow()
	start = get_time()
	popit()
	quick_print("Time taken: " + str(get_time() - start))
