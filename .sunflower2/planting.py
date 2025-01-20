def planting():
	P = min(max(0.1, num_items(Items.Power)/7800),1)
	pos_x = 0
	for movex in moves:
		thresholdx = threshold_dict[pos_x]
		for dir in movex:
			plant(Entities.Sunflower)
			m = measure()
			if m > 10:
				threshold = thresholdx[m] * P
				while get_water() < threshold and num_items(Items.Water):
					use_item(Items.Water)
			petals_list[15-m].add((pos_x, get_pos_y()))
			move(dir)
		pos_x += 1

	for movex in moves2:
		thresholdx = threshold_dict[pos_x]
		for dir in movex:
			m = replanting()
			if m > 10:
				threshold = thresholdx[m] * P
				while get_water() < threshold and num_items(Items.Water):
					use_item(Items.Water)
			petals_list[15-m].add((pos_x, get_pos_y()))
			move(dir)
		pos_x += 1


def replanting():
	plant(Entities.Sunflower)
	m = measure()
	if m == 15:
		if get_water() < 0.75:
			use_item(Items.Water)
		use_item(Items.Fertilizer)
		if can_harvest():
			harvest()
			m = replanting()
	return m
