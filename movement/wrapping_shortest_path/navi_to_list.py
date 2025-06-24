_move_x = None
_move_y = None

def update(size=get_world_size()):
	global _move_x
	global _move_y
	if size == 10:
		_move_x = (
			(),
			[East],
			(East, East),
			(East, East, East),
			(East, East, East, East),
			(West, West, West, West, West),
			(West, West, West, West),
			(West, West, West),
			(West, West),
			[West],
		)
		_move_y = (
			(),
			[North],
			(North, North),
			(North, North, North),
			(North, North, North, North),
			(South, South, South, South, South),
			(South, South, South, South),
			(South, South, South),
			(South, South),
			[South],
		)
	elif size == 3:
		_move_x = (
			(),
			[East],
			[West],
		)
		_move_y = (
			(),
			[North],
			[South],
		)
	elif size == 4:
		_move_x = (
			(),
			[East],
			(West, West),
			[West],
		)
		_move_y = (
			(),
			[North],
			(South, South),
			[South],
		)
	elif size == 5:
		_move_x = (
			(),
			[East],
			(East, East),
			(West, West),
			[West],
		)
		_move_y = (
			(),
			[North],
			(North, North),
			(South, South),
			[South],
		)
	elif size == 6:
		_move_x = (
			(),
			[East],
			(East, East),
			(West, West, West),
			(West, West),
			[West],
		)
		_move_y = (
			(),
			[North],
			(North, North),
			(South, South, South),
			(South, South),
			[South],
		)
	elif size == 7:
		_move_x = (
			(),
			[East],
			(East, East),
			(East, East, East),
			(West, West, West),
			(West, West),
			[West],
		)
		_move_y = (
			(),
			[North],
			(North, North),
			(North, North, North),
			(South, South, South),
			(South, South),
			[South],
		)
	elif size == 8:
		_move_x = (
			(),
			[East],
			(East, East),
			(East, East, East),
			(West, West, West, West),
			(West, West, West),
			(West, West),
			[West],
		)
		_move_y = (
			(),
			[North],
			(North, North),
			(North, North, North),
			(South, South, South, South),
			(South, South, South),
			(South, South),
			[South],
		)
	elif size == 9:
		_move_x = (
			(),
			[East],
			(East, East),
			(East, East, East),
			(East, East, East, East),
			(West, West, West, West),
			(West, West, West),
			(West, West),
			[West],
		)
		_move_y = (
			(),
			[North],
			(North, North),
			(North, North, North),
			(North, North, North, North),
			(South, South, South, South),
			(South, South, South),
			(South, South),
			[South],
		)

# Initialize on import
update()

def move_to(goal_x, goal_y, start_x = get_pos_x(), start_y = get_pos_y()):
	for fx in _move_x[goal_x-start_x]:
		move(fx)
	for fy in _move_y[goal_y-start_y]:
		move(fy)


def move_to_pos(goal_pos, start_pos):
	goal_x, goal_y = goal_pos
	start_x, start_y = start_pos
	move_to(goal_x, goal_y, start_x, start_y)
