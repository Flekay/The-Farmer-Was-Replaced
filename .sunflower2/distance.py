def shortest_dis(lst, mypos, closest = 0, closest_dis = 20):
	cur_x, cur_y = mypos
	for pos in lst:
		x, y = pos
		dx = abs(x - cur_x)
		dy = abs(y - cur_y)
		dis = min(dx, 10 - dx) + min(dy, 10 - dy)
		if dis < closest_dis:
			closest = pos
			closest_dis = dis
			if closest_dis < 3:
				break
	return closest
