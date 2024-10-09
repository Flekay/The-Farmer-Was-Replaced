
clear()
MOVES = generate_moves()
move_data_x, move_data_y = loadDataList(get_world_size())
power_modifier = {
	15: 100000000,
	14: 200000000,
	13: 300000000,
	12: 400000000,
	11: 500000000,
	10: 600000000,
	9:  700000000,
	8:  800000000,
	7:  900000000,
}



for direction in MOVES:
	till()
	move(direction)

def power_hash():
	i = 0
	# pre water
	for direction in MOVES:
		while get_water() != 1:
			use_item(Items.Water)
		move(direction)

	for _ in range(8): # ~1min
		# plant sunflowers
		for direction in MOVES:
			if get_entity_type():
				move(direction)
			else:
				plant(Entities.Sunflower)
				power[power_modifier[measure()]+i] = (get_pos_x(), get_pos_y())
				i += 1
				move(direction)

		# harvest sunflowers highest petals to lowest
		while len(power) > 10:
			navi_to_list_pos(power.pop(min(power)))
			while not can_harvest():
				use_item(Items.Fertilizer)
				# pass
			harvest()

	# remove the rest
	while power:
		navi_to_list_pos(power.pop(min(power)))
		harvest()


while True:
	power = {}
	power_hash()
