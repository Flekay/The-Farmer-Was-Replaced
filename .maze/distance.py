def manhatten_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


x1, y1 = 0, 0
x2, y2 = 3, 4
distances = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1)

ticks = get_tick_count()
distance = manhatten_distance(x1, y1, x2, y2)
ticks = get_tick_count() - ticks
quick_print("distance", distance, "ticks", ticks)

ticks = get_tick_count()
distance = distances[x2 - x1] + distances[y2 - y1]
ticks = get_tick_count() - ticks
quick_print("distance", distance, "ticks", ticks)




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

distances = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1)
bigset = {(2,4), (3,5), (4,6), (5,7), (6,8), (7,9), (8,4)}
pos = 0, 0

ticks = get_tick_count()
quick_print(pos in bigset)
quick_print("bigset", get_tick_count() - ticks)

ticks = get_tick_count()
quick_print(shortest_dis(bigset, (0,0)))
quick_print("shortest_dis", get_tick_count() - ticks)
