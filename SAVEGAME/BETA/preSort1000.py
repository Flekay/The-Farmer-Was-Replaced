clear()

def simple_swap():
	if measure(West) > measure():
		swap(West)
	if measure(North) < measure():
		swap(North)
	if measure(South) > measure():
		swap(South)
	if measure(East) < measure():
		swap(East)
	if measure(West) > measure():
		swap(West)
	if measure(North) < measure():
		swap(North)
	if measure(South) > measure():
		swap(South)
	if measure(East) < measure():
		swap(East)

farm_cacti_twice_optimized154()
def farm_cacti_twice_optimized154():
	ws = get_world_size()
	ws_range = range(ws)
	l = []

	# Combined till, plant and initial sort
	for x in ws_range:
		l.append([])
		for y in ws_range:
			# Till and plant
			till()
			plant(Entities.Cactus)

			# Initial sort
			if measure(West) and measure(West) > measure():
				swap(West)
			if measure(South) and measure(South) > measure():
				swap(South)
			if measure(West) and measure(West) > measure():
				swap(West)
			if measure(South) and measure(South) > measure():
				swap(South)

			# Store the measure
			l[x].append(measure())
			l[x-1][y] = measure(West)
			l[x][y-1] = measure(South)

			move(North)
		move(East)

	# preSort
	preTicks = get_tick_count()
	for dir in moves:
		move(dir)
		simple_swap()

	#quick_print("preSort1000",get_tick_count() - ticks)
	preTicks = get_tick_count() - preTicks

	# quick debug scan
	move_to(0, 0)
	for x in ws_range:
		for y in ws_range:
			l[get_pos_x()][get_pos_y()] = measure()
			move(North)
		move(East)

	ticks = get_tick_count()
	# Final sorting passes (using existing logic)
	def insert_low(i, j):
		cur = l[i][j]
		if i:
			if j:
				left = l[i - 1][j]
				down = l[i][j - 1]
				if cur < left or cur < down:
					move_to(i, j)
					while cur < left or cur < down:
						if left > down:
							swap(West)
							l[i][j] = left
							i -= 1
							l[i][j] = cur
							if i:
								move(West)
								left = l[i - 1][j]
								down = l[i][j - 1]
							else:
								break
						else:
							swap(South)
							l[i][j] = down
							j -= 1
							l[i][j] = cur
							if j:
								move(South)
								left = l[i - 1][j]
								down = l[i][j - 1]
							else:
								break
		if i:
			if cur < l[i - 1][j]:
				move_to(i, j)
				while cur < l[i - 1][j]:
					swap(West)
					l[i][j] = l[i - 1][j]
					i -= 1
					l[i][j] = cur
					if i:
						move(West)
					else:
						break
		if j:
			if cur < l[i][j - 1]:
				li = l[i]
				move_to(i, j)
				while cur < li[j - 1]:
					swap(South)
					li[j] = li[j - 1]
					j -= 1
					li[j] = cur
					if j:
						move(South)
					else:
						break

	n1 = ws - 1
	def insert_high(i, j):
		cur = l[i][j]
		if i < n1:
			if j < n1:
				right = l[i + 1][j]
				up = l[i][j + 1]
				if cur > right or cur > up:
					move_to(i, j)
					while cur > right or cur > up:
						if right < up:
							swap(East)
							l[i][j] = right
							i += 1
							l[i][j] = cur
							if i < n1:
								move(East)
								right = l[i + 1][j]
								up = l[i][j + 1]
							else:
								break
						else:
							swap(North)
							l[i][j] = up
							j += 1
							l[i][j] = cur
							if j < n1:
								move(North)
								right = l[i + 1][j]
								up = l[i][j + 1]
							else:
								break
		if i < n1:
			if cur > l[i + 1][j]:
				move_to(i, j)
				while cur > l[i + 1][j]:
					swap(East)
					l[i][j] = l[i + 1][j]
					i += 1
					l[i][j] = cur
					if i + 1 < ws:
						move(East)
					else:
						break
		if j < n1:
			if cur > l[i][j + 1]:
				li = l[i]
				move_to(i, j)
				while cur > li[j + 1]:
					swap(North)
					li[j] = li[j + 1]
					j += 1
					li[j] = cur
					if j < n1:
						move(North)
					else:
						break
	rn = range(ws)
	rrn = range(ws - 1, -1, -1)
	for size in range(5):
		for i in rn:
			for j in rn:
				if l[i][j] == size:
					insert_low(i, j)
		size = 9 - size
		for i in rrn:
			for j in rrn:
				if l[i][j] == size:
					insert_high(i, j)
	harvest()
	ticks = get_tick_count() - ticks
	quick_print(index,"preSort: ",preTicks, "targetedSort: ", ticks, "total: ", ticks + preTicks)
	