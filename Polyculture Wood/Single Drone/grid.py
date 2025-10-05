MOVES = (North,North,North,North,East)
EVENODD = (True, False, True, False, True, False, True, False, True, False)

def plant_tree():
	plant(Entities.Tree)
	companion, (x, y) = get_companion()
	while companion != Entities.Grass or EVENODD[x-y]:
		harvest()
		plant(Entities.Tree)
		companion, (x, y) = get_companion()

while num_items(Items.Wood) < 100000:
	for dir in MOVES:
		if not get_water():
			use_item(Items.Water)
		if not can_harvest() and use_item(Items.Fertilizer):
			use_item(Items.Weird_Substance)
		if can_harvest():
			harvest()
			plant_tree()
		move(dir)
		move(North)
