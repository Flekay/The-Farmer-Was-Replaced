def _move_to(goal_x, goal_y, current_x, current_y, ws):
	hws = ws // 2
	# Calculate the shortest x direction
	dx = (goal_x - current_x + hws) % ws - hws
	# Calculate the shortest y direction
	dy = (goal_y - current_y + hws) % ws - hws

	# Move in x direction
	for _ in range(dx):
		move(East)
	for _ in range(-dx):
		move(West)

	# Move in y direction
	for _ in range(dy):
		move(North)
	for _ in range(-dy):
		move(South)


def move_to_at(goal_x, goal_y, current_x, current_y, ws):
	_move_to(goal_x, goal_y, current_x, current_y, ws)


def move_to(goal_x, goal_y):
	_move_to(goal_x, goal_y, get_pos_x(), get_pos_y(), get_world_size())


def move_to_pos_at(goal_pos, current_pos, ws):
	_move_to(goal_pos[0], goal_pos[1], current_pos[0], current_pos[1], ws)


def move_to_pos(goal_pos, current_pos = None, ws = None):
	if ws == None:
		ws = get_world_size()
	if current_pos == None:
		current_pos = (get_pos_x(), get_pos_y())

	_move_to(goal_pos[0], goal_pos[1], current_pos[0], current_pos[1], ws)
