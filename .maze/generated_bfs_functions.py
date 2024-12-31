def bfs_0_0(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_0_1)
	bEast = lbWest(nop, bfs_east)(bfs_1_0)
	grid0[0] = [bNorth, bEast, false, false]
def bfs_0_1(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_0_2)
	bEast = lbWest(nop, bfs_east)(bfs_1_1)
	bSouth = lbNorth(nop, bfs_south)(bfs_0_0)
	grid0[1] = [bNorth, bEast, bSouth, false]
def bfs_0_2(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_0_3)
	bEast = lbWest(nop, bfs_east)(bfs_1_2)
	bSouth = lbNorth(nop, bfs_south)(bfs_0_1)
	grid0[2] = [bNorth, bEast, bSouth, false]
def bfs_0_3(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_0_4)
	bEast = lbWest(nop, bfs_east)(bfs_1_3)
	bSouth = lbNorth(nop, bfs_south)(bfs_0_2)
	grid0[3] = [bNorth, bEast, bSouth, false]
def bfs_0_4(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_0_5)
	bEast = lbWest(nop, bfs_east)(bfs_1_4)
	bSouth = lbNorth(nop, bfs_south)(bfs_0_3)
	grid0[4] = [bNorth, bEast, bSouth, false]
def bfs_0_5(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_0_6)
	bEast = lbWest(nop, bfs_east)(bfs_1_5)
	bSouth = lbNorth(nop, bfs_south)(bfs_0_4)
	grid0[5] = [bNorth, bEast, bSouth, false]
def bfs_0_6(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_0_7)
	bEast = lbWest(nop, bfs_east)(bfs_1_6)
	bSouth = lbNorth(nop, bfs_south)(bfs_0_5)
	grid0[6] = [bNorth, bEast, bSouth, false]
def bfs_0_7(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_0_8)
	bEast = lbWest(nop, bfs_east)(bfs_1_7)
	bSouth = lbNorth(nop, bfs_south)(bfs_0_6)
	grid0[7] = [bNorth, bEast, bSouth, false]
def bfs_0_8(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_0_9)
	bEast = lbWest(nop, bfs_east)(bfs_1_8)
	bSouth = lbNorth(nop, bfs_south)(bfs_0_7)
	grid0[8] = [bNorth, bEast, bSouth, false]
def bfs_0_9(lbNorth, lbEast, lbSouth, lbWest):
	bEast = lbWest(nop, bfs_east)(bfs_1_9)
	bSouth = lbNorth(nop, bfs_south)(bfs_0_8)
	grid0[9] = [false, bEast, bSouth, false]
def bfs_1_0(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_1_1)
	bEast = lbWest(nop, bfs_east)(bfs_2_0)
	bWest = lbEast(nop, bfs_west)(bfs_0_0)
	grid1[0] = [bNorth, bEast, false, bWest]
def bfs_1_1(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_1_2)
	bEast = lbWest(nop, bfs_east)(bfs_2_1)
	bSouth = lbNorth(nop, bfs_south)(bfs_1_0)
	bWest = lbEast(nop, bfs_west)(bfs_0_1)
	grid1[1] = [bNorth, bEast, bSouth, bWest]
def bfs_1_2(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_1_3)
	bEast = lbWest(nop, bfs_east)(bfs_2_2)
	bSouth = lbNorth(nop, bfs_south)(bfs_1_1)
	bWest = lbEast(nop, bfs_west)(bfs_0_2)
	grid1[2] = [bNorth, bEast, bSouth, bWest]
def bfs_1_3(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_1_4)
	bEast = lbWest(nop, bfs_east)(bfs_2_3)
	bSouth = lbNorth(nop, bfs_south)(bfs_1_2)
	bWest = lbEast(nop, bfs_west)(bfs_0_3)
	grid1[3] = [bNorth, bEast, bSouth, bWest]
