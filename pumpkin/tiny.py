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
		harvest()
		plant(Entities.Pumpkin)
		if get_water() < 0.25:
			use_item(Items.Water_Tank)
		move(direction)
