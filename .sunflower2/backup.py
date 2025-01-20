move_x, move_y = loadDataList(get_world_size())
rr7 = range(7)
rr79 = range(7,9)
rr9 = range(9)
rr10 = range(10)
distances = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1)
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
petals_list = (set(),set(),set(),set(),set(),set(),set(),set(),set())

till()
plant(Entities.Sunflower)
m=measure()
if m > 13:
	use_item(Items.Water)
petals_list[15-m].add((get_pos_x(), get_pos_y()))
move(North)
for i in rr9:
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
			goal_x, goal_y = closest
			start_x, start_y = cur_pos
			cur_pos = closest
			navi_to_list(goal_x, goal_y, start_x, start_y)
			while not can_harvest():
				use_item(Items.Fertilizer)
			harvest()
	navi_to_list(0, 0, goal_x, goal_y)













def shortest_dis(lst, mypos, closest = 0, closest_dis = 20):
	cur_x, cur_y = mypos
	for pos in lst:
		x, y = pos
		dis = distances[x - cur_x] + distances[y - cur_y]
		if dis < closest_dis:
			closest = pos
			closest_dis = dis
			if closest_dis < 2:
				break
	return closest

def shortest_path(lst, mypos):
	cur_pos = mypos
	path = []
	while lst:
		closest = shortest_dis(lst, cur_pos)
		path.append(closest)
		lst.remove(closest)
		cur_pos = closest
	return path













def plant_till():
	for x in rr9:
		for y in rr10:
			till()
			if get_pos_x() == 0:
				move(East)
			plant(Entities.Sunflower)
			m=measure()
			if m > 13:
				use_item(Items.Water)
			petals_list[15-m].add((get_pos_x(), get_pos_y()))
			move(North)
		move(East)











def planting():
	P = min(max(0.1, num_items(Items.Power)/7800),1)
	pos_x = 0
	for movex in moves:
		thresholdx = threshold_dict[pos_x]
		for dir in movex:
			plant(Entities.Sunflower)
			m = measure()
			if m > 10:
				threshold = thresholdx[m] * P
				while get_water() < threshold and num_items(Items.Water):
					use_item(Items.Water)
			petals_list[15-m].add((pos_x, get_pos_y()))
			move(dir)
		pos_x += 1

	for movex in moves2:
		thresholdx = threshold_dict[pos_x]
		for dir in movex:
			m = replanting()
			if m > 10:
				threshold = thresholdx[m] * P
				while get_water() < threshold and num_items(Items.Water):
					use_item(Items.Water)
			petals_list[15-m].add((pos_x, get_pos_y()))
			move(dir)
		pos_x += 1


def replanting():
	plant(Entities.Sunflower)
	m = measure()
	if m == 15:
		if get_water() < 0.75:
			use_item(Items.Water)
		use_item(Items.Fertilizer)
		if can_harvest():
			harvest()
			m = replanting()
	return m
