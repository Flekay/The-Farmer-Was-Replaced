def dir_forbidden():
	return {(0,0):[North,East],(0,1):[North,East,South],(0,2):[North,East,South],(0,3):[North,East,South],(0,4):[North,East,South],(0,5):[North,East,South],(0,6):[North,East,South],(0,7):[North,East,South],(0,8):[North,East,South],(0,9):[East,South],(1,0):[West,North,East],(1,1):[West,North,East,South],(1,2):[West,North,East,South],(1,3):[West,North,East,South],(1,4):[West,North,East,South],(1,5):[West,North,East,South],(1,6):[West,North,East,South],(1,7):[West,North,East,South],(1,8):[West,North,East,South],(1,9):[West,East,South],(2,0):[West,North,East],(2,1):[West,North,East,South],(2,2):[West,North,East,South],(2,3):[West,North,East,South],(2,4):[West,North,East,South],(2,5):[West,North,East,South],(2,6):[West,North,East,South],(2,7):[West,North,East,South],(2,8):[West,North,East,South],(2,9):[West,East,South],(3,0):[West,North,East],(3,1):[West,North,East,South],(3,2):[West,North,East,South],(3,3):[West,North,East,South],(3,4):[West,North,East,South],(3,5):[West,North,East,South],(3,6):[West,North,East,South],(3,7):[West,North,East,South],(3,8):[West,North,East,South],(3,9):[West,East,South],(4,0):[West,North,East],(4,1):[West,North,East,South],(4,2):[West,North,East,South],(4,3):[West,North,East,South],(4,4):[West,North,East,South],(4,5):[West,North,East,South],(4,6):[West,North,East,South],(4,7):[West,North,East,South],(4,8):[West,North,East,South],(4,9):[West,East,South],(5,0):[West,North,East],(5,1):[West,North,East,South],(5,2):[West,North,East,South],(5,3):[West,North,East,South],(5,4):[West,North,East,South],(5,5):[West,North,East,South],(5,6):[West,North,East,South],(5,7):[West,North,East,South],(5,8):[West,North,East,South],(5,9):[West,East,South],(6,0):[West,North,East],(6,1):[West,North,East,South],(6,2):[West,North,East,South],(6,3):[West,North,East,South],(6,4):[West,North,East,South],(6,5):[West,North,East,South],(6,6):[West,North,East,South],(6,7):[West,North,East,South],(6,8):[West,North,East,South],(6,9):[West,East,South],(7,0):[West,North,East],(7,1):[West,North,East,South],(7,2):[West,North,East,South],(7,3):[West,North,East,South],(7,4):[West,North,East,South],(7,5):[West,North,East,South],(7,6):[West,North,East,South],(7,7):[West,North,East,South],(7,8):[West,North,East,South],(7,9):[West,East,South],(8,0):[West,North,East],(8,1):[West,North,East,South],(8,2):[West,North,East,South],(8,3):[West,North,East,South],(8,4):[West,North,East,South],(8,5):[West,North,East,South],(8,6):[West,North,East,South],(8,7):[West,North,East,South],(8,8):[West,North,East,South],(8,9):[West,East,South],(9,0):[West,North],(9,1):[West,North,South],(9,2):[West,North,South],(9,3):[West,North,South],(9,4):[West,North,South],(9,5):[West,North,South],(9,6):[West,North,South],(9,7):[West,North,South],(9,8):[West,North,South],(9,9):[West,South]}
