def Astar(iterations, world_size):
	from initializeAstar import initialize_Astar
	from regularmapper import mapper

	ws = world_size
	ws_square = ws ** 2

	substance_needed = world_size * num_unlocked(Unlocks.Mazes)

	clear()

	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance_needed)

	none_none = (None, None)

	wall_dict = {}
	for t_index in range(ws_square):
		wall_dict[t_index] = {North, South, East, West}

	neighboors = {}
	for a_ in range(ws_square):
		neighboors[a_] = (a_ + ws, a_ + 1, a_ - ws, a_ - 1)

	i_ = 0
	index_converter = {}
	for y in range(ws):
		for x in range(ws):
			index_converter[i_] = (x, y)
			i_ += 1

	invert = {}
	invert[North] = South
	invert[East] = West
	invert[South] = North
	invert[West] = East

	pos_add = {}
	pos_add[North] = ws
	pos_add[East] = 1
	pos_add[South] = -ws
	pos_add[West] = -1

	tgt = mapper(wall_dict, invert, pos_add, ws, ws_square)
	tgt_x, tgt_y = index_converter[tgt]

	drone_x, drone_y = get_pos_x(), get_pos_y()
	drone_coord = drone_x + (drone_y * ws)

	if drone_coord == tgt:
		tgt_x, tgt_y = measure()
		tgt = tgt_x + (tgt_y * ws)
		iterations -= 1
		use_item(Items.Weird_Substance, substance_needed)

	for maze_iteration in range(iterations):
		Astar_flow_field = {tgt:none_none}

		queue = []
		if not initialize_Astar(tgt, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
			for item in queue:
				func, c_ = item
				if func(c_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					break

		drone_coord, dir = Astar_flow_field[drone_coord]
		while dir:
			move(dir)

			walls = wall_dict[drone_coord]
			for wall_dir in walls:
				if move(wall_dir):
					walls = set(walls)
					walls.remove(wall_dir)
					wall_dict[drone_coord] = walls

					neighboor_coord = drone_coord + pos_add[wall_dir]
					neighboor_walls = wall_dict[neighboor_coord]
					invert_dir = invert[wall_dir]
					neighboor_walls.remove(invert_dir)

					if neighboor_coord in Astar_flow_field:
						drone_coord = neighboor_coord
						break
					else:
						move(invert_dir)

			drone_coord, dir = Astar_flow_field[drone_coord]

		if maze_iteration != iterations - 1:
			drone_coord = tgt
			drone_x, drone_y = tgt_x, tgt_y
			tgt_x, tgt_y = measure()
			tgt = tgt_x + (tgt_y * ws)
			use_item(Items.Weird_Substance, substance_needed)

	harvest()
