MOVES = generate_moves()
MOVES_ONE_MIN = generate_moves(200)

def power_fart():
	# preplant
	for direction in MOVES:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)
		while measure() != 7:
			plant(Entities.Sunflower)
			if measure() != 7:
				till()
			else:
				break
		move(direction)

	# prewater
	for direction in MOVES:
		while get_water() != 1:
			use_item(Items.Water_Tank)
		move(direction)
	for direction in MOVES:
		use_item(Items.Water_Tank)
		move(direction)

	# spam
	i = 1
	time = get_time()
	for direction in MOVES_ONE_MIN:
		while True:
			harvest()
			plant(Entities.Sunflower)
			if measure() == 7 and i % 2:
				break
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
			i += 1
		if get_time() - time > 60:
			break
		move(direction)

	# post harvest
	for direction in MOVES:
		harvest()
		move(direction)


clear()
while True:
	power_fart()
