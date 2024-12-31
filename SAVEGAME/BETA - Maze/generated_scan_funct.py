def scan_0_0(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_0_1, 10, dist)
	bEast = lbWest(nop, scan_east)(scan_1_0, 1, dist)
	if measure():
		TREASURE_POS[0] = 0
	grid0[0] = [bNorth, bEast, false, false]
def scan_0_1(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_0_2, 20, dist)
	bEast = lbWest(nop, scan_east)(scan_1_1, 11, dist)
	bSouth = lbNorth(nop, scan_south)(scan_0_0, 0, dist)
	if measure():
		TREASURE_POS[0] = 10
	grid0[1] = [bNorth, bEast, bSouth, false]
def scan_0_2(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_0_3, 30, dist)
	bEast = lbWest(nop, scan_east)(scan_1_2, 21, dist)
	bSouth = lbNorth(nop, scan_south)(scan_0_1, 10, dist)
	if measure():
		TREASURE_POS[0] = 20
	grid0[2] = [bNorth, bEast, bSouth, false]
def scan_0_3(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_0_4, 40, dist)
	bEast = lbWest(nop, scan_east)(scan_1_3, 31, dist)
	bSouth = lbNorth(nop, scan_south)(scan_0_2, 20, dist)
	if measure():
		TREASURE_POS[0] = 30
	grid0[3] = [bNorth, bEast, bSouth, false]
def scan_0_4(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_0_5, 50, dist)
	bEast = lbWest(nop, scan_east)(scan_1_4, 41, dist)
	bSouth = lbNorth(nop, scan_south)(scan_0_3, 30, dist)
	if measure():
		TREASURE_POS[0] = 40
	grid0[4] = [bNorth, bEast, bSouth, false]
def scan_0_5(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_0_6, 60, dist)
	bEast = lbWest(nop, scan_east)(scan_1_5, 51, dist)
	bSouth = lbNorth(nop, scan_south)(scan_0_4, 40, dist)
	if measure():
		TREASURE_POS[0] = 50
	grid0[5] = [bNorth, bEast, bSouth, false]
def scan_0_6(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_0_7, 70, dist)
	bEast = lbWest(nop, scan_east)(scan_1_6, 61, dist)
	bSouth = lbNorth(nop, scan_south)(scan_0_5, 50, dist)
	if measure():
		TREASURE_POS[0] = 60
	grid0[6] = [bNorth, bEast, bSouth, false]
def scan_0_7(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_0_8, 80, dist)
	bEast = lbWest(nop, scan_east)(scan_1_7, 71, dist)
	bSouth = lbNorth(nop, scan_south)(scan_0_6, 60, dist)
	if measure():
		TREASURE_POS[0] = 70
	grid0[7] = [bNorth, bEast, bSouth, false]
def scan_0_8(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_0_9, 90, dist)
	bEast = lbWest(nop, scan_east)(scan_1_8, 81, dist)
	bSouth = lbNorth(nop, scan_south)(scan_0_7, 70, dist)
	if measure():
		TREASURE_POS[0] = 80
	grid0[8] = [bNorth, bEast, bSouth, false]
def scan_0_9(lbNorth, lbEast, lbSouth, lbWest, dist):
	bEast = lbWest(nop, scan_east)(scan_1_9, 91, dist)
	bSouth = lbNorth(nop, scan_south)(scan_0_8, 80, dist)
	if measure():
		TREASURE_POS[0] = 90
	grid0[9] = [false, bEast, bSouth, false]
def scan_1_0(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_1_1, 11, dist)
	bEast = lbWest(nop, scan_east)(scan_2_0, 2, dist)
	bWest = lbEast(nop, scan_west)(scan_0_0, 0, dist)
	if measure():
		TREASURE_POS[0] = 1
	grid1[0] = [bNorth, bEast, false, bWest]
def scan_1_1(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_1_2, 21, dist)
	bEast = lbWest(nop, scan_east)(scan_2_1, 12, dist)
	bSouth = lbNorth(nop, scan_south)(scan_1_0, 1, dist)
	bWest = lbEast(nop, scan_west)(scan_0_1, 10, dist)
	if measure():
		TREASURE_POS[0] = 11
	grid1[1] = [bNorth, bEast, bSouth, bWest]
def scan_1_2(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_1_3, 31, dist)
	bEast = lbWest(nop, scan_east)(scan_2_2, 22, dist)
	bSouth = lbNorth(nop, scan_south)(scan_1_1, 11, dist)
	bWest = lbEast(nop, scan_west)(scan_0_2, 20, dist)
	if measure():
		TREASURE_POS[0] = 21
	grid1[2] = [bNorth, bEast, bSouth, bWest]
def scan_1_3(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_1_4, 41, dist)
	bEast = lbWest(nop, scan_east)(scan_2_3, 32, dist)
	bSouth = lbNorth(nop, scan_south)(scan_1_2, 21, dist)
	bWest = lbEast(nop, scan_west)(scan_0_3, 30, dist)
	if measure():
		TREASURE_POS[0] = 31
	grid1[3] = [bNorth, bEast, bSouth, bWest]