def bfs_1_4(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_1_5)
	bEast = lbWest(nop, bfs_east)(bfs_2_4)
	bSouth = lbNorth(nop, bfs_south)(bfs_1_3)
	bWest = lbEast(nop, bfs_west)(bfs_0_4)
	grid1[4] = [bNorth, bEast, bSouth, bWest]
def bfs_1_5(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_1_6)
	bEast = lbWest(nop, bfs_east)(bfs_2_5)
	bSouth = lbNorth(nop, bfs_south)(bfs_1_4)
	bWest = lbEast(nop, bfs_west)(bfs_0_5)
	grid1[5] = [bNorth, bEast, bSouth, bWest]
def bfs_1_6(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_1_7)
	bEast = lbWest(nop, bfs_east)(bfs_2_6)
	bSouth = lbNorth(nop, bfs_south)(bfs_1_5)
	bWest = lbEast(nop, bfs_west)(bfs_0_6)
	grid1[6] = [bNorth, bEast, bSouth, bWest]
def bfs_1_7(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_1_8)
	bEast = lbWest(nop, bfs_east)(bfs_2_7)
	bSouth = lbNorth(nop, bfs_south)(bfs_1_6)
	bWest = lbEast(nop, bfs_west)(bfs_0_7)
	grid1[7] = [bNorth, bEast, bSouth, bWest]
def bfs_1_8(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_1_9)
	bEast = lbWest(nop, bfs_east)(bfs_2_8)
	bSouth = lbNorth(nop, bfs_south)(bfs_1_7)
	bWest = lbEast(nop, bfs_west)(bfs_0_8)
	grid1[8] = [bNorth, bEast, bSouth, bWest]
def bfs_1_9(lbNorth, lbEast, lbSouth, lbWest):
	bEast = lbWest(nop, bfs_east)(bfs_2_9)
	bSouth = lbNorth(nop, bfs_south)(bfs_1_8)
	bWest = lbEast(nop, bfs_west)(bfs_0_9)
	grid1[9] = [false, bEast, bSouth, bWest]
def bfs_2_0(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_2_1)
	bEast = lbWest(nop, bfs_east)(bfs_3_0)
	bWest = lbEast(nop, bfs_west)(bfs_1_0)
	grid2[0] = [bNorth, bEast, false, bWest]
def bfs_2_1(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_2_2)
	bEast = lbWest(nop, bfs_east)(bfs_3_1)
	bSouth = lbNorth(nop, bfs_south)(bfs_2_0)
	bWest = lbEast(nop, bfs_west)(bfs_1_1)
	grid2[1] = [bNorth, bEast, bSouth, bWest]
def bfs_2_2(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_2_3)
	bEast = lbWest(nop, bfs_east)(bfs_3_2)
	bSouth = lbNorth(nop, bfs_south)(bfs_2_1)
	bWest = lbEast(nop, bfs_west)(bfs_1_2)
	grid2[2] = [bNorth, bEast, bSouth, bWest]
def bfs_2_3(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_2_4)
	bEast = lbWest(nop, bfs_east)(bfs_3_3)
	bSouth = lbNorth(nop, bfs_south)(bfs_2_2)
	bWest = lbEast(nop, bfs_west)(bfs_1_3)
	grid2[3] = [bNorth, bEast, bSouth, bWest]
def bfs_2_4(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_2_5)
	bEast = lbWest(nop, bfs_east)(bfs_3_4)
	bSouth = lbNorth(nop, bfs_south)(bfs_2_3)
	bWest = lbEast(nop, bfs_west)(bfs_1_4)
	grid2[4] = [bNorth, bEast, bSouth, bWest]
def bfs_2_5(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_2_6)
	bEast = lbWest(nop, bfs_east)(bfs_3_5)
	bSouth = lbNorth(nop, bfs_south)(bfs_2_4)
	bWest = lbEast(nop, bfs_west)(bfs_1_5)
	grid2[5] = [bNorth, bEast, bSouth, bWest]
