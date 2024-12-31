def scan_north_0_0():
	if move(North):
		WALL[0][1].remove(mnb_south)
		WALL[0][0].remove(mnb_north)
		PATH[0][1].add(bfs_south)
		PATH[0][0].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (0, 1)
		scan_east_0_1()
		scan_north_0_1()
		move(South)
def scan_east_0_0():
	if move(East):
		WALL[1][0].remove(mnb_west)
		WALL[0][0].remove(mnb_east)
		PATH[1][0].add(bfs_west)
		PATH[0][0].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (1, 0)
		scan_east_1_0()
		scan_north_1_0()
		move(West)
def scan_north_0_1():
	if move(North):
		WALL[0][2].remove(mnb_south)
		WALL[0][1].remove(mnb_north)
		PATH[0][2].add(bfs_south)
		PATH[0][1].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (0, 2)
		scan_east_0_2()
		scan_north_0_2()
		move(South)
def scan_east_0_1():
	if move(East):
		WALL[1][1].remove(mnb_west)
		WALL[0][1].remove(mnb_east)
		PATH[1][1].add(bfs_west)
		PATH[0][1].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (1, 1)
		scan_east_1_1()
		scan_south_1_1()
		scan_north_1_1()
		move(West)
def scan_south_0_1():
	if move(South):
		WALL[0][0].remove(mnb_north)
		WALL[0][1].remove(mnb_south)
		PATH[0][0].add(bfs_north)
		PATH[0][1].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (0, 0)
		scan_east_0_0()
		move(North)
def scan_north_0_2():
	if move(North):
		WALL[0][3].remove(mnb_south)
		WALL[0][2].remove(mnb_north)
		PATH[0][3].add(bfs_south)
		PATH[0][2].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (0, 3)
		scan_east_0_3()
		scan_north_0_3()
		move(South)
def scan_east_0_2():
	if move(East):
		WALL[1][2].remove(mnb_west)
		WALL[0][2].remove(mnb_east)
		PATH[1][2].add(bfs_west)
		PATH[0][2].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (1, 2)
		scan_east_1_2()
		scan_south_1_2()
		scan_north_1_2()
		move(West)
def scan_south_0_2():
	if move(South):
		WALL[0][1].remove(mnb_north)
		WALL[0][2].remove(mnb_south)
		PATH[0][1].add(bfs_north)
		PATH[0][2].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (0, 1)
		scan_east_0_1()
		scan_south_0_1()
		move(North)
def scan_north_0_3():
	if move(North):
		WALL[0][4].remove(mnb_south)
		WALL[0][3].remove(mnb_north)
		PATH[0][4].add(bfs_south)
		PATH[0][3].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (0, 4)
		scan_east_0_4()
		scan_north_0_4()
		move(South)
def scan_east_0_3():
	if move(East):
		WALL[1][3].remove(mnb_west)
		WALL[0][3].remove(mnb_east)
		PATH[1][3].add(bfs_west)
		PATH[0][3].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (1, 3)
		scan_east_1_3()
		scan_south_1_3()
		scan_north_1_3()
		move(West)
def scan_south_0_3():
	if move(South):
		WALL[0][2].remove(mnb_north)
		WALL[0][3].remove(mnb_south)
		PATH[0][2].add(bfs_north)
		PATH[0][3].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (0, 2)
		scan_east_0_2()
		scan_south_0_2()
		move(North)
def scan_north_0_4():
	if move(North):
		WALL[0][5].remove(mnb_south)
		WALL[0][4].remove(mnb_north)
		PATH[0][5].add(bfs_south)
		PATH[0][4].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (0, 5)
		scan_east_0_5()
		scan_north_0_5()
		move(South)
def scan_east_0_4():
	if move(East):
		WALL[1][4].remove(mnb_west)
		WALL[0][4].remove(mnb_east)
		PATH[1][4].add(bfs_west)
		PATH[0][4].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (1, 4)
		scan_east_1_4()
		scan_south_1_4()
		scan_north_1_4()
		move(West)
def scan_south_0_4():
	if move(South):
		WALL[0][3].remove(mnb_north)
		WALL[0][4].remove(mnb_south)
		PATH[0][3].add(bfs_north)
		PATH[0][4].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (0, 3)
		scan_east_0_3()
		scan_south_0_3()
		move(North)
def scan_north_0_5():
	if move(North):
		WALL[0][6].remove(mnb_south)
		WALL[0][5].remove(mnb_north)
		PATH[0][6].add(bfs_south)
		PATH[0][5].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (0, 6)
		scan_east_0_6()
		scan_north_0_6()
		move(South)
def scan_east_0_5():
	if move(East):
		WALL[1][5].remove(mnb_west)
		WALL[0][5].remove(mnb_east)
		PATH[1][5].add(bfs_west)
		PATH[0][5].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (1, 5)
		scan_east_1_5()
		scan_south_1_5()
		scan_north_1_5()
		move(West)
def scan_south_0_5():
	if move(South):
		WALL[0][4].remove(mnb_north)
		WALL[0][5].remove(mnb_south)
		PATH[0][4].add(bfs_north)
		PATH[0][5].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (0, 4)
		scan_east_0_4()
		scan_south_0_4()
		move(North)
def scan_north_0_6():
	if move(North):
		WALL[0][7].remove(mnb_south)
		WALL[0][6].remove(mnb_north)
		PATH[0][7].add(bfs_south)
		PATH[0][6].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (0, 7)
		scan_east_0_7()
		scan_north_0_7()
		move(South)
def scan_east_0_6():
	if move(East):
		WALL[1][6].remove(mnb_west)
		WALL[0][6].remove(mnb_east)
		PATH[1][6].add(bfs_west)
		PATH[0][6].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (1, 6)
		scan_east_1_6()
		scan_south_1_6()
		scan_north_1_6()
		move(West)
def scan_south_0_6():
	if move(South):
		WALL[0][5].remove(mnb_north)
		WALL[0][6].remove(mnb_south)
		PATH[0][5].add(bfs_north)
		PATH[0][6].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (0, 5)
		scan_east_0_5()
		scan_south_0_5()
		move(North)
def scan_north_0_7():
	if move(North):
		WALL[0][8].remove(mnb_south)
		WALL[0][7].remove(mnb_north)
		PATH[0][8].add(bfs_south)
		PATH[0][7].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (0, 8)
		scan_east_0_8()
		scan_north_0_8()
		move(South)
def scan_east_0_7():
	if move(East):
		WALL[1][7].remove(mnb_west)
		WALL[0][7].remove(mnb_east)
		PATH[1][7].add(bfs_west)
		PATH[0][7].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (1, 7)
		scan_east_1_7()
		scan_south_1_7()
		scan_north_1_7()
		move(West)
def scan_south_0_7():
	if move(South):
		WALL[0][6].remove(mnb_north)
		WALL[0][7].remove(mnb_south)
		PATH[0][6].add(bfs_north)
		PATH[0][7].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (0, 6)
		scan_east_0_6()
		scan_south_0_6()
		move(North)
def scan_north_0_8():
	if move(North):
		WALL[0][9].remove(mnb_south)
		WALL[0][8].remove(mnb_north)
		PATH[0][9].add(bfs_south)
		PATH[0][8].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (0, 9)
		scan_east_0_9()
		move(South)
def scan_east_0_8():
	if move(East):
		WALL[1][8].remove(mnb_west)
		WALL[0][8].remove(mnb_east)
		PATH[1][8].add(bfs_west)
		PATH[0][8].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (1, 8)
		scan_east_1_8()
		scan_south_1_8()
		scan_north_1_8()
		move(West)
def scan_south_0_8():
	if move(South):
		WALL[0][7].remove(mnb_north)
		WALL[0][8].remove(mnb_south)
		PATH[0][7].add(bfs_north)
		PATH[0][8].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (0, 7)
		scan_east_0_7()
		scan_south_0_7()
		move(North)
def scan_east_0_9():
	if move(East):
		WALL[1][9].remove(mnb_west)
		WALL[0][9].remove(mnb_east)
		PATH[1][9].add(bfs_west)
		PATH[0][9].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (1, 9)
		scan_east_1_9()
		scan_south_1_9()
		move(West)
def scan_south_0_9():
	if move(South):
		WALL[0][8].remove(mnb_north)
		WALL[0][9].remove(mnb_south)
		PATH[0][8].add(bfs_north)
		PATH[0][9].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (0, 8)
		scan_east_0_8()
		scan_south_0_8()
		move(North)
def scan_north_1_0():
	if move(North):
		WALL[1][1].remove(mnb_south)
		WALL[1][0].remove(mnb_north)
		PATH[1][1].add(bfs_south)
		PATH[1][0].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (1, 1)
		scan_west_1_1()
		scan_east_1_1()
		scan_north_1_1()
		move(South)
def scan_east_1_0():
	if move(East):
		WALL[2][0].remove(mnb_west)
		WALL[1][0].remove(mnb_east)
		PATH[2][0].add(bfs_west)
		PATH[1][0].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (2, 0)
		scan_east_2_0()
		scan_north_2_0()
		move(West)
def scan_west_1_0():
	if move(West):
		WALL[0][0].remove(mnb_east)
		WALL[1][0].remove(mnb_west)
		PATH[0][0].add(bfs_east)
		PATH[1][0].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (0, 0)
		scan_north_0_0()
		move(East)
def scan_north_1_1():
	if move(North):
		WALL[1][2].remove(mnb_south)
		WALL[1][1].remove(mnb_north)
		PATH[1][2].add(bfs_south)
		PATH[1][1].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (1, 2)
		scan_west_1_2()
		scan_east_1_2()
		scan_north_1_2()
		move(South)
def scan_east_1_1():
	if move(East):
		WALL[2][1].remove(mnb_west)
		WALL[1][1].remove(mnb_east)
		PATH[2][1].add(bfs_west)
		PATH[1][1].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (2, 1)
		scan_east_2_1()
		scan_south_2_1()
		scan_north_2_1()
		move(West)
def scan_south_1_1():
	if move(South):
		WALL[1][0].remove(mnb_north)
		WALL[1][1].remove(mnb_south)
		PATH[1][0].add(bfs_north)
		PATH[1][1].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (1, 0)
		scan_west_1_0()
		scan_east_1_0()
		move(North)
def scan_west_1_1():
	if move(West):
		WALL[0][1].remove(mnb_east)
		WALL[1][1].remove(mnb_west)
		PATH[0][1].add(bfs_east)
		PATH[1][1].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (0, 1)
		scan_south_0_1()
		scan_north_0_1()
		move(East)
def scan_north_1_2():
	if move(North):
		WALL[1][3].remove(mnb_south)
		WALL[1][2].remove(mnb_north)
		PATH[1][3].add(bfs_south)
		PATH[1][2].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (1, 3)
		scan_west_1_3()
		scan_east_1_3()
		scan_north_1_3()
		move(South)
def scan_east_1_2():
	if move(East):
		WALL[2][2].remove(mnb_west)
		WALL[1][2].remove(mnb_east)
		PATH[2][2].add(bfs_west)
		PATH[1][2].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (2, 2)
		scan_east_2_2()
		scan_south_2_2()
		scan_north_2_2()
		move(West)
def scan_south_1_2():
	if move(South):
		WALL[1][1].remove(mnb_north)
		WALL[1][2].remove(mnb_south)
		PATH[1][1].add(bfs_north)
		PATH[1][2].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (1, 1)
		scan_west_1_1()
		scan_east_1_1()
		scan_south_1_1()
		move(North)
def scan_west_1_2():
	if move(West):
		WALL[0][2].remove(mnb_east)
		WALL[1][2].remove(mnb_west)
		PATH[0][2].add(bfs_east)
		PATH[1][2].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (0, 2)
		scan_south_0_2()
		scan_north_0_2()
		move(East)
def scan_north_1_3():
	if move(North):
		WALL[1][4].remove(mnb_south)
		WALL[1][3].remove(mnb_north)
		PATH[1][4].add(bfs_south)
		PATH[1][3].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (1, 4)
		scan_west_1_4()
		scan_east_1_4()
		scan_north_1_4()
		move(South)
def scan_east_1_3():
	if move(East):
		WALL[2][3].remove(mnb_west)
		WALL[1][3].remove(mnb_east)
		PATH[2][3].add(bfs_west)
		PATH[1][3].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (2, 3)
		scan_east_2_3()
		scan_south_2_3()
		scan_north_2_3()
		move(West)
def scan_south_1_3():
	if move(South):
		WALL[1][2].remove(mnb_north)
		WALL[1][3].remove(mnb_south)
		PATH[1][2].add(bfs_north)
		PATH[1][3].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (1, 2)
		scan_west_1_2()
		scan_east_1_2()
		scan_south_1_2()
		move(North)
def scan_west_1_3():
	if move(West):
		WALL[0][3].remove(mnb_east)
		WALL[1][3].remove(mnb_west)
		PATH[0][3].add(bfs_east)
		PATH[1][3].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (0, 3)
		scan_south_0_3()
		scan_north_0_3()
		move(East)
def scan_north_1_4():
	if move(North):
		WALL[1][5].remove(mnb_south)
		WALL[1][4].remove(mnb_north)
		PATH[1][5].add(bfs_south)
		PATH[1][4].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (1, 5)
		scan_west_1_5()
		scan_east_1_5()
		scan_north_1_5()
		move(South)
def scan_east_1_4():
	if move(East):
		WALL[2][4].remove(mnb_west)
		WALL[1][4].remove(mnb_east)
		PATH[2][4].add(bfs_west)
		PATH[1][4].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (2, 4)
		scan_east_2_4()
		scan_south_2_4()
		scan_north_2_4()
		move(West)
def scan_south_1_4():
	if move(South):
		WALL[1][3].remove(mnb_north)
		WALL[1][4].remove(mnb_south)
		PATH[1][3].add(bfs_north)
		PATH[1][4].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (1, 3)
		scan_west_1_3()
		scan_east_1_3()
		scan_south_1_3()
		move(North)