def scan_1_4(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_1_5, 51, dist)
	bEast = lbWest(nop, scan_east)(scan_2_4, 42, dist)
	bSouth = lbNorth(nop, scan_south)(scan_1_3, 31, dist)
	bWest = lbEast(nop, scan_west)(scan_0_4, 40, dist)
	if measure():
		TREASURE_POS[0] = 41
	grid1[4] = [bNorth, bEast, bSouth, bWest]
def scan_1_5(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_1_6, 61, dist)
	bEast = lbWest(nop, scan_east)(scan_2_5, 52, dist)
	bSouth = lbNorth(nop, scan_south)(scan_1_4, 41, dist)
	bWest = lbEast(nop, scan_west)(scan_0_5, 50, dist)
	if measure():
		TREASURE_POS[0] = 51
	grid1[5] = [bNorth, bEast, bSouth, bWest]
def scan_1_6(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_1_7, 71, dist)
	bEast = lbWest(nop, scan_east)(scan_2_6, 62, dist)
	bSouth = lbNorth(nop, scan_south)(scan_1_5, 51, dist)
	bWest = lbEast(nop, scan_west)(scan_0_6, 60, dist)
	if measure():
		TREASURE_POS[0] = 61
	grid1[6] = [bNorth, bEast, bSouth, bWest]
def scan_1_7(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_1_8, 81, dist)
	bEast = lbWest(nop, scan_east)(scan_2_7, 72, dist)
	bSouth = lbNorth(nop, scan_south)(scan_1_6, 61, dist)
	bWest = lbEast(nop, scan_west)(scan_0_7, 70, dist)
	if measure():
		TREASURE_POS[0] = 71
	grid1[7] = [bNorth, bEast, bSouth, bWest]
def scan_1_8(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_1_9, 91, dist)
	bEast = lbWest(nop, scan_east)(scan_2_8, 82, dist)
	bSouth = lbNorth(nop, scan_south)(scan_1_7, 71, dist)
	bWest = lbEast(nop, scan_west)(scan_0_8, 80, dist)
	if measure():
		TREASURE_POS[0] = 81
	grid1[8] = [bNorth, bEast, bSouth, bWest]
def scan_1_9(lbNorth, lbEast, lbSouth, lbWest, dist):
	bEast = lbWest(nop, scan_east)(scan_2_9, 92, dist)
	bSouth = lbNorth(nop, scan_south)(scan_1_8, 81, dist)
	bWest = lbEast(nop, scan_west)(scan_0_9, 90, dist)
	if measure():
		TREASURE_POS[0] = 91
	grid1[9] = [false, bEast, bSouth, bWest]
def scan_2_0(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_2_1, 12, dist)
	bEast = lbWest(nop, scan_east)(scan_3_0, 3, dist)
	bWest = lbEast(nop, scan_west)(scan_1_0, 1, dist)
	if measure():
		TREASURE_POS[0] = 2
	grid2[0] = [bNorth, bEast, false, bWest]
def scan_2_1(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_2_2, 22, dist)
	bEast = lbWest(nop, scan_east)(scan_3_1, 13, dist)
	bSouth = lbNorth(nop, scan_south)(scan_2_0, 2, dist)
	bWest = lbEast(nop, scan_west)(scan_1_1, 11, dist)
	if measure():
		TREASURE_POS[0] = 12
	grid2[1] = [bNorth, bEast, bSouth, bWest]
def scan_2_2(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_2_3, 32, dist)
	bEast = lbWest(nop, scan_east)(scan_3_2, 23, dist)
	bSouth = lbNorth(nop, scan_south)(scan_2_1, 12, dist)
	bWest = lbEast(nop, scan_west)(scan_1_2, 21, dist)
	if measure():
		TREASURE_POS[0] = 22
	grid2[2] = [bNorth, bEast, bSouth, bWest]
def scan_2_3(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_2_4, 42, dist)
	bEast = lbWest(nop, scan_east)(scan_3_3, 33, dist)
	bSouth = lbNorth(nop, scan_south)(scan_2_2, 22, dist)
	bWest = lbEast(nop, scan_west)(scan_1_3, 31, dist)
	if measure():
		TREASURE_POS[0] = 32
	grid2[3] = [bNorth, bEast, bSouth, bWest]
def scan_2_4(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_2_5, 52, dist)
	bEast = lbWest(nop, scan_east)(scan_3_4, 43, dist)
	bSouth = lbNorth(nop, scan_south)(scan_2_3, 32, dist)
	bWest = lbEast(nop, scan_west)(scan_1_4, 41, dist)
	if measure():
		TREASURE_POS[0] = 42
	grid2[4] = [bNorth, bEast, bSouth, bWest]
def scan_2_5(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_2_6, 62, dist)
	bEast = lbWest(nop, scan_east)(scan_3_5, 53, dist)
	bSouth = lbNorth(nop, scan_south)(scan_2_4, 42, dist)
	bWest = lbEast(nop, scan_west)(scan_1_5, 51, dist)
	if measure():
		TREASURE_POS[0] = 52
	grid2[5] = [bNorth, bEast, bSouth, bWest]
