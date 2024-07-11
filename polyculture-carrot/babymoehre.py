set_farm_size(3)
clear()
MOVES = generate_moves()
move_x2, move_y2 = loadData(get_world_size())
GRID_SIZE = get_world_size()**2
CARROT = Entities.Carrots
GRASS = Entities.Grass
TREE = Entities.Tree
WATER = Items.Water_Tank
FERTILIZER = Items.Fertilizer
companion = {}

for x in range(get_world_size()):
	for y in range(get_world_size()):
		companion[(x,y)] = GRASS

for dir in MOVES:
	till()
	plant(GRASS)
	move(dir)

navi_to(1, 1)
for i in range(0,1,0):
	plant(CARROT)
	a,b,c = get_companion()
	if companion[(b,c)] != a:
		companion[(b,c)] = a
		navi_to(b, c)
		harvest()
		plant(a)
		navi_to(1, 1)
	while not can_harvest():
		use_item(FERTILIZER)
	harvest()
