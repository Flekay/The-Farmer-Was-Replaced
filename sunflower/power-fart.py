NAVI_TO_NEXT_TILE = navi_to_next_tile()
MOVES = generate_moves()
WATER = Items.Water_Tank
FERTILIZER = Items.Fertilizer
SUNFLOWER = Entities.Sunflower

def powerFart():

	def plant7s():
		for direction in MOVES:
			if get_ground_type() != Grounds.Soil:
				till()
			plant(SUNFLOWER)
			while measure() != 7:
				plant(SUNFLOWER)
				if measure() != 7:
					till()
				else:
					break
			move(direction)

	def water():
		for direction in MOVES:
			use_item(WATER)
			use_item(WATER)
			use_item(WATER)
			use_item(WATER)
			move(direction)
		for direction in MOVES:
			use_item(WATER)
			move(direction)


	plant7s()
	water()

	for i in range(1067):
		harvest()
		plant(SUNFLOWER)
		if measure() == 7:
			move(NAVI_TO_NEXT_TILE[get_pos_x()][get_pos_y()])
		elif get_water():
			use_item(FERTILIZER)
		else:
			use_item(WATER)
			use_item(WATER)
			use_item(FERTILIZER)

	for dir in MOVES:
		harvest()
		move(dir)


while True:
	powerFart()








op = get_op_count()
use_item(FERTILIZER)
quick_print("Time:", get_op_count() - op)