def scan_2_6(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_2_7, 72, dist)
	bEast = lbWest(nop, scan_east)(scan_3_6, 63, dist)
	bSouth = lbNorth(nop, scan_south)(scan_2_5, 52, dist)
	bWest = lbEast(nop, scan_west)(scan_1_6, 61, dist)
	if measure():
		TREASURE_POS[0] = 62
	grid2[6] = [bNorth, bEast, bSouth, bWest]
def scan_2_7(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_2_8, 82, dist)
	bEast = lbWest(nop, scan_east)(scan_3_7, 73, dist)
	bSouth = lbNorth(nop, scan_south)(scan_2_6, 62, dist)
	bWest = lbEast(nop, scan_west)(scan_1_7, 71, dist)
	if measure():
		TREASURE_POS[0] = 72
	grid2[7] = [bNorth, bEast, bSouth, bWest]
def scan_2_8(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_2_9, 92, dist)
	bEast = lbWest(nop, scan_east)(scan_3_8, 83, dist)
	bSouth = lbNorth(nop, scan_south)(scan_2_7, 72, dist)
	bWest = lbEast(nop, scan_west)(scan_1_8, 81, dist)
	if measure():
		TREASURE_POS[0] = 82
	grid2[8] = [bNorth, bEast, bSouth, bWest]
def scan_2_9(lbNorth, lbEast, lbSouth, lbWest, dist):
	bEast = lbWest(nop, scan_east)(scan_3_9, 93, dist)
	bSouth = lbNorth(nop, scan_south)(scan_2_8, 82, dist)
	bWest = lbEast(nop, scan_west)(scan_1_9, 91, dist)
	if measure():
		TREASURE_POS[0] = 92
	grid2[9] = [false, bEast, bSouth, bWest]
def scan_3_0(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_3_1, 13, dist)
	bEast = lbWest(nop, scan_east)(scan_4_0, 4, dist)
	bWest = lbEast(nop, scan_west)(scan_2_0, 2, dist)
	if measure():
		TREASURE_POS[0] = 3
	grid3[0] = [bNorth, bEast, false, bWest]
def scan_3_1(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_3_2, 23, dist)
	bEast = lbWest(nop, scan_east)(scan_4_1, 14, dist)
	bSouth = lbNorth(nop, scan_south)(scan_3_0, 3, dist)
	bWest = lbEast(nop, scan_west)(scan_2_1, 12, dist)
	if measure():
		TREASURE_POS[0] = 13
	grid3[1] = [bNorth, bEast, bSouth, bWest]
def scan_3_2(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_3_3, 33, dist)
	bEast = lbWest(nop, scan_east)(scan_4_2, 24, dist)
	bSouth = lbNorth(nop, scan_south)(scan_3_1, 13, dist)
	bWest = lbEast(nop, scan_west)(scan_2_2, 22, dist)
	if measure():
		TREASURE_POS[0] = 23
	grid3[2] = [bNorth, bEast, bSouth, bWest]
def scan_3_3(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_3_4, 43, dist)
	bEast = lbWest(nop, scan_east)(scan_4_3, 34, dist)
	bSouth = lbNorth(nop, scan_south)(scan_3_2, 23, dist)
	bWest = lbEast(nop, scan_west)(scan_2_3, 32, dist)
	if measure():
		TREASURE_POS[0] = 33
	grid3[3] = [bNorth, bEast, bSouth, bWest]
def scan_3_4(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_3_5, 53, dist)
	bEast = lbWest(nop, scan_east)(scan_4_4, 44, dist)
	bSouth = lbNorth(nop, scan_south)(scan_3_3, 33, dist)
	bWest = lbEast(nop, scan_west)(scan_2_4, 42, dist)
	if measure():
		TREASURE_POS[0] = 43
	grid3[4] = [bNorth, bEast, bSouth, bWest]
def scan_3_5(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_3_6, 63, dist)
	bEast = lbWest(nop, scan_east)(scan_4_5, 54, dist)
	bSouth = lbNorth(nop, scan_south)(scan_3_4, 43, dist)
	bWest = lbEast(nop, scan_west)(scan_2_5, 52, dist)
	if measure():
		TREASURE_POS[0] = 53
	grid3[5] = [bNorth, bEast, bSouth, bWest]
def scan_3_6(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_3_7, 73, dist)
	bEast = lbWest(nop, scan_east)(scan_4_6, 64, dist)
	bSouth = lbNorth(nop, scan_south)(scan_3_5, 53, dist)
	bWest = lbEast(nop, scan_west)(scan_2_6, 62, dist)
	if measure():
		TREASURE_POS[0] = 63
	grid3[6] = [bNorth, bEast, bSouth, bWest]
def scan_3_7(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_3_8, 83, dist)
	bEast = lbWest(nop, scan_east)(scan_4_7, 74, dist)
	bSouth = lbNorth(nop, scan_south)(scan_3_6, 63, dist)
	bWest = lbEast(nop, scan_west)(scan_2_7, 72, dist)
	if measure():
		TREASURE_POS[0] = 73
	grid3[7] = [bNorth, bEast, bSouth, bWest]
