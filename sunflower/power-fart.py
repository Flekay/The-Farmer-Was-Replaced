MOVES = generate_moves()
MOVES_ONE_MIN = generate_moves(1250)

def powerFart():
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
	for direction in MOVES_ONE_MIN:
		harvest()
		plant(Entities.Sunflower)
		if measure() == 7:
			move(direction)
		if get_water() < 0.5:
			use_item(Items.Water_Tank)
		use_item(Items.Fertilizer)
		use_item(Items.Weird_Substance)

	# post harvest
	for direction in MOVES:
		harvest()
		move(direction)


clear()
while True:
	powerFart()
