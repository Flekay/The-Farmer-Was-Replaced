MOVES = generate_moves()
PUMPKIN = Entities.Pumpkin
FERTILIZER = Items.Fertilizer
WATER = Items.Water_Tank

clear()
for direction in MOVES:
	till()
	move(direction)

for i in range(0, 1, 0):
	for direction in MOVES:
		harvest()
		plant(PUMPKIN)
		if get_water() < 0.25:
			use_item(WATER)
		move(direction)