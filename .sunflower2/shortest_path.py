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


distances = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1)





lst = [(3,6), (4,5), (5,4), (6,3), (7,2), (8,1), (9,0), (0,9), (1,8), (2,7)]
mypos = (1,1)
pos = (8,8)
x1, y1 = mypos
x2, y2 = pos
# quick_print(x1-x2, y1-y2)
ticks = get_tick_count()
quick_print(distance(mypos, pos))
quick_print(get_tick_count()-ticks)

ticks = get_tick_count()
quick_print(distances[x1-x2] + distances[y1-y2])
quick_print(get_tick_count()-ticks)


dict = {(2,4): 1, (3,5): 2, (4,6): 3, (5,7): 4, (6,8): 5, (7,9): 6, (8,4): 7}
ticks = get_tick_count()
quick_print(pos in dict)
quick_print(get_tick_count()-ticks)
