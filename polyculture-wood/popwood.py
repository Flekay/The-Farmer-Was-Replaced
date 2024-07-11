MOVES = generate_moves()
MOVES_ONE_MIN = generate_moves(2500)
GRID_SIZE = get_world_size()**2
CARROT = Entities.Carrots
BUSH = Entities.Bush
GRASS = Entities.Grass
TREE = Entities.Tree
FERTILIZER = Items.Fertilizer
WATER = Items.Water_Tank
TREE_GRID = {}
TREE_GRID_POS = {}
current_companion = {}
used_by_companion = {}
companion_by_index = {}
INDEX_MAP = {}
BUSH_LOCATIONS = [(1,1),(3,6),(6,3),(9,6),(6,9)]

def dieselloc():
	for i in range(GRID_SIZE):
		companion_by_index[i] = 0
		if not i % 2:
			current_companion[i] = TREE
			used_by_companion[i] = 99
			TREE_GRID[i] = True
		else:
			current_companion[i] = GRASS
			used_by_companion[i] = 0
			TREE_GRID[i] = False

	clear()
	i = 0
	for direction in MOVES:
		INDEX_MAP[(get_pos_x(), get_pos_y())] = i
		if (get_pos_x() + get_pos_y()) % 2:
			TREE_GRID_POS[(get_pos_x(), get_pos_y())] = True
		else:
			TREE_GRID_POS[(get_pos_x(), get_pos_y())] = False
		i+=1
		# till()
		# use_item(WATER)
		move(direction)

	def preplant():
		for dir in MOVES:
			till()
			if (get_pos_x(), get_pos_y()) in BUSH_LOCATIONS:
				plant(BUSH)
			else:
				plant(TREE)
				companion, x, y = get_companion()
				while not (x, y) in BUSH_LOCATIONS:
					harvest()
					plant(TREE)
					companion, x, y = get_companion()
			use_item(WATER)
			use_item(WATER)
			use_item(WATER)
			use_item(WATER)
			move(dir)

	preplant()
	def pregrow():
		for dir in MOVES:
			while not can_harvest():
				use_item(FERTILIZER)
			use_item(WATER)
			use_item(WATER)
			use_item(WATER)
			use_item(WATER)
			move(dir)
	pregrow()

	def prewater():
		for dir in MOVES:
			use_item(WATER)
			move(dir)
	prewater()



	companions = {(1,1):BUSH, (3,6):BUSH, (6,3):BUSH, (9,6):BUSH, (6,9):BUSH}
	start = get_time()
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
			if TREE_GRID_POS[coords]:
				move(dir)
			else:
				plant(TREE)
				companion, x, y = get_companion()
				# while (x,y) in companions:
				# 	harvest()
				# 	plant(CARROT)
				# 	companion, x, y = get_companion()

				companions[(x,y)] = companion
				move(dir)

	quick_print("Time taken: " + str(get_time() - start))

for i in range(0,1,0):
	dieselloc()