def bfs_2_6(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_2_7)
	bEast = lbWest(nop, bfs_east)(bfs_3_6)
	bSouth = lbNorth(nop, bfs_south)(bfs_2_5)
	bWest = lbEast(nop, bfs_west)(bfs_1_6)
	grid2[6] = [bNorth, bEast, bSouth, bWest]
def bfs_2_7(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_2_8)
	bEast = lbWest(nop, bfs_east)(bfs_3_7)
	bSouth = lbNorth(nop, bfs_south)(bfs_2_6)
	bWest = lbEast(nop, bfs_west)(bfs_1_7)
	grid2[7] = [bNorth, bEast, bSouth, bWest]
def bfs_2_8(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_2_9)
	bEast = lbWest(nop, bfs_east)(bfs_3_8)
	bSouth = lbNorth(nop, bfs_south)(bfs_2_7)
	bWest = lbEast(nop, bfs_west)(bfs_1_8)
	grid2[8] = [bNorth, bEast, bSouth, bWest]
def bfs_2_9(lbNorth, lbEast, lbSouth, lbWest):
	bEast = lbWest(nop, bfs_east)(bfs_3_9)
	bSouth = lbNorth(nop, bfs_south)(bfs_2_8)
	bWest = lbEast(nop, bfs_west)(bfs_1_9)
	grid2[9] = [false, bEast, bSouth, bWest]
def bfs_3_0(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_3_1)
	bEast = lbWest(nop, bfs_east)(bfs_4_0)
	bWest = lbEast(nop, bfs_west)(bfs_2_0)
	grid3[0] = [bNorth, bEast, false, bWest]
def bfs_3_1(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_3_2)
	bEast = lbWest(nop, bfs_east)(bfs_4_1)
	bSouth = lbNorth(nop, bfs_south)(bfs_3_0)
	bWest = lbEast(nop, bfs_west)(bfs_2_1)
	grid3[1] = [bNorth, bEast, bSouth, bWest]
def bfs_3_2(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_3_3)
	bEast = lbWest(nop, bfs_east)(bfs_4_2)
	bSouth = lbNorth(nop, bfs_south)(bfs_3_1)
	bWest = lbEast(nop, bfs_west)(bfs_2_2)
	grid3[2] = [bNorth, bEast, bSouth, bWest]
def bfs_3_3(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_3_4)
	bEast = lbWest(nop, bfs_east)(bfs_4_3)
	bSouth = lbNorth(nop, bfs_south)(bfs_3_2)
	bWest = lbEast(nop, bfs_west)(bfs_2_3)
	grid3[3] = [bNorth, bEast, bSouth, bWest]
def bfs_3_4(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_3_5)
	bEast = lbWest(nop, bfs_east)(bfs_4_4)
	bSouth = lbNorth(nop, bfs_south)(bfs_3_3)
	bWest = lbEast(nop, bfs_west)(bfs_2_4)
	grid3[4] = [bNorth, bEast, bSouth, bWest]
def bfs_3_5(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_3_6)
	bEast = lbWest(nop, bfs_east)(bfs_4_5)
	bSouth = lbNorth(nop, bfs_south)(bfs_3_4)
	bWest = lbEast(nop, bfs_west)(bfs_2_5)
	grid3[5] = [bNorth, bEast, bSouth, bWest]
def bfs_3_6(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_3_7)
	bEast = lbWest(nop, bfs_east)(bfs_4_6)
	bSouth = lbNorth(nop, bfs_south)(bfs_3_5)
	bWest = lbEast(nop, bfs_west)(bfs_2_6)
	grid3[6] = [bNorth, bEast, bSouth, bWest]
def bfs_3_7(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_3_8)
	bEast = lbWest(nop, bfs_east)(bfs_4_7)
	bSouth = lbNorth(nop, bfs_south)(bfs_3_6)
	bWest = lbEast(nop, bfs_west)(bfs_2_7)
	grid3[7] = [bNorth, bEast, bSouth, bWest]