def scan_3_8(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_3_9, 93, dist)
	bEast = lbWest(nop, scan_east)(scan_4_8, 84, dist)
	bSouth = lbNorth(nop, scan_south)(scan_3_7, 73, dist)
	bWest = lbEast(nop, scan_west)(scan_2_8, 82, dist)
	if measure():
		TREASURE_POS[0] = 83
	grid3[8] = [bNorth, bEast, bSouth, bWest]
def scan_3_9(lbNorth, lbEast, lbSouth, lbWest, dist):
	bEast = lbWest(nop, scan_east)(scan_4_9, 94, dist)
	bSouth = lbNorth(nop, scan_south)(scan_3_8, 83, dist)
	bWest = lbEast(nop, scan_west)(scan_2_9, 92, dist)
	if measure():
		TREASURE_POS[0] = 93
	grid3[9] = [false, bEast, bSouth, bWest]
def scan_4_0(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_4_1, 14, dist)
	bEast = lbWest(nop, scan_east)(scan_5_0, 5, dist)
	bWest = lbEast(nop, scan_west)(scan_3_0, 3, dist)
	if measure():
		TREASURE_POS[0] = 4
	grid4[0] = [bNorth, bEast, false, bWest]
def scan_4_1(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_4_2, 24, dist)
	bEast = lbWest(nop, scan_east)(scan_5_1, 15, dist)
	bSouth = lbNorth(nop, scan_south)(scan_4_0, 4, dist)
	bWest = lbEast(nop, scan_west)(scan_3_1, 13, dist)
	if measure():
		TREASURE_POS[0] = 14
	grid4[1] = [bNorth, bEast, bSouth, bWest]
def scan_4_2(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_4_3, 34, dist)
	bEast = lbWest(nop, scan_east)(scan_5_2, 25, dist)
	bSouth = lbNorth(nop, scan_south)(scan_4_1, 14, dist)
	bWest = lbEast(nop, scan_west)(scan_3_2, 23, dist)
	if measure():
		TREASURE_POS[0] = 24
	grid4[2] = [bNorth, bEast, bSouth, bWest]
def scan_4_3(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_4_4, 44, dist)
	bEast = lbWest(nop, scan_east)(scan_5_3, 35, dist)
	bSouth = lbNorth(nop, scan_south)(scan_4_2, 24, dist)
	bWest = lbEast(nop, scan_west)(scan_3_3, 33, dist)
	if measure():
		TREASURE_POS[0] = 34
	grid4[3] = [bNorth, bEast, bSouth, bWest]
def scan_4_4(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_4_5, 54, dist)
	bEast = lbWest(nop, scan_east)(scan_5_4, 45, dist)
	bSouth = lbNorth(nop, scan_south)(scan_4_3, 34, dist)
	bWest = lbEast(nop, scan_west)(scan_3_4, 43, dist)
	if measure():
		TREASURE_POS[0] = 44
	grid4[4] = [bNorth, bEast, bSouth, bWest]
def scan_4_5(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_4_6, 64, dist)
	bEast = lbWest(nop, scan_east)(scan_5_5, 55, dist)
	bSouth = lbNorth(nop, scan_south)(scan_4_4, 44, dist)
	bWest = lbEast(nop, scan_west)(scan_3_5, 53, dist)
	if measure():
		TREASURE_POS[0] = 54
	grid4[5] = [bNorth, bEast, bSouth, bWest]
def scan_4_6(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_4_7, 74, dist)
	bEast = lbWest(nop, scan_east)(scan_5_6, 65, dist)
	bSouth = lbNorth(nop, scan_south)(scan_4_5, 54, dist)
	bWest = lbEast(nop, scan_west)(scan_3_6, 63, dist)
	if measure():
		TREASURE_POS[0] = 64
	grid4[6] = [bNorth, bEast, bSouth, bWest]
def scan_4_7(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_4_8, 84, dist)
	bEast = lbWest(nop, scan_east)(scan_5_7, 75, dist)
	bSouth = lbNorth(nop, scan_south)(scan_4_6, 64, dist)
	bWest = lbEast(nop, scan_west)(scan_3_7, 73, dist)
	if measure():
		TREASURE_POS[0] = 74
	grid4[7] = [bNorth, bEast, bSouth, bWest]
def scan_4_8(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_4_9, 94, dist)
	bEast = lbWest(nop, scan_east)(scan_5_8, 85, dist)
	bSouth = lbNorth(nop, scan_south)(scan_4_7, 74, dist)
	bWest = lbEast(nop, scan_west)(scan_3_8, 83, dist)
	if measure():
		TREASURE_POS[0] = 84
	grid4[8] = [bNorth, bEast, bSouth, bWest]
def scan_4_9(lbNorth, lbEast, lbSouth, lbWest, dist):
	bEast = lbWest(nop, scan_east)(scan_5_9, 95, dist)
	bSouth = lbNorth(nop, scan_south)(scan_4_8, 84, dist)
	bWest = lbEast(nop, scan_west)(scan_3_9, 93, dist)
	if measure():
		TREASURE_POS[0] = 94
	grid4[9] = [false, bEast, bSouth, bWest]
