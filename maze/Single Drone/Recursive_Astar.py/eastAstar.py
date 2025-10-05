def east_Astar(coord_index, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
	from northAstar import north_Astar
	from westAstar import west_Astar
	from southAstar import south_Astar
	
	if coord_index == drone_coord:
		n_, e_, s_, w_ = neighboors[coord_index]
		Astar_flow_field[coord_index] = (w_, West)
		return True
	
	curr_x, curr_y = index_converter[coord_index]
	walls = wall_dict[coord_index]
	
	n_, e_, s_, w_ = neighboors[coord_index]
	
	Astar_flow_field[coord_index] = (w_, West)
	
	if drone_x > curr_x:
		if drone_y > curr_y:
			if South not in walls and s_ not in Astar_flow_field:
				queue.append((south_Astar, s_))
				
			if East not in walls and e_ not in Astar_flow_field:
				if east_Astar(e_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
			
			if North not in walls and n_ not in Astar_flow_field:
				if north_Astar(n_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
					
		elif drone_y < curr_y:
			if North not in walls and n_ not in Astar_flow_field:
				queue.append((north_Astar, n_))
				
			if East not in walls and e_ not in Astar_flow_field:
				if east_Astar(e_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
			
			if South not in walls and s_ not in Astar_flow_field:
				if south_Astar(s_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
				
		else:
			if North not in walls and n_ not in Astar_flow_field:
				queue.append((north_Astar, n_))
				
			if South not in walls and s_ not in Astar_flow_field:
				queue.append((south_Astar, s_))
				
			if East not in walls and e_ not in Astar_flow_field:
				if east_Astar(e_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
					
	else:
		if drone_y > curr_y:
			if East not in walls and e_ not in Astar_flow_field:
				queue.append((east_Astar, e_))
				
			if South not in walls and s_ not in Astar_flow_field:
				queue.append((south_Astar, s_))
			
			if North not in walls and n_ not in Astar_flow_field:
				if north_Astar(n_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
					
		elif drone_y < curr_y:
			if East not in walls and e_ not in Astar_flow_field:
				queue.append((east_Astar, e_))

			if North not in walls and n_ not in Astar_flow_field:
				queue.append((north_Astar, n_))
			
			if South not in walls and s_ not in Astar_flow_field:
				if south_Astar(s_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
				
		else:
			if East not in walls and e_ not in Astar_flow_field:
				queue.append((east_Astar, e_))

			if North not in walls and n_ not in Astar_flow_field:
				queue.append((north_Astar, n_))
				
			if South not in walls and s_ not in Astar_flow_field:
				queue.append((south_Astar, s_))