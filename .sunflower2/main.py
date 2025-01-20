move_x, move_y = loadDataList(get_world_size())
rr7 = range(7)
rr79 = range(7,9)
rr9 = range(9)
rr10 = range(10)
moves = (
	[East],
	(North, North, North, North, North, North, North, North, North, East),
	(South, South, South, South, South, South, South, South, South, East),
	(North, North, North, North, North, North, North, North, North, East),
	(South, South, South, South, South, South, South, South, South, East),
	(North, North, North, North, North, North, North, North, North, East),
	(South, South, South, South, South, South, South, South, South, East),
)
moves2 = (
	(North, North, North, North, North, North, North, North, North, East),
	(South, South, South, South, South, South, South, South, South, East),
	(North, North, North, North, North, North, North, North, North, East),
)

for i in rr10:
	till()
	plant(Entities.Sunflower)
	while measure() != 7:
		harvest()
		plant(Entities.Sunflower)
	move(North)
move(East)
threshold_dict = {}
for x in rr10:
	threshold_dict[x] = {}
	for i in range(11,16,1):
		threshold_dict[x][i] = 0.05 + 0.7 * (0.37 * ((i - 11)/4) + 0.6 * (x/8))

petals_list = (set(),set(),set(),set(),set(),set(),set(),set(),set())
tilling = True
while num_items(Items.Power) < 100000:
	if tilling:
		plant_till()
		tilling = False
	else:
		planting()

	cur_pos = get_pos_x(), get_pos_y()
	for petals_set in petals_list:
		path = shortest_path(petals_set, cur_pos)
		for closest in path:
			# closest = shortest_dis(petals_set, cur_pos)
			goal_x, goal_y = closest
			start_x, start_y = cur_pos
			cur_pos = closest
			navi_to_list(goal_x, goal_y, start_x, start_y)
			# petals_set.remove(closest)
			while not can_harvest():
				use_item(Items.Fertilizer)
			harvest()
	navi_to_list(0, 0, goal_x, goal_y)
