
def get_ranked_dirs(pos_x, pos_y, goal_x, goal_y, exclude=None):
	if goal_x == None:
		all_dirs = [(1, North), (2, East), (3, South), (4, West)]
	else:
		all_dirs = [
			(goal_y - pos_y + 0.1, North),
			(goal_x - pos_x + 0.2, East),
			(pos_y - goal_y + 0.3, South),
			(pos_x - goal_x + 0.4, West)]

	ranked_dirs = []
	for i in range(len(all_dirs)):
		worst_dir = min(all_dirs)
		all_dirs.remove(worst_dir)
		if worst_dir[1] != exclude:
			ranked_dirs.append(worst_dir[1])

	return ranked_dirs