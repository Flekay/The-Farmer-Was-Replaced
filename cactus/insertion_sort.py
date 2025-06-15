# any move_to function can be used.
# /movement/wrapping_shortest_path/navi_to_list.py
from navi_to_deltalist import *

def insertion_sort(grid):
	ws = get_world_size()
	rn = range(ws)
	n1 = ws - 1
	rrn = range(n1, -1, -1)

	def insert_low(x, y):
		cur = grid[x][y]
		if x:
			if y:
				left = grid[x - 1][y]
				down = grid[x][y - 1]
				if cur < left or cur < down:
					navi_to_deltalist(x, y)
					while cur < left or cur < down:
						if left > down:
							swap(West)
							grid[x][y] = left
							x -= 1
							grid[x][y] = cur
							if x:
								move(West)
								left = grid[x - 1][y]
								down = grid[x][y - 1]
							else:
								break
						else:
							swap(South)
							grid[x][y] = down
							y -= 1
							grid[x][y] = cur
							if y:
								move(South)
								left = grid[x - 1][y]
								down = grid[x][y - 1]
							else:
								break
		if x:
			if cur < grid[x - 1][y]:
				navi_to_deltalist(x, y)
				while cur < grid[x - 1][y]:
					swap(West)
					grid[x][y] = grid[x - 1][y]
					x -= 1
					grid[x][y] = cur
					if x:
						move(West)
					else:
						break
		if y:
			if cur < grid[x][y - 1]:
				li = grid[x]
				navi_to_deltalist(x, y)
				while cur < li[y - 1]:
					swap(South)
					li[y] = li[y - 1]
					y -= 1
					li[y] = cur
					if y:
						move(South)
					else:
						break

	def insert_high(x, y):
		cur = grid[x][y]
		if x < n1:
			if y < n1:
				right = grid[x + 1][y]
				up = grid[x][y + 1]
				if cur > right or cur > up:
					navi_to_deltalist(x, y)
					while cur > right or cur > up:
						if right < up:
							swap(East)
							grid[x][y] = right
							x += 1
							grid[x][y] = cur
							if x < n1:
								move(East)
								right = grid[x + 1][y]
								up = grid[x][y + 1]
							else:
								break
						else:
							swap(North)
							grid[x][y] = up
							y += 1
							grid[x][y] = cur
							if y < n1:
								move(North)
								right = grid[x + 1][y]
								up = grid[x][y + 1]
							else:
								break
		if x < n1:
			if cur > grid[x + 1][y]:
				navi_to_deltalist(x, y)
				while cur > grid[x + 1][y]:
					swap(East)
					grid[x][y] = grid[x + 1][y]
					x += 1
					grid[x][y] = cur
					if x + 1 < ws:
						move(East)
					else:
						break
		if y < n1:
			if cur > grid[x][y + 1]:
				li = grid[x]
				navi_to_deltalist(x, y)
				while cur > li[y + 1]:
					swap(North)
					li[y] = li[y + 1]
					y += 1
					li[y] = cur
					if y < n1:
						move(North)
					else:
						break
	for size in range(5):
		for x in rn:
			gridx = grid[x]
			for y in rn:
				if gridx[y] == size:
					insert_low(x, y)
		size = 9 - size
		for x in rrn:
			gridx = grid[x]
			for y in rrn:
				if gridx[y] == size:
					insert_high(x, y)
