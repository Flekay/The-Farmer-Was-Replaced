
def cactusV2(measures=None):
	size=get_world_size()
	#move_to(0,0,size)
	# if measures == None:
	# 	measures = plant_cactiV2(size)
	#quick_print(measures)

	sm1 = size - 1
	rn = range(size)
	rrn = range(sm1, -1, -1)
	for s in range(9):
		for i in rn:
			for j in rn:
				m = measures[i][j]
				if m == s:
					insert_low(i, j, m, measures, size)

		s = 9 - s
		for i in rrn:
			for j in rrn:
				m = measures[i][j]
				if m == s:
					insert_high(i, j, m, measures, size)

	harvest()
	