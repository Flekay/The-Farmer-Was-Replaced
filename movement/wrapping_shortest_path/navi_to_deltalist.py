_moves = None
def update(ws=get_world_size()):
	global _moves
	if ws == 10:
		_moves = (
			(
				(),
				(North,),
				(North, North),
				(North, North, North),
				(North, North, North, North),
				(South, South, South, South, South),
				(South, South, South, South),
				(South, South, South),
				(South, South),
				(South,),
			),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, North, North, North),
				(East, North, North, North, North),
				(East, South, South, South, South, South),
				(East, South, South, South, South),
				(East, South, South, South),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, North, North, North),
				(East, East, North, North, North, North),
				(East, East, South, South, South, South, South),
				(East, East, South, South, South, South),
				(East, East, South, South, South),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(East, East, East),
				(East, East, East, North),
				(East, East, East, North, North),
				(East, East, East, North, North, North),
				(East, East, East, North, North, North, North),
				(East, East, East, South, South, South, South, South),
				(East, East, East, South, South, South, South),
				(East, East, East, South, South, South),
				(East, East, East, South, South),
				(East, East, East, South),
			),
			(
				(East, East, East, East),
				(East, East, East, East, North),
				(East, East, East, East, North, North),
				(East, East, East, East, North, North, North),
				(East, East, East, East, North, North, North, North),
				(East, East, East, East, South, South, South, South, South),
				(East, East, East, East, South, South, South, South),
				(East, East, East, East, South, South, South),
				(East, East, East, East, South, South),
				(East, East, East, East, South),
			),
			(
				(West, West, West, West, West),
				(West, West, West, West, West, North),
				(West, West, West, West, West, North, North),
				(West, West, West, West, West, North, North, North),
				(West, West, West, West, West, North, North, North, North, ),
				(West, West, West, West, West, South, South, South, South, South),
				(West, West, West, West, West, South, South, South, South),
				(West, West, West, West, West, South, South, South),
				(West, West, West, West, West, South, South),
				(West, West, West, West, West, South),
			),
			(
				(West, West, West, West),
				(West, West, West, West, North),
				(West, West, West, West, North, North),
				(West, West, West, West, North, North, North),
				(West, West, West, West, North, North, North, North),
				(West, West, West, West, South, South, South, South, South),
				(West, West, West, West, South, South, South, South),
				(West, West, West, West, South, South, South),
				(West, West, West, West, South, South),
				(West, West, West, West, South),
			),
			(
				(West, West, West),
				(West, West, West, North),
				(West, West, West, North, North),
				(West, West, West, North, North, North),
				(West, West, West, North, North, North, North),
				(West, West, West, South, South, South, South, South),
				(West, West, West, South, South, South, South),
				(West, West, West, South, South, South),
				(West, West, West, South, South),
				(West, West, West, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, North, North, North),
				(West, West, North, North, North, North),
				(West, West, South, South, South, South, South),
				(West, West, South, South, South, South),
				(West, West, South, South, South),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, North, North, North),
				(West, North, North, North, North),
				(West, South, South, South, South, South),
				(West, South, South, South, South),
				(West, South, South, South),
				(West, South, South),
				(West, South),
			),
		)
	elif ws == 3:
		_moves = (
			((), (North,), (South,)),
			((East,), (East, North), (East, South)),
			((West,), (West, North), (West, South)),
		)
	elif ws == 4:
		_moves = (
			((), (North,), (South, South), (South,)),
			((East,), (East, North), (East, South, South), (East, South)),
			(
				(West, West),
				(West, West, North),
				(West, West, South, South),
				(West, West, South),
			),
			((West,), (West, North), (West, South, South), (West, South)),
		)
	elif ws == 5:
		_moves = (
			((), (North,), (North, North), (South, South), (South,)),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, South, South),
				(West, South),
			),
		)
	elif ws == 6:
		_moves = (
			(
				(),
				(North,),
				(North, North),
				(South, South, South),
				(South, South),
				(South,),
			),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, South, South, South),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, South, South, South),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(West, West, West),
				(West, West, West, North),
				(West, West, West, North, North),
				(West, West, West, South, South, South),
				(West, West, West, South, South),
				(West, West, West, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, South, South, South),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, South, South, South),
				(West, South, South),
				(West, South),
			),
		)
	elif ws == 7:
		_moves = (
			(
				(),
				(North,),
				(North, North),
				(North, North, North),
				(South, South, South),
				(South, South),
				(South,),
			),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, North, North, North),
				(East, South, South, South),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, North, North, North),
				(East, East, South, South, South),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(East, East, East),
				(East, East, East, North),
				(East, East, East, North, North),
				(East, East, East, North, North, North),
				(East, East, East, South, South, South),
				(East, East, East, South, South),
				(East, East, East, South),
			),
			(
				(West, West, West),
				(West, West, West, North),
				(West, West, West, North, North),
				(West, West, West, North, North, North),
				(West, West, West, South, South, South),
				(West, West, West, South, South),
				(West, West, West, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, North, North, North),
				(West, West, South, South, South),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, North, North, North),
				(West, South, South, South),
				(West, South, South),
				(West, South),
			),
		)
	elif ws == 8:
		_moves = (
			(
				(),
				(North,),
				(North, North),
				(North, North, North),
				(South, South, South, South),
				(South, South, South),
				(South, South),
				(South,),
			),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, North, North, North),
				(East, South, South, South, South),
				(East, South, South, South),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, North, North, North),
				(East, East, South, South, South, South),
				(East, East, South, South, South),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(East, East, East),
				(East, East, East, North),
				(East, East, East, North, North),
				(East, East, East, North, North, North),
				(East, East, East, South, South, South, South),
				(East, East, East, South, South, South),
				(East, East, East, South, South),
				(East, East, East, South),
			),
			(
				(West, West, West, West),
				(West, West, West, West, North),
				(West, West, West, West, North, North),
				(West, West, West, West, North, North, North),
				(West, West, West, West, South, South, South, South),
				(West, West, West, West, South, South, South),
				(West, West, West, West, South, South),
				(West, West, West, West, South),
			),
			(
				(West, West, West),
				(West, West, West, North),
				(West, West, West, North, North),
				(West, West, West, North, North, North),
				(West, West, West, South, South, South, South),
				(West, West, West, South, South, South),
				(West, West, West, South, South),
				(West, West, West, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, North, North, North),
				(West, West, South, South, South, South),
				(West, West, South, South, South),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, North, North, North),
				(West, South, South, South, South),
				(West, South, South, South),
				(West, South, South),
				(West, South),
			),
		)
	elif ws == 9:
		_moves = (
			(
				(),
				(North,),
				(North, North),
				(North, North, North),
				(North, North, North, North),
				(South, South, South, South),
				(South, South, South),
				(South, South),
				(South,),
			),
			(
				(East,),
				(East, North),
				(East, North, North),
				(East, North, North, North),
				(East, North, North, North, North),
				(East, South, South, South, South),
				(East, South, South, South),
				(East, South, South),
				(East, South),
			),
			(
				(East, East),
				(East, East, North),
				(East, East, North, North),
				(East, East, North, North, North),
				(East, East, North, North, North, North),
				(East, East, South, South, South, South),
				(East, East, South, South, South),
				(East, East, South, South),
				(East, East, South),
			),
			(
				(East, East, East),
				(East, East, East, North),
				(East, East, East, North, North),
				(East, East, East, North, North, North),
				(East, East, East, North, North, North, North),
				(East, East, East, South, South, South, South),
				(East, East, East, South, South, South),
				(East, East, East, South, South),
				(East, East, East, South),
			),
			(
				(East, East, East, East),
				(East, East, East, East, North),
				(East, East, East, East, North, North),
				(East, East, East, East, North, North, North),
				(East, East, East, East, North, North, North, North),
				(East, East, East, East, South, South, South, South),
				(East, East, East, East, South, South, South),
				(East, East, East, East, South, South),
				(East, East, East, East, South),
			),
			(
				(West, West, West, West),
				(West, West, West, West, North),
				(West, West, West, West, North, North),
				(West, West, West, West, North, North, North),
				(West, West, West, West, North, North, North, North),
				(West, West, West, West, South, South, South, South),
				(West, West, West, West, South, South, South),
				(West, West, West, West, South, South),
				(West, West, West, West, South),
			),
			(
				(West, West, West),
				(West, West, West, North),
				(West, West, West, North, North),
				(West, West, West, North, North, North),
				(West, West, West, North, North, North, North),
				(West, West, West, South, South, South, South),
				(West, West, West, South, South, South),
				(West, West, West, South, South),
				(West, West, West, South),
			),
			(
				(West, West),
				(West, West, North),
				(West, West, North, North),
				(West, West, North, North, North),
				(West, West, North, North, North, North),
				(West, West, South, South, South, South),
				(West, West, South, South, South),
				(West, West, South, South),
				(West, West, South),
			),
			(
				(West,),
				(West, North),
				(West, North, North),
				(West, North, North, North),
				(West, North, North, North, North),
				(West, South, South, South, South),
				(West, South, South, South),
				(West, South, South),
				(West, South),
			),
		)

# Initialize on import
update()

def move_to(goal_x, goal_y, start_x=get_pos_x(), start_y=get_pos_y()):
	dx = goal_x - start_x
	dy = goal_y - start_y
	for fx in _moves[dx][dy]:
		move(fx)

def move_to_pos(goal_pos, start_pos):
	goal_x, goal_y = goal_pos
	start_x, start_y = start_pos
	move_to(goal_x, goal_y, start_x, start_y)
