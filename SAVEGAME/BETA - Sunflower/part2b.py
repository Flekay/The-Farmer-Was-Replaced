def part3(loops):
	for _ in range(loops):
		for direction in SMALL_MOVES:
			plant(Entities.Sunflower)
			m = measure()
			power[index[m]].append((get_pos_x(), get_pos_y()))
			if m > 13 and get_water() < 0.35:
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
				if not can_harvest() and get_water() < 0.25:
					use_item(Items.Water)

				if can_harvest() or (len(points) < 4 and use_item(Items.Fertilizer) and can_harvest()):
					points.pop(0)
					harvest()
				else:
					points.append(points.pop(0))

		navi_to_list(0,1,x,y)
		