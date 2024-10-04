
MOVES = generate_moves()

def power_till():
	for direction in MOVES:
		harvest()
		plant(Entities.Sunflower)
		while measure() != 15:
			till()
			plant(Entities.Sunflower)
		move(direction)

while True:
	power_till()
