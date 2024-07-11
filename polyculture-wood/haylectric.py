MOVES = generate_moves()
GRID_SIZE = get_world_size()**2
GRASS = Entities.Grass
TREE = Entities.Tree
WATER = Items.Water_Tank
TREE_GRID = {}
INDEX_MAP = {}

def haylectric():
	for i in range(GRID_SIZE):
		if not i % 2:
			TREE_GRID[i] = True
		else:
			TREE_GRID[i] = False

	clear()
	i = 0
	for direction in MOVES:
		INDEX_MAP[(get_pos_x(), get_pos_y())] = i
		i+=1
		till()
		plant(GRASS)
		move(direction)

	for min in range(11):
		for i in range(GRID_SIZE):
			if TREE_GRID[i]:
				harvest()
				for inf in range(1337):
					plant(TREE)
					a,b,c = get_companion()
					if a != GRASS:
						harvest()
						continue
					x = INDEX_MAP[(b,c)]
					if TREE_GRID[x]:
						harvest()
						continue
					break
				if get_water() < 0.7:
					use_item(WATER)
			move(MOVES[i])

	for i in range(GRID_SIZE):
		if TREE_GRID[i]:
			harvest()
		move(MOVES[i])

for i in range(0,1,0):
	haylectric()
