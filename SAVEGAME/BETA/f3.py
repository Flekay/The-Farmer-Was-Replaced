clear()
moves = {}
moves[0] = 0
m = move
def dbg_move(direction):
	moves[0] += m(direction)
move = dbg_move

swaps = {}
swaps[0] = 0
s = swap
def dbg_swap(direction):
	swaps[0] += s(direction)
swap = dbg_swap

	
farm_cacti_twice_optimized2()
quick_print("f3 moves: ",moves[0])
quick_print("f3 swaps: ",swaps[0])
def farm_cacti_twice_optimized2():
	ticks = get_tick_count()
	move_to = gen_move_to()
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
	# rn = range(ws)
	rrn = range(n1, -1, -1)
	for size in range(5):
		for x in ws_range:
			for y in ws_range:
				if l[x][y] == size:
					insert_low(x, y)
		size = 9 - size
		for x in rrn:
			for y in rrn:
				if l[x][y] == size:
					insert_high(x, y)
	harvest()
	quick_print("f3",get_tick_count() - ticks)
	