def bfs_3_8(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_3_9)
	bEast = lbWest(nop, bfs_east)(bfs_4_8)
	bSouth = lbNorth(nop, bfs_south)(bfs_3_7)
	bWest = lbEast(nop, bfs_west)(bfs_2_8)
	grid3[8] = [bNorth, bEast, bSouth, bWest]
def bfs_3_9(lbNorth, lbEast, lbSouth, lbWest):
	bEast = lbWest(nop, bfs_east)(bfs_4_9)
	bSouth = lbNorth(nop, bfs_south)(bfs_3_8)
	bWest = lbEast(nop, bfs_west)(bfs_2_9)
	grid3[9] = [false, bEast, bSouth, bWest]
def bfs_4_0(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_4_1)
	bEast = lbWest(nop, bfs_east)(bfs_5_0)
	bWest = lbEast(nop, bfs_west)(bfs_3_0)
	grid4[0] = [bNorth, bEast, false, bWest]
def bfs_4_1(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_4_2)
	bEast = lbWest(nop, bfs_east)(bfs_5_1)
	bSouth = lbNorth(nop, bfs_south)(bfs_4_0)
	bWest = lbEast(nop, bfs_west)(bfs_3_1)
	grid4[1] = [bNorth, bEast, bSouth, bWest]
def bfs_4_2(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_4_3)
	bEast = lbWest(nop, bfs_east)(bfs_5_2)
	bSouth = lbNorth(nop, bfs_south)(bfs_4_1)
	bWest = lbEast(nop, bfs_west)(bfs_3_2)
	grid4[2] = [bNorth, bEast, bSouth, bWest]
def bfs_4_3(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_4_4)
	bEast = lbWest(nop, bfs_east)(bfs_5_3)
	bSouth = lbNorth(nop, bfs_south)(bfs_4_2)
	bWest = lbEast(nop, bfs_west)(bfs_3_3)
	grid4[3] = [bNorth, bEast, bSouth, bWest]
def bfs_4_4(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_4_5)
	bEast = lbWest(nop, bfs_east)(bfs_5_4)
	bSouth = lbNorth(nop, bfs_south)(bfs_4_3)
	bWest = lbEast(nop, bfs_west)(bfs_3_4)
	grid4[4] = [bNorth, bEast, bSouth, bWest]
def bfs_4_5(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_4_6)
	bEast = lbWest(nop, bfs_east)(bfs_5_5)
	bSouth = lbNorth(nop, bfs_south)(bfs_4_4)
	bWest = lbEast(nop, bfs_west)(bfs_3_5)
	grid4[5] = [bNorth, bEast, bSouth, bWest]
def bfs_4_6(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_4_7)
	bEast = lbWest(nop, bfs_east)(bfs_5_6)
	bSouth = lbNorth(nop, bfs_south)(bfs_4_5)
	bWest = lbEast(nop, bfs_west)(bfs_3_6)
	grid4[6] = [bNorth, bEast, bSouth, bWest]
def bfs_4_7(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_4_8)
	bEast = lbWest(nop, bfs_east)(bfs_5_7)
	bSouth = lbNorth(nop, bfs_south)(bfs_4_6)
	bWest = lbEast(nop, bfs_west)(bfs_3_7)
	grid4[7] = [bNorth, bEast, bSouth, bWest]
def bfs_4_8(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_4_9)
	bEast = lbWest(nop, bfs_east)(bfs_5_8)
	bSouth = lbNorth(nop, bfs_south)(bfs_4_7)
	bWest = lbEast(nop, bfs_west)(bfs_3_8)
	grid4[8] = [bNorth, bEast, bSouth, bWest]
def bfs_4_9(lbNorth, lbEast, lbSouth, lbWest):
	bEast = lbWest(nop, bfs_east)(bfs_5_9)
	bSouth = lbNorth(nop, bfs_south)(bfs_4_8)
	bWest = lbEast(nop, bfs_west)(bfs_3_9)
	grid4[9] = [false, bEast, bSouth, bWest]
