_delta_lookup = None
def update():
	global _delta_lookup
	ws = get_world_size()
	hws = ws // 2
	# Precompute delta lookup table
	_delta_lookup = {}
	for delta in range(-ws + 1, ws):
		_delta_lookup[delta] = (delta + hws) % ws - hws

# Initialize on import
update()

def move_to(goal_x, goal_y, current_x=get_pos_x(), current_y=get_pos_y()):
	dx = _delta_lookup[goal_x - current_x]
	dy = _delta_lookup[goal_y - current_y]

	for _ in range(dx):
		move(East)
	for _ in range(-dx):
		move(West)
	for _ in range(dy):
		move(North)
	for _ in range(-dy):
		move(South)

def move_to_pos(goal_pos, current_pos):
	goal_x, goal_y = goal_pos
	start_x, start_y = current_pos
	dx = _delta_lookup[goal_x - start_x]
	dy = _delta_lookup[goal_y - start_y]
	for _ in range(dx):
		move(East)
	for _ in range(-dx):
		move(West)
	for _ in range(dy):
		move(North)
	for _ in range(-dy):
		move(South)
