def power_runs():
	# pre plant
	for direction in MOVES:
		if get_ground_type() == Grounds.Turf:
			till()
		while measure() != 7:
			harvest()
			plant(Entities.Sunflower)
		use_item(Items.Water_Tank)
		use_item(Items.Water_Tank)
		move(direction)

	# pre water
	for direction in MOVES:
		while get_water() != 1:
			use_item(Items.Water_Tank)
		move(direction)

	# harvest and plant
	for _ in range(18):
		for direction in MOVES:
			harvest()
			plant(Entities.Sunflower)
			move(direction)

	# post harvest
	for direction in MOVES:
		harvest()
		move(direction)


clear()
MOVES = generate_moves()
while True:
	power_runs()