def bfs_5_0(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_5_1)
	bEast = lbWest(nop, bfs_east)(bfs_6_0)
	bWest = lbEast(nop, bfs_west)(bfs_4_0)
	grid5[0] = [bNorth, bEast, false, bWest]
def bfs_5_1(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_5_2)
	bEast = lbWest(nop, bfs_east)(bfs_6_1)
	bSouth = lbNorth(nop, bfs_south)(bfs_5_0)
	bWest = lbEast(nop, bfs_west)(bfs_4_1)
	grid5[1] = [bNorth, bEast, bSouth, bWest]
def bfs_5_2(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_5_3)
	bEast = lbWest(nop, bfs_east)(bfs_6_2)
	bSouth = lbNorth(nop, bfs_south)(bfs_5_1)
	bWest = lbEast(nop, bfs_west)(bfs_4_2)
	grid5[2] = [bNorth, bEast, bSouth, bWest]
def bfs_5_3(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_5_4)
	bEast = lbWest(nop, bfs_east)(bfs_6_3)
	bSouth = lbNorth(nop, bfs_south)(bfs_5_2)
	bWest = lbEast(nop, bfs_west)(bfs_4_3)
	grid5[3] = [bNorth, bEast, bSouth, bWest]
def bfs_5_4(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_5_5)
	bEast = lbWest(nop, bfs_east)(bfs_6_4)
	bSouth = lbNorth(nop, bfs_south)(bfs_5_3)
	bWest = lbEast(nop, bfs_west)(bfs_4_4)
	grid5[4] = [bNorth, bEast, bSouth, bWest]
def bfs_5_5(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_5_6)
	bEast = lbWest(nop, bfs_east)(bfs_6_5)
	bSouth = lbNorth(nop, bfs_south)(bfs_5_4)
	bWest = lbEast(nop, bfs_west)(bfs_4_5)
	grid5[5] = [bNorth, bEast, bSouth, bWest]
def bfs_5_6(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_5_7)
	bEast = lbWest(nop, bfs_east)(bfs_6_6)
	bSouth = lbNorth(nop, bfs_south)(bfs_5_5)
	bWest = lbEast(nop, bfs_west)(bfs_4_6)
	grid5[6] = [bNorth, bEast, bSouth, bWest]
def bfs_5_7(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_5_8)
	bEast = lbWest(nop, bfs_east)(bfs_6_7)
	bSouth = lbNorth(nop, bfs_south)(bfs_5_6)
	bWest = lbEast(nop, bfs_west)(bfs_4_7)
	grid5[7] = [bNorth, bEast, bSouth, bWest]
def bfs_5_8(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_5_9)
	bEast = lbWest(nop, bfs_east)(bfs_6_8)
	bSouth = lbNorth(nop, bfs_south)(bfs_5_7)
	bWest = lbEast(nop, bfs_west)(bfs_4_8)
	grid5[8] = [bNorth, bEast, bSouth, bWest]
def bfs_5_9(lbNorth, lbEast, lbSouth, lbWest):
	bEast = lbWest(nop, bfs_east)(bfs_6_9)
	bSouth = lbNorth(nop, bfs_south)(bfs_5_8)
	bWest = lbEast(nop, bfs_west)(bfs_4_9)
	grid5[9] = [false, bEast, bSouth, bWest]
def bfs_6_0(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_6_1)
	bEast = lbWest(nop, bfs_east)(bfs_7_0)
	bWest = lbEast(nop, bfs_west)(bfs_5_0)
	grid6[0] = [bNorth, bEast, false, bWest]
def bfs_6_1(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_6_2)
	bEast = lbWest(nop, bfs_east)(bfs_7_1)
	bSouth = lbNorth(nop, bfs_south)(bfs_6_0)
	bWest = lbEast(nop, bfs_west)(bfs_5_1)
	grid6[1] = [bNorth, bEast, bSouth, bWest]
