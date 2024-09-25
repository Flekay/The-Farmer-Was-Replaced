MOVES = generate_moves()

clear()
for direction in MOVES:
	till()
	move(direction)



while True:
	for direction in MOVES:
		plant(Entities.Cactus)
		while measure() != 0:
			till()
			till()
			plant(Entities.Cactus)
		move(direction)
	harvest()
