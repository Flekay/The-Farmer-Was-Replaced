def plant_till():
	for x in rr9:
		for y in rr10:
			till()
			if get_pos_x() == 0:
				move(East)
			plant(Entities.Sunflower)
			m=measure()
			if m > 13:
				use_item(Items.Water)
			petals_list[15-m].add((get_pos_x(), get_pos_y()))
			move(North)
		move(East)