def scan_5_0(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_5_1, 15, dist)
	bEast = lbWest(nop, scan_east)(scan_6_0, 6, dist)
	bWest = lbEast(nop, scan_west)(scan_4_0, 4, dist)
	if measure():
		TREASURE_POS[0] = 5
	grid5[0] = [bNorth, bEast, false, bWest]
def scan_5_1(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_5_2, 25, dist)
	bEast = lbWest(nop, scan_east)(scan_6_1, 16, dist)
	bSouth = lbNorth(nop, scan_south)(scan_5_0, 5, dist)
	bWest = lbEast(nop, scan_west)(scan_4_1, 14, dist)
	if measure():
		TREASURE_POS[0] = 15
	grid5[1] = [bNorth, bEast, bSouth, bWest]
def scan_5_2(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_5_3, 35, dist)
	bEast = lbWest(nop, scan_east)(scan_6_2, 26, dist)
	bSouth = lbNorth(nop, scan_south)(scan_5_1, 15, dist)
	bWest = lbEast(nop, scan_west)(scan_4_2, 24, dist)
	if measure():
		TREASURE_POS[0] = 25
	grid5[2] = [bNorth, bEast, bSouth, bWest]
def scan_5_3(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_5_4, 45, dist)
	bEast = lbWest(nop, scan_east)(scan_6_3, 36, dist)
	bSouth = lbNorth(nop, scan_south)(scan_5_2, 25, dist)
	bWest = lbEast(nop, scan_west)(scan_4_3, 34, dist)
	if measure():
		TREASURE_POS[0] = 35
	grid5[3] = [bNorth, bEast, bSouth, bWest]
def scan_5_4(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_5_5, 55, dist)
	bEast = lbWest(nop, scan_east)(scan_6_4, 46, dist)
	bSouth = lbNorth(nop, scan_south)(scan_5_3, 35, dist)
	bWest = lbEast(nop, scan_west)(scan_4_4, 44, dist)
	if measure():
		TREASURE_POS[0] = 45
	grid5[4] = [bNorth, bEast, bSouth, bWest]
def scan_5_5(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_5_6, 65, dist)
	bEast = lbWest(nop, scan_east)(scan_6_5, 56, dist)
	bSouth = lbNorth(nop, scan_south)(scan_5_4, 45, dist)
	bWest = lbEast(nop, scan_west)(scan_4_5, 54, dist)
	if measure():
		TREASURE_POS[0] = 55
	grid5[5] = [bNorth, bEast, bSouth, bWest]
def scan_5_6(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_5_7, 75, dist)
	bEast = lbWest(nop, scan_east)(scan_6_6, 66, dist)
	bSouth = lbNorth(nop, scan_south)(scan_5_5, 55, dist)
	bWest = lbEast(nop, scan_west)(scan_4_6, 64, dist)
	if measure():
		TREASURE_POS[0] = 65
	grid5[6] = [bNorth, bEast, bSouth, bWest]
def scan_5_7(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_5_8, 85, dist)
	bEast = lbWest(nop, scan_east)(scan_6_7, 76, dist)
	bSouth = lbNorth(nop, scan_south)(scan_5_6, 65, dist)
	bWest = lbEast(nop, scan_west)(scan_4_7, 74, dist)
	if measure():
		TREASURE_POS[0] = 75
	grid5[7] = [bNorth, bEast, bSouth, bWest]
def scan_5_8(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_5_9, 95, dist)
	bEast = lbWest(nop, scan_east)(scan_6_8, 86, dist)
	bSouth = lbNorth(nop, scan_south)(scan_5_7, 75, dist)
	bWest = lbEast(nop, scan_west)(scan_4_8, 84, dist)
	if measure():
		TREASURE_POS[0] = 85
	grid5[8] = [bNorth, bEast, bSouth, bWest]
def scan_5_9(lbNorth, lbEast, lbSouth, lbWest, dist):
	bEast = lbWest(nop, scan_east)(scan_6_9, 96, dist)
	bSouth = lbNorth(nop, scan_south)(scan_5_8, 85, dist)
	bWest = lbEast(nop, scan_west)(scan_4_9, 94, dist)
	if measure():
		TREASURE_POS[0] = 95
	grid5[9] = [false, bEast, bSouth, bWest]
def scan_6_0(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_6_1, 16, dist)
	bEast = lbWest(nop, scan_east)(scan_7_0, 7, dist)
	bWest = lbEast(nop, scan_west)(scan_5_0, 5, dist)
	if measure():
		TREASURE_POS[0] = 6
	grid6[0] = [bNorth, bEast, false, bWest]
def scan_6_1(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_6_2, 26, dist)
	bEast = lbWest(nop, scan_east)(scan_7_1, 17, dist)
	bSouth = lbNorth(nop, scan_south)(scan_6_0, 6, dist)
	bWest = lbEast(nop, scan_west)(scan_5_1, 15, dist)
	if measure():
		TREASURE_POS[0] = 16
	grid6[1] = [bNorth, bEast, bSouth, bWest]
