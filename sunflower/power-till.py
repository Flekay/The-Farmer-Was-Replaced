
MOVES = generate_moves()
SUNFLOWER = Entities.Sunflower

for i in range(0,1,0):
	for direction in MOVES:
		harvest()
		plant(SUNFLOWER)
		while measure() != 15:
			till()
			plant(SUNFLOWER)
		move(direction)
