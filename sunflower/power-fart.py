NAVI_TO_NEXT_TILE = loadNaviToNextTile()
MOVES = generate_moves()

def powerFart():
	size = get_world_size()**2
	WATER = Items.Water_Tank
	FERTILIZER = Items.Fertilizer
	SUNFLOWER = Entities.Sunflower

	def plant7s():
		for i in range(size):
			for i in range(0, 1, 0):
				if get_ground_type() != Grounds.Soil:
					till()
				plant(SUNFLOWER)
				
				if measure() != 7:
					till()
				else:
					break
			move(NAVI_TO_NEXT_TILE[get_pos_x()][get_pos_y()])

	def water():
		for i in range(size):
			use_item(WATER)
			use_item(WATER)
			use_item(WATER)
			use_item(WATER)
			move(NAVI_TO_NEXT_TILE[get_pos_x()][get_pos_y()])
		for i in range(size):
			use_item(WATER)
			move(NAVI_TO_NEXT_TILE[get_pos_x()][get_pos_y()])


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


for i in range(0, 1, 0):
	powerFart()