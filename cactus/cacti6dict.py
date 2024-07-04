def setup():
	clear()
	till()
	move(North)
	till()
	move(North)
	till()
	move(South)
	move(East)
	till()
	move(South)
	till()
	move(East)
	till()
	move(West)
	move(West)

setup()
start = get_time()
cactus_grid_1st = build_grid_dict()
# cactus_grid_1st = build_grid_dict_alt()
cactus_grid_2nd = build_grid_dict2()
quick_print("Time taken to build the grid", get_time() - start)
cactus1 = None
cactus2 = None
cactus3 = None
cactus4 = None
CACTUS = Entities.Cactus



for i in range(0,1,0):
	# 1st cactus
	move(North)
	plant(CACTUS)
	cactus1 = measure()
	swap(cactus_grid_1st[(cactus1, None, None, None)])

	# 2nd cactus
	plant(CACTUS)
	cactus2 = measure()
	swap(cactus_grid_1st[(cactus1, cactus2, None, None)])

	# 3rd cactus
	plant(CACTUS)
	cactus3 = measure()
	swap(cactus_grid_1st[(cactus1, cactus2, cactus3, None)])

	# 4th cactus
	plant(CACTUS)
	for swaps in cactus_grid_1st[(cactus1, cactus2, cactus3, measure())]:
		swap(swaps)

	# 5th and 6th cactus
	move(South)
	move(East)
	plant(CACTUS)
	swap(East)
	plant(CACTUS)


	# final swap
	for swaps in cactus_grid_2nd[(measure(North), measure(East), measure(West), measure())]:
		swap(swaps)

	# reset
	move(West)
	harvest()