def dir_allowed():
	return {(0,0):[],(0,1):[],(0,2):[],(0,3):[],(0,4):[],(0,5):[],(0,6):[],(0,7):[],(0,8):[],(0,9):[],(1,0):[],(1,1):[],(1,2):[],(1,3):[],(1,4):[],(1,5):[],(1,6):[],(1,7):[],(1,8):[],(1,9):[],(2,0):[],(2,1):[],(2,2):[],(2,3):[],(2,4):[],(2,5):[],(2,6):[],(2,7):[],(2,8):[],(2,9):[],(3,0):[],(3,1):[],(3,2):[],(3,3):[],(3,4):[],(3,5):[],(3,6):[],(3,7):[],(3,8):[],(3,9):[],(4,0):[],(4,1):[],(4,2):[],(4,3):[],(4,4):[],(4,5):[],(4,6):[],(4,7):[],(4,8):[],(4,9):[],(5,0):[],(5,1):[],(5,2):[],(5,3):[],(5,4):[],(5,5):[],(5,6):[],(5,7):[],(5,8):[],(5,9):[],(6,0):[],(6,1):[],(6,2):[],(6,3):[],(6,4):[],(6,5):[],(6,6):[],(6,7):[],(6,8):[],(6,9):[],(7,0):[],(7,1):[],(7,2):[],(7,3):[],(7,4):[],(7,5):[],(7,6):[],(7,7):[],(7,8):[],(7,9):[],(8,0):[],(8,1):[],(8,2):[],(8,3):[],(8,4):[],(8,5):[],(8,6):[],(8,7):[],(8,8):[],(8,9):[],(9,0):[],(9,1):[],(9,2):[],(9,3):[],(9,4):[],(9,5):[],(9,6):[],(9,7):[],(9,8):[],(9,9):[]}
def map_forbidden_moves_init2_10():
	return [[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]]]
