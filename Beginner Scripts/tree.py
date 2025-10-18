while True:
	for _ in range(get_world_size()):
		if can_harvest():
			harvest()
		if (get_pos_x() + get_pos_y()) % 2:
			plant(Entities.Tree)
		move(North)
	move(East)