def bfs_6_2(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_6_3)
	bEast = lbWest(nop, bfs_east)(bfs_7_2)
	bSouth = lbNorth(nop, bfs_south)(bfs_6_1)
	bWest = lbEast(nop, bfs_west)(bfs_5_2)
	grid6[2] = [bNorth, bEast, bSouth, bWest]
def bfs_6_3(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_6_4)
	bEast = lbWest(nop, bfs_east)(bfs_7_3)
	bSouth = lbNorth(nop, bfs_south)(bfs_6_2)
	bWest = lbEast(nop, bfs_west)(bfs_5_3)
	grid6[3] = [bNorth, bEast, bSouth, bWest]
def bfs_6_4(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_6_5)
	bEast = lbWest(nop, bfs_east)(bfs_7_4)
	bSouth = lbNorth(nop, bfs_south)(bfs_6_3)
	bWest = lbEast(nop, bfs_west)(bfs_5_4)
	grid6[4] = [bNorth, bEast, bSouth, bWest]
def bfs_6_5(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_6_6)
	bEast = lbWest(nop, bfs_east)(bfs_7_5)
	bSouth = lbNorth(nop, bfs_south)(bfs_6_4)
	bWest = lbEast(nop, bfs_west)(bfs_5_5)
	grid6[5] = [bNorth, bEast, bSouth, bWest]
def bfs_6_6(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_6_7)
	bEast = lbWest(nop, bfs_east)(bfs_7_6)
	bSouth = lbNorth(nop, bfs_south)(bfs_6_5)
	bWest = lbEast(nop, bfs_west)(bfs_5_6)
	grid6[6] = [bNorth, bEast, bSouth, bWest]
def bfs_6_7(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_6_8)
	bEast = lbWest(nop, bfs_east)(bfs_7_7)
	bSouth = lbNorth(nop, bfs_south)(bfs_6_6)
	bWest = lbEast(nop, bfs_west)(bfs_5_7)
	grid6[7] = [bNorth, bEast, bSouth, bWest]
def bfs_6_8(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_6_9)
	bEast = lbWest(nop, bfs_east)(bfs_7_8)
	bSouth = lbNorth(nop, bfs_south)(bfs_6_7)
	bWest = lbEast(nop, bfs_west)(bfs_5_8)
	grid6[8] = [bNorth, bEast, bSouth, bWest]
def bfs_6_9(lbNorth, lbEast, lbSouth, lbWest):
	bEast = lbWest(nop, bfs_east)(bfs_7_9)
	bSouth = lbNorth(nop, bfs_south)(bfs_6_8)
	bWest = lbEast(nop, bfs_west)(bfs_5_9)
	grid6[9] = [false, bEast, bSouth, bWest]
def bfs_7_0(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_7_1)
	bEast = lbWest(nop, bfs_east)(bfs_8_0)
	bWest = lbEast(nop, bfs_west)(bfs_6_0)
	grid7[0] = [bNorth, bEast, false, bWest]
def bfs_7_1(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_7_2)
	bEast = lbWest(nop, bfs_east)(bfs_8_1)
	bSouth = lbNorth(nop, bfs_south)(bfs_7_0)
	bWest = lbEast(nop, bfs_west)(bfs_6_1)
	grid7[1] = [bNorth, bEast, bSouth, bWest]
def bfs_7_2(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_7_3)
	bEast = lbWest(nop, bfs_east)(bfs_8_2)
	bSouth = lbNorth(nop, bfs_south)(bfs_7_1)
	bWest = lbEast(nop, bfs_west)(bfs_6_2)
	grid7[2] = [bNorth, bEast, bSouth, bWest]
def bfs_7_3(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_7_4)
	bEast = lbWest(nop, bfs_east)(bfs_8_3)
	bSouth = lbNorth(nop, bfs_south)(bfs_7_2)
	bWest = lbEast(nop, bfs_west)(bfs_6_3)
	grid7[3] = [bNorth, bEast, bSouth, bWest]
