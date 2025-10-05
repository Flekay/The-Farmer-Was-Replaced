# variables
MOVES = generate_moves()
GRASS_TILES = [
	(4, 1), (3, 2), (4, 2), (5, 2), (2, 3),
	(3, 3), (4, 3), (5, 3), (6, 3), (1, 4),
	(2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
	(2, 5), (3, 5), (4, 5), (5, 5), (6, 5),
	(3, 6), (4, 6), (5, 6), (4, 7), (9, 9),
]

# Reset
clear()
move_to(4,4)

# main loop
while True:
	range3 = range(3)
	range888 = range(888)
	# preplant
	for direction in MOVES:
		if (get_pos_x(), get_pos_y()) not in GRASS_TILES:
			till()
			plant(Entities.Tree)
			companion, pos = get_companion()
			while companion != Entities.Grass or pos not in GRASS_TILES:
				harvest()
				plant(Entities.Tree)
				companion, pos = get_companion()
			while not can_harvest():
				use_item(Items.Fertilizer)
		move(direction)


	# water to save fertilizer
	use_item(Items.Water)
	use_item(Items.Water)
	use_item(Items.Water)

	# spam trees
	harvest()
	for _ in range3:
		use_item(Items.Water)
		for _ in range888: # get_water <= 0.78
			plant(Entities.Tree)
			if Entities.Grass in get_companion():
				use_item(Items.Fertilizer)
			harvest()

	# harvest
	# function can be found in the poly-hay folder `harvest_polyhay.py`
	harvest_polyhay()

	# spam trees
	for _ in range3:
		use_item(Items.Water)
		for _ in range888: # get_water <= 0.78
			plant(Entities.Tree)
			if Entities.Grass in get_companion():
				use_item(Items.Fertilizer)
			harvest()
