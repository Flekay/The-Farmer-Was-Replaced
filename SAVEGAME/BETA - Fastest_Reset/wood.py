def get_wood(amount, ws=get_world_size()):
	if ws == 1:
		clear()
		plant(Entities.Bush)
		while num_items(Items.Wood) < amount:
			if can_harvest():
				harvest()
				plant(Entities.Bush)
	else:
		if ws == 3:
			MOVES = [North,North,North]
		else:
			MOVES = generate_moves()
		clear()
		contin = True


		for dir in MOVES:
			plant(Entities.Bush)
			move(dir)

		while contin:
			while not can_harvest():
				pass
			for dir in MOVES:
				harvest()
				if num_items(Items.Wood) >= amount:
					contin = False
					break
				plant(Entities.Bush)
				move(dir)
				