def bfs_7_4(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_7_5)
	bEast = lbWest(nop, bfs_east)(bfs_8_4)
	bSouth = lbNorth(nop, bfs_south)(bfs_7_3)
	bWest = lbEast(nop, bfs_west)(bfs_6_4)
	grid7[4] = [bNorth, bEast, bSouth, bWest]
def bfs_7_5(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_7_6)
	bEast = lbWest(nop, bfs_east)(bfs_8_5)
	bSouth = lbNorth(nop, bfs_south)(bfs_7_4)
	bWest = lbEast(nop, bfs_west)(bfs_6_5)
	grid7[5] = [bNorth, bEast, bSouth, bWest]
def bfs_7_6(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_7_7)
	bEast = lbWest(nop, bfs_east)(bfs_8_6)
	bSouth = lbNorth(nop, bfs_south)(bfs_7_5)
	bWest = lbEast(nop, bfs_west)(bfs_6_6)
	grid7[6] = [bNorth, bEast, bSouth, bWest]
def bfs_7_7(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_7_8)
	bEast = lbWest(nop, bfs_east)(bfs_8_7)
	bSouth = lbNorth(nop, bfs_south)(bfs_7_6)
	bWest = lbEast(nop, bfs_west)(bfs_6_7)
	grid7[7] = [bNorth, bEast, bSouth, bWest]
def bfs_7_8(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_7_9)
	bEast = lbWest(nop, bfs_east)(bfs_8_8)
	bSouth = lbNorth(nop, bfs_south)(bfs_7_7)
	bWest = lbEast(nop, bfs_west)(bfs_6_8)
	grid7[8] = [bNorth, bEast, bSouth, bWest]
def bfs_7_9(lbNorth, lbEast, lbSouth, lbWest):
	bEast = lbWest(nop, bfs_east)(bfs_8_9)
	bSouth = lbNorth(nop, bfs_south)(bfs_7_8)
	bWest = lbEast(nop, bfs_west)(bfs_6_9)
	grid7[9] = [false, bEast, bSouth, bWest]
def bfs_8_0(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_8_1)
	bEast = lbWest(nop, bfs_east)(bfs_9_0)
	bWest = lbEast(nop, bfs_west)(bfs_7_0)
	grid8[0] = [bNorth, bEast, false, bWest]
def bfs_8_1(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_8_2)
	bEast = lbWest(nop, bfs_east)(bfs_9_1)
	bSouth = lbNorth(nop, bfs_south)(bfs_8_0)
	bWest = lbEast(nop, bfs_west)(bfs_7_1)
	grid8[1] = [bNorth, bEast, bSouth, bWest]
def bfs_8_2(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_8_3)
	bEast = lbWest(nop, bfs_east)(bfs_9_2)
	bSouth = lbNorth(nop, bfs_south)(bfs_8_1)
	bWest = lbEast(nop, bfs_west)(bfs_7_2)
	grid8[2] = [bNorth, bEast, bSouth, bWest]
def bfs_8_3(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_8_4)
	bEast = lbWest(nop, bfs_east)(bfs_9_3)
	bSouth = lbNorth(nop, bfs_south)(bfs_8_2)
	bWest = lbEast(nop, bfs_west)(bfs_7_3)
	grid8[3] = [bNorth, bEast, bSouth, bWest]
def bfs_8_4(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_8_5)
	bEast = lbWest(nop, bfs_east)(bfs_9_4)
	bSouth = lbNorth(nop, bfs_south)(bfs_8_3)
	bWest = lbEast(nop, bfs_west)(bfs_7_4)
	grid8[4] = [bNorth, bEast, bSouth, bWest]
def bfs_8_5(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_8_6)
	bEast = lbWest(nop, bfs_east)(bfs_9_5)
	bSouth = lbNorth(nop, bfs_south)(bfs_8_4)
	bWest = lbEast(nop, bfs_west)(bfs_7_5)
	grid8[5] = [bNorth, bEast, bSouth, bWest]
