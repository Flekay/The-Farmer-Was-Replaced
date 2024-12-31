def part1():
	i = 0
	for direction in FULL_MOVES:
		till()
		plant(Entities.Sunflower)
		if get_pos_y() == 0:
			while measure() != 7:
				harvest()
				plant(Entities.Sunflower)
		else:
			m = measure()
			power[index[m]].append((get_pos_x(), get_pos_y()))
			if m > 13:
				use_item(Items.Water)
				if i > 83:
					use_item(Items.Water)
			i += 1
		move(direction)
	
	x = 0
	y = 1
	for points in power:
		while points:
			tx = x
			ty = y
			x, y = points[0]
			navi_to_list(x,y,tx,ty)
			if not can_harvest() and get_water() < 0.25:
				use_item(Items.Water)
	
			if can_harvest() or (len(points) < 4 and use_item(Items.Fertilizer) and can_harvest()):
				points.pop(0)
				harvest()
			else:
				points.append(points.pop(0))
	navi_to_list(0,1,x,y)