def scan_west_1_4():
	if move(West):
		WALL[0][4].remove(mnb_east)
		WALL[1][4].remove(mnb_west)
		PATH[0][4].add(bfs_east)
		PATH[1][4].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (0, 4)
		scan_south_0_4()
		scan_north_0_4()
		move(East)
def scan_north_1_5():
	if move(North):
		WALL[1][6].remove(mnb_south)
		WALL[1][5].remove(mnb_north)
		PATH[1][6].add(bfs_south)
		PATH[1][5].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (1, 6)
		scan_west_1_6()
		scan_east_1_6()
		scan_north_1_6()
		move(South)
def scan_east_1_5():
	if move(East):
		WALL[2][5].remove(mnb_west)
		WALL[1][5].remove(mnb_east)
		PATH[2][5].add(bfs_west)
		PATH[1][5].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (2, 5)
		scan_east_2_5()
		scan_south_2_5()
		scan_north_2_5()
		move(West)
def scan_south_1_5():
	if move(South):
		WALL[1][4].remove(mnb_north)
		WALL[1][5].remove(mnb_south)
		PATH[1][4].add(bfs_north)
		PATH[1][5].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (1, 4)
		scan_west_1_4()
		scan_east_1_4()
		scan_south_1_4()
		move(North)
def scan_west_1_5():
	if move(West):
		WALL[0][5].remove(mnb_east)
		WALL[1][5].remove(mnb_west)
		PATH[0][5].add(bfs_east)
		PATH[1][5].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (0, 5)
		scan_south_0_5()
		scan_north_0_5()
		move(East)
def scan_north_1_6():
	if move(North):
		WALL[1][7].remove(mnb_south)
		WALL[1][6].remove(mnb_north)
		PATH[1][7].add(bfs_south)
		PATH[1][6].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (1, 7)
		scan_west_1_7()
		scan_east_1_7()
		scan_north_1_7()
		move(South)
def scan_east_1_6():
	if move(East):
		WALL[2][6].remove(mnb_west)
		WALL[1][6].remove(mnb_east)
		PATH[2][6].add(bfs_west)
		PATH[1][6].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (2, 6)
		scan_east_2_6()
		scan_south_2_6()
		scan_north_2_6()
		move(West)
def scan_south_1_6():
	if move(South):
		WALL[1][5].remove(mnb_north)
		WALL[1][6].remove(mnb_south)
		PATH[1][5].add(bfs_north)
		PATH[1][6].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (1, 5)
		scan_west_1_5()
		scan_east_1_5()
		scan_south_1_5()
		move(North)
def scan_west_1_6():
	if move(West):
		WALL[0][6].remove(mnb_east)
		WALL[1][6].remove(mnb_west)
		PATH[0][6].add(bfs_east)
		PATH[1][6].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (0, 6)
		scan_south_0_6()
		scan_north_0_6()
		move(East)
def scan_north_1_7():
	if move(North):
		WALL[1][8].remove(mnb_south)
		WALL[1][7].remove(mnb_north)
		PATH[1][8].add(bfs_south)
		PATH[1][7].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (1, 8)
		scan_west_1_8()
		scan_east_1_8()
		scan_north_1_8()
		move(South)
def scan_east_1_7():
	if move(East):
		WALL[2][7].remove(mnb_west)
		WALL[1][7].remove(mnb_east)
		PATH[2][7].add(bfs_west)
		PATH[1][7].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (2, 7)
		scan_east_2_7()
		scan_south_2_7()
		scan_north_2_7()
		move(West)
def scan_south_1_7():
	if move(South):
		WALL[1][6].remove(mnb_north)
		WALL[1][7].remove(mnb_south)
		PATH[1][6].add(bfs_north)
		PATH[1][7].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (1, 6)
		scan_west_1_6()
		scan_east_1_6()
		scan_south_1_6()
		move(North)
def scan_west_1_7():
	if move(West):
		WALL[0][7].remove(mnb_east)
		WALL[1][7].remove(mnb_west)
		PATH[0][7].add(bfs_east)
		PATH[1][7].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (0, 7)
		scan_south_0_7()
		scan_north_0_7()
		move(East)
def scan_north_1_8():
	if move(North):
		WALL[1][9].remove(mnb_south)
		WALL[1][8].remove(mnb_north)
		PATH[1][9].add(bfs_south)
		PATH[1][8].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (1, 9)
		scan_west_1_9()
		scan_east_1_9()
		move(South)
def scan_east_1_8():
	if move(East):
		WALL[2][8].remove(mnb_west)
		WALL[1][8].remove(mnb_east)
		PATH[2][8].add(bfs_west)
		PATH[1][8].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (2, 8)
		scan_east_2_8()
		scan_south_2_8()
		scan_north_2_8()
		move(West)
def scan_south_1_8():
	if move(South):
		WALL[1][7].remove(mnb_north)
		WALL[1][8].remove(mnb_south)
		PATH[1][7].add(bfs_north)
		PATH[1][8].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (1, 7)
		scan_west_1_7()
		scan_east_1_7()
		scan_south_1_7()
		move(North)
def scan_west_1_8():
	if move(West):
		WALL[0][8].remove(mnb_east)
		WALL[1][8].remove(mnb_west)
		PATH[0][8].add(bfs_east)
		PATH[1][8].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (0, 8)
		scan_south_0_8()
		scan_north_0_8()
		move(East)
def scan_east_1_9():
	if move(East):
		WALL[2][9].remove(mnb_west)
		WALL[1][9].remove(mnb_east)
		PATH[2][9].add(bfs_west)
		PATH[1][9].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (2, 9)
		scan_east_2_9()
		scan_south_2_9()
		move(West)
def scan_south_1_9():
	if move(South):
		WALL[1][8].remove(mnb_north)
		WALL[1][9].remove(mnb_south)
		PATH[1][8].add(bfs_north)
		PATH[1][9].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (1, 8)
		scan_west_1_8()
		scan_east_1_8()
		scan_south_1_8()
		move(North)
def scan_west_1_9():
	if move(West):
		WALL[0][9].remove(mnb_east)
		WALL[1][9].remove(mnb_west)
		PATH[0][9].add(bfs_east)
		PATH[1][9].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (0, 9)
		scan_south_0_9()
		move(East)
def scan_north_2_0():
	if move(North):
		WALL[2][1].remove(mnb_south)
		WALL[2][0].remove(mnb_north)
		PATH[2][1].add(bfs_south)
		PATH[2][0].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (2, 1)
		scan_west_2_1()
		scan_east_2_1()
		scan_north_2_1()
		move(South)
def scan_east_2_0():
	if move(East):
		WALL[3][0].remove(mnb_west)
		WALL[2][0].remove(mnb_east)
		PATH[3][0].add(bfs_west)
		PATH[2][0].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (3, 0)
		scan_east_3_0()
		scan_north_3_0()
		move(West)
def scan_west_2_0():
	if move(West):
		WALL[1][0].remove(mnb_east)
		WALL[2][0].remove(mnb_west)
		PATH[1][0].add(bfs_east)
		PATH[2][0].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (1, 0)
		scan_west_1_0()
		scan_north_1_0()
		move(East)
def scan_north_2_1():
	if move(North):
		WALL[2][2].remove(mnb_south)
		WALL[2][1].remove(mnb_north)
		PATH[2][2].add(bfs_south)
		PATH[2][1].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (2, 2)
		scan_west_2_2()
		scan_east_2_2()
		scan_north_2_2()
		move(South)
def scan_east_2_1():
	if move(East):
		WALL[3][1].remove(mnb_west)
		WALL[2][1].remove(mnb_east)
		PATH[3][1].add(bfs_west)
		PATH[2][1].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (3, 1)
		scan_east_3_1()
		scan_south_3_1()
		scan_north_3_1()
		move(West)
def scan_south_2_1():
	if move(South):
		WALL[2][0].remove(mnb_north)
		WALL[2][1].remove(mnb_south)
		PATH[2][0].add(bfs_north)
		PATH[2][1].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (2, 0)
		scan_west_2_0()
		scan_east_2_0()
		move(North)
def scan_west_2_1():
	if move(West):
		WALL[1][1].remove(mnb_east)
		WALL[2][1].remove(mnb_west)
		PATH[1][1].add(bfs_east)
		PATH[2][1].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (1, 1)
		scan_west_1_1()
		scan_south_1_1()
		scan_north_1_1()
		move(East)
def scan_north_2_2():
	if move(North):
		WALL[2][3].remove(mnb_south)
		WALL[2][2].remove(mnb_north)
		PATH[2][3].add(bfs_south)
		PATH[2][2].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (2, 3)
		scan_west_2_3()
		scan_east_2_3()
		scan_north_2_3()
		move(South)
def scan_east_2_2():
	if move(East):
		WALL[3][2].remove(mnb_west)
		WALL[2][2].remove(mnb_east)
		PATH[3][2].add(bfs_west)
		PATH[2][2].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (3, 2)
		scan_east_3_2()
		scan_south_3_2()
		scan_north_3_2()
		move(West)
def scan_south_2_2():
	if move(South):
		WALL[2][1].remove(mnb_north)
		WALL[2][2].remove(mnb_south)
		PATH[2][1].add(bfs_north)
		PATH[2][2].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (2, 1)
		scan_west_2_1()
		scan_east_2_1()
		scan_south_2_1()
		move(North)
def scan_west_2_2():
	if move(West):
		WALL[1][2].remove(mnb_east)
		WALL[2][2].remove(mnb_west)
		PATH[1][2].add(bfs_east)
		PATH[2][2].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (1, 2)
		scan_west_1_2()
		scan_south_1_2()
		scan_north_1_2()
		move(East)
def scan_north_2_3():
	if move(North):
		WALL[2][4].remove(mnb_south)
		WALL[2][3].remove(mnb_north)
		PATH[2][4].add(bfs_south)
		PATH[2][3].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (2, 4)
		scan_west_2_4()
		scan_east_2_4()
		scan_north_2_4()
		move(South)
def scan_east_2_3():
	if move(East):
		WALL[3][3].remove(mnb_west)
		WALL[2][3].remove(mnb_east)
		PATH[3][3].add(bfs_west)
		PATH[2][3].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (3, 3)
		scan_east_3_3()
		scan_south_3_3()
		scan_north_3_3()
		move(West)
def scan_south_2_3():
	if move(South):
		WALL[2][2].remove(mnb_north)
		WALL[2][3].remove(mnb_south)
		PATH[2][2].add(bfs_north)
		PATH[2][3].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (2, 2)
		scan_west_2_2()
		scan_east_2_2()
		scan_south_2_2()
		move(North)
def scan_west_2_3():
	if move(West):
		WALL[1][3].remove(mnb_east)
		WALL[2][3].remove(mnb_west)
		PATH[1][3].add(bfs_east)
		PATH[2][3].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (1, 3)
		scan_west_1_3()
		scan_south_1_3()
		scan_north_1_3()
		move(East)
def scan_north_2_4():
	if move(North):
		WALL[2][5].remove(mnb_south)
		WALL[2][4].remove(mnb_north)
		PATH[2][5].add(bfs_south)
		PATH[2][4].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (2, 5)
		scan_west_2_5()
		scan_east_2_5()
		scan_north_2_5()
		move(South)
def scan_east_2_4():
	if move(East):
		WALL[3][4].remove(mnb_west)
		WALL[2][4].remove(mnb_east)
		PATH[3][4].add(bfs_west)
		PATH[2][4].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (3, 4)
		scan_east_3_4()
		scan_south_3_4()
		scan_north_3_4()
		move(West)
def scan_south_2_4():
	if move(South):
		WALL[2][3].remove(mnb_north)
		WALL[2][4].remove(mnb_south)
		PATH[2][3].add(bfs_north)
		PATH[2][4].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (2, 3)
		scan_west_2_3()
		scan_east_2_3()
		scan_south_2_3()
		move(North)
def scan_west_2_4():
	if move(West):
		WALL[1][4].remove(mnb_east)
		WALL[2][4].remove(mnb_west)
		PATH[1][4].add(bfs_east)
		PATH[2][4].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (1, 4)
		scan_west_1_4()
		scan_south_1_4()
		scan_north_1_4()
		move(East)
def scan_north_2_5():
	if move(North):
		WALL[2][6].remove(mnb_south)
		WALL[2][5].remove(mnb_north)
		PATH[2][6].add(bfs_south)
		PATH[2][5].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (2, 6)
		scan_west_2_6()
		scan_east_2_6()
		scan_north_2_6()
		move(South)
def scan_east_2_5():
	if move(East):
		WALL[3][5].remove(mnb_west)
		WALL[2][5].remove(mnb_east)
		PATH[3][5].add(bfs_west)
		PATH[2][5].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (3, 5)
		scan_east_3_5()
		scan_south_3_5()
		scan_north_3_5()
		move(West)
def scan_south_2_5():
	if move(South):
		WALL[2][4].remove(mnb_north)
		WALL[2][5].remove(mnb_south)
		PATH[2][4].add(bfs_north)
		PATH[2][5].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (2, 4)
		scan_west_2_4()
		scan_east_2_4()
		scan_south_2_4()
		move(North)
def scan_west_2_5():
	if move(West):
		WALL[1][5].remove(mnb_east)
		WALL[2][5].remove(mnb_west)
		PATH[1][5].add(bfs_east)
		PATH[2][5].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (1, 5)
		scan_west_1_5()
		scan_south_1_5()
		scan_north_1_5()
		move(East)
def scan_north_2_6():
	if move(North):
		WALL[2][7].remove(mnb_south)
		WALL[2][6].remove(mnb_north)
		PATH[2][7].add(bfs_south)
		PATH[2][6].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (2, 7)
		scan_west_2_7()
		scan_east_2_7()
		scan_north_2_7()
		move(South)
def scan_east_2_6():
	if move(East):
		WALL[3][6].remove(mnb_west)
		WALL[2][6].remove(mnb_east)
		PATH[3][6].add(bfs_west)
		PATH[2][6].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (3, 6)
		scan_east_3_6()
		scan_south_3_6()
		scan_north_3_6()
		move(West)
