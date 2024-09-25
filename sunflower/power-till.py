
MOVES = generate_moves()

while True:
	for direction in MOVES:
		harvest()
		plant(Entities.Sunflower)
		while measure() != 15:
			till()
			plant(Entities.Sunflower)
		move(direction)
