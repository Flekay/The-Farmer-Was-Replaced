while True:
	for _ in range(get_world_size()):
		if get_ground_type() == Grounds.Grassland:
			till()
		if can_harvest():
			harvest()
		plant(Entities.Carrot)
		move(North)
	move(East)