def scan_south_2_6():
	if move(South):
		WALL[2][5].remove(mnb_north)
		WALL[2][6].remove(mnb_south)
		PATH[2][5].add(bfs_north)
		PATH[2][6].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (2, 5)
		scan_west_2_5()
		scan_east_2_5()
		scan_south_2_5()
		move(North)
def scan_west_2_6():
	if move(West):
		WALL[1][6].remove(mnb_east)
		WALL[2][6].remove(mnb_west)
		PATH[1][6].add(bfs_east)
		PATH[2][6].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (1, 6)
		scan_west_1_6()
		scan_south_1_6()
		scan_north_1_6()
		move(East)
def scan_north_2_7():
	if move(North):
		WALL[2][8].remove(mnb_south)
		WALL[2][7].remove(mnb_north)
		PATH[2][8].add(bfs_south)
		PATH[2][7].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (2, 8)
		scan_west_2_8()
		scan_east_2_8()
		scan_north_2_8()
		move(South)
def scan_east_2_7():
	if move(East):
		WALL[3][7].remove(mnb_west)
		WALL[2][7].remove(mnb_east)
		PATH[3][7].add(bfs_west)
		PATH[2][7].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (3, 7)
		scan_east_3_7()
		scan_south_3_7()
		scan_north_3_7()
		move(West)
def scan_south_2_7():
	if move(South):
		WALL[2][6].remove(mnb_north)
		WALL[2][7].remove(mnb_south)
		PATH[2][6].add(bfs_north)
		PATH[2][7].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (2, 6)
		scan_west_2_6()
		scan_east_2_6()
		scan_south_2_6()
		move(North)
def scan_west_2_7():
	if move(West):
		WALL[1][7].remove(mnb_east)
		WALL[2][7].remove(mnb_west)
		PATH[1][7].add(bfs_east)
		PATH[2][7].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (1, 7)
		scan_west_1_7()
		scan_south_1_7()
		scan_north_1_7()
		move(East)
def scan_north_2_8():
	if move(North):
		WALL[2][9].remove(mnb_south)
		WALL[2][8].remove(mnb_north)
		PATH[2][9].add(bfs_south)
		PATH[2][8].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (2, 9)
		scan_west_2_9()
		scan_east_2_9()
		move(South)
def scan_east_2_8():
	if move(East):
		WALL[3][8].remove(mnb_west)
		WALL[2][8].remove(mnb_east)
		PATH[3][8].add(bfs_west)
		PATH[2][8].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (3, 8)
		scan_east_3_8()
		scan_south_3_8()
		scan_north_3_8()
		move(West)
def scan_south_2_8():
	if move(South):
		WALL[2][7].remove(mnb_north)
		WALL[2][8].remove(mnb_south)
		PATH[2][7].add(bfs_north)
		PATH[2][8].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (2, 7)
		scan_west_2_7()
		scan_east_2_7()
		scan_south_2_7()
		move(North)
def scan_west_2_8():
	if move(West):
		WALL[1][8].remove(mnb_east)
		WALL[2][8].remove(mnb_west)
		PATH[1][8].add(bfs_east)
		PATH[2][8].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (1, 8)
		scan_west_1_8()
		scan_south_1_8()
		scan_north_1_8()
		move(East)
def scan_east_2_9():
	if move(East):
		WALL[3][9].remove(mnb_west)
		WALL[2][9].remove(mnb_east)
		PATH[3][9].add(bfs_west)
		PATH[2][9].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (3, 9)
		scan_east_3_9()
		scan_south_3_9()
		move(West)
def scan_south_2_9():
	if move(South):
		WALL[2][8].remove(mnb_north)
		WALL[2][9].remove(mnb_south)
		PATH[2][8].add(bfs_north)
		PATH[2][9].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (2, 8)
		scan_west_2_8()
		scan_east_2_8()
		scan_south_2_8()
		move(North)
def scan_west_2_9():
	if move(West):
		WALL[1][9].remove(mnb_east)
		WALL[2][9].remove(mnb_west)
		PATH[1][9].add(bfs_east)
		PATH[2][9].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (1, 9)
		scan_west_1_9()
		scan_south_1_9()
		move(East)
def scan_north_3_0():
	if move(North):
		WALL[3][1].remove(mnb_south)
		WALL[3][0].remove(mnb_north)
		PATH[3][1].add(bfs_south)
		PATH[3][0].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (3, 1)
		scan_west_3_1()
		scan_east_3_1()
		scan_north_3_1()
		move(South)
def scan_east_3_0():
	if move(East):
		WALL[4][0].remove(mnb_west)
		WALL[3][0].remove(mnb_east)
		PATH[4][0].add(bfs_west)
		PATH[3][0].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (4, 0)
		scan_east_4_0()
		scan_north_4_0()
		move(West)
def scan_west_3_0():
	if move(West):
		WALL[2][0].remove(mnb_east)
		WALL[3][0].remove(mnb_west)
		PATH[2][0].add(bfs_east)
		PATH[3][0].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (2, 0)
		scan_west_2_0()
		scan_north_2_0()
		move(East)
def scan_north_3_1():
	if move(North):
		WALL[3][2].remove(mnb_south)
		WALL[3][1].remove(mnb_north)
		PATH[3][2].add(bfs_south)
		PATH[3][1].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (3, 2)
		scan_west_3_2()
		scan_east_3_2()
		scan_north_3_2()
		move(South)
def scan_east_3_1():
	if move(East):
		WALL[4][1].remove(mnb_west)
		WALL[3][1].remove(mnb_east)
		PATH[4][1].add(bfs_west)
		PATH[3][1].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (4, 1)
		scan_east_4_1()
		scan_south_4_1()
		scan_north_4_1()
		move(West)
def scan_south_3_1():
	if move(South):
		WALL[3][0].remove(mnb_north)
		WALL[3][1].remove(mnb_south)
		PATH[3][0].add(bfs_north)
		PATH[3][1].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (3, 0)
		scan_west_3_0()
		scan_east_3_0()
		move(North)
def scan_west_3_1():
	if move(West):
		WALL[2][1].remove(mnb_east)
		WALL[3][1].remove(mnb_west)
		PATH[2][1].add(bfs_east)
		PATH[3][1].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (2, 1)
		scan_west_2_1()
		scan_south_2_1()
		scan_north_2_1()
		move(East)
def scan_north_3_2():
	if move(North):
		WALL[3][3].remove(mnb_south)
		WALL[3][2].remove(mnb_north)
		PATH[3][3].add(bfs_south)
		PATH[3][2].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (3, 3)
		scan_west_3_3()
		scan_east_3_3()
		scan_north_3_3()
		move(South)
def scan_east_3_2():
	if move(East):
		WALL[4][2].remove(mnb_west)
		WALL[3][2].remove(mnb_east)
		PATH[4][2].add(bfs_west)
		PATH[3][2].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (4, 2)
		scan_east_4_2()
		scan_south_4_2()
		scan_north_4_2()
		move(West)
def scan_south_3_2():
	if move(South):
		WALL[3][1].remove(mnb_north)
		WALL[3][2].remove(mnb_south)
		PATH[3][1].add(bfs_north)
		PATH[3][2].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (3, 1)
		scan_west_3_1()
		scan_east_3_1()
		scan_south_3_1()
		move(North)
def scan_west_3_2():
	if move(West):
		WALL[2][2].remove(mnb_east)
		WALL[3][2].remove(mnb_west)
		PATH[2][2].add(bfs_east)
		PATH[3][2].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (2, 2)
		scan_west_2_2()
		scan_south_2_2()
		scan_north_2_2()
		move(East)
def scan_north_3_3():
	if move(North):
		WALL[3][4].remove(mnb_south)
		WALL[3][3].remove(mnb_north)
		PATH[3][4].add(bfs_south)
		PATH[3][3].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (3, 4)
		scan_west_3_4()
		scan_east_3_4()
		scan_north_3_4()
		move(South)
def scan_east_3_3():
	if move(East):
		WALL[4][3].remove(mnb_west)
		WALL[3][3].remove(mnb_east)
		PATH[4][3].add(bfs_west)
		PATH[3][3].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (4, 3)
		scan_east_4_3()
		scan_south_4_3()
		scan_north_4_3()
		move(West)
def scan_south_3_3():
	if move(South):
		WALL[3][2].remove(mnb_north)
		WALL[3][3].remove(mnb_south)
		PATH[3][2].add(bfs_north)
		PATH[3][3].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (3, 2)
		scan_west_3_2()
		scan_east_3_2()
		scan_south_3_2()
		move(North)
def scan_west_3_3():
	if move(West):
		WALL[2][3].remove(mnb_east)
		WALL[3][3].remove(mnb_west)
		PATH[2][3].add(bfs_east)
		PATH[3][3].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (2, 3)
		scan_west_2_3()
		scan_south_2_3()
		scan_north_2_3()
		move(East)
def scan_north_3_4():
	if move(North):
		WALL[3][5].remove(mnb_south)
		WALL[3][4].remove(mnb_north)
		PATH[3][5].add(bfs_south)
		PATH[3][4].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (3, 5)
		scan_west_3_5()
		scan_east_3_5()
		scan_north_3_5()
		move(South)
def scan_east_3_4():
	if move(East):
		WALL[4][4].remove(mnb_west)
		WALL[3][4].remove(mnb_east)
		PATH[4][4].add(bfs_west)
		PATH[3][4].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (4, 4)
		scan_east_4_4()
		scan_south_4_4()
		scan_north_4_4()
		move(West)
def scan_south_3_4():
	if move(South):
		WALL[3][3].remove(mnb_north)
		WALL[3][4].remove(mnb_south)
		PATH[3][3].add(bfs_north)
		PATH[3][4].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (3, 3)
		scan_west_3_3()
		scan_east_3_3()
		scan_south_3_3()
		move(North)
def scan_west_3_4():
	if move(West):
		WALL[2][4].remove(mnb_east)
		WALL[3][4].remove(mnb_west)
		PATH[2][4].add(bfs_east)
		PATH[3][4].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (2, 4)
		scan_west_2_4()
		scan_south_2_4()
		scan_north_2_4()
		move(East)
def scan_north_3_5():
	if move(North):
		WALL[3][6].remove(mnb_south)
		WALL[3][5].remove(mnb_north)
		PATH[3][6].add(bfs_south)
		PATH[3][5].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (3, 6)
		scan_west_3_6()
		scan_east_3_6()
		scan_north_3_6()
		move(South)
def scan_east_3_5():
	if move(East):
		WALL[4][5].remove(mnb_west)
		WALL[3][5].remove(mnb_east)
		PATH[4][5].add(bfs_west)
		PATH[3][5].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (4, 5)
		scan_east_4_5()
		scan_south_4_5()
		scan_north_4_5()
		move(West)
def scan_south_3_5():
	if move(South):
		WALL[3][4].remove(mnb_north)
		WALL[3][5].remove(mnb_south)
		PATH[3][4].add(bfs_north)
		PATH[3][5].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (3, 4)
		scan_west_3_4()
		scan_east_3_4()
		scan_south_3_4()
		move(North)
def scan_west_3_5():
	if move(West):
		WALL[2][5].remove(mnb_east)
		WALL[3][5].remove(mnb_west)
		PATH[2][5].add(bfs_east)
		PATH[3][5].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (2, 5)
		scan_west_2_5()
		scan_south_2_5()
		scan_north_2_5()
		move(East)
def scan_north_3_6():
	if move(North):
		WALL[3][7].remove(mnb_south)
		WALL[3][6].remove(mnb_north)
		PATH[3][7].add(bfs_south)
		PATH[3][6].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (3, 7)
		scan_west_3_7()
		scan_east_3_7()
		scan_north_3_7()
		move(South)
def scan_east_3_6():
	if move(East):
		WALL[4][6].remove(mnb_west)
		WALL[3][6].remove(mnb_east)
		PATH[4][6].add(bfs_west)
		PATH[3][6].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (4, 6)
		scan_east_4_6()
		scan_south_4_6()
		scan_north_4_6()
		move(West)
def scan_south_3_6():
	if move(South):
		WALL[3][5].remove(mnb_north)
		WALL[3][6].remove(mnb_south)
		PATH[3][5].add(bfs_north)
		PATH[3][6].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (3, 5)
		scan_west_3_5()
		scan_east_3_5()
		scan_south_3_5()
		move(North)
def scan_west_3_6():
	if move(West):
		WALL[2][6].remove(mnb_east)
		WALL[3][6].remove(mnb_west)
		PATH[2][6].add(bfs_east)
		PATH[3][6].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (2, 6)
		scan_west_2_6()
		scan_south_2_6()
		scan_north_2_6()
		move(East)
def scan_north_3_7():
	if move(North):
		WALL[3][8].remove(mnb_south)
		WALL[3][7].remove(mnb_north)
		PATH[3][8].add(bfs_south)
		PATH[3][7].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (3, 8)
		scan_west_3_8()
		scan_east_3_8()
		scan_north_3_8()
		move(South)
def scan_east_3_7():
	if move(East):
		WALL[4][7].remove(mnb_west)
		WALL[3][7].remove(mnb_east)
		PATH[4][7].add(bfs_west)
		PATH[3][7].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (4, 7)
		scan_east_4_7()
		scan_south_4_7()
		scan_north_4_7()
		move(West)
def scan_south_3_7():
	if move(South):
		WALL[3][6].remove(mnb_north)
		WALL[3][7].remove(mnb_south)
		PATH[3][6].add(bfs_north)
		PATH[3][7].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (3, 6)
		scan_west_3_6()
		scan_east_3_6()
		scan_south_3_6()
		move(North)
def scan_west_3_7():
	if move(West):
		WALL[2][7].remove(mnb_east)
		WALL[3][7].remove(mnb_west)
		PATH[2][7].add(bfs_east)
		PATH[3][7].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (2, 7)
		scan_west_2_7()
		scan_south_2_7()
		scan_north_2_7()
		move(East)
def scan_north_3_8():
	if move(North):
		WALL[3][9].remove(mnb_south)
		WALL[3][8].remove(mnb_north)
		PATH[3][9].add(bfs_south)
		PATH[3][8].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (3, 9)
		scan_west_3_9()
		scan_east_3_9()
		move(South)
