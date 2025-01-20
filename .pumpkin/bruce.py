delta_lookup = {}
for delta in range(-9, 10):
	delta_lookup[delta] = (delta + 5) % 10 - 5
def pump_moveto(dx, dy):
	for i in range(dx):
		move(East)
	for i in range(-dx):
		move(West)
	for i in range(dy):
		move(North)
	for i in range(-dy):
		move(South)

while num_items(Items.Pumpkin) < 100000:
	pump_set = set()
	for i in range(10):
		for j in range(10):
			if not num_items(Items.Pumpkin):
				till()
			plant(Entities.Pumpkin)
			move(North)
		move(East)
	for i in range(10):
		for j in range(10):
			if not can_harvest():
				plant(Entities.Pumpkin)
				pump_set.add((get_pos_x(),get_pos_y()))
			move(North)
		move(East)
	while pump_set:
		del_set= set()
		for pos in pump_set:
			pump_moveto(delta_lookup[pos[0]-get_pos_x()], delta_lookup[pos[1]-get_pos_y()])
			if can_harvest():
				del_set.add(pos)
			else:
				plant(Entities.Pumpkin)
				if get_water() < 0.2:
					use_item(Items.Water)
				if len(pump_set)-len(del_set) < 8:
					while not can_harvest():
						plant(Entities.Pumpkin)
						if get_water() < 0.4:
							use_item(Items.Water)
						use_item(Items.Fertilizer)
					del_set.add(pos)
		for p in del_set:
			pump_set.remove(p)
	harvest()



