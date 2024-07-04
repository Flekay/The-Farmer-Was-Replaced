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
		plant(PUMPKIN)
		if get_water():
			move(direction)
		else:
			use_item(WATER)
			move(direction)
	for direction in MOVES:
		while not can_harvest():
			plant(PUMPKIN)
			use_item(FERTILIZER)
		move(direction)
	harvest()