def scan_6_2(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_6_3, 36, dist)
	bEast = lbWest(nop, scan_east)(scan_7_2, 27, dist)
	bSouth = lbNorth(nop, scan_south)(scan_6_1, 16, dist)
	bWest = lbEast(nop, scan_west)(scan_5_2, 25, dist)
	if measure():
		TREASURE_POS[0] = 26
	grid6[2] = [bNorth, bEast, bSouth, bWest]
def scan_6_3(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_6_4, 46, dist)
	bEast = lbWest(nop, scan_east)(scan_7_3, 37, dist)
	bSouth = lbNorth(nop, scan_south)(scan_6_2, 26, dist)
	bWest = lbEast(nop, scan_west)(scan_5_3, 35, dist)
	if measure():
		TREASURE_POS[0] = 36
	grid6[3] = [bNorth, bEast, bSouth, bWest]
def scan_6_4(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_6_5, 56, dist)
	bEast = lbWest(nop, scan_east)(scan_7_4, 47, dist)
	bSouth = lbNorth(nop, scan_south)(scan_6_3, 36, dist)
	bWest = lbEast(nop, scan_west)(scan_5_4, 45, dist)
	if measure():
		TREASURE_POS[0] = 46
	grid6[4] = [bNorth, bEast, bSouth, bWest]
def scan_6_5(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_6_6, 66, dist)
	bEast = lbWest(nop, scan_east)(scan_7_5, 57, dist)
	bSouth = lbNorth(nop, scan_south)(scan_6_4, 46, dist)
	bWest = lbEast(nop, scan_west)(scan_5_5, 55, dist)
	if measure():
		TREASURE_POS[0] = 56
	grid6[5] = [bNorth, bEast, bSouth, bWest]
def scan_6_6(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_6_7, 76, dist)
	bEast = lbWest(nop, scan_east)(scan_7_6, 67, dist)
	bSouth = lbNorth(nop, scan_south)(scan_6_5, 56, dist)
	bWest = lbEast(nop, scan_west)(scan_5_6, 65, dist)
	if measure():
		TREASURE_POS[0] = 66
	grid6[6] = [bNorth, bEast, bSouth, bWest]
def scan_6_7(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_6_8, 86, dist)
	bEast = lbWest(nop, scan_east)(scan_7_7, 77, dist)
	bSouth = lbNorth(nop, scan_south)(scan_6_6, 66, dist)
	bWest = lbEast(nop, scan_west)(scan_5_7, 75, dist)
	if measure():
		TREASURE_POS[0] = 76
	grid6[7] = [bNorth, bEast, bSouth, bWest]
def scan_6_8(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_6_9, 96, dist)
	bEast = lbWest(nop, scan_east)(scan_7_8, 87, dist)
	bSouth = lbNorth(nop, scan_south)(scan_6_7, 76, dist)
	bWest = lbEast(nop, scan_west)(scan_5_8, 85, dist)
	if measure():
		TREASURE_POS[0] = 86
	grid6[8] = [bNorth, bEast, bSouth, bWest]
def scan_6_9(lbNorth, lbEast, lbSouth, lbWest, dist):
	bEast = lbWest(nop, scan_east)(scan_7_9, 97, dist)
	bSouth = lbNorth(nop, scan_south)(scan_6_8, 86, dist)
	bWest = lbEast(nop, scan_west)(scan_5_9, 95, dist)
	if measure():
		TREASURE_POS[0] = 96
	grid6[9] = [false, bEast, bSouth, bWest]
def scan_7_0(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_7_1, 17, dist)
	bEast = lbWest(nop, scan_east)(scan_8_0, 8, dist)
	bWest = lbEast(nop, scan_west)(scan_6_0, 6, dist)
	if measure():
		TREASURE_POS[0] = 7
	grid7[0] = [bNorth, bEast, false, bWest]
def scan_7_1(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_7_2, 27, dist)
	bEast = lbWest(nop, scan_east)(scan_8_1, 18, dist)
	bSouth = lbNorth(nop, scan_south)(scan_7_0, 7, dist)
	bWest = lbEast(nop, scan_west)(scan_6_1, 16, dist)
	if measure():
		TREASURE_POS[0] = 17
	grid7[1] = [bNorth, bEast, bSouth, bWest]
def scan_7_2(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_7_3, 37, dist)
	bEast = lbWest(nop, scan_east)(scan_8_2, 28, dist)
	bSouth = lbNorth(nop, scan_south)(scan_7_1, 17, dist)
	bWest = lbEast(nop, scan_west)(scan_6_2, 26, dist)
	if measure():
		TREASURE_POS[0] = 27
	grid7[2] = [bNorth, bEast, bSouth, bWest]
def scan_7_3(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_7_4, 47, dist)
	bEast = lbWest(nop, scan_east)(scan_8_3, 38, dist)
	bSouth = lbNorth(nop, scan_south)(scan_7_2, 27, dist)
	bWest = lbEast(nop, scan_west)(scan_6_3, 36, dist)
	if measure():
		TREASURE_POS[0] = 37
	grid7[3] = [bNorth, bEast, bSouth, bWest]
