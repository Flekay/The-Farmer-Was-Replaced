
def plant_cactiV2(size=get_world_size()):
	measures = []
	# Plant
	for i in range(size):
		measures.append([])
		line = measures[i]
		for j in range(size):
			#harvest() # only for full reset runs
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			m = measure()
			line.append(m)

			do_swaps_low(i, j, measures, size)

			move(North)
		move(East)
	return measures
	