
clear()
MOVES = generate_moves()
move_x2, move_y2 = loadData(get_world_size()) # can be replaced with navi-to-pos.py for better performance
power = {
	15: [],
	14: [],
	13: [],
	12: [],
	11: [],
	10: [],
	9: [],
	8: [],
	7: [],
}

for direction in MOVES:
	till()
	move(direction)

while True:
	# replant sunflowers
	for direction in MOVES:
		plant(Entities.Sunflower)
		power[measure()].append((get_pos_x(), get_pos_y()))
		if get_water() < 0.76:
			use_item(Items.Water_Tank)
		move(direction)


	# harvest sunflowers highest petals to lowest
	for i in range(15, 8, -1):
		for x in range(len(power[i])):
			navi_to_pos(power[i][x])
			while not can_harvest():
				use_item(Items.Fertilizer)
			harvest()
		power[i] = []
	# destroy 7s and 8s
	navi_to_pos(power[i-2][0])
	harvest()
	power[i-1] = []
	power[i-2] = []