def scan_7_4(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_7_5, 57, dist)
	bEast = lbWest(nop, scan_east)(scan_8_4, 48, dist)
	bSouth = lbNorth(nop, scan_south)(scan_7_3, 37, dist)
	bWest = lbEast(nop, scan_west)(scan_6_4, 46, dist)
	if measure():
		TREASURE_POS[0] = 47
	grid7[4] = [bNorth, bEast, bSouth, bWest]
def scan_7_5(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_7_6, 67, dist)
	bEast = lbWest(nop, scan_east)(scan_8_5, 58, dist)
	bSouth = lbNorth(nop, scan_south)(scan_7_4, 47, dist)
	bWest = lbEast(nop, scan_west)(scan_6_5, 56, dist)
	if measure():
		TREASURE_POS[0] = 57
	grid7[5] = [bNorth, bEast, bSouth, bWest]
def scan_7_6(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_7_7, 77, dist)
	bEast = lbWest(nop, scan_east)(scan_8_6, 68, dist)
	bSouth = lbNorth(nop, scan_south)(scan_7_5, 57, dist)
	bWest = lbEast(nop, scan_west)(scan_6_6, 66, dist)
	if measure():
		TREASURE_POS[0] = 67
	grid7[6] = [bNorth, bEast, bSouth, bWest]
def scan_7_7(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_7_8, 87, dist)
	bEast = lbWest(nop, scan_east)(scan_8_7, 78, dist)
	bSouth = lbNorth(nop, scan_south)(scan_7_6, 67, dist)
	bWest = lbEast(nop, scan_west)(scan_6_7, 76, dist)
	if measure():
		TREASURE_POS[0] = 77
	grid7[7] = [bNorth, bEast, bSouth, bWest]
def scan_7_8(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_7_9, 97, dist)
	bEast = lbWest(nop, scan_east)(scan_8_8, 88, dist)
	bSouth = lbNorth(nop, scan_south)(scan_7_7, 77, dist)
	bWest = lbEast(nop, scan_west)(scan_6_8, 86, dist)
	if measure():
		TREASURE_POS[0] = 87
	grid7[8] = [bNorth, bEast, bSouth, bWest]
def scan_7_9(lbNorth, lbEast, lbSouth, lbWest, dist):
	bEast = lbWest(nop, scan_east)(scan_8_9, 98, dist)
	bSouth = lbNorth(nop, scan_south)(scan_7_8, 87, dist)
	bWest = lbEast(nop, scan_west)(scan_6_9, 96, dist)
	if measure():
		TREASURE_POS[0] = 97
	grid7[9] = [false, bEast, bSouth, bWest]
def scan_8_0(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_8_1, 18, dist)
	bEast = lbWest(nop, scan_east)(scan_9_0, 9, dist)
	bWest = lbEast(nop, scan_west)(scan_7_0, 7, dist)
	if measure():
		TREASURE_POS[0] = 8
	grid8[0] = [bNorth, bEast, false, bWest]
def scan_8_1(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_8_2, 28, dist)
	bEast = lbWest(nop, scan_east)(scan_9_1, 19, dist)
	bSouth = lbNorth(nop, scan_south)(scan_8_0, 8, dist)
	bWest = lbEast(nop, scan_west)(scan_7_1, 17, dist)
	if measure():
		TREASURE_POS[0] = 18
	grid8[1] = [bNorth, bEast, bSouth, bWest]
def scan_8_2(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_8_3, 38, dist)
	bEast = lbWest(nop, scan_east)(scan_9_2, 29, dist)
	bSouth = lbNorth(nop, scan_south)(scan_8_1, 18, dist)
	bWest = lbEast(nop, scan_west)(scan_7_2, 27, dist)
	if measure():
		TREASURE_POS[0] = 28
	grid8[2] = [bNorth, bEast, bSouth, bWest]
def scan_8_3(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_8_4, 48, dist)
	bEast = lbWest(nop, scan_east)(scan_9_3, 39, dist)
	bSouth = lbNorth(nop, scan_south)(scan_8_2, 28, dist)
	bWest = lbEast(nop, scan_west)(scan_7_3, 37, dist)
	if measure():
		TREASURE_POS[0] = 38
	grid8[3] = [bNorth, bEast, bSouth, bWest]
def scan_8_4(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_8_5, 58, dist)
	bEast = lbWest(nop, scan_east)(scan_9_4, 49, dist)
	bSouth = lbNorth(nop, scan_south)(scan_8_3, 38, dist)
	bWest = lbEast(nop, scan_west)(scan_7_4, 47, dist)
	if measure():
		TREASURE_POS[0] = 48
	grid8[4] = [bNorth, bEast, bSouth, bWest]
def scan_8_5(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_8_6, 68, dist)
	bEast = lbWest(nop, scan_east)(scan_9_5, 59, dist)
	bSouth = lbNorth(nop, scan_south)(scan_8_4, 48, dist)
	bWest = lbEast(nop, scan_west)(scan_7_5, 57, dist)
	if measure():
		TREASURE_POS[0] = 58
	grid8[5] = [bNorth, bEast, bSouth, bWest]
