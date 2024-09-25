MOVES = generate_moves()

clear()
for direction in MOVES:
	till()
	use_item(Items.Water_Tank)
	use_item(Items.Water_Tank)
	use_item(Items.Water_Tank)
	use_item(Items.Water_Tank)
	move(direction)

while True:
	for direction in MOVES:
		plant(Entities.Pumpkin)
		if get_water():
			move(direction)
		else:
			use_item(Items.Water_Tank)
			move(direction)
	for direction in MOVES:
		while not can_harvest():
			plant(Entities.Pumpkin)
			use_item(Items.Fertilizer)
		move(direction)
	harvest()
