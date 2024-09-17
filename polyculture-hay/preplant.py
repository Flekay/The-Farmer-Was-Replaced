# variables
MOVES = generate_moves()
FERTILIZER = Items.Fertilizer
BUSH = Entities.Bush
GRASS = Entities.Grass
BUSH_SET = {Entities.Bush}
BUSH_TILES = [
	(4, 1), (3, 2), (4, 2), (5, 2), (2, 3),
	(3, 3), (4, 3), (5, 3), (6, 3), (1, 4),
	(2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
	(2, 5), (3, 5), (4, 5), (5, 5), (6, 5),
	(3, 6), (4, 6), (5, 6), (4, 7), (9, 9),
]

# Reset
clear()
move_to(4,4)

# preplant bushes
for dir in MOVES:
	plant(BUSH)
	move(dir)

# main loop
while True:
	# preplant
	for direction in MOVES:
		if (get_pos_x(), get_pos_y()) not in BUSH_TILES:
			companion, x, y = get_companion()
			while companion != BUSH or (x, y) not in BUSH_TILES:
				harvest()
				companion, x, y = get_companion()
		move(direction)

	# spam fertilizer
	harvest()
	for i in range(3750):
		if get_companion()[0] in BUSH_SET:
			use_item(FERTILIZER)
		harvest()

	# harvest
	harvest_polyhay()

	# spam fertilizer
	harvest()
	for i in range(3750):
		if get_companion()[0] in BUSH_SET:
			use_item(FERTILIZER)
		harvest()