def scan_8_6(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_8_7, 78, dist)
	bEast = lbWest(nop, scan_east)(scan_9_6, 69, dist)
	bSouth = lbNorth(nop, scan_south)(scan_8_5, 58, dist)
	bWest = lbEast(nop, scan_west)(scan_7_6, 67, dist)
	if measure():
		TREASURE_POS[0] = 68
	grid8[6] = [bNorth, bEast, bSouth, bWest]
def scan_8_7(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_8_8, 88, dist)
	bEast = lbWest(nop, scan_east)(scan_9_7, 79, dist)
	bSouth = lbNorth(nop, scan_south)(scan_8_6, 68, dist)
	bWest = lbEast(nop, scan_west)(scan_7_7, 77, dist)
	if measure():
		TREASURE_POS[0] = 78
	grid8[7] = [bNorth, bEast, bSouth, bWest]
def scan_8_8(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_8_9, 98, dist)
	bEast = lbWest(nop, scan_east)(scan_9_8, 89, dist)
	bSouth = lbNorth(nop, scan_south)(scan_8_7, 78, dist)
	bWest = lbEast(nop, scan_west)(scan_7_8, 87, dist)
	if measure():
		TREASURE_POS[0] = 88
	grid8[8] = [bNorth, bEast, bSouth, bWest]
def scan_8_9(lbNorth, lbEast, lbSouth, lbWest, dist):
	bEast = lbWest(nop, scan_east)(scan_9_9, 99, dist)
	bSouth = lbNorth(nop, scan_south)(scan_8_8, 88, dist)
	bWest = lbEast(nop, scan_west)(scan_7_9, 97, dist)
	if measure():
		TREASURE_POS[0] = 98
	grid8[9] = [false, bEast, bSouth, bWest]
def scan_9_0(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_9_1, 19, dist)
	bWest = lbEast(nop, scan_west)(scan_8_0, 8, dist)
	if measure():
		TREASURE_POS[0] = 9
	grid9[0] = [bNorth, false, false, bWest]
def scan_9_1(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_9_2, 29, dist)
	bSouth = lbNorth(nop, scan_south)(scan_9_0, 9, dist)
	bWest = lbEast(nop, scan_west)(scan_8_1, 18, dist)
	if measure():
		TREASURE_POS[0] = 19
	grid9[1] = [bNorth, false, bSouth, bWest]
def scan_9_2(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_9_3, 39, dist)
	bSouth = lbNorth(nop, scan_south)(scan_9_1, 19, dist)
	bWest = lbEast(nop, scan_west)(scan_8_2, 28, dist)
	if measure():
		TREASURE_POS[0] = 29
	grid9[2] = [bNorth, false, bSouth, bWest]
def scan_9_3(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_9_4, 49, dist)
	bSouth = lbNorth(nop, scan_south)(scan_9_2, 29, dist)
	bWest = lbEast(nop, scan_west)(scan_8_3, 38, dist)
	if measure():
		TREASURE_POS[0] = 39
	grid9[3] = [bNorth, false, bSouth, bWest]
def scan_9_4(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_9_5, 59, dist)
	bSouth = lbNorth(nop, scan_south)(scan_9_3, 39, dist)
	bWest = lbEast(nop, scan_west)(scan_8_4, 48, dist)
	if measure():
		TREASURE_POS[0] = 49
	grid9[4] = [bNorth, false, bSouth, bWest]
def scan_9_5(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_9_6, 69, dist)
	bSouth = lbNorth(nop, scan_south)(scan_9_4, 49, dist)
	bWest = lbEast(nop, scan_west)(scan_8_5, 58, dist)
	if measure():
		TREASURE_POS[0] = 59
	grid9[5] = [bNorth, false, bSouth, bWest]
def scan_9_6(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_9_7, 79, dist)
	bSouth = lbNorth(nop, scan_south)(scan_9_5, 59, dist)
	bWest = lbEast(nop, scan_west)(scan_8_6, 68, dist)
	if measure():
		TREASURE_POS[0] = 69
	grid9[6] = [bNorth, false, bSouth, bWest]
def scan_9_7(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_9_8, 89, dist)
	bSouth = lbNorth(nop, scan_south)(scan_9_6, 69, dist)
	bWest = lbEast(nop, scan_west)(scan_8_7, 78, dist)
	if measure():
		TREASURE_POS[0] = 79
	grid9[7] = [bNorth, false, bSouth, bWest]
def scan_9_8(lbNorth, lbEast, lbSouth, lbWest, dist):
	bNorth = lbSouth(nop, scan_north)(scan_9_9, 99, dist)
	bSouth = lbNorth(nop, scan_south)(scan_9_7, 79, dist)
	bWest = lbEast(nop, scan_west)(scan_8_8, 88, dist)
	if measure():
		TREASURE_POS[0] = 89
	grid9[8] = [bNorth, false, bSouth, bWest]
def scan_9_9(lbNorth, lbEast, lbSouth, lbWest, dist):
	bSouth = lbNorth(nop, scan_south)(scan_9_8, 89, dist)
	bWest = lbEast(nop, scan_west)(scan_8_9, 98, dist)
	if measure():
		TREASURE_POS[0] = 99
	grid9[9] = [false, false, bSouth, bWest]
	