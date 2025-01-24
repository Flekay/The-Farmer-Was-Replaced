def loadDataList(size=get_world_size()):
	if size == 10:
		move_x = (
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
		move_y = (
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
		move_x = (
			(),
			[East],
			[West],
		)
		move_y = (
			(),
			[North],
			[South],
		)
	elif size == 4:
		move_x = (
			(),
			[East],
			(West, West),
			[West],
		)
		move_y = (
			(),
			[North],
			(South, South),
			[South],
		)
	elif size == 5:
		move_x = (
			(),
			[East],
			(East, East),
			(West, West),
			[West],
		)
		move_y = (
			(),
			[North],
			(North, North),
			(South, South),
			[South],
		)
	elif size == 6:
		move_x = (
			(),
			[East],
			(East, East),
			(West, West, West),
			(West, West),
			[West],
		)
		move_y = (
			(),
			[North],
			(North, North),
			(South, South, South),
			(South, South),
			[South],
		)
	elif size == 7:
		move_x = (
			(),
			[East],
			(East, East),
			(East, East, East),
			(West, West, West),
			(West, West),
			[West],
		)
		move_y = (
			(),
			[North],
			(North, North),
			(North, North, North),
			(South, South, South),
			(South, South),
			[South],
		)
	elif size == 8:
		move_x = (
			(),
			[East],
			(East, East),
			(East, East, East),
			(West, West, West, West),
			(West, West, West),
			(West, West),
			[West],
		)
		move_y = (
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
		move_x = (
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
		move_y = (
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
	return move_x, move_y

move_x, move_y = loadDataList(get_world_size())

def navi_to_list(goal_x, goal_y, start_x = get_pos_x(), start_y = get_pos_y()):
	for fx in move_x[goal_x-start_x]:
		move(fx)
	for fy in move_y[goal_y-start_y]:
		move(fy)


def navi_to_list_pos(goal_pos, start_pos):
	goal_x, goal_y = goal_pos
	start_x, start_y = start_pos
	navi_to_list(goal_x, goal_y, start_x, start_y)
