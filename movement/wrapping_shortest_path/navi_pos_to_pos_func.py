_navi_to_func_pos = None
def update(ws=get_world_size()):
	global _navi_to_func_pos
	def init_move_to_func_map(ws=get_world_size()):
		def m0m0():
			pass
		def m0e1():
			move(East)
		def m0e2():
			move(East)
			move(East)
		def m0e3():
			move(East)
			move(East)
			move(East)
		def m0e4():
			move(East)
			move(East)
			move(East)
			move(East)
		def m0e5():
			move(East)
			move(East)
			move(East)
			move(East)
			move(East)
		def m0w4():
			move(West)
			move(West)
			move(West)
			move(West)
		def m0w3():
			move(West)
			move(West)
			move(West)
		def m0w2():
			move(West)
			move(West)
		def m0w1():
			move(West)
		def n1m0():
			move(North)
		def n1e1():
			move(North)
			move(East)
		def n1e2():
			move(North)
			move(East)
			move(East)
		def n1e3():
			move(North)
			move(East)
			move(East)
			move(East)
		def n1e4():
			move(North)
			move(East)
			move(East)
			move(East)
			move(East)
		def n1e5():
			move(North)
			move(East)
			move(East)
			move(East)
			move(East)
			move(East)
		def n1w4():
			move(North)
			move(West)
			move(West)
			move(West)
			move(West)
		def n1w3():
			move(North)
			move(West)
			move(West)
			move(West)
		def n1w2():
			move(North)
			move(West)
			move(West)
		def n1w1():
			move(North)
			move(West)
		def n2m0():
			move(North)
			move(North)
		def n2e1():
			move(North)
			move(North)
			move(East)
		def n2e2():
			move(North)
			move(North)
			move(East)
			move(East)
		def n2e3():
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
		def n2e4():
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
			move(East)
		def n2e5():
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
			move(East)
			move(East)
		def n2w4():
			move(North)
			move(North)
			move(West)
			move(West)
			move(West)
			move(West)
		def n2w3():
			move(North)
			move(North)
			move(West)
			move(West)
			move(West)
		def n2w2():
			move(North)
			move(North)
			move(West)
			move(West)
		def n2w1():
			move(North)
			move(North)
			move(West)
		def n3m0():
			move(North)
			move(North)
			move(North)
		def n3e1():
			move(North)
			move(North)
			move(North)
			move(East)
		def n3e2():
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
		def n3e3():
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
		def n3e4():
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
			move(East)
		def n3e5():
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
			move(East)
			move(East)
		def n3w4():
			move(North)
			move(North)
			move(North)
			move(West)
			move(West)
			move(West)
			move(West)
		def n3w3():
			move(North)
			move(North)
			move(North)
			move(West)
			move(West)
			move(West)
		def n3w2():
			move(North)
			move(North)
			move(North)
			move(West)
			move(West)
		def n3w1():
			move(North)
			move(North)
			move(North)
			move(West)
		def n4m0():
			move(North)
			move(North)
			move(North)
			move(North)
		def n4e1():
			move(North)
			move(North)
			move(North)
			move(North)
			move(East)
		def n4e2():
			move(North)
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
		def n4e3():
			move(North)
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
		def n4e4():
			move(North)
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
			move(East)
		def n4e5():
			move(North)
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
			move(East)
			move(East)
		def n4w4():
			move(North)
			move(North)
			move(North)
			move(North)
			move(West)
			move(West)
			move(West)
			move(West)
		def n4w3():
			move(North)
			move(North)
			move(North)
			move(North)
			move(West)
			move(West)
			move(West)
		def n4w2():
			move(North)
			move(North)
			move(North)
			move(North)
			move(West)
			move(West)
		def n4w1():
			move(North)
			move(North)
			move(North)
			move(North)
			move(West)
		def n5m0():
			move(North)
			move(North)
			move(North)
			move(North)
			move(North)
		def n5e1():
			move(North)
			move(North)
			move(North)
			move(North)
			move(North)
			move(East)
		def n5e2():
			move(North)
			move(North)
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
		def n5e3():
			move(North)
			move(North)
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
		def n5e4():
			move(North)
			move(North)
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
			move(East)
		def n5e5():
			move(North)
			move(North)
			move(North)
			move(North)
			move(North)
			move(East)
			move(East)
			move(East)
			move(East)
			move(East)
		def n5w4():
			move(North)
			move(North)
			move(North)
			move(North)
			move(North)
			move(West)
			move(West)
			move(West)
			move(West)
		def n5w3():
			move(North)
			move(North)
			move(North)
			move(North)
			move(North)
			move(West)
			move(West)
			move(West)
		def n5w2():
			move(North)
			move(North)
			move(North)
			move(North)
			move(North)
			move(West)
			move(West)
		def n5w1():
			move(North)
			move(North)
			move(North)
			move(North)
			move(North)
			move(West)
		def s4m0():
			move(South)
			move(South)
			move(South)
			move(South)
		def s4e1():
			move(South)
			move(South)
			move(South)
			move(South)
			move(East)
		def s4e2():
			move(South)
			move(South)
			move(South)
			move(South)
			move(East)
			move(East)
		def s4e3():
			move(South)
			move(South)
			move(South)
			move(South)
			move(East)
			move(East)
			move(East)
		def s4e4():
			move(South)
			move(South)
			move(South)
			move(South)
			move(East)
			move(East)
			move(East)
			move(East)
		def s4e5():
			move(South)
			move(South)
			move(South)
			move(South)
			move(East)
			move(East)
			move(East)
			move(East)
			move(East)
		def s4w4():
			move(South)
			move(South)
			move(South)
			move(South)
			move(West)
			move(West)
			move(West)
			move(West)
		def s4w3():
			move(South)
			move(South)
			move(South)
			move(South)
			move(West)
			move(West)
			move(West)
		def s4w2():
			move(South)
			move(South)
			move(South)
			move(South)
			move(West)
			move(West)
		def s4w1():
			move(South)
			move(South)
			move(South)
			move(South)
			move(West)
		def s3m0():
			move(South)
			move(South)
			move(South)
		def s3e1():
			move(South)
			move(South)
			move(South)
			move(East)
		def s3e2():
			move(South)
			move(South)
			move(South)
			move(East)
			move(East)
		def s3e3():
			move(South)
			move(South)
			move(South)
			move(East)
			move(East)
			move(East)
		def s3e4():
			move(South)
			move(South)
			move(South)
			move(East)
			move(East)
			move(East)
			move(East)
		def s3e5():
			move(South)
			move(South)
			move(South)
			move(East)
			move(East)
			move(East)
			move(East)
			move(East)
		def s3w4():
			move(South)
			move(South)
			move(South)
			move(West)
			move(West)
			move(West)
			move(West)
		def s3w3():
			move(South)
			move(South)
			move(South)
			move(West)
			move(West)
			move(West)
		def s3w2():
			move(South)
			move(South)
			move(South)
			move(West)
			move(West)
		def s3w1():
			move(South)
			move(South)
			move(South)
			move(West)
		def s2m0():
			move(South)
			move(South)
		def s2e1():
			move(South)
			move(South)
			move(East)
		def s2e2():
			move(South)
			move(South)
			move(East)
			move(East)
		def s2e3():
			move(South)
			move(South)
			move(East)
			move(East)
			move(East)
		def s2e4():
			move(South)
			move(South)
			move(East)
			move(East)
			move(East)
			move(East)
		def s2e5():
			move(South)
			move(South)
			move(East)
			move(East)
			move(East)
			move(East)
			move(East)
		def s2w4():
			move(South)
			move(South)
			move(West)
			move(West)
			move(West)
			move(West)
		def s2w3():
			move(South)
			move(South)
			move(West)
			move(West)
			move(West)
		def s2w2():
			move(South)
			move(South)
			move(West)
			move(West)
		def s2w1():
			move(South)
			move(South)
			move(West)
		def s1m0():
			move(South)
		def s1e1():
			move(South)
			move(East)
		def s1e2():
			move(South)
			move(East)
			move(East)
		def s1e3():
			move(South)
			move(East)
			move(East)
			move(East)
		def s1e4():
			move(South)
			move(East)
			move(East)
			move(East)
			move(East)
		def s1e5():
			move(South)
			move(East)
			move(East)
			move(East)
			move(East)
			move(East)
		def s1w4():
			move(South)
			move(West)
			move(West)
			move(West)
			move(West)
		def s1w3():
			move(South)
			move(West)
			move(West)
			move(West)
		def s1w2():
			move(South)
			move(West)
			move(West)
		def s1w1():
			move(South)
			move(West)

		if ws == 3:
			return [
				[m0m0, m0e1, m0w1, ],
				[n1m0, n1e1, n1w1, ],
				[s1m0, s1e1, s1w1, ],
			]
		if ws == 4:
			return [
				[m0m0, m0e1, m0e2, m0w1, ],
				[n1m0, n1e1, n1e2, n1w1, ],
				[n2m0, n2e1, n2e2, n2w1, ],
				[s1m0, s1e1, s1e2, s1w1, ],
			]
		if ws == 5:
			return [
				[m0m0, m0e1, m0e2, m0w2, m0w1, ],
				[n1m0, n1e1, n1e2, n1w2, n1w1, ],
				[n2m0, n2e1, n2e2, n2w2, n2w1, ],
				[s2m0, s2e1, s2e2, s2w2, s2w1, ],
				[s1m0, s1e1, s1e2, s1w2, s1w1, ],
			]
		if ws == 6:
			return [
				[m0m0, m0e1, m0e2, m0e3, m0w2, m0w1, ],
				[n1m0, n1e1, n1e2, n1e3, n1w2, n1w1, ],
				[n2m0, n2e1, n2e2, n2e3, n2w2, n2w1, ],
				[n3m0, n3e1, n3e2, n3e3, n3w2, n3w1, ],
				[s2m0, s2e1, s2e2, s2e3, s2w2, s2w1, ],
				[s1m0, s1e1, s1e2, s1e3, s1w2, s1w1, ],
			]
		if ws == 7:
			return [
				[m0m0, m0e1, m0e2, m0e3, m0w3, m0w2, m0w1, ],
				[n1m0, n1e1, n1e2, n1e3, n1w3, n1w2, n1w1, ],
				[n2m0, n2e1, n2e2, n2e3, n2w3, n2w2, n2w1, ],
				[n3m0, n3e1, n3e2, n3e3, n3w3, n3w2, n3w1, ],
				[s3m0, s3e1, s3e2, s3e3, s3w3, s3w2, s3w1, ],
				[s2m0, s2e1, s2e2, s2e3, s2w3, s2w2, s2w1, ],
				[s1m0, s1e1, s1e2, s1e3, s1w3, s1w2, s1w1, ],
			]
		if ws == 8:
			return [
				[m0m0, m0e1, m0e2, m0e3, m0e4, m0w3, m0w2, m0w1, ],
				[n1m0, n1e1, n1e2, n1e3, n1e4, n1w3, n1w2, n1w1, ],
				[n2m0, n2e1, n2e2, n2e3, n2e4, n2w3, n2w2, n2w1, ],
				[n3m0, n3e1, n3e2, n3e3, n3e4, n3w3, n3w2, n3w1, ],
				[n4m0, n4e1, n4e2, n4e3, n4e4, n4w3, n4w2, n4w1, ],
				[s3m0, s3e1, s3e2, s3e3, s3e4, s3w3, s3w2, s3w1, ],
				[s2m0, s2e1, s2e2, s2e3, s2e4, s2w3, s2w2, s2w1, ],
				[s1m0, s1e1, s1e2, s1e3, s1e4, s1w3, s1w2, s1w1, ],
			]
		if ws == 9:
			return [
				[m0m0, m0e1, m0e2, m0e3, m0e4, m0w4, m0w3, m0w2, m0w1, ],
				[n1m0, n1e1, n1e2, n1e3, n1e4, n1w4, n1w3, n1w2, n1w1, ],
				[n2m0, n2e1, n2e2, n2e3, n2e4, n2w4, n2w3, n2w2, n2w1, ],
				[n3m0, n3e1, n3e2, n3e3, n3e4, n3w4, n3w3, n3w2, n3w1, ],
				[n4m0, n4e1, n4e2, n4e3, n4e4, n4w4, n4w3, n4w2, n4w1, ],
				[s4m0, s4e1, s4e2, s4e3, s4e4, s4w4, s4w3, s4w2, s4w1, ],
				[s3m0, s3e1, s3e2, s3e3, s3e4, s3w4, s3w3, s3w2, s3w1, ],
				[s2m0, s2e1, s2e2, s2e3, s2e4, s2w4, s2w3, s2w2, s2w1, ],
				[s1m0, s1e1, s1e2, s1e3, s1e4, s1w4, s1w3, s1w2, s1w1, ],
			]
		if ws == 10:
			return [
				[m0m0, m0e1, m0e2, m0e3, m0e4, m0e5, m0w4, m0w3, m0w2, m0w1, ],
				[n1m0, n1e1, n1e2, n1e3, n1e4, n1e5, n1w4, n1w3, n1w2, n1w1, ],
				[n2m0, n2e1, n2e2, n2e3, n2e4, n2e5, n2w4, n2w3, n2w2, n2w1, ],
				[n3m0, n3e1, n3e2, n3e3, n3e4, n3e5, n3w4, n3w3, n3w2, n3w1, ],
				[n4m0, n4e1, n4e2, n4e3, n4e4, n4e5, n4w4, n4w3, n4w2, n4w1, ],
				[n5m0, n5e1, n5e2, n5e3, n5e4, n5e5, n5w4, n5w3, n5w2, n5w1, ],
				[s4m0, s4e1, s4e2, s4e3, s4e4, s4e5, s4w4, s4w3, s4w2, s4w1, ],
				[s3m0, s3e1, s3e2, s3e3, s3e4, s3e5, s3w4, s3w3, s3w2, s3w1, ],
				[s2m0, s2e1, s2e2, s2e3, s2e4, s2e5, s2w4, s2w3, s2w2, s2w1, ],
				[s1m0, s1e1, s1e2, s1e3, s1e4, s1e5, s1w4, s1w3, s1w2, s1w1, ],
			]

	move_to_func_map = init_move_to_func_map(ws)
	path_func_map = {}
	for x in range(ws):
		for y in range(ws):
			path_func_map[(x, y)] = {}

	for start_pos in path_func_map:
		sx, sy = start_pos
		for end_pos in path_func_map:
			ex, ey = end_pos
			path_func_map[start_pos][end_pos] = move_to_func_map[ey - sy][ex - sx]
	_navi_to_func_pos = path_func_map

# Initialize on import
update()

def move_to(goal_x, goal_y, current_x = get_pos_x(), current_y = get_pos_y()):
	_navi_to_func_pos[(current_x, current_y)][(goal_x, goal_y)]()

def move_to_pos(pos, current_pos):
	_navi_to_func_pos[current_pos][pos]()
