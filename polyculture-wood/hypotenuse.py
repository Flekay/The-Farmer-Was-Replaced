while num_items(Items.Wood) < 100000:
	if get_water() < 0.75:
		use_item(Items.Water)
	if not can_harvest() and use_item(Items.Fertilizer):
		use_item(Items.Weird_Substance)

	if can_harvest():
		harvest()
		plant(Entities.Tree)
		comp, (x,y) = get_companion()
		while comp != Entities.Grass or x == y:
			harvest()
			plant(Entities.Tree)
			comp, (x,y) = get_companion()
	move(North)
	move(East)
