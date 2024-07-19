def goto(goal_x, goal_y, curr_x = get_pos_x(), curr_y = get_pos_y()):
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

def goto2(goal_x, goal_y, curr_x = get_pos_x(), curr_y = get_pos_y()):
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
