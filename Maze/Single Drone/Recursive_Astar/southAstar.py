def south_Astar(coord_index, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
	from northAstar import north_Astar
	from eastAstar import east_Astar
	from westAstar import west_Astar
	
	if coord_index == drone_coord:
		n_, e_, s_, w_ = neighboors[coord_index]
		Astar_flow_field[coord_index] = (n_, North)
		return True
	
	curr_x, curr_y = index_converter[coord_index]
	walls = wall_dict[coord_index]
	
	n_, e_, s_, w_ = neighboors[coord_index]
	
	Astar_flow_field[coord_index] = (n_, North)
	
	if drone_x > curr_x:
		if drone_y < curr_y:
			if West not in walls and w_ not in Astar_flow_field:
				queue.append((west_Astar, w_))

			if East not in walls and e_ not in Astar_flow_field:
				if east_Astar(e_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
			
			if South not in walls and s_ not in Astar_flow_field:
				if south_Astar(s_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
				
		else:
			if West not in walls and w_ not in Astar_flow_field:
				queue.append((west_Astar, w_))

			if South not in walls and s_ not in Astar_flow_field:
				queue.append((south_Astar, s_))
				
			if East not in walls and e_ not in Astar_flow_field:
				if east_Astar(e_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
					
	elif drone_x < curr_x:
		if drone_y < curr_y:
			if East not in walls and e_ not in Astar_flow_field:
				queue.append((east_Astar, e_))

			if West not in walls and w_ not in Astar_flow_field:
				if west_Astar(w_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
			
			if South not in walls and s_ not in Astar_flow_field:
				if south_Astar(s_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
				
		else:
			if East not in walls and e_ not in Astar_flow_field:
				queue.append((east_Astar, e_))
	
			if South not in walls and s_ not in Astar_flow_field:
				queue.append((south_Astar, s_))
				
			if West not in walls and w_ not in Astar_flow_field:
				if west_Astar(w_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
					
	else:
		if drone_y < curr_y:
			if East not in walls and e_ not in Astar_flow_field:
				queue.append((east_Astar, e_))
			
			if West not in walls and w_ not in Astar_flow_field:
				queue.append((west_Astar, w_))

			if South not in walls and s_ not in Astar_flow_field:
				if south_Astar(s_, wall_dict, drone_coord, drone_x, drone_y, Astar_flow_field, queue, neighboors, index_converter):
					return True
				
		else:
			if East not in walls and e_ not in Astar_flow_field:
				queue.append((east_Astar, e_))
			
			if West not in walls and w_ not in Astar_flow_field:
				queue.append((west_Astar, w_))
	
			if South not in walls and s_ not in Astar_flow_field:
				queue.append((south_Astar, s_))