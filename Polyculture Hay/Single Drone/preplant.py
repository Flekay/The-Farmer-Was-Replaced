# variables
MOVES = generate_moves()
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
	plant(Entities.Bush)
	move(dir)

# main loop
def hay():
	# preplant
	for direction in MOVES:
		if (get_pos_x(), get_pos_y()) not in BUSH_TILES:
			companion, pos = get_companion()
			while companion != Entities.Bush or pos not in BUSH_TILES:
				harvest()
				companion, pos = get_companion()
		move(direction)

	# spam fertilizer
	harvest()
	for i in range(3000):
		if Entities.Bush in get_companion():
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
		harvest()

	# harvest
	harvest_polyhay()

	# spam fertilizer
	harvest()
	for i in range(3000):
		if Entities.Bush in get_companion():
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
		harvest()


while True:
	hay()