def scan_east_3_8():
	if move(East):
		WALL[4][8].remove(mnb_west)
		WALL[3][8].remove(mnb_east)
		PATH[4][8].add(bfs_west)
		PATH[3][8].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (4, 8)
		scan_east_4_8()
		scan_south_4_8()
		scan_north_4_8()
		move(West)
def scan_south_3_8():
	if move(South):
		WALL[3][7].remove(mnb_north)
		WALL[3][8].remove(mnb_south)
		PATH[3][7].add(bfs_north)
		PATH[3][8].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (3, 7)
		scan_west_3_7()
		scan_east_3_7()
		scan_south_3_7()
		move(North)
def scan_west_3_8():
	if move(West):
		WALL[2][8].remove(mnb_east)
		WALL[3][8].remove(mnb_west)
		PATH[2][8].add(bfs_east)
		PATH[3][8].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (2, 8)
		scan_west_2_8()
		scan_south_2_8()
		scan_north_2_8()
		move(East)
def scan_east_3_9():
	if move(East):
		WALL[4][9].remove(mnb_west)
		WALL[3][9].remove(mnb_east)
		PATH[4][9].add(bfs_west)
		PATH[3][9].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (4, 9)
		scan_east_4_9()
		scan_south_4_9()
		move(West)
def scan_south_3_9():
	if move(South):
		WALL[3][8].remove(mnb_north)
		WALL[3][9].remove(mnb_south)
		PATH[3][8].add(bfs_north)
		PATH[3][9].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (3, 8)
		scan_west_3_8()
		scan_east_3_8()
		scan_south_3_8()
		move(North)
def scan_west_3_9():
	if move(West):
		WALL[2][9].remove(mnb_east)
		WALL[3][9].remove(mnb_west)
		PATH[2][9].add(bfs_east)
		PATH[3][9].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (2, 9)
		scan_west_2_9()
		scan_south_2_9()
		move(East)
def scan_north_4_0():
	if move(North):
		WALL[4][1].remove(mnb_south)
		WALL[4][0].remove(mnb_north)
		PATH[4][1].add(bfs_south)
		PATH[4][0].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (4, 1)
		scan_west_4_1()
		scan_east_4_1()
		scan_north_4_1()
		move(South)
def scan_east_4_0():
	if move(East):
		WALL[5][0].remove(mnb_west)
		WALL[4][0].remove(mnb_east)
		PATH[5][0].add(bfs_west)
		PATH[4][0].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (5, 0)
		scan_east_5_0()
		scan_north_5_0()
		move(West)
def scan_west_4_0():
	if move(West):
		WALL[3][0].remove(mnb_east)
		WALL[4][0].remove(mnb_west)
		PATH[3][0].add(bfs_east)
		PATH[4][0].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (3, 0)
		scan_west_3_0()
		scan_north_3_0()
		move(East)
def scan_north_4_1():
	if move(North):
		WALL[4][2].remove(mnb_south)
		WALL[4][1].remove(mnb_north)
		PATH[4][2].add(bfs_south)
		PATH[4][1].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (4, 2)
		scan_west_4_2()
		scan_east_4_2()
		scan_north_4_2()
		move(South)
def scan_east_4_1():
	if move(East):
		WALL[5][1].remove(mnb_west)
		WALL[4][1].remove(mnb_east)
		PATH[5][1].add(bfs_west)
		PATH[4][1].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (5, 1)
		scan_east_5_1()
		scan_south_5_1()
		scan_north_5_1()
		move(West)
def scan_south_4_1():
	if move(South):
		WALL[4][0].remove(mnb_north)
		WALL[4][1].remove(mnb_south)
		PATH[4][0].add(bfs_north)
		PATH[4][1].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (4, 0)
		scan_west_4_0()
		scan_east_4_0()
		move(North)
def scan_west_4_1():
	if move(West):
		WALL[3][1].remove(mnb_east)
		WALL[4][1].remove(mnb_west)
		PATH[3][1].add(bfs_east)
		PATH[4][1].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (3, 1)
		scan_west_3_1()
		scan_south_3_1()
		scan_north_3_1()
		move(East)
def scan_north_4_2():
	if move(North):
		WALL[4][3].remove(mnb_south)
		WALL[4][2].remove(mnb_north)
		PATH[4][3].add(bfs_south)
		PATH[4][2].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (4, 3)
		scan_west_4_3()
		scan_east_4_3()
		scan_north_4_3()
		move(South)
def scan_east_4_2():
	if move(East):
		WALL[5][2].remove(mnb_west)
		WALL[4][2].remove(mnb_east)
		PATH[5][2].add(bfs_west)
		PATH[4][2].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (5, 2)
		scan_east_5_2()
		scan_south_5_2()
		scan_north_5_2()
		move(West)
def scan_south_4_2():
	if move(South):
		WALL[4][1].remove(mnb_north)
		WALL[4][2].remove(mnb_south)
		PATH[4][1].add(bfs_north)
		PATH[4][2].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (4, 1)
		scan_west_4_1()
		scan_east_4_1()
		scan_south_4_1()
		move(North)
def scan_west_4_2():
	if move(West):
		WALL[3][2].remove(mnb_east)
		WALL[4][2].remove(mnb_west)
		PATH[3][2].add(bfs_east)
		PATH[4][2].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (3, 2)
		scan_west_3_2()
		scan_south_3_2()
		scan_north_3_2()
		move(East)
def scan_north_4_3():
	if move(North):
		WALL[4][4].remove(mnb_south)
		WALL[4][3].remove(mnb_north)
		PATH[4][4].add(bfs_south)
		PATH[4][3].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (4, 4)
		scan_west_4_4()
		scan_east_4_4()
		scan_north_4_4()
		move(South)
def scan_east_4_3():
	if move(East):
		WALL[5][3].remove(mnb_west)
		WALL[4][3].remove(mnb_east)
		PATH[5][3].add(bfs_west)
		PATH[4][3].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (5, 3)
		scan_east_5_3()
		scan_south_5_3()
		scan_north_5_3()
		move(West)
def scan_south_4_3():
	if move(South):
		WALL[4][2].remove(mnb_north)
		WALL[4][3].remove(mnb_south)
		PATH[4][2].add(bfs_north)
		PATH[4][3].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (4, 2)
		scan_west_4_2()
		scan_east_4_2()
		scan_south_4_2()
		move(North)
def scan_west_4_3():
	if move(West):
		WALL[3][3].remove(mnb_east)
		WALL[4][3].remove(mnb_west)
		PATH[3][3].add(bfs_east)
		PATH[4][3].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (3, 3)
		scan_west_3_3()
		scan_south_3_3()
		scan_north_3_3()
		move(East)
def scan_north_4_4():
	if move(North):
		WALL[4][5].remove(mnb_south)
		WALL[4][4].remove(mnb_north)
		PATH[4][5].add(bfs_south)
		PATH[4][4].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (4, 5)
		scan_west_4_5()
		scan_east_4_5()
		scan_north_4_5()
		move(South)
def scan_east_4_4():
	if move(East):
		WALL[5][4].remove(mnb_west)
		WALL[4][4].remove(mnb_east)
		PATH[5][4].add(bfs_west)
		PATH[4][4].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (5, 4)
		scan_east_5_4()
		scan_south_5_4()
		scan_north_5_4()
		move(West)
def scan_south_4_4():
	if move(South):
		WALL[4][3].remove(mnb_north)
		WALL[4][4].remove(mnb_south)
		PATH[4][3].add(bfs_north)
		PATH[4][4].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (4, 3)
		scan_west_4_3()
		scan_east_4_3()
		scan_south_4_3()
		move(North)
def scan_west_4_4():
	if move(West):
		WALL[3][4].remove(mnb_east)
		WALL[4][4].remove(mnb_west)
		PATH[3][4].add(bfs_east)
		PATH[4][4].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (3, 4)
		scan_west_3_4()
		scan_south_3_4()
		scan_north_3_4()
		move(East)
def scan_north_4_5():
	if move(North):
		WALL[4][6].remove(mnb_south)
		WALL[4][5].remove(mnb_north)
		PATH[4][6].add(bfs_south)
		PATH[4][5].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (4, 6)
		scan_west_4_6()
		scan_east_4_6()
		scan_north_4_6()
		move(South)
def scan_east_4_5():
	if move(East):
		WALL[5][5].remove(mnb_west)
		WALL[4][5].remove(mnb_east)
		PATH[5][5].add(bfs_west)
		PATH[4][5].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (5, 5)
		scan_east_5_5()
		scan_south_5_5()
		scan_north_5_5()
		move(West)
def scan_south_4_5():
	if move(South):
		WALL[4][4].remove(mnb_north)
		WALL[4][5].remove(mnb_south)
		PATH[4][4].add(bfs_north)
		PATH[4][5].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (4, 4)
		scan_west_4_4()
		scan_east_4_4()
		scan_south_4_4()
		move(North)
def scan_west_4_5():
	if move(West):
		WALL[3][5].remove(mnb_east)
		WALL[4][5].remove(mnb_west)
		PATH[3][5].add(bfs_east)
		PATH[4][5].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (3, 5)
		scan_west_3_5()
		scan_south_3_5()
		scan_north_3_5()
		move(East)
def scan_north_4_6():
	if move(North):
		WALL[4][7].remove(mnb_south)
		WALL[4][6].remove(mnb_north)
		PATH[4][7].add(bfs_south)
		PATH[4][6].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (4, 7)
		scan_west_4_7()
		scan_east_4_7()
		scan_north_4_7()
		move(South)
def scan_east_4_6():
	if move(East):
		WALL[5][6].remove(mnb_west)
		WALL[4][6].remove(mnb_east)
		PATH[5][6].add(bfs_west)
		PATH[4][6].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (5, 6)
		scan_east_5_6()
		scan_south_5_6()
		scan_north_5_6()
		move(West)
def scan_south_4_6():
	if move(South):
		WALL[4][5].remove(mnb_north)
		WALL[4][6].remove(mnb_south)
		PATH[4][5].add(bfs_north)
		PATH[4][6].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (4, 5)
		scan_west_4_5()
		scan_east_4_5()
		scan_south_4_5()
		move(North)
def scan_west_4_6():
	if move(West):
		WALL[3][6].remove(mnb_east)
		WALL[4][6].remove(mnb_west)
		PATH[3][6].add(bfs_east)
		PATH[4][6].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (3, 6)
		scan_west_3_6()
		scan_south_3_6()
		scan_north_3_6()
		move(East)
def scan_north_4_7():
	if move(North):
		WALL[4][8].remove(mnb_south)
		WALL[4][7].remove(mnb_north)
		PATH[4][8].add(bfs_south)
		PATH[4][7].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (4, 8)
		scan_west_4_8()
		scan_east_4_8()
		scan_north_4_8()
		move(South)
def scan_east_4_7():
	if move(East):
		WALL[5][7].remove(mnb_west)
		WALL[4][7].remove(mnb_east)
		PATH[5][7].add(bfs_west)
		PATH[4][7].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (5, 7)
		scan_east_5_7()
		scan_south_5_7()
		scan_north_5_7()
		move(West)
def scan_south_4_7():
	if move(South):
		WALL[4][6].remove(mnb_north)
		WALL[4][7].remove(mnb_south)
		PATH[4][6].add(bfs_north)
		PATH[4][7].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (4, 6)
		scan_west_4_6()
		scan_east_4_6()
		scan_south_4_6()
		move(North)
def scan_west_4_7():
	if move(West):
		WALL[3][7].remove(mnb_east)
		WALL[4][7].remove(mnb_west)
		PATH[3][7].add(bfs_east)
		PATH[4][7].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (3, 7)
		scan_west_3_7()
		scan_south_3_7()
		scan_north_3_7()
		move(East)
def scan_north_4_8():
	if move(North):
		WALL[4][9].remove(mnb_south)
		WALL[4][8].remove(mnb_north)
		PATH[4][9].add(bfs_south)
		PATH[4][8].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (4, 9)
		scan_west_4_9()
		scan_east_4_9()
		move(South)
def scan_east_4_8():
	if move(East):
		WALL[5][8].remove(mnb_west)
		WALL[4][8].remove(mnb_east)
		PATH[5][8].add(bfs_west)
		PATH[4][8].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (5, 8)
		scan_east_5_8()
		scan_south_5_8()
		scan_north_5_8()
		move(West)
def scan_south_4_8():
	if move(South):
		WALL[4][7].remove(mnb_north)
		WALL[4][8].remove(mnb_south)
		PATH[4][7].add(bfs_north)
		PATH[4][8].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (4, 7)
		scan_west_4_7()
		scan_east_4_7()
		scan_south_4_7()
		move(North)
def scan_west_4_8():
	if move(West):
		WALL[3][8].remove(mnb_east)
		WALL[4][8].remove(mnb_west)
		PATH[3][8].add(bfs_east)
		PATH[4][8].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (3, 8)
		scan_west_3_8()
		scan_south_3_8()
		scan_north_3_8()
		move(East)
def scan_east_4_9():
	if move(East):
		WALL[5][9].remove(mnb_west)
		WALL[4][9].remove(mnb_east)
		PATH[5][9].add(bfs_west)
		PATH[4][9].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (5, 9)
		scan_east_5_9()
		scan_south_5_9()
		move(West)
def scan_south_4_9():
	if move(South):
		WALL[4][8].remove(mnb_north)
		WALL[4][9].remove(mnb_south)
		PATH[4][8].add(bfs_north)
		PATH[4][9].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (4, 8)
		scan_west_4_8()
		scan_east_4_8()
		scan_south_4_8()
		move(North)
def scan_west_4_9():
	if move(West):
		WALL[3][9].remove(mnb_east)
		WALL[4][9].remove(mnb_west)
		PATH[3][9].add(bfs_east)
		PATH[4][9].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (3, 9)
		scan_west_3_9()
		scan_south_3_9()
		move(East)
