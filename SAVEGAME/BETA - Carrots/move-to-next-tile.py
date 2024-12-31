def move_to_next_tile():
	if get_pos_x() != get_pos_y():
		move(East)
	else:
		move(South)