while True:
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Bush)
		move(North)
	move(East)
