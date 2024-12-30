def gen_move_to(ws=get_world_size()):
	hws = ws // 2
	# Precompute delta lookup table
	delta_lookup = {}
	for delta in range(-ws + 1, ws):
		delta_lookup[delta] = (delta + hws) % ws - hws

	def _gen_move_to(goal_x, goal_y, current_x=get_pos_x(), current_y=get_pos_y()):
		dx = delta_lookup[goal_x - current_x]
		dy = delta_lookup[goal_y - current_y]

		for i in range(dx):
			move(East)
		for i in range(-dx):
			move(West)
		for i in range(dy):
			move(North)
		for i in range(-dy):
			move(South)

	return _gen_move_to
