while True:
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
		if (get_pos_x() + get_pos_y()) % 2:
			plant(Entities.Tree)
		else:
			if get_ground_type() == Grounds.Grassland:
				till()
			if not plant(Entities.Carrot):
				plant(Entities.Grass)
		move(North)
	move(East)
