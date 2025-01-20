
# main.py
MOVES = generate_moves_light()
move_x, move_y = loadDataList(get_world_size())
distances = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1)
start = (0,0)

# 0. Preplant
# 1 * ~5000
pos = tilling()

# 19 * ~5000
for _ in range(19):
	pumpkin_set = set()
	# 1. just plant and move
	planting()
	# 2. plant and append to dict
	appanting(pumpkin_set)
	# 3. visit all missing pumpkins until ready to harvest
	pos = pathing(pumpkin_set, pos)
	# 4. fertilize the remaining pumpkins
	pos = fertilizing(pumpkin_set, pos)
	# 5. harvest
	harvest()

if num_items(Items.Pumpkin) + 1675 > 100000:
	# 1 * ~1800
	sixing(pos)
else:
	# 1 * ~2450
	sevening(pos)














# functions.py
def tilling():
	pumpkin_set = set()
	for direction in MOVES:
		till()
		plant(Entities.Pumpkin)
		move(direction)
	appanting(pumpkin_set)
	pos = pathing(pumpkin_set, start)
	pos = fertilizing(pumpkin_set, pos)
	harvest()
	return pos

def planting(MOVES=MOVES):
	for direction in MOVES:
		plant(Entities.Pumpkin)
		move(direction)

def appanting(pumpkin_set, MOVES=MOVES):
	for direction in MOVES:
		if not can_harvest():
			plant(Entities.Pumpkin)
			pumpkin_set.add((get_pos_x(), get_pos_y()))
		move(direction)

def pathing(pumpkin_set, tpos):
	while len(pumpkin_set) > num_items(Items.Fertilizer)/2+2:
		path = shortest_path(set(pumpkin_set), tpos)
		for pos in path:
			navi_to_list_pos(pos, tpos)
			tpos = pos
			if can_harvest():
				pumpkin_set.remove(pos)
			else:
				plant(Entities.Pumpkin)
				if get_water() < 0.2:
					use_item(Items.Water)
	return tpos

def fertilizing(pumpkin_set, tpos):
	for pos in pumpkin_set:
		navi_to_list_pos(pos, tpos)
		tpos = pos
		while not can_harvest():
			plant(Entities.Pumpkin)
			use_item(Items.Fertilizer)
	return tpos

def sixing(pos):
	pumpkin_set = set()
	navi_to_list_pos(start, pos)
	MOVES = (
		North, North, North, North, North, East,
		South, South, South, South, East,
		North, North, North, North, East,
		South, South, South, South, East,
		North, North, North, North, East,
		South, South, South, South, South,
		West,  West,  West,  West,  West,
	)
	planting(MOVES)
	appanting(pumpkin_set, MOVES)
	pos = pathing(pumpkin_set, start)
	pos = fertilizing(pumpkin_set, pos)
	harvest()

def sevening(pos):
	start = (3,3)
	pumpkin_set = set()
	navi_to_list_pos(start, pos)
	MOVES = (
		North, East, South, South, West, West, North,
		West, South, South, East, East, East, East,
		North, North, North, North, West, West, West,
		West, West, North, East, East, East, East,
		East, East, South, South, South, South, South,
		South, West, West, West, West, West, West, North,
		North, North, North, East, East, East
	)
	planting(MOVES)
	MOVES = (
		East, South, South, West, West, North,
		West, South, South, East, East, East, East,
		North, North, North, North, West, West, West,
		West, West, North, East, East, East, East,
		East, East, South, South, South, South, South,
		South, West, West, West, West, West, West, North,
		North, North, North, East, East, East
	)
	appanting(pumpkin_set, MOVES)

	move(South)
	if not can_harvest():
		plant(Entities.Pumpkin)
		pumpkin_set.add((get_pos_x(), get_pos_y()))

	pos = pathing(pumpkin_set, start)
	pos = fertilizing(pumpkin_set, pos)
	harvest()














# pathing.py
def shortest_dis(lst, mypos, closest = 0, closest_dis = 20):
	cur_x, cur_y = mypos
	for pos in lst:
		x, y = pos
		dis = distances[x - cur_x] + distances[y - cur_y]
		if dis < closest_dis:
			closest = pos
			closest_dis = dis
			if closest_dis < 3:
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
	
