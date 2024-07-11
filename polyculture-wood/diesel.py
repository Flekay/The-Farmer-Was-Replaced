MOVES = generate_moves()
GRID_SIZE = get_world_size()**2
CARROT = Entities.Cactus
BUSH = Entities.Bush
GRASS = Entities.Grass
TREE = Entities.Tree
FERTILIZER = Items.Fertilizer
WATER = Items.Water_Tank
TREE_GRID = {}
current_companion = {}
used_by_companion = {}
companion_by_index = {}
INDEX_MAP = {}

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
	i+=1
	till()
	move(direction)

for min in range(11):
	for i in range(GRID_SIZE):
		if TREE_GRID[i]:
			used_by_companion[companion_by_index[i]] -= 1
			harvest()
			for inf in range(1337):
				plant(TREE)
				a,b,c = get_companion()
				x = INDEX_MAP[(b,c)]
				if TREE_GRID[x]:
					harvest()
					continue
				if a == current_companion[x]:
					used_by_companion[x] += 1
					companion_by_index[i] = x
					break
				elif used_by_companion[x] == 0:
					current_companion[x] = a
					used_by_companion[x] = 1
					companion_by_index[i] = x
					break
				else:
					harvest()
			if get_water() < 0.7:
				use_item(WATER)
		elif get_entity_type() != current_companion[i]:
			harvest()
			plant(current_companion[i])
		move(MOVES[i])

for i in range(GRID_SIZE):
	if TREE_GRID[i]:
		harvest()
	move(MOVES[i])
