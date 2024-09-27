clear()
move_to(4, 4)
till()

def pine():
	# water to save fertilizer
	use_item(Items.Water_Tank)
	use_item(Items.Water_Tank)
	use_item(Items.Water_Tank)
	use_item(Items.Water_Tank)

	# spam trees
	for _ in range(1050): # ~30 seconds
		plant(Entities.Tree)
		if Entities.Grass in get_companion():
			while not can_harvest():
				use_item(Items.Fertilizer)
		harvest()

	# refill water
	use_item(Items.Water_Tank)

	# spam trees
	for _ in range(1050): # ~30 seconds
		plant(Entities.Tree)
		if Entities.Grass in get_companion():
			while not can_harvest():
				use_item(Items.Fertilizer)
		harvest()


while True:
	pine()
