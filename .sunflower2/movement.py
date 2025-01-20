clear()
moves = (
	[East],
	(North, North, North, North, North, North, North, North, North, East),
	(South, South, South, South, South, South, South, South, South, East),
	(North, North, North, North, North, North, North, North, North, East),
	(South, South, South, South, South, South, South, South, South, East),
	(North, North, North, North, North, North, North, North, North, East),
	(South, South, South, South, South, South, South, South, South, East),
	(North, North, North, North, North, North, North, North, North, East),
)
moves2 = (
	[East],
	(South, South, South, South, South, South, South, South, South, East),
	(North, North, North, North, North, North, North, North, North, East),
)
ticks = get_tick_count()
x = 0
for moves2 in moves:
	x+=1
	for dir in moves2:
		till()
		if get_pos_x() == 0:
			move(East)
		plant(Entities.Sunflower)
		m=measure()
		if m > 13:
			use_item(Items.Water)
		petals_list[15-m].add((get_pos_x(), get_pos_y()))
		move(dir)
move(North)
quick_print(get_tick_count()-ticks)


def planting():
	P = min(max(0.1, num_items(Items.Power)/7800),1)
	pos_x = get_pos_x()
	for movex in moves:
		x = pos_x
		pos_x += 1
		for _ in movex:
			plant(Entities.Sunflower)
			m = measure()
			if m > 10:
				threshold = threshold_dict[(m,x)] * P
				while get_water() < threshold and num_items(Items.Water):
					use_item(Items.Water)
			petals_list[15-m].add((pos_x, get_pos_y()))
			move(North)
		move(East)
	for movex in moves2:
		x = pos_x
		pos_x += 1
		for _ in movex:
			m = replanting()
			if m > 10:
				threshold = threshold_dict[(m,x)] * P
				while get_water() < threshold and num_items(Items.Water):
					use_item(Items.Water)
			petals_list[15-m].add((pos_x, get_pos_y()))
			move(North)
		move(East)