def bfs_8_6(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_8_7)
	bEast = lbWest(nop, bfs_east)(bfs_9_6)
	bSouth = lbNorth(nop, bfs_south)(bfs_8_5)
	bWest = lbEast(nop, bfs_west)(bfs_7_6)
	grid8[6] = [bNorth, bEast, bSouth, bWest]
def bfs_8_7(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_8_8)
	bEast = lbWest(nop, bfs_east)(bfs_9_7)
	bSouth = lbNorth(nop, bfs_south)(bfs_8_6)
	bWest = lbEast(nop, bfs_west)(bfs_7_7)
	grid8[7] = [bNorth, bEast, bSouth, bWest]
def bfs_8_8(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_8_9)
	bEast = lbWest(nop, bfs_east)(bfs_9_8)
	bSouth = lbNorth(nop, bfs_south)(bfs_8_7)
	bWest = lbEast(nop, bfs_west)(bfs_7_8)
	grid8[8] = [bNorth, bEast, bSouth, bWest]
def bfs_8_9(lbNorth, lbEast, lbSouth, lbWest):
	bEast = lbWest(nop, bfs_east)(bfs_9_9)
	bSouth = lbNorth(nop, bfs_south)(bfs_8_8)
	bWest = lbEast(nop, bfs_west)(bfs_7_9)
	grid8[9] = [false, bEast, bSouth, bWest]
def bfs_9_0(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_9_1)
	bWest = lbEast(nop, bfs_west)(bfs_8_0)
	grid9[0] = [bNorth, false, false, bWest]
def bfs_9_1(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_9_2)
	bSouth = lbNorth(nop, bfs_south)(bfs_9_0)
	bWest = lbEast(nop, bfs_west)(bfs_8_1)
	grid9[1] = [bNorth, false, bSouth, bWest]
def bfs_9_2(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_9_3)
	bSouth = lbNorth(nop, bfs_south)(bfs_9_1)
	bWest = lbEast(nop, bfs_west)(bfs_8_2)
	grid9[2] = [bNorth, false, bSouth, bWest]
def bfs_9_3(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_9_4)
	bSouth = lbNorth(nop, bfs_south)(bfs_9_2)
	bWest = lbEast(nop, bfs_west)(bfs_8_3)
	grid9[3] = [bNorth, false, bSouth, bWest]
def bfs_9_4(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_9_5)
	bSouth = lbNorth(nop, bfs_south)(bfs_9_3)
	bWest = lbEast(nop, bfs_west)(bfs_8_4)
	grid9[4] = [bNorth, false, bSouth, bWest]
def bfs_9_5(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_9_6)
	bSouth = lbNorth(nop, bfs_south)(bfs_9_4)
	bWest = lbEast(nop, bfs_west)(bfs_8_5)
	grid9[5] = [bNorth, false, bSouth, bWest]
def bfs_9_6(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_9_7)
	bSouth = lbNorth(nop, bfs_south)(bfs_9_5)
	bWest = lbEast(nop, bfs_west)(bfs_8_6)
	grid9[6] = [bNorth, false, bSouth, bWest]
def bfs_9_7(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_9_8)
	bSouth = lbNorth(nop, bfs_south)(bfs_9_6)
	bWest = lbEast(nop, bfs_west)(bfs_8_7)
	grid9[7] = [bNorth, false, bSouth, bWest]
def bfs_9_8(lbNorth, lbEast, lbSouth, lbWest):
	bNorth = lbSouth(nop, bfs_north)(bfs_9_9)
	bSouth = lbNorth(nop, bfs_south)(bfs_9_7)
	bWest = lbEast(nop, bfs_west)(bfs_8_8)
	grid9[8] = [bNorth, false, bSouth, bWest]
def bfs_9_9(lbNorth, lbEast, lbSouth, lbWest):
	bSouth = lbNorth(nop, bfs_south)(bfs_9_8)
	bWest = lbEast(nop, bfs_west)(bfs_8_9)
	grid9[9] = [false, false, bSouth, bWest]
