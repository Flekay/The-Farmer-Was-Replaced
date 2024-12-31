def part2(loops=5, pre_water=0.35, fert_water=0.25, point_len=4):
	for _ in range(loops):
		for direction in SMALL_MOVES:
			plant(Entities.Sunflower)
			m = measure()
			power[index[m]].append((get_pos_x(), get_pos_y()))
			if m > 13 and get_water() < pre_water:
				use_item(Items.Water)
			move(direction)
		
		x = 0
		y = 1
		for points in power:
			while points:
				tx = x
				ty = y
				x, y = points[0]
				navi_to_list(x,y,tx,ty)
				if not can_harvest() and get_water() < fert_water:
					use_item(Items.Water)

				if can_harvest() or (len(points) < point_len and use_item(Items.Fertilizer) and can_harvest()):
					points.pop(0)
					harvest()
				else:
					points.append(points.pop(0))

		navi_to_list(0,1,x,y)
		