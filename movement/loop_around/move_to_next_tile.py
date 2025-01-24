def move_to_next_tile(x=get_pos_x(), y=get_pos_y()):
	if x != y:
		move(East)
	else:
		move(South)
