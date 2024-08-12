MOVES = generate_moves()
CACTUS = Entities.Cactus

clear()
for direction in MOVES:
	till()
	move(direction)



for i in range(0, 1, 0):
	for direction in MOVES:
		plant(CACTUS)
		while measure() != 0:
			till()
			till()
			plant(CACTUS)
		move(direction)
	harvest()