def scan_north_5_0():
	if move(North):
		WALL[5][1].remove(mnb_south)
		WALL[5][0].remove(mnb_north)
		PATH[5][1].add(bfs_south)
		PATH[5][0].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (5, 1)
		scan_west_5_1()
		scan_east_5_1()
		scan_north_5_1()
		move(South)
def scan_east_5_0():
	if move(East):
		WALL[6][0].remove(mnb_west)
		WALL[5][0].remove(mnb_east)
		PATH[6][0].add(bfs_west)
		PATH[5][0].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (6, 0)
		scan_east_6_0()
		scan_north_6_0()
		move(West)
def scan_west_5_0():
	if move(West):
		WALL[4][0].remove(mnb_east)
		WALL[5][0].remove(mnb_west)
		PATH[4][0].add(bfs_east)
		PATH[5][0].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (4, 0)
		scan_west_4_0()
		scan_north_4_0()
		move(East)
def scan_north_5_1():
	if move(North):
		WALL[5][2].remove(mnb_south)
		WALL[5][1].remove(mnb_north)
		PATH[5][2].add(bfs_south)
		PATH[5][1].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (5, 2)
		scan_west_5_2()
		scan_east_5_2()
		scan_north_5_2()
		move(South)
def scan_east_5_1():
	if move(East):
		WALL[6][1].remove(mnb_west)
		WALL[5][1].remove(mnb_east)
		PATH[6][1].add(bfs_west)
		PATH[5][1].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (6, 1)
		scan_east_6_1()
		scan_south_6_1()
		scan_north_6_1()
		move(West)
def scan_south_5_1():
	if move(South):
		WALL[5][0].remove(mnb_north)
		WALL[5][1].remove(mnb_south)
		PATH[5][0].add(bfs_north)
		PATH[5][1].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (5, 0)
		scan_west_5_0()
		scan_east_5_0()
		move(North)
def scan_west_5_1():
	if move(West):
		WALL[4][1].remove(mnb_east)
		WALL[5][1].remove(mnb_west)
		PATH[4][1].add(bfs_east)
		PATH[5][1].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (4, 1)
		scan_west_4_1()
		scan_south_4_1()
		scan_north_4_1()
		move(East)
def scan_north_5_2():
	if move(North):
		WALL[5][3].remove(mnb_south)
		WALL[5][2].remove(mnb_north)
		PATH[5][3].add(bfs_south)
		PATH[5][2].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (5, 3)
		scan_west_5_3()
		scan_east_5_3()
		scan_north_5_3()
		move(South)
def scan_east_5_2():
	if move(East):
		WALL[6][2].remove(mnb_west)
		WALL[5][2].remove(mnb_east)
		PATH[6][2].add(bfs_west)
		PATH[5][2].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (6, 2)
		scan_east_6_2()
		scan_south_6_2()
		scan_north_6_2()
		move(West)
def scan_south_5_2():
	if move(South):
		WALL[5][1].remove(mnb_north)
		WALL[5][2].remove(mnb_south)
		PATH[5][1].add(bfs_north)
		PATH[5][2].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (5, 1)
		scan_west_5_1()
		scan_east_5_1()
		scan_south_5_1()
		move(North)
def scan_west_5_2():
	if move(West):
		WALL[4][2].remove(mnb_east)
		WALL[5][2].remove(mnb_west)
		PATH[4][2].add(bfs_east)
		PATH[5][2].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (4, 2)
		scan_west_4_2()
		scan_south_4_2()
		scan_north_4_2()
		move(East)
def scan_north_5_3():
	if move(North):
		WALL[5][4].remove(mnb_south)
		WALL[5][3].remove(mnb_north)
		PATH[5][4].add(bfs_south)
		PATH[5][3].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (5, 4)
		scan_west_5_4()
		scan_east_5_4()
		scan_north_5_4()
		move(South)
def scan_east_5_3():
	if move(East):
		WALL[6][3].remove(mnb_west)
		WALL[5][3].remove(mnb_east)
		PATH[6][3].add(bfs_west)
		PATH[5][3].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (6, 3)
		scan_east_6_3()
		scan_south_6_3()
		scan_north_6_3()
		move(West)
def scan_south_5_3():
	if move(South):
		WALL[5][2].remove(mnb_north)
		WALL[5][3].remove(mnb_south)
		PATH[5][2].add(bfs_north)
		PATH[5][3].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (5, 2)
		scan_west_5_2()
		scan_east_5_2()
		scan_south_5_2()
		move(North)
def scan_west_5_3():
	if move(West):
		WALL[4][3].remove(mnb_east)
		WALL[5][3].remove(mnb_west)
		PATH[4][3].add(bfs_east)
		PATH[5][3].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (4, 3)
		scan_west_4_3()
		scan_south_4_3()
		scan_north_4_3()
		move(East)
def scan_north_5_4():
	if move(North):
		WALL[5][5].remove(mnb_south)
		WALL[5][4].remove(mnb_north)
		PATH[5][5].add(bfs_south)
		PATH[5][4].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (5, 5)
		scan_west_5_5()
		scan_east_5_5()
		scan_north_5_5()
		move(South)
def scan_east_5_4():
	if move(East):
		WALL[6][4].remove(mnb_west)
		WALL[5][4].remove(mnb_east)
		PATH[6][4].add(bfs_west)
		PATH[5][4].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (6, 4)
		scan_east_6_4()
		scan_south_6_4()
		scan_north_6_4()
		move(West)
def scan_south_5_4():
	if move(South):
		WALL[5][3].remove(mnb_north)
		WALL[5][4].remove(mnb_south)
		PATH[5][3].add(bfs_north)
		PATH[5][4].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (5, 3)
		scan_west_5_3()
		scan_east_5_3()
		scan_south_5_3()
		move(North)
def scan_west_5_4():
	if move(West):
		WALL[4][4].remove(mnb_east)
		WALL[5][4].remove(mnb_west)
		PATH[4][4].add(bfs_east)
		PATH[5][4].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (4, 4)
		scan_west_4_4()
		scan_south_4_4()
		scan_north_4_4()
		move(East)
def scan_north_5_5():
	if move(North):
		WALL[5][6].remove(mnb_south)
		WALL[5][5].remove(mnb_north)
		PATH[5][6].add(bfs_south)
		PATH[5][5].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (5, 6)
		scan_west_5_6()
		scan_east_5_6()
		scan_north_5_6()
		move(South)
def scan_east_5_5():
	if move(East):
		WALL[6][5].remove(mnb_west)
		WALL[5][5].remove(mnb_east)
		PATH[6][5].add(bfs_west)
		PATH[5][5].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (6, 5)
		scan_east_6_5()
		scan_south_6_5()
		scan_north_6_5()
		move(West)
def scan_south_5_5():
	if move(South):
		WALL[5][4].remove(mnb_north)
		WALL[5][5].remove(mnb_south)
		PATH[5][4].add(bfs_north)
		PATH[5][5].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (5, 4)
		scan_west_5_4()
		scan_east_5_4()
		scan_south_5_4()
		move(North)
def scan_west_5_5():
	if move(West):
		WALL[4][5].remove(mnb_east)
		WALL[5][5].remove(mnb_west)
		PATH[4][5].add(bfs_east)
		PATH[5][5].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (4, 5)
		scan_west_4_5()
		scan_south_4_5()
		scan_north_4_5()
		move(East)
def scan_north_5_6():
	if move(North):
		WALL[5][7].remove(mnb_south)
		WALL[5][6].remove(mnb_north)
		PATH[5][7].add(bfs_south)
		PATH[5][6].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (5, 7)
		scan_west_5_7()
		scan_east_5_7()
		scan_north_5_7()
		move(South)
def scan_east_5_6():
	if move(East):
		WALL[6][6].remove(mnb_west)
		WALL[5][6].remove(mnb_east)
		PATH[6][6].add(bfs_west)
		PATH[5][6].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (6, 6)
		scan_east_6_6()
		scan_south_6_6()
		scan_north_6_6()
		move(West)
def scan_south_5_6():
	if move(South):
		WALL[5][5].remove(mnb_north)
		WALL[5][6].remove(mnb_south)
		PATH[5][5].add(bfs_north)
		PATH[5][6].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (5, 5)
		scan_west_5_5()
		scan_east_5_5()
		scan_south_5_5()
		move(North)
def scan_west_5_6():
	if move(West):
		WALL[4][6].remove(mnb_east)
		WALL[5][6].remove(mnb_west)
		PATH[4][6].add(bfs_east)
		PATH[5][6].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (4, 6)
		scan_west_4_6()
		scan_south_4_6()
		scan_north_4_6()
		move(East)
def scan_north_5_7():
	if move(North):
		WALL[5][8].remove(mnb_south)
		WALL[5][7].remove(mnb_north)
		PATH[5][8].add(bfs_south)
		PATH[5][7].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (5, 8)
		scan_west_5_8()
		scan_east_5_8()
		scan_north_5_8()
		move(South)
def scan_east_5_7():
	if move(East):
		WALL[6][7].remove(mnb_west)
		WALL[5][7].remove(mnb_east)
		PATH[6][7].add(bfs_west)
		PATH[5][7].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (6, 7)
		scan_east_6_7()
		scan_south_6_7()
		scan_north_6_7()
		move(West)
def scan_south_5_7():
	if move(South):
		WALL[5][6].remove(mnb_north)
		WALL[5][7].remove(mnb_south)
		PATH[5][6].add(bfs_north)
		PATH[5][7].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (5, 6)
		scan_west_5_6()
		scan_east_5_6()
		scan_south_5_6()
		move(North)
def scan_west_5_7():
	if move(West):
		WALL[4][7].remove(mnb_east)
		WALL[5][7].remove(mnb_west)
		PATH[4][7].add(bfs_east)
		PATH[5][7].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (4, 7)
		scan_west_4_7()
		scan_south_4_7()
		scan_north_4_7()
		move(East)
def scan_north_5_8():
	if move(North):
		WALL[5][9].remove(mnb_south)
		WALL[5][8].remove(mnb_north)
		PATH[5][9].add(bfs_south)
		PATH[5][8].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (5, 9)
		scan_west_5_9()
		scan_east_5_9()
		move(South)
def scan_east_5_8():
	if move(East):
		WALL[6][8].remove(mnb_west)
		WALL[5][8].remove(mnb_east)
		PATH[6][8].add(bfs_west)
		PATH[5][8].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (6, 8)
		scan_east_6_8()
		scan_south_6_8()
		scan_north_6_8()
		move(West)
def scan_south_5_8():
	if move(South):
		WALL[5][7].remove(mnb_north)
		WALL[5][8].remove(mnb_south)
		PATH[5][7].add(bfs_north)
		PATH[5][8].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (5, 7)
		scan_west_5_7()
		scan_east_5_7()
		scan_south_5_7()
		move(North)
def scan_west_5_8():
	if move(West):
		WALL[4][8].remove(mnb_east)
		WALL[5][8].remove(mnb_west)
		PATH[4][8].add(bfs_east)
		PATH[5][8].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (4, 8)
		scan_west_4_8()
		scan_south_4_8()
		scan_north_4_8()
		move(East)
def scan_east_5_9():
	if move(East):
		WALL[6][9].remove(mnb_west)
		WALL[5][9].remove(mnb_east)
		PATH[6][9].add(bfs_west)
		PATH[5][9].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (6, 9)
		scan_east_6_9()
		scan_south_6_9()
		move(West)
def scan_south_5_9():
	if move(South):
		WALL[5][8].remove(mnb_north)
		WALL[5][9].remove(mnb_south)
		PATH[5][8].add(bfs_north)
		PATH[5][9].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (5, 8)
		scan_west_5_8()
		scan_east_5_8()
		scan_south_5_8()
		move(North)
def scan_west_5_9():
	if move(West):
		WALL[4][9].remove(mnb_east)
		WALL[5][9].remove(mnb_west)
		PATH[4][9].add(bfs_east)
		PATH[5][9].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (4, 9)
		scan_west_4_9()
		scan_south_4_9()
		move(East)
def scan_north_6_0():
	if move(North):
		WALL[6][1].remove(mnb_south)
		WALL[6][0].remove(mnb_north)
		PATH[6][1].add(bfs_south)
		PATH[6][0].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (6, 1)
		scan_west_6_1()
		scan_east_6_1()
		scan_north_6_1()
		move(South)
def scan_east_6_0():
	if move(East):
		WALL[7][0].remove(mnb_west)
		WALL[6][0].remove(mnb_east)
		PATH[7][0].add(bfs_west)
		PATH[6][0].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (7, 0)
		scan_east_7_0()
		scan_north_7_0()
		move(West)
def scan_west_6_0():
	if move(West):
		WALL[5][0].remove(mnb_east)
		WALL[6][0].remove(mnb_west)
		PATH[5][0].add(bfs_east)
		PATH[6][0].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (5, 0)
		scan_west_5_0()
		scan_north_5_0()
		move(East)
def scan_north_6_1():
	if move(North):
		WALL[6][2].remove(mnb_south)
		WALL[6][1].remove(mnb_north)
		PATH[6][2].add(bfs_south)
		PATH[6][1].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (6, 2)
		scan_west_6_2()
		scan_east_6_2()
		scan_north_6_2()
		move(South)
def scan_east_6_1():
	if move(East):
		WALL[7][1].remove(mnb_west)
		WALL[6][1].remove(mnb_east)
		PATH[7][1].add(bfs_west)
		PATH[6][1].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (7, 1)
		scan_east_7_1()
		scan_south_7_1()
		scan_north_7_1()
		move(West)
def scan_south_6_1():
	if move(South):
		WALL[6][0].remove(mnb_north)
		WALL[6][1].remove(mnb_south)
		PATH[6][0].add(bfs_north)
		PATH[6][1].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (6, 0)
		scan_west_6_0()
		scan_east_6_0()
		move(North)
def scan_west_6_1():
	if move(West):
		WALL[5][1].remove(mnb_east)
		WALL[6][1].remove(mnb_west)
		PATH[5][1].add(bfs_east)
		PATH[6][1].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (5, 1)
		scan_west_5_1()
		scan_south_5_1()
		scan_north_5_1()
		move(East)
