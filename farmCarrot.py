def farmCarrot(farmAmount):
	clear()
	while num_items(Items.Carrot) < farmAmount:
		if can_harvest():
			harvest()
		if num_items(Items.Carrot_Seed) < 1:
			trade(Items.Carrot_Seed)
		if get_ground_type() == Grounds.Turf:
			till()
		plant(Entities.Carrots)
		# tryWatering()
		moveToNextTile()