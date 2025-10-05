clear()
MOVES = generate_moves()

while True:
	# pre plant
	for direction in MOVES:
		if get_ground_type() == Grounds.Grassland:
			till()
		while measure() != 7:
			harvest()
			plant(Entities.Sunflower)
		move(direction)

	# pre water
	for _ in range(10):
		move(North)
		use_item(Items.Water)
		use_item(Items.Water)
		use_item(Items.Water)
		use_item(Items.Water)

	# main loop
	time = get_time()
	while get_time() - time < 60:
		if get_water() <= 0.78:
			use_item(Items.Water)
		harvest()
		plant(Entities.Sunflower)
		while measure() != 7:
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
			harvest()
			plant(Entities.Sunflower)
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
			harvest()
			plant(Entities.Sunflower)
		move(North)

	# post harvest
	for direction in MOVES:
		harvest()
		move(direction)