def scan_north_6_2():
	if move(North):
		WALL[6][3].remove(mnb_south)
		WALL[6][2].remove(mnb_north)
		PATH[6][3].add(bfs_south)
		PATH[6][2].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (6, 3)
		scan_west_6_3()
		scan_east_6_3()
		scan_north_6_3()
		move(South)
def scan_east_6_2():
	if move(East):
		WALL[7][2].remove(mnb_west)
		WALL[6][2].remove(mnb_east)
		PATH[7][2].add(bfs_west)
		PATH[6][2].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (7, 2)
		scan_east_7_2()
		scan_south_7_2()
		scan_north_7_2()
		move(West)
def scan_south_6_2():
	if move(South):
		WALL[6][1].remove(mnb_north)
		WALL[6][2].remove(mnb_south)
		PATH[6][1].add(bfs_north)
		PATH[6][2].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (6, 1)
		scan_west_6_1()
		scan_east_6_1()
		scan_south_6_1()
		move(North)
def scan_west_6_2():
	if move(West):
		WALL[5][2].remove(mnb_east)
		WALL[6][2].remove(mnb_west)
		PATH[5][2].add(bfs_east)
		PATH[6][2].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (5, 2)
		scan_west_5_2()
		scan_south_5_2()
		scan_north_5_2()
		move(East)
def scan_north_6_3():
	if move(North):
		WALL[6][4].remove(mnb_south)
		WALL[6][3].remove(mnb_north)
		PATH[6][4].add(bfs_south)
		PATH[6][3].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (6, 4)
		scan_west_6_4()
		scan_east_6_4()
		scan_north_6_4()
		move(South)
def scan_east_6_3():
	if move(East):
		WALL[7][3].remove(mnb_west)
		WALL[6][3].remove(mnb_east)
		PATH[7][3].add(bfs_west)
		PATH[6][3].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (7, 3)
		scan_east_7_3()
		scan_south_7_3()
		scan_north_7_3()
		move(West)
def scan_south_6_3():
	if move(South):
		WALL[6][2].remove(mnb_north)
		WALL[6][3].remove(mnb_south)
		PATH[6][2].add(bfs_north)
		PATH[6][3].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (6, 2)
		scan_west_6_2()
		scan_east_6_2()
		scan_south_6_2()
		move(North)
def scan_west_6_3():
	if move(West):
		WALL[5][3].remove(mnb_east)
		WALL[6][3].remove(mnb_west)
		PATH[5][3].add(bfs_east)
		PATH[6][3].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (5, 3)
		scan_west_5_3()
		scan_south_5_3()
		scan_north_5_3()
		move(East)
def scan_north_6_4():
	if move(North):
		WALL[6][5].remove(mnb_south)
		WALL[6][4].remove(mnb_north)
		PATH[6][5].add(bfs_south)
		PATH[6][4].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (6, 5)
		scan_west_6_5()
		scan_east_6_5()
		scan_north_6_5()
		move(South)
def scan_east_6_4():
	if move(East):
		WALL[7][4].remove(mnb_west)
		WALL[6][4].remove(mnb_east)
		PATH[7][4].add(bfs_west)
		PATH[6][4].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (7, 4)
		scan_east_7_4()
		scan_south_7_4()
		scan_north_7_4()
		move(West)
def scan_south_6_4():
	if move(South):
		WALL[6][3].remove(mnb_north)
		WALL[6][4].remove(mnb_south)
		PATH[6][3].add(bfs_north)
		PATH[6][4].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (6, 3)
		scan_west_6_3()
		scan_east_6_3()
		scan_south_6_3()
		move(North)
def scan_west_6_4():
	if move(West):
		WALL[5][4].remove(mnb_east)
		WALL[6][4].remove(mnb_west)
		PATH[5][4].add(bfs_east)
		PATH[6][4].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (5, 4)
		scan_west_5_4()
		scan_south_5_4()
		scan_north_5_4()
		move(East)
def scan_north_6_5():
	if move(North):
		WALL[6][6].remove(mnb_south)
		WALL[6][5].remove(mnb_north)
		PATH[6][6].add(bfs_south)
		PATH[6][5].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (6, 6)
		scan_west_6_6()
		scan_east_6_6()
		scan_north_6_6()
		move(South)
def scan_east_6_5():
	if move(East):
		WALL[7][5].remove(mnb_west)
		WALL[6][5].remove(mnb_east)
		PATH[7][5].add(bfs_west)
		PATH[6][5].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (7, 5)
		scan_east_7_5()
		scan_south_7_5()
		scan_north_7_5()
		move(West)
def scan_south_6_5():
	if move(South):
		WALL[6][4].remove(mnb_north)
		WALL[6][5].remove(mnb_south)
		PATH[6][4].add(bfs_north)
		PATH[6][5].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (6, 4)
		scan_west_6_4()
		scan_east_6_4()
		scan_south_6_4()
		move(North)
def scan_west_6_5():
	if move(West):
		WALL[5][5].remove(mnb_east)
		WALL[6][5].remove(mnb_west)
		PATH[5][5].add(bfs_east)
		PATH[6][5].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (5, 5)
		scan_west_5_5()
		scan_south_5_5()
		scan_north_5_5()
		move(East)
def scan_north_6_6():
	if move(North):
		WALL[6][7].remove(mnb_south)
		WALL[6][6].remove(mnb_north)
		PATH[6][7].add(bfs_south)
		PATH[6][6].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (6, 7)
		scan_west_6_7()
		scan_east_6_7()
		scan_north_6_7()
		move(South)
def scan_east_6_6():
	if move(East):
		WALL[7][6].remove(mnb_west)
		WALL[6][6].remove(mnb_east)
		PATH[7][6].add(bfs_west)
		PATH[6][6].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (7, 6)
		scan_east_7_6()
		scan_south_7_6()
		scan_north_7_6()
		move(West)
def scan_south_6_6():
	if move(South):
		WALL[6][5].remove(mnb_north)
		WALL[6][6].remove(mnb_south)
		PATH[6][5].add(bfs_north)
		PATH[6][6].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (6, 5)
		scan_west_6_5()
		scan_east_6_5()
		scan_south_6_5()
		move(North)
def scan_west_6_6():
	if move(West):
		WALL[5][6].remove(mnb_east)
		WALL[6][6].remove(mnb_west)
		PATH[5][6].add(bfs_east)
		PATH[6][6].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (5, 6)
		scan_west_5_6()
		scan_south_5_6()
		scan_north_5_6()
		move(East)
def scan_north_6_7():
	if move(North):
		WALL[6][8].remove(mnb_south)
		WALL[6][7].remove(mnb_north)
		PATH[6][8].add(bfs_south)
		PATH[6][7].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (6, 8)
		scan_west_6_8()
		scan_east_6_8()
		scan_north_6_8()
		move(South)
def scan_east_6_7():
	if move(East):
		WALL[7][7].remove(mnb_west)
		WALL[6][7].remove(mnb_east)
		PATH[7][7].add(bfs_west)
		PATH[6][7].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (7, 7)
		scan_east_7_7()
		scan_south_7_7()
		scan_north_7_7()
		move(West)
def scan_south_6_7():
	if move(South):
		WALL[6][6].remove(mnb_north)
		WALL[6][7].remove(mnb_south)
		PATH[6][6].add(bfs_north)
		PATH[6][7].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (6, 6)
		scan_west_6_6()
		scan_east_6_6()
		scan_south_6_6()
		move(North)
def scan_west_6_7():
	if move(West):
		WALL[5][7].remove(mnb_east)
		WALL[6][7].remove(mnb_west)
		PATH[5][7].add(bfs_east)
		PATH[6][7].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (5, 7)
		scan_west_5_7()
		scan_south_5_7()
		scan_north_5_7()
		move(East)
def scan_north_6_8():
	if move(North):
		WALL[6][9].remove(mnb_south)
		WALL[6][8].remove(mnb_north)
		PATH[6][9].add(bfs_south)
		PATH[6][8].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (6, 9)
		scan_west_6_9()
		scan_east_6_9()
		move(South)
def scan_east_6_8():
	if move(East):
		WALL[7][8].remove(mnb_west)
		WALL[6][8].remove(mnb_east)
		PATH[7][8].add(bfs_west)
		PATH[6][8].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (7, 8)
		scan_east_7_8()
		scan_south_7_8()
		scan_north_7_8()
		move(West)
def scan_south_6_8():
	if move(South):
		WALL[6][7].remove(mnb_north)
		WALL[6][8].remove(mnb_south)
		PATH[6][7].add(bfs_north)
		PATH[6][8].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (6, 7)
		scan_west_6_7()
		scan_east_6_7()
		scan_south_6_7()
		move(North)
def scan_west_6_8():
	if move(West):
		WALL[5][8].remove(mnb_east)
		WALL[6][8].remove(mnb_west)
		PATH[5][8].add(bfs_east)
		PATH[6][8].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (5, 8)
		scan_west_5_8()
		scan_south_5_8()
		scan_north_5_8()
		move(East)
def scan_east_6_9():
	if move(East):
		WALL[7][9].remove(mnb_west)
		WALL[6][9].remove(mnb_east)
		PATH[7][9].add(bfs_west)
		PATH[6][9].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (7, 9)
		scan_east_7_9()
		scan_south_7_9()
		move(West)
def scan_south_6_9():
	if move(South):
		WALL[6][8].remove(mnb_north)
		WALL[6][9].remove(mnb_south)
		PATH[6][8].add(bfs_north)
		PATH[6][9].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (6, 8)
		scan_west_6_8()
		scan_east_6_8()
		scan_south_6_8()
		move(North)
def scan_west_6_9():
	if move(West):
		WALL[5][9].remove(mnb_east)
		WALL[6][9].remove(mnb_west)
		PATH[5][9].add(bfs_east)
		PATH[6][9].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (5, 9)
		scan_west_5_9()
		scan_south_5_9()
		move(East)
def scan_north_7_0():
	if move(North):
		WALL[7][1].remove(mnb_south)
		WALL[7][0].remove(mnb_north)
		PATH[7][1].add(bfs_south)
		PATH[7][0].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (7, 1)
		scan_west_7_1()
		scan_east_7_1()
		scan_north_7_1()
		move(South)
def scan_east_7_0():
	if move(East):
		WALL[8][0].remove(mnb_west)
		WALL[7][0].remove(mnb_east)
		PATH[8][0].add(bfs_west)
		PATH[7][0].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (8, 0)
		scan_east_8_0()
		scan_north_8_0()
		move(West)
def scan_west_7_0():
	if move(West):
		WALL[6][0].remove(mnb_east)
		WALL[7][0].remove(mnb_west)
		PATH[6][0].add(bfs_east)
		PATH[7][0].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (6, 0)
		scan_west_6_0()
		scan_north_6_0()
		move(East)
def scan_north_7_1():
	if move(North):
		WALL[7][2].remove(mnb_south)
		WALL[7][1].remove(mnb_north)
		PATH[7][2].add(bfs_south)
		PATH[7][1].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (7, 2)
		scan_west_7_2()
		scan_east_7_2()
		scan_north_7_2()
		move(South)
def scan_east_7_1():
	if move(East):
		WALL[8][1].remove(mnb_west)
		WALL[7][1].remove(mnb_east)
		PATH[8][1].add(bfs_west)
		PATH[7][1].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (8, 1)
		scan_east_8_1()
		scan_south_8_1()
		scan_north_8_1()
		move(West)
def scan_south_7_1():
	if move(South):
		WALL[7][0].remove(mnb_north)
		WALL[7][1].remove(mnb_south)
		PATH[7][0].add(bfs_north)
		PATH[7][1].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (7, 0)
		scan_west_7_0()
		scan_east_7_0()
		move(North)
def scan_west_7_1():
	if move(West):
		WALL[6][1].remove(mnb_east)
		WALL[7][1].remove(mnb_west)
		PATH[6][1].add(bfs_east)
		PATH[7][1].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (6, 1)
		scan_west_6_1()
		scan_south_6_1()
		scan_north_6_1()
		move(East)
def scan_north_7_2():
	if move(North):
		WALL[7][3].remove(mnb_south)
		WALL[7][2].remove(mnb_north)
		PATH[7][3].add(bfs_south)
		PATH[7][2].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (7, 3)
		scan_west_7_3()
		scan_east_7_3()
		scan_north_7_3()
		move(South)
def scan_east_7_2():
	if move(East):
		WALL[8][2].remove(mnb_west)
		WALL[7][2].remove(mnb_east)
		PATH[8][2].add(bfs_west)
		PATH[7][2].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (8, 2)
		scan_east_8_2()
		scan_south_8_2()
		scan_north_8_2()
		move(West)
def scan_south_7_2():
	if move(South):
		WALL[7][1].remove(mnb_north)
		WALL[7][2].remove(mnb_south)
		PATH[7][1].add(bfs_north)
		PATH[7][2].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (7, 1)
		scan_west_7_1()
		scan_east_7_1()
		scan_south_7_1()
		move(North)
def scan_west_7_2():
	if move(West):
		WALL[6][2].remove(mnb_east)
		WALL[7][2].remove(mnb_west)
		PATH[6][2].add(bfs_east)
		PATH[7][2].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (6, 2)
		scan_west_6_2()
		scan_south_6_2()
		scan_north_6_2()
		move(East)
def scan_north_7_3():
	if move(North):
		WALL[7][4].remove(mnb_south)
		WALL[7][3].remove(mnb_north)
		PATH[7][4].add(bfs_south)
		PATH[7][3].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (7, 4)
		scan_west_7_4()
		scan_east_7_4()
		scan_north_7_4()
		move(South)
def scan_east_7_3():
	if move(East):
		WALL[8][3].remove(mnb_west)
		WALL[7][3].remove(mnb_east)
		PATH[8][3].add(bfs_west)
		PATH[7][3].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (8, 3)
		scan_east_8_3()
		scan_south_8_3()
		scan_north_8_3()
		move(West)
def scan_south_7_3():
	if move(South):
		WALL[7][2].remove(mnb_north)
		WALL[7][3].remove(mnb_south)
		PATH[7][2].add(bfs_north)
		PATH[7][3].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (7, 2)
		scan_west_7_2()
		scan_east_7_2()
		scan_south_7_2()
		move(North)