def map_distance_init2_10():
	return [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
def plant_maze():
	plant(Entities.Bush)
	while get_entity_type() == Entities.Bush:
		use_item(Items.Fertilizer)

def go_to_target(goal_x, goal_y, curr_x = get_pos_x(), curr_y = get_pos_y()):
	if goal_x > curr_x:
		for i in range(goal_x - curr_x):
			move(East)
	else:
		for i in range(curr_x - goal_x):
			move(West)
	if goal_y > curr_y:
		for i in range(goal_y - curr_y):
			move(North)
	else:
		for i in range(curr_y - goal_y):
			move(South)
def go_to_target2(goal_x, goal_y, curr_x = get_pos_x(), curr_y = get_pos_y()):
	if goal_y > curr_y:
		for i in range(goal_y - curr_y):
			move(North)
	else:
		for i in range(curr_y - goal_y):
			move(South)
	if goal_x > curr_x:
		for i in range(goal_x - curr_x):
			move(East)
	else:
		for i in range(curr_x - goal_x):
			move(West)

def solving_mazes(solves_lol):
	start = get_op_count()
	backwards = {North:South, East:West, South:North, West:East}
	direction_x = {North: 0, South: 0, East: 1, West: -1}
	direction_y = {North: 1, South: -1, East: 0, West: 0}
	cur_direction = [North, East, South, West]
	has_been_visited = map_distance_init2_10()

	forbidden_moves = dir_forbidden()
	allowed_moves = dir_allowed()
	how_to_walk = dir_allowed()
	goal = []



	number_of_runs = 0
	n = 0
	move_counter = 0



	clear()
	plant_maze()

	def move_direction(move_direction):
		move(move_direction)
		cur_pos = (get_pos_x(), get_pos_y())
		for check in forbidden_moves[cur_pos]:
			if move(check):
				move(backwards[check])
				allowed_moves[cur_pos].append(check)
				new_pos = (cur_pos[0] + direction_x[check], cur_pos[1] + direction_y[check])
				allowed_moves[new_pos].append(backwards[check])
				forbidden_moves[cur_pos].remove(check)
				forbidden_moves[new_pos].remove(backwards[check])


	while move_counter < 100:
		cur_pos_x = get_pos_x()
		cur_pos_y = get_pos_y()
		direction = cur_direction[n % 4]
		if get_entity_type() == Entities.Treasure:
			goal = (cur_pos_x, cur_pos_y)

		if move(direction):
			if has_been_visited[cur_pos_x][cur_pos_y] == -1:
				has_been_visited[cur_pos_x][cur_pos_y] = 1
				move_counter += 1
			if get_entity_type() == Entities.Treasure:
				goal = (get_pos_x(), get_pos_y())
			if direction not in allowed_moves[(cur_pos_x, cur_pos_y)]:
				allowed_moves[(cur_pos_x, cur_pos_y)].append(direction)
				allowed_moves[(cur_pos_x + direction_x[direction], cur_pos_y + direction_y[direction])].append(backwards[direction])
				if direction in forbidden_moves[(cur_pos_x, cur_pos_y)]:
					forbidden_moves[(cur_pos_x, cur_pos_y)].remove(direction)
					forbidden_moves[(cur_pos_x + direction_x[direction], cur_pos_y + direction_y[direction])].remove(backwards[direction])
			n += 1
		else:
			n -= 1

	def maze_solve(solves):
		if solves == 0:
			return

		how_to_walk = dir_allowed()
		moves_list = [(4, 4)]
		while moves_list:
			moves_list_new = []
			for pos in moves_list:
				for moves in allowed_moves[(pos[0],pos[1])]:
					if not how_to_walk[(pos[0] + direction_x[moves],pos[1] + direction_y[moves])]:
						moves_list_new.append((pos[0] + direction_x[moves],pos[1] + direction_y[moves]))
						how_to_walk[(pos[0] + direction_x[moves],pos[1] + direction_y[moves])] = how_to_walk[(pos[0],pos[1])] + [moves]
			moves_list = moves_list_new

		for i in range(solves):
			walking_back = how_to_walk[(get_pos_x(), get_pos_y())] + []
			walking_to = how_to_walk[(goal[0], goal[1])] + []
			while walking_back and walking_to and walking_back[0] == walking_to[0]:
				walking_back.pop(0)
				walking_to.pop(0)
			for direction_back in walking_back[::-1]:
				move_direction(backwards[direction_back])
			for direction_to in walking_to:
				move_direction(direction_to)
			goal = measure()
			while get_entity_type() == Entities.Treasure:
				use_item(Items.Fertilizer)

		return goal

	def maze_solve2(solves):
		#start1 = get_time()
		if solves == 0:
			return

		how_to_walk = dir_allowed()
		moves_list = [(4, 4)]
		while moves_list:
			moves_list_new = []
			for pos in moves_list:
				for moves in allowed_moves[(pos[0],pos[1])]:
					if not how_to_walk[(pos[0] + direction_x[moves],pos[1] + direction_y[moves])]:
						moves_list_new.append((pos[0] + direction_x[moves],pos[1] + direction_y[moves]))
						how_to_walk[(pos[0] + direction_x[moves],pos[1] + direction_y[moves])] = how_to_walk[(pos[0],pos[1])] + [moves]
			moves_list = moves_list_new

		for i in range(solves):
			go_to_target(goal[0], goal[1])
			go_to_target2(goal[0], goal[1])
			walking_back = how_to_walk[(get_pos_x(), get_pos_y())] + []
			walking_to = how_to_walk[(goal[0], goal[1])] + []
			while walking_back and walking_to and walking_back[0] == walking_to[0]:
				walking_back.pop(0)
				walking_to.pop(0)
			for direction_back in walking_back[::-1]:
				move(backwards[direction_back])
			for direction_to in walking_to:
				move(direction_to)
			goal = measure()
			if goal == None:
				#end1 = get_time()
				#quick_print("last ", solves_lol[-1], ": ", end1-start1)
				return goal
			while get_entity_type() == Entities.Treasure:
				use_item(Items.Fertilizer)

		return goal

	length = len(solves_lol)
	for i in range(length):
		if i == length - 1:
			maze_solve2(solves_lol[i])
		else:
			goal = maze_solve(solves_lol[i])


	harvest()
	end = get_op_count()
	return end-start

	#quick_print(end-start,"seconds")

times2 = []
for i in range(10000):
	# times2.append((solving_mazes([15,25,35,50,87,88])/16800)) # 1x300
	times2.append((solving_mazes([15, 25, 60, 0])/16800)) # 1x100
	# times2.append((solving_mazes([20, 0])/16800)) # 1x20

	if i % 10 == 0:

		quick_print("min: ", min(times2))
		times2 = []
