clear()
farm_cacti_once_v5()

def plant_cacti():
	n = get_world_size()
	l = []
	move_to(0, 0)
	for i in range(n):
		l.append([])
		for j in range(n):
			till()
			plant(Entities.Cactus)
			l[i].append(measure())
			move(North)
		move(East)
	return l

def farm_cacti_once_v5():
	ws = get_world_size()
	l = plant_cacti()
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
	