def scan_west_7_3():
	if move(West):
		WALL[6][3].remove(mnb_east)
		WALL[7][3].remove(mnb_west)
		PATH[6][3].add(bfs_east)
		PATH[7][3].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (6, 3)
		scan_west_6_3()
		scan_south_6_3()
		scan_north_6_3()
		move(East)
def scan_north_7_4():
	if move(North):
		WALL[7][5].remove(mnb_south)
		WALL[7][4].remove(mnb_north)
		PATH[7][5].add(bfs_south)
		PATH[7][4].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (7, 5)
		scan_west_7_5()
		scan_east_7_5()
		scan_north_7_5()
		move(South)
def scan_east_7_4():
	if move(East):
		WALL[8][4].remove(mnb_west)
		WALL[7][4].remove(mnb_east)
		PATH[8][4].add(bfs_west)
		PATH[7][4].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (8, 4)
		scan_east_8_4()
		scan_south_8_4()
		scan_north_8_4()
		move(West)
def scan_south_7_4():
	if move(South):
		WALL[7][3].remove(mnb_north)
		WALL[7][4].remove(mnb_south)
		PATH[7][3].add(bfs_north)
		PATH[7][4].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (7, 3)
		scan_west_7_3()
		scan_east_7_3()
		scan_south_7_3()
		move(North)
def scan_west_7_4():
	if move(West):
		WALL[6][4].remove(mnb_east)
		WALL[7][4].remove(mnb_west)
		PATH[6][4].add(bfs_east)
		PATH[7][4].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (6, 4)
		scan_west_6_4()
		scan_south_6_4()
		scan_north_6_4()
		move(East)
def scan_north_7_5():
	if move(North):
		WALL[7][6].remove(mnb_south)
		WALL[7][5].remove(mnb_north)
		PATH[7][6].add(bfs_south)
		PATH[7][5].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (7, 6)
		scan_west_7_6()
		scan_east_7_6()
		scan_north_7_6()
		move(South)
def scan_east_7_5():
	if move(East):
		WALL[8][5].remove(mnb_west)
		WALL[7][5].remove(mnb_east)
		PATH[8][5].add(bfs_west)
		PATH[7][5].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (8, 5)
		scan_east_8_5()
		scan_south_8_5()
		scan_north_8_5()
		move(West)
def scan_south_7_5():
	if move(South):
		WALL[7][4].remove(mnb_north)
		WALL[7][5].remove(mnb_south)
		PATH[7][4].add(bfs_north)
		PATH[7][5].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (7, 4)
		scan_west_7_4()
		scan_east_7_4()
		scan_south_7_4()
		move(North)
def scan_west_7_5():
	if move(West):
		WALL[6][5].remove(mnb_east)
		WALL[7][5].remove(mnb_west)
		PATH[6][5].add(bfs_east)
		PATH[7][5].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (6, 5)
		scan_west_6_5()
		scan_south_6_5()
		scan_north_6_5()
		move(East)
def scan_north_7_6():
	if move(North):
		WALL[7][7].remove(mnb_south)
		WALL[7][6].remove(mnb_north)
		PATH[7][7].add(bfs_south)
		PATH[7][6].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (7, 7)
		scan_west_7_7()
		scan_east_7_7()
		scan_north_7_7()
		move(South)
def scan_east_7_6():
	if move(East):
		WALL[8][6].remove(mnb_west)
		WALL[7][6].remove(mnb_east)
		PATH[8][6].add(bfs_west)
		PATH[7][6].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (8, 6)
		scan_east_8_6()
		scan_south_8_6()
		scan_north_8_6()
		move(West)
def scan_south_7_6():
	if move(South):
		WALL[7][5].remove(mnb_north)
		WALL[7][6].remove(mnb_south)
		PATH[7][5].add(bfs_north)
		PATH[7][6].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (7, 5)
		scan_west_7_5()
		scan_east_7_5()
		scan_south_7_5()
		move(North)
def scan_west_7_6():
	if move(West):
		WALL[6][6].remove(mnb_east)
		WALL[7][6].remove(mnb_west)
		PATH[6][6].add(bfs_east)
		PATH[7][6].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (6, 6)
		scan_west_6_6()
		scan_south_6_6()
		scan_north_6_6()
		move(East)
def scan_north_7_7():
	if move(North):
		WALL[7][8].remove(mnb_south)
		WALL[7][7].remove(mnb_north)
		PATH[7][8].add(bfs_south)
		PATH[7][7].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (7, 8)
		scan_west_7_8()
		scan_east_7_8()
		scan_north_7_8()
		move(South)
def scan_east_7_7():
	if move(East):
		WALL[8][7].remove(mnb_west)
		WALL[7][7].remove(mnb_east)
		PATH[8][7].add(bfs_west)
		PATH[7][7].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (8, 7)
		scan_east_8_7()
		scan_south_8_7()
		scan_north_8_7()
		move(West)
def scan_south_7_7():
	if move(South):
		WALL[7][6].remove(mnb_north)
		WALL[7][7].remove(mnb_south)
		PATH[7][6].add(bfs_north)
		PATH[7][7].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (7, 6)
		scan_west_7_6()
		scan_east_7_6()
		scan_south_7_6()
		move(North)
def scan_west_7_7():
	if move(West):
		WALL[6][7].remove(mnb_east)
		WALL[7][7].remove(mnb_west)
		PATH[6][7].add(bfs_east)
		PATH[7][7].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (6, 7)
		scan_west_6_7()
		scan_south_6_7()
		scan_north_6_7()
		move(East)
def scan_north_7_8():
	if move(North):
		WALL[7][9].remove(mnb_south)
		WALL[7][8].remove(mnb_north)
		PATH[7][9].add(bfs_south)
		PATH[7][8].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (7, 9)
		scan_west_7_9()
		scan_east_7_9()
		move(South)
def scan_east_7_8():
	if move(East):
		WALL[8][8].remove(mnb_west)
		WALL[7][8].remove(mnb_east)
		PATH[8][8].add(bfs_west)
		PATH[7][8].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (8, 8)
		scan_east_8_8()
		scan_south_8_8()
		scan_north_8_8()
		move(West)
def scan_south_7_8():
	if move(South):
		WALL[7][7].remove(mnb_north)
		WALL[7][8].remove(mnb_south)
		PATH[7][7].add(bfs_north)
		PATH[7][8].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (7, 7)
		scan_west_7_7()
		scan_east_7_7()
		scan_south_7_7()
		move(North)
def scan_west_7_8():
	if move(West):
		WALL[6][8].remove(mnb_east)
		WALL[7][8].remove(mnb_west)
		PATH[6][8].add(bfs_east)
		PATH[7][8].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (6, 8)
		scan_west_6_8()
		scan_south_6_8()
		scan_north_6_8()
		move(East)
def scan_east_7_9():
	if move(East):
		WALL[8][9].remove(mnb_west)
		WALL[7][9].remove(mnb_east)
		PATH[8][9].add(bfs_west)
		PATH[7][9].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (8, 9)
		scan_east_8_9()
		scan_south_8_9()
		move(West)
def scan_south_7_9():
	if move(South):
		WALL[7][8].remove(mnb_north)
		WALL[7][9].remove(mnb_south)
		PATH[7][8].add(bfs_north)
		PATH[7][9].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (7, 8)
		scan_west_7_8()
		scan_east_7_8()
		scan_south_7_8()
		move(North)
def scan_west_7_9():
	if move(West):
		WALL[6][9].remove(mnb_east)
		WALL[7][9].remove(mnb_west)
		PATH[6][9].add(bfs_east)
		PATH[7][9].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (6, 9)
		scan_west_6_9()
		scan_south_6_9()
		move(East)
def scan_north_8_0():
	if move(North):
		WALL[8][1].remove(mnb_south)
		WALL[8][0].remove(mnb_north)
		PATH[8][1].add(bfs_south)
		PATH[8][0].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (8, 1)
		scan_west_8_1()
		scan_east_8_1()
		scan_north_8_1()
		move(South)
def scan_east_8_0():
	if move(East):
		WALL[9][0].remove(mnb_west)
		WALL[8][0].remove(mnb_east)
		PATH[9][0].add(bfs_west)
		PATH[8][0].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (9, 0)
		scan_north_9_0()
		move(West)
def scan_west_8_0():
	if move(West):
		WALL[7][0].remove(mnb_east)
		WALL[8][0].remove(mnb_west)
		PATH[7][0].add(bfs_east)
		PATH[8][0].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (7, 0)
		scan_west_7_0()
		scan_north_7_0()
		move(East)
def scan_north_8_1():
	if move(North):
		WALL[8][2].remove(mnb_south)
		WALL[8][1].remove(mnb_north)
		PATH[8][2].add(bfs_south)
		PATH[8][1].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (8, 2)
		scan_west_8_2()
		scan_east_8_2()
		scan_north_8_2()
		move(South)
def scan_east_8_1():
	if move(East):
		WALL[9][1].remove(mnb_west)
		WALL[8][1].remove(mnb_east)
		PATH[9][1].add(bfs_west)
		PATH[8][1].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (9, 1)
		scan_south_9_1()
		scan_north_9_1()
		move(West)
def scan_south_8_1():
	if move(South):
		WALL[8][0].remove(mnb_north)
		WALL[8][1].remove(mnb_south)
		PATH[8][0].add(bfs_north)
		PATH[8][1].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (8, 0)
		scan_west_8_0()
		scan_east_8_0()
		move(North)
def scan_west_8_1():
	if move(West):
		WALL[7][1].remove(mnb_east)
		WALL[8][1].remove(mnb_west)
		PATH[7][1].add(bfs_east)
		PATH[8][1].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (7, 1)
		scan_west_7_1()
		scan_south_7_1()
		scan_north_7_1()
		move(East)
def scan_north_8_2():
	if move(North):
		WALL[8][3].remove(mnb_south)
		WALL[8][2].remove(mnb_north)
		PATH[8][3].add(bfs_south)
		PATH[8][2].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (8, 3)
		scan_west_8_3()
		scan_east_8_3()
		scan_north_8_3()
		move(South)
def scan_east_8_2():
	if move(East):
		WALL[9][2].remove(mnb_west)
		WALL[8][2].remove(mnb_east)
		PATH[9][2].add(bfs_west)
		PATH[8][2].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (9, 2)
		scan_south_9_2()
		scan_north_9_2()
		move(West)
def scan_south_8_2():
	if move(South):
		WALL[8][1].remove(mnb_north)
		WALL[8][2].remove(mnb_south)
		PATH[8][1].add(bfs_north)
		PATH[8][2].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (8, 1)
		scan_west_8_1()
		scan_east_8_1()
		scan_south_8_1()
		move(North)
def scan_west_8_2():
	if move(West):
		WALL[7][2].remove(mnb_east)
		WALL[8][2].remove(mnb_west)
		PATH[7][2].add(bfs_east)
		PATH[8][2].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (7, 2)
		scan_west_7_2()
		scan_south_7_2()
		scan_north_7_2()
		move(East)
def scan_north_8_3():
	if move(North):
		WALL[8][4].remove(mnb_south)
		WALL[8][3].remove(mnb_north)
		PATH[8][4].add(bfs_south)
		PATH[8][3].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (8, 4)
		scan_west_8_4()
		scan_east_8_4()
		scan_north_8_4()
		move(South)
def scan_east_8_3():
	if move(East):
		WALL[9][3].remove(mnb_west)
		WALL[8][3].remove(mnb_east)
		PATH[9][3].add(bfs_west)
		PATH[8][3].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (9, 3)
		scan_south_9_3()
		scan_north_9_3()
		move(West)
def scan_south_8_3():
	if move(South):
		WALL[8][2].remove(mnb_north)
		WALL[8][3].remove(mnb_south)
		PATH[8][2].add(bfs_north)
		PATH[8][3].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (8, 2)
		scan_west_8_2()
		scan_east_8_2()
		scan_south_8_2()
		move(North)
def scan_west_8_3():
	if move(West):
		WALL[7][3].remove(mnb_east)
		WALL[8][3].remove(mnb_west)
		PATH[7][3].add(bfs_east)
		PATH[8][3].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (7, 3)
		scan_west_7_3()
		scan_south_7_3()
		scan_north_7_3()
		move(East)
def scan_north_8_4():
	if move(North):
		WALL[8][5].remove(mnb_south)
		WALL[8][4].remove(mnb_north)
		PATH[8][5].add(bfs_south)
		PATH[8][4].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (8, 5)
		scan_west_8_5()
		scan_east_8_5()
		scan_north_8_5()
		move(South)
def scan_east_8_4():
	if move(East):
		WALL[9][4].remove(mnb_west)
		WALL[8][4].remove(mnb_east)
		PATH[9][4].add(bfs_west)
		PATH[8][4].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (9, 4)
		scan_south_9_4()
		scan_north_9_4()
		move(West)
def scan_south_8_4():
	if move(South):
		WALL[8][3].remove(mnb_north)
		WALL[8][4].remove(mnb_south)
		PATH[8][3].add(bfs_north)
		PATH[8][4].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (8, 3)
		scan_west_8_3()
		scan_east_8_3()
		scan_south_8_3()
		move(North)
def scan_west_8_4():
	if move(West):
		WALL[7][4].remove(mnb_east)
		WALL[8][4].remove(mnb_west)
		PATH[7][4].add(bfs_east)
		PATH[8][4].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (7, 4)
		scan_west_7_4()
		scan_south_7_4()
		scan_north_7_4()
		move(East)
def scan_north_8_5():
	if move(North):
		WALL[8][6].remove(mnb_south)
		WALL[8][5].remove(mnb_north)
		PATH[8][6].add(bfs_south)
		PATH[8][5].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (8, 6)
		scan_west_8_6()
		scan_east_8_6()
		scan_north_8_6()
		move(South)
