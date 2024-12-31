def get_hay(amount, ws=get_world_size()):
	quick_print("farming:",amount,"hay")
	if ws == 1:
		clear()
		while num_items(Items.Hay) < amount:
			if can_harvest():
				harvest()
	elif ws == 3:
		clear()
		while num_items(Items.Hay) < amount:
			if can_harvest():
				harvest()
			move(North)
	else:
		MOVES = generate_moves()
		clear()
		for dir in MOVES:
			if can_harvest():
				harvest()
				if num_items(Items.Hay) >= amount:
					break
			move(dir)
	quick_print("completed eith", num_items(Items.Hay),"hay")