def scan_east_8_5():
	if move(East):
		WALL[9][5].remove(mnb_west)
		WALL[8][5].remove(mnb_east)
		PATH[9][5].add(bfs_west)
		PATH[8][5].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (9, 5)
		scan_south_9_5()
		scan_north_9_5()
		move(West)
def scan_south_8_5():
	if move(South):
		WALL[8][4].remove(mnb_north)
		WALL[8][5].remove(mnb_south)
		PATH[8][4].add(bfs_north)
		PATH[8][5].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (8, 4)
		scan_west_8_4()
		scan_east_8_4()
		scan_south_8_4()
		move(North)
def scan_west_8_5():
	if move(West):
		WALL[7][5].remove(mnb_east)
		WALL[8][5].remove(mnb_west)
		PATH[7][5].add(bfs_east)
		PATH[8][5].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (7, 5)
		scan_west_7_5()
		scan_south_7_5()
		scan_north_7_5()
		move(East)
def scan_north_8_6():
	if move(North):
		WALL[8][7].remove(mnb_south)
		WALL[8][6].remove(mnb_north)
		PATH[8][7].add(bfs_south)
		PATH[8][6].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (8, 7)
		scan_west_8_7()
		scan_east_8_7()
		scan_north_8_7()
		move(South)
def scan_east_8_6():
	if move(East):
		WALL[9][6].remove(mnb_west)
		WALL[8][6].remove(mnb_east)
		PATH[9][6].add(bfs_west)
		PATH[8][6].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (9, 6)
		scan_south_9_6()
		scan_north_9_6()
		move(West)
def scan_south_8_6():
	if move(South):
		WALL[8][5].remove(mnb_north)
		WALL[8][6].remove(mnb_south)
		PATH[8][5].add(bfs_north)
		PATH[8][6].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (8, 5)
		scan_west_8_5()
		scan_east_8_5()
		scan_south_8_5()
		move(North)
def scan_west_8_6():
	if move(West):
		WALL[7][6].remove(mnb_east)
		WALL[8][6].remove(mnb_west)
		PATH[7][6].add(bfs_east)
		PATH[8][6].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (7, 6)
		scan_west_7_6()
		scan_south_7_6()
		scan_north_7_6()
		move(East)
def scan_north_8_7():
	if move(North):
		WALL[8][8].remove(mnb_south)
		WALL[8][7].remove(mnb_north)
		PATH[8][8].add(bfs_south)
		PATH[8][7].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (8, 8)
		scan_west_8_8()
		scan_east_8_8()
		scan_north_8_8()
		move(South)
def scan_east_8_7():
	if move(East):
		WALL[9][7].remove(mnb_west)
		WALL[8][7].remove(mnb_east)
		PATH[9][7].add(bfs_west)
		PATH[8][7].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (9, 7)
		scan_south_9_7()
		scan_north_9_7()
		move(West)
def scan_south_8_7():
	if move(South):
		WALL[8][6].remove(mnb_north)
		WALL[8][7].remove(mnb_south)
		PATH[8][6].add(bfs_north)
		PATH[8][7].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (8, 6)
		scan_west_8_6()
		scan_east_8_6()
		scan_south_8_6()
		move(North)
def scan_west_8_7():
	if move(West):
		WALL[7][7].remove(mnb_east)
		WALL[8][7].remove(mnb_west)
		PATH[7][7].add(bfs_east)
		PATH[8][7].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (7, 7)
		scan_west_7_7()
		scan_south_7_7()
		scan_north_7_7()
		move(East)
def scan_north_8_8():
	if move(North):
		WALL[8][9].remove(mnb_south)
		WALL[8][8].remove(mnb_north)
		PATH[8][9].add(bfs_south)
		PATH[8][8].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (8, 9)
		scan_west_8_9()
		scan_east_8_9()
		move(South)
def scan_east_8_8():
	if move(East):
		WALL[9][8].remove(mnb_west)
		WALL[8][8].remove(mnb_east)
		PATH[9][8].add(bfs_west)
		PATH[8][8].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (9, 8)
		scan_south_9_8()
		scan_north_9_8()
		move(West)
def scan_south_8_8():
	if move(South):
		WALL[8][7].remove(mnb_north)
		WALL[8][8].remove(mnb_south)
		PATH[8][7].add(bfs_north)
		PATH[8][8].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (8, 7)
		scan_west_8_7()
		scan_east_8_7()
		scan_south_8_7()
		move(North)
def scan_west_8_8():
	if move(West):
		WALL[7][8].remove(mnb_east)
		WALL[8][8].remove(mnb_west)
		PATH[7][8].add(bfs_east)
		PATH[8][8].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (7, 8)
		scan_west_7_8()
		scan_south_7_8()
		scan_north_7_8()
		move(East)
def scan_east_8_9():
	if move(East):
		WALL[9][9].remove(mnb_west)
		WALL[8][9].remove(mnb_east)
		PATH[9][9].add(bfs_west)
		PATH[8][9].add(bfs_east)
		if measure():
			TREASURE_POS[0] = (9, 9)
		scan_south_9_9()
		move(West)
def scan_south_8_9():
	if move(South):
		WALL[8][8].remove(mnb_north)
		WALL[8][9].remove(mnb_south)
		PATH[8][8].add(bfs_north)
		PATH[8][9].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (8, 8)
		scan_west_8_8()
		scan_east_8_8()
		scan_south_8_8()
		move(North)
def scan_west_8_9():
	if move(West):
		WALL[7][9].remove(mnb_east)
		WALL[8][9].remove(mnb_west)
		PATH[7][9].add(bfs_east)
		PATH[8][9].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (7, 9)
		scan_west_7_9()
		scan_south_7_9()
		move(East)
def scan_north_9_0():
	if move(North):
		WALL[9][1].remove(mnb_south)
		WALL[9][0].remove(mnb_north)
		PATH[9][1].add(bfs_south)
		PATH[9][0].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (9, 1)
		scan_west_9_1()
		scan_north_9_1()
		move(South)
def scan_west_9_0():
	if move(West):
		WALL[8][0].remove(mnb_east)
		WALL[9][0].remove(mnb_west)
		PATH[8][0].add(bfs_east)
		PATH[9][0].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (8, 0)
		scan_west_8_0()
		scan_north_8_0()
		move(East)
def scan_north_9_1():
	if move(North):
		WALL[9][2].remove(mnb_south)
		WALL[9][1].remove(mnb_north)
		PATH[9][2].add(bfs_south)
		PATH[9][1].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (9, 2)
		scan_west_9_2()
		scan_north_9_2()
		move(South)
def scan_south_9_1():
	if move(South):
		WALL[9][0].remove(mnb_north)
		WALL[9][1].remove(mnb_south)
		PATH[9][0].add(bfs_north)
		PATH[9][1].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (9, 0)
		scan_west_9_0()
		move(North)
def scan_west_9_1():
	if move(West):
		WALL[8][1].remove(mnb_east)
		WALL[9][1].remove(mnb_west)
		PATH[8][1].add(bfs_east)
		PATH[9][1].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (8, 1)
		scan_west_8_1()
		scan_south_8_1()
		scan_north_8_1()
		move(East)
def scan_north_9_2():
	if move(North):
		WALL[9][3].remove(mnb_south)
		WALL[9][2].remove(mnb_north)
		PATH[9][3].add(bfs_south)
		PATH[9][2].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (9, 3)
		scan_west_9_3()
		scan_north_9_3()
		move(South)
def scan_south_9_2():
	if move(South):
		WALL[9][1].remove(mnb_north)
		WALL[9][2].remove(mnb_south)
		PATH[9][1].add(bfs_north)
		PATH[9][2].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (9, 1)
		scan_west_9_1()
		scan_south_9_1()
		move(North)
def scan_west_9_2():
	if move(West):
		WALL[8][2].remove(mnb_east)
		WALL[9][2].remove(mnb_west)
		PATH[8][2].add(bfs_east)
		PATH[9][2].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (8, 2)
		scan_west_8_2()
		scan_south_8_2()
		scan_north_8_2()
		move(East)
def scan_north_9_3():
	if move(North):
		WALL[9][4].remove(mnb_south)
		WALL[9][3].remove(mnb_north)
		PATH[9][4].add(bfs_south)
		PATH[9][3].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (9, 4)
		scan_west_9_4()
		scan_north_9_4()
		move(South)
def scan_south_9_3():
	if move(South):
		WALL[9][2].remove(mnb_north)
		WALL[9][3].remove(mnb_south)
		PATH[9][2].add(bfs_north)
		PATH[9][3].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (9, 2)
		scan_west_9_2()
		scan_south_9_2()
		move(North)
def scan_west_9_3():
	if move(West):
		WALL[8][3].remove(mnb_east)
		WALL[9][3].remove(mnb_west)
		PATH[8][3].add(bfs_east)
		PATH[9][3].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (8, 3)
		scan_west_8_3()
		scan_south_8_3()
		scan_north_8_3()
		move(East)
def scan_north_9_4():
	if move(North):
		WALL[9][5].remove(mnb_south)
		WALL[9][4].remove(mnb_north)
		PATH[9][5].add(bfs_south)
		PATH[9][4].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (9, 5)
		scan_west_9_5()
		scan_north_9_5()
		move(South)
def scan_south_9_4():
	if move(South):
		WALL[9][3].remove(mnb_north)
		WALL[9][4].remove(mnb_south)
		PATH[9][3].add(bfs_north)
		PATH[9][4].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (9, 3)
		scan_west_9_3()
		scan_south_9_3()
		move(North)
def scan_west_9_4():
	if move(West):
		WALL[8][4].remove(mnb_east)
		WALL[9][4].remove(mnb_west)
		PATH[8][4].add(bfs_east)
		PATH[9][4].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (8, 4)
		scan_west_8_4()
		scan_south_8_4()
		scan_north_8_4()
		move(East)
def scan_north_9_5():
	if move(North):
		WALL[9][6].remove(mnb_south)
		WALL[9][5].remove(mnb_north)
		PATH[9][6].add(bfs_south)
		PATH[9][5].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (9, 6)
		scan_west_9_6()
		scan_north_9_6()
		move(South)
def scan_south_9_5():
	if move(South):
		WALL[9][4].remove(mnb_north)
		WALL[9][5].remove(mnb_south)
		PATH[9][4].add(bfs_north)
		PATH[9][5].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (9, 4)
		scan_west_9_4()
		scan_south_9_4()
		move(North)
def scan_west_9_5():
	if move(West):
		WALL[8][5].remove(mnb_east)
		WALL[9][5].remove(mnb_west)
		PATH[8][5].add(bfs_east)
		PATH[9][5].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (8, 5)
		scan_west_8_5()
		scan_south_8_5()
		scan_north_8_5()
		move(East)
def scan_north_9_6():
	if move(North):
		WALL[9][7].remove(mnb_south)
		WALL[9][6].remove(mnb_north)
		PATH[9][7].add(bfs_south)
		PATH[9][6].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (9, 7)
		scan_west_9_7()
		scan_north_9_7()
		move(South)
def scan_south_9_6():
	if move(South):
		WALL[9][5].remove(mnb_north)
		WALL[9][6].remove(mnb_south)
		PATH[9][5].add(bfs_north)
		PATH[9][6].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (9, 5)
		scan_west_9_5()
		scan_south_9_5()
		move(North)
def scan_west_9_6():
	if move(West):
		WALL[8][6].remove(mnb_east)
		WALL[9][6].remove(mnb_west)
		PATH[8][6].add(bfs_east)
		PATH[9][6].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (8, 6)
		scan_west_8_6()
		scan_south_8_6()
		scan_north_8_6()
		move(East)
def scan_north_9_7():
	if move(North):
		WALL[9][8].remove(mnb_south)
		WALL[9][7].remove(mnb_north)
		PATH[9][8].add(bfs_south)
		PATH[9][7].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (9, 8)
		scan_west_9_8()
		scan_north_9_8()
		move(South)
def scan_south_9_7():
	if move(South):
		WALL[9][6].remove(mnb_north)
		WALL[9][7].remove(mnb_south)
		PATH[9][6].add(bfs_north)
		PATH[9][7].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (9, 6)
		scan_west_9_6()
		scan_south_9_6()
		move(North)
def scan_west_9_7():
	if move(West):
		WALL[8][7].remove(mnb_east)
		WALL[9][7].remove(mnb_west)
		PATH[8][7].add(bfs_east)
		PATH[9][7].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (8, 7)
		scan_west_8_7()
		scan_south_8_7()
		scan_north_8_7()
		move(East)
def scan_north_9_8():
	if move(North):
		WALL[9][9].remove(mnb_south)
		WALL[9][8].remove(mnb_north)
		PATH[9][9].add(bfs_south)
		PATH[9][8].add(bfs_north)
		if measure():
			TREASURE_POS[0] = (9, 9)
		scan_west_9_9()
		move(South)
def scan_south_9_8():
	if move(South):
		WALL[9][7].remove(mnb_north)
		WALL[9][8].remove(mnb_south)
		PATH[9][7].add(bfs_north)
		PATH[9][8].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (9, 7)
		scan_west_9_7()
		scan_south_9_7()
		move(North)
def scan_west_9_8():
	if move(West):
		WALL[8][8].remove(mnb_east)
		WALL[9][8].remove(mnb_west)
		PATH[8][8].add(bfs_east)
		PATH[9][8].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (8, 8)
		scan_west_8_8()
		scan_south_8_8()
		scan_north_8_8()
		move(East)
def scan_south_9_9():
	if move(South):
		WALL[9][8].remove(mnb_north)
		WALL[9][9].remove(mnb_south)
		PATH[9][8].add(bfs_north)
		PATH[9][9].add(bfs_south)
		if measure():
			TREASURE_POS[0] = (9, 8)
		scan_west_9_8()
		scan_south_9_8()
		move(North)
def scan_west_9_9():
	if move(West):
		WALL[8][9].remove(mnb_east)
		WALL[9][9].remove(mnb_west)
		PATH[8][9].add(bfs_east)
		PATH[9][9].add(bfs_west)
		if measure():
			TREASURE_POS[0] = (8, 9)
		scan_west_8_9()
		scan_south_8_9()
		move(East)
		