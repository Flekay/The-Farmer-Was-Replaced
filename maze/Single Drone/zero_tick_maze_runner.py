def true(x, y):
	return x

def false(x, y):
	return y

def Not(x):
	return x(false, true)

def And(x, y):
	return x(y, false)

def And3(x, y, z = true):
	return x(y(z, false), false)

def And4(x, y, z = true, i = true):
	return x(y(z(i, false), false), false)

def And5(x, y, z = true, i = true, j = true):
	return x(y(z(i(j, false), false), false), false)

def And10(x, y, z, i, j, k, a, b, c, d):
	return And(And5(x, y, z, i, j), And5(k, a, b, c, d))

def Or(x, y):
	return x(true, y)

def Or3(x, y, z = false):
	return x(true, y(true, z(true, false)))

def Or4(x, y, z = false, i = false):
	return x(true, y(true, z(true, i(true, false))))

def Or5(x, y, z = false, i = false, j = false):
	return x(true, y(true, z(true, i(true, j(true, false)))))

def Or10(x, y, z, i, j, k, a, b, c, d):
	return Or(Or5(x, y, z, i, j), Or5(k, a, b, c, d))

def Nand(x, y):
	return x(Not(y), true)

def Nor(x, y):
	return x(false, Not(y))

def Xor(x, y):
	return x(Not(y), y)

def Encoder4bit(x, y, z, i):
	return x(y(z(i(15, 14), i(13, 12)), z(i(11, 10), i(9, 8))),
	y(z(i(7, 6), i(5, 4)), z(i(3, 2), i(1, 0))))

def alt_move_north():
	if move(North):
		return true
	else:
		return false

def alt_move_east():
	if move(East):
		return true
	else:
		return false

def alt_move_south():
	if move(South):
		return true
	else:
		return false

def alt_move_west():
	if move(West):
		return true
	else:
		return false

def dud():
	return false

def nothing(x = 0, y = 0, z = 0):
    return False

def check_north_wall():
    return drone_at_0_0(vert_wall_0_0, drone_at_1_0(vert_wall_1_0, drone_at_2_0(vert_wall_2_0, drone_at_3_0(vert_wall_3_0, drone_at_4_0(vert_wall_4_0, drone_at_5_0(vert_wall_5_0, drone_at_6_0(vert_wall_6_0, drone_at_7_0(vert_wall_7_0, drone_at_8_0(vert_wall_8_0, drone_at_9_0(vert_wall_9_0,
    drone_at_0_1(vert_wall_0_1, drone_at_1_1(vert_wall_1_1, drone_at_2_1(vert_wall_2_1, drone_at_3_1(vert_wall_3_1, drone_at_4_1(vert_wall_4_1, drone_at_5_1(vert_wall_5_1, drone_at_6_1(vert_wall_6_1, drone_at_7_1(vert_wall_7_1, drone_at_8_1(vert_wall_8_1, drone_at_9_1(vert_wall_9_1,
    drone_at_0_2(vert_wall_0_2, drone_at_1_2(vert_wall_1_2, drone_at_2_2(vert_wall_2_2, drone_at_3_2(vert_wall_3_2, drone_at_4_2(vert_wall_4_2, drone_at_5_2(vert_wall_5_2, drone_at_6_2(vert_wall_6_2, drone_at_7_2(vert_wall_7_2, drone_at_8_2(vert_wall_8_2, drone_at_9_2(vert_wall_9_2,
    drone_at_0_3(vert_wall_0_3, drone_at_1_3(vert_wall_1_3, drone_at_2_3(vert_wall_2_3, drone_at_3_3(vert_wall_3_3, drone_at_4_3(vert_wall_4_3, drone_at_5_3(vert_wall_5_3, drone_at_6_3(vert_wall_6_3, drone_at_7_3(vert_wall_7_3, drone_at_8_3(vert_wall_8_3, drone_at_9_3(vert_wall_9_3,
    drone_at_0_4(vert_wall_0_4, drone_at_1_4(vert_wall_1_4, drone_at_2_4(vert_wall_2_4, drone_at_3_4(vert_wall_3_4, drone_at_4_4(vert_wall_4_4, drone_at_5_4(vert_wall_5_4, drone_at_6_4(vert_wall_6_4, drone_at_7_4(vert_wall_7_4, drone_at_8_4(vert_wall_8_4, drone_at_9_4(vert_wall_9_4,
    drone_at_0_5(vert_wall_0_5, drone_at_1_5(vert_wall_1_5, drone_at_2_5(vert_wall_2_5, drone_at_3_5(vert_wall_3_5, drone_at_4_5(vert_wall_4_5, drone_at_5_5(vert_wall_5_5, drone_at_6_5(vert_wall_6_5, drone_at_7_5(vert_wall_7_5, drone_at_8_5(vert_wall_8_5, drone_at_9_5(vert_wall_9_5,
    drone_at_0_6(vert_wall_0_6, drone_at_1_6(vert_wall_1_6, drone_at_2_6(vert_wall_2_6, drone_at_3_6(vert_wall_3_6, drone_at_4_6(vert_wall_4_6, drone_at_5_6(vert_wall_5_6, drone_at_6_6(vert_wall_6_6, drone_at_7_6(vert_wall_7_6, drone_at_8_6(vert_wall_8_6, drone_at_9_6(vert_wall_9_6,
    drone_at_0_7(vert_wall_0_7, drone_at_1_7(vert_wall_1_7, drone_at_2_7(vert_wall_2_7, drone_at_3_7(vert_wall_3_7, drone_at_4_7(vert_wall_4_7, drone_at_5_7(vert_wall_5_7, drone_at_6_7(vert_wall_6_7, drone_at_7_7(vert_wall_7_7, drone_at_8_7(vert_wall_8_7, drone_at_9_7(vert_wall_9_7,
    drone_at_0_8(vert_wall_0_8, drone_at_1_8(vert_wall_1_8, drone_at_2_8(vert_wall_2_8, drone_at_3_8(vert_wall_3_8, drone_at_4_8(vert_wall_4_8, drone_at_5_8(vert_wall_5_8, drone_at_6_8(vert_wall_6_8, drone_at_7_8(vert_wall_7_8, drone_at_8_8(vert_wall_8_8,
    drone_at_9_8(vert_wall_9_8, false))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

def check_east_wall():
    return drone_at_0_0(horiz_wall_0_0, drone_at_1_0(horiz_wall_1_0, drone_at_2_0(horiz_wall_2_0, drone_at_3_0(horiz_wall_3_0, drone_at_4_0(horiz_wall_4_0, drone_at_5_0(horiz_wall_5_0, drone_at_6_0(horiz_wall_6_0, drone_at_7_0(horiz_wall_7_0, drone_at_8_0(horiz_wall_8_0,
    drone_at_0_1(horiz_wall_0_1, drone_at_1_1(horiz_wall_1_1, drone_at_2_1(horiz_wall_2_1, drone_at_3_1(horiz_wall_3_1, drone_at_4_1(horiz_wall_4_1, drone_at_5_1(horiz_wall_5_1, drone_at_6_1(horiz_wall_6_1, drone_at_7_1(horiz_wall_7_1, drone_at_8_1(horiz_wall_8_1,
    drone_at_0_2(horiz_wall_0_2, drone_at_1_2(horiz_wall_1_2, drone_at_2_2(horiz_wall_2_2, drone_at_3_2(horiz_wall_3_2, drone_at_4_2(horiz_wall_4_2, drone_at_5_2(horiz_wall_5_2, drone_at_6_2(horiz_wall_6_2, drone_at_7_2(horiz_wall_7_2, drone_at_8_2(horiz_wall_8_2,
    drone_at_0_3(horiz_wall_0_3, drone_at_1_3(horiz_wall_1_3, drone_at_2_3(horiz_wall_2_3, drone_at_3_3(horiz_wall_3_3, drone_at_4_3(horiz_wall_4_3, drone_at_5_3(horiz_wall_5_3, drone_at_6_3(horiz_wall_6_3, drone_at_7_3(horiz_wall_7_3, drone_at_8_3(horiz_wall_8_3,
    drone_at_0_4(horiz_wall_0_4, drone_at_1_4(horiz_wall_1_4, drone_at_2_4(horiz_wall_2_4, drone_at_3_4(horiz_wall_3_4, drone_at_4_4(horiz_wall_4_4, drone_at_5_4(horiz_wall_5_4, drone_at_6_4(horiz_wall_6_4, drone_at_7_4(horiz_wall_7_4, drone_at_8_4(horiz_wall_8_4,
    drone_at_0_5(horiz_wall_0_5, drone_at_1_5(horiz_wall_1_5, drone_at_2_5(horiz_wall_2_5, drone_at_3_5(horiz_wall_3_5, drone_at_4_5(horiz_wall_4_5, drone_at_5_5(horiz_wall_5_5, drone_at_6_5(horiz_wall_6_5, drone_at_7_5(horiz_wall_7_5, drone_at_8_5(horiz_wall_8_5,
    drone_at_0_6(horiz_wall_0_6, drone_at_1_6(horiz_wall_1_6, drone_at_2_6(horiz_wall_2_6, drone_at_3_6(horiz_wall_3_6, drone_at_4_6(horiz_wall_4_6, drone_at_5_6(horiz_wall_5_6, drone_at_6_6(horiz_wall_6_6, drone_at_7_6(horiz_wall_7_6, drone_at_8_6(horiz_wall_8_6,
    drone_at_0_7(horiz_wall_0_7, drone_at_1_7(horiz_wall_1_7, drone_at_2_7(horiz_wall_2_7, drone_at_3_7(horiz_wall_3_7, drone_at_4_7(horiz_wall_4_7, drone_at_5_7(horiz_wall_5_7, drone_at_6_7(horiz_wall_6_7, drone_at_7_7(horiz_wall_7_7, drone_at_8_7(horiz_wall_8_7,
    drone_at_0_8(horiz_wall_0_8, drone_at_1_8(horiz_wall_1_8, drone_at_2_8(horiz_wall_2_8, drone_at_3_8(horiz_wall_3_8, drone_at_4_8(horiz_wall_4_8, drone_at_5_8(horiz_wall_5_8, drone_at_6_8(horiz_wall_6_8, drone_at_7_8(horiz_wall_7_8, drone_at_8_8(horiz_wall_8_8,
    drone_at_0_9(horiz_wall_0_9, drone_at_1_9(horiz_wall_1_9, drone_at_2_9(horiz_wall_2_9, drone_at_3_9(horiz_wall_3_9, drone_at_4_9(horiz_wall_4_9, drone_at_5_9(horiz_wall_5_9, drone_at_6_9(horiz_wall_6_9, drone_at_7_9(horiz_wall_7_9,
    drone_at_8_9(horiz_wall_8_9, false))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

def check_south_wall():
    return drone_at_0_1(vert_wall_0_0, drone_at_1_1(vert_wall_1_0, drone_at_2_1(vert_wall_2_0, drone_at_3_1(vert_wall_3_0, drone_at_4_1(vert_wall_4_0, drone_at_5_1(vert_wall_5_0, drone_at_6_1(vert_wall_6_0, drone_at_7_1(vert_wall_7_0, drone_at_8_1(vert_wall_8_0, drone_at_9_1(vert_wall_9_0,
    drone_at_0_2(vert_wall_0_1, drone_at_1_2(vert_wall_1_1, drone_at_2_2(vert_wall_2_1, drone_at_3_2(vert_wall_3_1, drone_at_4_2(vert_wall_4_1, drone_at_5_2(vert_wall_5_1, drone_at_6_2(vert_wall_6_1, drone_at_7_2(vert_wall_7_1, drone_at_8_2(vert_wall_8_1, drone_at_9_2(vert_wall_9_1,
    drone_at_0_3(vert_wall_0_2, drone_at_1_3(vert_wall_1_2, drone_at_2_3(vert_wall_2_2, drone_at_3_3(vert_wall_3_2, drone_at_4_3(vert_wall_4_2, drone_at_5_3(vert_wall_5_2, drone_at_6_3(vert_wall_6_2, drone_at_7_3(vert_wall_7_2, drone_at_8_3(vert_wall_8_2, drone_at_9_3(vert_wall_9_2,
    drone_at_0_4(vert_wall_0_3, drone_at_1_4(vert_wall_1_3, drone_at_2_4(vert_wall_2_3, drone_at_3_4(vert_wall_3_3, drone_at_4_4(vert_wall_4_3, drone_at_5_4(vert_wall_5_3, drone_at_6_4(vert_wall_6_3, drone_at_7_4(vert_wall_7_3, drone_at_8_4(vert_wall_8_3, drone_at_9_4(vert_wall_9_3,
    drone_at_0_5(vert_wall_0_4, drone_at_1_5(vert_wall_1_4, drone_at_2_5(vert_wall_2_4, drone_at_3_5(vert_wall_3_4, drone_at_4_5(vert_wall_4_4, drone_at_5_5(vert_wall_5_4, drone_at_6_5(vert_wall_6_4, drone_at_7_5(vert_wall_7_4, drone_at_8_5(vert_wall_8_4, drone_at_9_5(vert_wall_9_4,
    drone_at_0_6(vert_wall_0_5, drone_at_1_6(vert_wall_1_5, drone_at_2_6(vert_wall_2_5, drone_at_3_6(vert_wall_3_5, drone_at_4_6(vert_wall_4_5, drone_at_5_6(vert_wall_5_5, drone_at_6_6(vert_wall_6_5, drone_at_7_6(vert_wall_7_5, drone_at_8_6(vert_wall_8_5, drone_at_9_6(vert_wall_9_5,
    drone_at_0_7(vert_wall_0_6, drone_at_1_7(vert_wall_1_6, drone_at_2_7(vert_wall_2_6, drone_at_3_7(vert_wall_3_6, drone_at_4_7(vert_wall_4_6, drone_at_5_7(vert_wall_5_6, drone_at_6_7(vert_wall_6_6, drone_at_7_7(vert_wall_7_6, drone_at_8_7(vert_wall_8_6, drone_at_9_7(vert_wall_9_6,
    drone_at_0_8(vert_wall_0_7, drone_at_1_8(vert_wall_1_7, drone_at_2_8(vert_wall_2_7, drone_at_3_8(vert_wall_3_7, drone_at_4_8(vert_wall_4_7, drone_at_5_8(vert_wall_5_7, drone_at_6_8(vert_wall_6_7, drone_at_7_8(vert_wall_7_7, drone_at_8_8(vert_wall_8_7, drone_at_9_8(vert_wall_9_7,
    drone_at_0_9(vert_wall_0_8, drone_at_1_9(vert_wall_1_8, drone_at_2_9(vert_wall_2_8, drone_at_3_9(vert_wall_3_8, drone_at_4_9(vert_wall_4_8, drone_at_5_9(vert_wall_5_8, drone_at_6_9(vert_wall_6_8, drone_at_7_9(vert_wall_7_8, drone_at_8_9(vert_wall_8_8,
    drone_at_9_9(vert_wall_9_8, false))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))


def check_west_wall():
    return drone_at_1_0(horiz_wall_0_0, drone_at_2_0(horiz_wall_1_0, drone_at_3_0(horiz_wall_2_0, drone_at_4_0(horiz_wall_3_0, drone_at_5_0(horiz_wall_4_0, drone_at_6_0(horiz_wall_5_0, drone_at_7_0(horiz_wall_6_0, drone_at_8_0(horiz_wall_7_0, drone_at_9_0(horiz_wall_8_0,
    drone_at_1_1(horiz_wall_0_1, drone_at_2_1(horiz_wall_1_1, drone_at_3_1(horiz_wall_2_1, drone_at_4_1(horiz_wall_3_1, drone_at_5_1(horiz_wall_4_1, drone_at_6_1(horiz_wall_5_1, drone_at_7_1(horiz_wall_6_1, drone_at_8_1(horiz_wall_7_1, drone_at_9_1(horiz_wall_8_1,
    drone_at_1_2(horiz_wall_0_2, drone_at_2_2(horiz_wall_1_2, drone_at_3_2(horiz_wall_2_2, drone_at_4_2(horiz_wall_3_2, drone_at_5_2(horiz_wall_4_2, drone_at_6_2(horiz_wall_5_2, drone_at_7_2(horiz_wall_6_2, drone_at_8_2(horiz_wall_7_2, drone_at_9_2(horiz_wall_8_2,
    drone_at_1_3(horiz_wall_0_3, drone_at_2_3(horiz_wall_1_3, drone_at_3_3(horiz_wall_2_3, drone_at_4_3(horiz_wall_3_3, drone_at_5_3(horiz_wall_4_3, drone_at_6_3(horiz_wall_5_3, drone_at_7_3(horiz_wall_6_3, drone_at_8_3(horiz_wall_7_3, drone_at_9_3(horiz_wall_8_3,
    drone_at_1_4(horiz_wall_0_4, drone_at_2_4(horiz_wall_1_4, drone_at_3_4(horiz_wall_2_4, drone_at_4_4(horiz_wall_3_4, drone_at_5_4(horiz_wall_4_4, drone_at_6_4(horiz_wall_5_4, drone_at_7_4(horiz_wall_6_4, drone_at_8_4(horiz_wall_7_4, drone_at_9_4(horiz_wall_8_4,
    drone_at_1_5(horiz_wall_0_5, drone_at_2_5(horiz_wall_1_5, drone_at_3_5(horiz_wall_2_5, drone_at_4_5(horiz_wall_3_5, drone_at_5_5(horiz_wall_4_5, drone_at_6_5(horiz_wall_5_5, drone_at_7_5(horiz_wall_6_5, drone_at_8_5(horiz_wall_7_5, drone_at_9_5(horiz_wall_8_5,
    drone_at_1_6(horiz_wall_0_6, drone_at_2_6(horiz_wall_1_6, drone_at_3_6(horiz_wall_2_6, drone_at_4_6(horiz_wall_3_6, drone_at_5_6(horiz_wall_4_6, drone_at_6_6(horiz_wall_5_6, drone_at_7_6(horiz_wall_6_6, drone_at_8_6(horiz_wall_7_6, drone_at_9_6(horiz_wall_8_6,
    drone_at_1_7(horiz_wall_0_7, drone_at_2_7(horiz_wall_1_7, drone_at_3_7(horiz_wall_2_7, drone_at_4_7(horiz_wall_3_7, drone_at_5_7(horiz_wall_4_7, drone_at_6_7(horiz_wall_5_7, drone_at_7_7(horiz_wall_6_7, drone_at_8_7(horiz_wall_7_7, drone_at_9_7(horiz_wall_8_7,
    drone_at_1_8(horiz_wall_0_8, drone_at_2_8(horiz_wall_1_8, drone_at_3_8(horiz_wall_2_8, drone_at_4_8(horiz_wall_3_8, drone_at_5_8(horiz_wall_4_8, drone_at_6_8(horiz_wall_5_8, drone_at_7_8(horiz_wall_6_8, drone_at_8_8(horiz_wall_7_8, drone_at_9_8(horiz_wall_8_8,
    drone_at_1_9(horiz_wall_0_9, drone_at_2_9(horiz_wall_1_9, drone_at_3_9(horiz_wall_2_9, drone_at_4_9(horiz_wall_3_9, drone_at_5_9(horiz_wall_4_9, drone_at_6_9(horiz_wall_5_9, drone_at_7_9(horiz_wall_6_9, drone_at_8_9(horiz_wall_7_9,
    drone_at_9_9(horiz_wall_8_9, false))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

def check_north_spread():
    return drone_at_0_0(t_0_1_spread, drone_at_1_0(t_1_1_spread, drone_at_2_0(t_2_1_spread, drone_at_3_0(t_3_1_spread, drone_at_4_0(t_4_1_spread, drone_at_5_0(t_5_1_spread, drone_at_6_0(t_6_1_spread, drone_at_7_0(t_7_1_spread, drone_at_8_0(t_8_1_spread, drone_at_9_0(t_9_1_spread,
    drone_at_0_1(t_0_2_spread, drone_at_1_1(t_1_2_spread, drone_at_2_1(t_2_2_spread, drone_at_3_1(t_3_2_spread, drone_at_4_1(t_4_2_spread, drone_at_5_1(t_5_2_spread, drone_at_6_1(t_6_2_spread, drone_at_7_1(t_7_2_spread, drone_at_8_1(t_8_2_spread, drone_at_9_1(t_9_2_spread,
    drone_at_0_2(t_0_3_spread, drone_at_1_2(t_1_3_spread, drone_at_2_2(t_2_3_spread, drone_at_3_2(t_3_3_spread, drone_at_4_2(t_4_3_spread, drone_at_5_2(t_5_3_spread, drone_at_6_2(t_6_3_spread, drone_at_7_2(t_7_3_spread, drone_at_8_2(t_8_3_spread, drone_at_9_2(t_9_3_spread,
    drone_at_0_3(t_0_4_spread, drone_at_1_3(t_1_4_spread, drone_at_2_3(t_2_4_spread, drone_at_3_3(t_3_4_spread, drone_at_4_3(t_4_4_spread, drone_at_5_3(t_5_4_spread, drone_at_6_3(t_6_4_spread, drone_at_7_3(t_7_4_spread, drone_at_8_3(t_8_4_spread, drone_at_9_3(t_9_4_spread,
    drone_at_0_4(t_0_5_spread, drone_at_1_4(t_1_5_spread, drone_at_2_4(t_2_5_spread, drone_at_3_4(t_3_5_spread, drone_at_4_4(t_4_5_spread, drone_at_5_4(t_5_5_spread, drone_at_6_4(t_6_5_spread, drone_at_7_4(t_7_5_spread, drone_at_8_4(t_8_5_spread, drone_at_9_4(t_9_5_spread,
    drone_at_0_5(t_0_6_spread, drone_at_1_5(t_1_6_spread, drone_at_2_5(t_2_6_spread, drone_at_3_5(t_3_6_spread, drone_at_4_5(t_4_6_spread, drone_at_5_5(t_5_6_spread, drone_at_6_5(t_6_6_spread, drone_at_7_5(t_7_6_spread, drone_at_8_5(t_8_6_spread, drone_at_9_5(t_9_6_spread,
    drone_at_0_6(t_0_7_spread, drone_at_1_6(t_1_7_spread, drone_at_2_6(t_2_7_spread, drone_at_3_6(t_3_7_spread, drone_at_4_6(t_4_7_spread, drone_at_5_6(t_5_7_spread, drone_at_6_6(t_6_7_spread, drone_at_7_6(t_7_7_spread, drone_at_8_6(t_8_7_spread, drone_at_9_6(t_9_7_spread,
    drone_at_0_7(t_0_8_spread, drone_at_1_7(t_1_8_spread, drone_at_2_7(t_2_8_spread, drone_at_3_7(t_3_8_spread, drone_at_4_7(t_4_8_spread, drone_at_5_7(t_5_8_spread, drone_at_6_7(t_6_8_spread, drone_at_7_7(t_7_8_spread, drone_at_8_7(t_8_8_spread, drone_at_9_7(t_9_8_spread,
    drone_at_0_8(t_0_9_spread, drone_at_1_8(t_1_9_spread, drone_at_2_8(t_2_9_spread, drone_at_3_8(t_3_9_spread, drone_at_4_8(t_4_9_spread, drone_at_5_8(t_5_9_spread, drone_at_6_8(t_6_9_spread, drone_at_7_8(t_7_9_spread, drone_at_8_8(t_8_9_spread,
    drone_at_9_8(t_9_9_spread, false))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

def check_east_spread():
    return drone_at_0_0(t_1_0_spread, drone_at_1_0(t_2_0_spread, drone_at_2_0(t_3_0_spread, drone_at_3_0(t_4_0_spread, drone_at_4_0(t_5_0_spread, drone_at_5_0(t_6_0_spread, drone_at_6_0(t_7_0_spread, drone_at_7_0(t_8_0_spread, drone_at_8_0(t_9_0_spread,
    drone_at_0_1(t_1_1_spread, drone_at_1_1(t_2_1_spread, drone_at_2_1(t_3_1_spread, drone_at_3_1(t_4_1_spread, drone_at_4_1(t_5_1_spread, drone_at_5_1(t_6_1_spread, drone_at_6_1(t_7_1_spread, drone_at_7_1(t_8_1_spread, drone_at_8_1(t_9_1_spread,
    drone_at_0_2(t_1_2_spread, drone_at_1_2(t_2_2_spread, drone_at_2_2(t_3_2_spread, drone_at_3_2(t_4_2_spread, drone_at_4_2(t_5_2_spread, drone_at_5_2(t_6_2_spread, drone_at_6_2(t_7_2_spread, drone_at_7_2(t_8_2_spread, drone_at_8_2(t_9_2_spread,
    drone_at_0_3(t_1_3_spread, drone_at_1_3(t_2_3_spread, drone_at_2_3(t_3_3_spread, drone_at_3_3(t_4_3_spread, drone_at_4_3(t_5_3_spread, drone_at_5_3(t_6_3_spread, drone_at_6_3(t_7_3_spread, drone_at_7_3(t_8_3_spread, drone_at_8_3(t_9_3_spread,
    drone_at_0_4(t_1_4_spread, drone_at_1_4(t_2_4_spread, drone_at_2_4(t_3_4_spread, drone_at_3_4(t_4_4_spread, drone_at_4_4(t_5_4_spread, drone_at_5_4(t_6_4_spread, drone_at_6_4(t_7_4_spread, drone_at_7_4(t_8_4_spread, drone_at_8_4(t_9_4_spread,
    drone_at_0_5(t_1_5_spread, drone_at_1_5(t_2_5_spread, drone_at_2_5(t_3_5_spread, drone_at_3_5(t_4_5_spread, drone_at_4_5(t_5_5_spread, drone_at_5_5(t_6_5_spread, drone_at_6_5(t_7_5_spread, drone_at_7_5(t_8_5_spread, drone_at_8_5(t_9_5_spread,
    drone_at_0_6(t_1_6_spread, drone_at_1_6(t_2_6_spread, drone_at_2_6(t_3_6_spread, drone_at_3_6(t_4_6_spread, drone_at_4_6(t_5_6_spread, drone_at_5_6(t_6_6_spread, drone_at_6_6(t_7_6_spread, drone_at_7_6(t_8_6_spread, drone_at_8_6(t_9_6_spread,
    drone_at_0_7(t_1_7_spread, drone_at_1_7(t_2_7_spread, drone_at_2_7(t_3_7_spread, drone_at_3_7(t_4_7_spread, drone_at_4_7(t_5_7_spread, drone_at_5_7(t_6_7_spread, drone_at_6_7(t_7_7_spread, drone_at_7_7(t_8_7_spread, drone_at_8_7(t_9_7_spread,
    drone_at_0_8(t_1_8_spread, drone_at_1_8(t_2_8_spread, drone_at_2_8(t_3_8_spread, drone_at_3_8(t_4_8_spread, drone_at_4_8(t_5_8_spread, drone_at_5_8(t_6_8_spread, drone_at_6_8(t_7_8_spread, drone_at_7_8(t_8_8_spread, drone_at_8_8(t_9_8_spread,
    drone_at_0_9(t_1_9_spread, drone_at_1_9(t_2_9_spread, drone_at_2_9(t_3_9_spread, drone_at_3_9(t_4_9_spread, drone_at_4_9(t_5_9_spread, drone_at_5_9(t_6_9_spread, drone_at_6_9(t_7_9_spread, drone_at_7_9(t_8_9_spread,
    drone_at_8_9(t_9_9_spread, false))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

def check_south_spread():
    return drone_at_0_1(t_0_0_spread, drone_at_1_1(t_1_0_spread, drone_at_2_1(t_2_0_spread, drone_at_3_1(t_3_0_spread, drone_at_4_1(t_4_0_spread, drone_at_5_1(t_5_0_spread, drone_at_6_1(t_6_0_spread, drone_at_7_1(t_7_0_spread, drone_at_8_1(t_8_0_spread, drone_at_9_1(t_9_0_spread,
    drone_at_0_2(t_0_1_spread, drone_at_1_2(t_1_1_spread, drone_at_2_2(t_2_1_spread, drone_at_3_2(t_3_1_spread, drone_at_4_2(t_4_1_spread, drone_at_5_2(t_5_1_spread, drone_at_6_2(t_6_1_spread, drone_at_7_2(t_7_1_spread, drone_at_8_2(t_8_1_spread, drone_at_9_2(t_9_1_spread,
    drone_at_0_3(t_0_2_spread, drone_at_1_3(t_1_2_spread, drone_at_2_3(t_2_2_spread, drone_at_3_3(t_3_2_spread, drone_at_4_3(t_4_2_spread, drone_at_5_3(t_5_2_spread, drone_at_6_3(t_6_2_spread, drone_at_7_3(t_7_2_spread, drone_at_8_3(t_8_2_spread, drone_at_9_3(t_9_2_spread,
    drone_at_0_4(t_0_3_spread, drone_at_1_4(t_1_3_spread, drone_at_2_4(t_2_3_spread, drone_at_3_4(t_3_3_spread, drone_at_4_4(t_4_3_spread, drone_at_5_4(t_5_3_spread, drone_at_6_4(t_6_3_spread, drone_at_7_4(t_7_3_spread, drone_at_8_4(t_8_3_spread, drone_at_9_4(t_9_3_spread,
    drone_at_0_5(t_0_4_spread, drone_at_1_5(t_1_4_spread, drone_at_2_5(t_2_4_spread, drone_at_3_5(t_3_4_spread, drone_at_4_5(t_4_4_spread, drone_at_5_5(t_5_4_spread, drone_at_6_5(t_6_4_spread, drone_at_7_5(t_7_4_spread, drone_at_8_5(t_8_4_spread, drone_at_9_5(t_9_4_spread,
    drone_at_0_6(t_0_5_spread, drone_at_1_6(t_1_5_spread, drone_at_2_6(t_2_5_spread, drone_at_3_6(t_3_5_spread, drone_at_4_6(t_4_5_spread, drone_at_5_6(t_5_5_spread, drone_at_6_6(t_6_5_spread, drone_at_7_6(t_7_5_spread, drone_at_8_6(t_8_5_spread, drone_at_9_6(t_9_5_spread,
    drone_at_0_7(t_0_6_spread, drone_at_1_7(t_1_6_spread, drone_at_2_7(t_2_6_spread, drone_at_3_7(t_3_6_spread, drone_at_4_7(t_4_6_spread, drone_at_5_7(t_5_6_spread, drone_at_6_7(t_6_6_spread, drone_at_7_7(t_7_6_spread, drone_at_8_7(t_8_6_spread, drone_at_9_7(t_9_6_spread,
    drone_at_0_8(t_0_7_spread, drone_at_1_8(t_1_7_spread, drone_at_2_8(t_2_7_spread, drone_at_3_8(t_3_7_spread, drone_at_4_8(t_4_7_spread, drone_at_5_8(t_5_7_spread, drone_at_6_8(t_6_7_spread, drone_at_7_8(t_7_7_spread, drone_at_8_8(t_8_7_spread, drone_at_9_8(t_9_7_spread,
    drone_at_0_9(t_0_8_spread, drone_at_1_9(t_1_8_spread, drone_at_2_9(t_2_8_spread, drone_at_3_9(t_3_8_spread, drone_at_4_9(t_4_8_spread, drone_at_5_9(t_5_8_spread, drone_at_6_9(t_6_8_spread, drone_at_7_9(t_7_8_spread, drone_at_8_9(t_8_8_spread,
    drone_at_9_9(t_9_8_spread, false))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

def check_west_spread():
    return drone_at_1_0(t_0_0_spread, drone_at_2_0(t_1_0_spread, drone_at_3_0(t_2_0_spread, drone_at_4_0(t_3_0_spread, drone_at_5_0(t_4_0_spread, drone_at_6_0(t_5_0_spread, drone_at_7_0(t_6_0_spread, drone_at_8_0(t_7_0_spread, drone_at_9_0(t_8_0_spread,
    drone_at_1_1(t_0_1_spread, drone_at_2_1(t_1_1_spread, drone_at_3_1(t_2_1_spread, drone_at_4_1(t_3_1_spread, drone_at_5_1(t_4_1_spread, drone_at_6_1(t_5_1_spread, drone_at_7_1(t_6_1_spread, drone_at_8_1(t_7_1_spread, drone_at_9_1(t_8_1_spread,
    drone_at_1_2(t_0_2_spread, drone_at_2_2(t_1_2_spread, drone_at_3_2(t_2_2_spread, drone_at_4_2(t_3_2_spread, drone_at_5_2(t_4_2_spread, drone_at_6_2(t_5_2_spread, drone_at_7_2(t_6_2_spread, drone_at_8_2(t_7_2_spread, drone_at_9_2(t_8_2_spread,
    drone_at_1_3(t_0_3_spread, drone_at_2_3(t_1_3_spread, drone_at_3_3(t_2_3_spread, drone_at_4_3(t_3_3_spread, drone_at_5_3(t_4_3_spread, drone_at_6_3(t_5_3_spread, drone_at_7_3(t_6_3_spread, drone_at_8_3(t_7_3_spread, drone_at_9_3(t_8_3_spread,
    drone_at_1_4(t_0_4_spread, drone_at_2_4(t_1_4_spread, drone_at_3_4(t_2_4_spread, drone_at_4_4(t_3_4_spread, drone_at_5_4(t_4_4_spread, drone_at_6_4(t_5_4_spread, drone_at_7_4(t_6_4_spread, drone_at_8_4(t_7_4_spread, drone_at_9_4(t_8_4_spread,
    drone_at_1_5(t_0_5_spread, drone_at_2_5(t_1_5_spread, drone_at_3_5(t_2_5_spread, drone_at_4_5(t_3_5_spread, drone_at_5_5(t_4_5_spread, drone_at_6_5(t_5_5_spread, drone_at_7_5(t_6_5_spread, drone_at_8_5(t_7_5_spread, drone_at_9_5(t_8_5_spread,
    drone_at_1_6(t_0_6_spread, drone_at_2_6(t_1_6_spread, drone_at_3_6(t_2_6_spread, drone_at_4_6(t_3_6_spread, drone_at_5_6(t_4_6_spread, drone_at_6_6(t_5_6_spread, drone_at_7_6(t_6_6_spread, drone_at_8_6(t_7_6_spread, drone_at_9_6(t_8_6_spread,
    drone_at_1_7(t_0_7_spread, drone_at_2_7(t_1_7_spread, drone_at_3_7(t_2_7_spread, drone_at_4_7(t_3_7_spread, drone_at_5_7(t_4_7_spread, drone_at_6_7(t_5_7_spread, drone_at_7_7(t_6_7_spread, drone_at_8_7(t_7_7_spread, drone_at_9_7(t_8_7_spread,
    drone_at_1_8(t_0_8_spread, drone_at_2_8(t_1_8_spread, drone_at_3_8(t_2_8_spread, drone_at_4_8(t_3_8_spread, drone_at_5_8(t_4_8_spread, drone_at_6_8(t_5_8_spread, drone_at_7_8(t_6_8_spread, drone_at_8_8(t_7_8_spread, drone_at_9_8(t_8_8_spread,
    drone_at_1_9(t_0_9_spread, drone_at_2_9(t_1_9_spread, drone_at_3_9(t_2_9_spread, drone_at_4_9(t_3_9_spread, drone_at_5_9(t_4_9_spread, drone_at_6_9(t_5_9_spread, drone_at_7_9(t_6_9_spread, drone_at_8_9(t_7_9_spread,
    drone_at_9_9(t_8_9_spread, false))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

fully_mapped = False

t_0_0_visited = true
t_1_0_visited = false
t_2_0_visited = false
t_3_0_visited = false
t_4_0_visited = false
t_5_0_visited = false
t_6_0_visited = false
t_7_0_visited = false
t_8_0_visited = false
t_9_0_visited = false
t_0_1_visited = false
t_1_1_visited = false
t_2_1_visited = false
t_3_1_visited = false
t_4_1_visited = false
t_5_1_visited = false
t_6_1_visited = false
t_7_1_visited = false
t_8_1_visited = false
t_9_1_visited = false
t_0_2_visited = false
t_1_2_visited = false
t_2_2_visited = false
t_3_2_visited = false
t_4_2_visited = false
t_5_2_visited = false
t_6_2_visited = false
t_7_2_visited = false
t_8_2_visited = false
t_9_2_visited = false
t_0_3_visited = false
t_1_3_visited = false
t_2_3_visited = false
t_3_3_visited = false
t_4_3_visited = false
t_5_3_visited = false
t_6_3_visited = false
t_7_3_visited = false
t_8_3_visited = false
t_9_3_visited = false
t_0_4_visited = false
t_1_4_visited = false
t_2_4_visited = false
t_3_4_visited = false
t_4_4_visited = false
t_5_4_visited = false
t_6_4_visited = false
t_7_4_visited = false
t_8_4_visited = false
t_9_4_visited = false
t_0_5_visited = false
t_1_5_visited = false
t_2_5_visited = false
t_3_5_visited = false
t_4_5_visited = false
t_5_5_visited = false
t_6_5_visited = false
t_7_5_visited = false
t_8_5_visited = false
t_9_5_visited = false
t_0_6_visited = false
t_1_6_visited = false
t_2_6_visited = false
t_3_6_visited = false
t_4_6_visited = false
t_5_6_visited = false
t_6_6_visited = false
t_7_6_visited = false
t_8_6_visited = false
t_9_6_visited = false
t_0_7_visited = false
t_1_7_visited = false
t_2_7_visited = false
t_3_7_visited = false
t_4_7_visited = false
t_5_7_visited = false
t_6_7_visited = false
t_7_7_visited = false
t_8_7_visited = false
t_9_7_visited = false
t_0_8_visited = false
t_1_8_visited = false
t_2_8_visited = false
t_3_8_visited = false
t_4_8_visited = false
t_5_8_visited = false
t_6_8_visited = false
t_7_8_visited = false
t_8_8_visited = false
t_9_8_visited = false
t_0_9_visited = false
t_1_9_visited = false
t_2_9_visited = false
t_3_9_visited = false
t_4_9_visited = false
t_5_9_visited = false
t_6_9_visited = false
t_7_9_visited = false
t_8_9_visited = false
t_9_9_visited = false

vert_wall_0_0 = true
vert_wall_1_0 = true
vert_wall_2_0 = true
vert_wall_3_0 = true
vert_wall_4_0 = true
vert_wall_5_0 = true
vert_wall_6_0 = true
vert_wall_7_0 = true
vert_wall_8_0 = true
vert_wall_9_0 = true
vert_wall_0_1 = true
vert_wall_1_1 = true
vert_wall_2_1 = true
vert_wall_3_1 = true
vert_wall_4_1 = true
vert_wall_5_1 = true
vert_wall_6_1 = true
vert_wall_7_1 = true
vert_wall_8_1 = true
vert_wall_9_1 = true
vert_wall_0_2 = true
vert_wall_1_2 = true
vert_wall_2_2 = true
vert_wall_3_2 = true
vert_wall_4_2 = true
vert_wall_5_2 = true
vert_wall_6_2 = true
vert_wall_7_2 = true
vert_wall_8_2 = true
vert_wall_9_2 = true
vert_wall_0_3 = true
vert_wall_1_3 = true
vert_wall_2_3 = true
vert_wall_3_3 = true
vert_wall_4_3 = true
vert_wall_5_3 = true
vert_wall_6_3 = true
vert_wall_7_3 = true
vert_wall_8_3 = true
vert_wall_9_3 = true
vert_wall_0_4 = true
vert_wall_1_4 = true
vert_wall_2_4 = true
vert_wall_3_4 = true
vert_wall_4_4 = true
vert_wall_5_4 = true
vert_wall_6_4 = true
vert_wall_7_4 = true
vert_wall_8_4 = true
vert_wall_9_4 = true
vert_wall_0_5 = true
vert_wall_1_5 = true
vert_wall_2_5 = true
vert_wall_3_5 = true
vert_wall_4_5 = true
vert_wall_5_5 = true
vert_wall_6_5 = true
vert_wall_7_5 = true
vert_wall_8_5 = true
vert_wall_9_5 = true
vert_wall_0_6 = true
vert_wall_1_6 = true
vert_wall_2_6 = true
vert_wall_3_6 = true
vert_wall_4_6 = true
vert_wall_5_6 = true
vert_wall_6_6 = true
vert_wall_7_6 = true
vert_wall_8_6 = true
vert_wall_9_6 = true
vert_wall_0_7 = true
vert_wall_1_7 = true
vert_wall_2_7 = true
vert_wall_3_7 = true
vert_wall_4_7 = true
vert_wall_5_7 = true
vert_wall_6_7 = true
vert_wall_7_7 = true
vert_wall_8_7 = true
vert_wall_9_7 = true
vert_wall_0_8 = true
vert_wall_1_8 = true
vert_wall_2_8 = true
vert_wall_3_8 = true
vert_wall_4_8 = true
vert_wall_5_8 = true
vert_wall_6_8 = true
vert_wall_7_8 = true
vert_wall_8_8 = true
vert_wall_9_8 = true

horiz_wall_0_0 = true
horiz_wall_1_0 = true
horiz_wall_2_0 = true
horiz_wall_3_0 = true
horiz_wall_4_0 = true
horiz_wall_5_0 = true
horiz_wall_6_0 = true
horiz_wall_7_0 = true
horiz_wall_8_0 = true
horiz_wall_0_1 = true
horiz_wall_1_1 = true
horiz_wall_2_1 = true
horiz_wall_3_1 = true
horiz_wall_4_1 = true
horiz_wall_5_1 = true
horiz_wall_6_1 = true
horiz_wall_7_1 = true
horiz_wall_8_1 = true
horiz_wall_0_2 = true
horiz_wall_1_2 = true
horiz_wall_2_2 = true
horiz_wall_3_2 = true
horiz_wall_4_2 = true
horiz_wall_5_2 = true
horiz_wall_6_2 = true
horiz_wall_7_2 = true
horiz_wall_8_2 = true
horiz_wall_0_3 = true
horiz_wall_1_3 = true
horiz_wall_2_3 = true
horiz_wall_3_3 = true
horiz_wall_4_3 = true
horiz_wall_5_3 = true
horiz_wall_6_3 = true
horiz_wall_7_3 = true
horiz_wall_8_3 = true
horiz_wall_0_4 = true
horiz_wall_1_4 = true
horiz_wall_2_4 = true
horiz_wall_3_4 = true
horiz_wall_4_4 = true
horiz_wall_5_4 = true
horiz_wall_6_4 = true
horiz_wall_7_4 = true
horiz_wall_8_4 = true
horiz_wall_0_5 = true
horiz_wall_1_5 = true
horiz_wall_2_5 = true
horiz_wall_3_5 = true
horiz_wall_4_5 = true
horiz_wall_5_5 = true
horiz_wall_6_5 = true
horiz_wall_7_5 = true
horiz_wall_8_5 = true
horiz_wall_0_6 = true
horiz_wall_1_6 = true
horiz_wall_2_6 = true
horiz_wall_3_6 = true
horiz_wall_4_6 = true
horiz_wall_5_6 = true
horiz_wall_6_6 = true
horiz_wall_7_6 = true
horiz_wall_8_6 = true
horiz_wall_0_7 = true
horiz_wall_1_7 = true
horiz_wall_2_7 = true
horiz_wall_3_7 = true
horiz_wall_4_7 = true
horiz_wall_5_7 = true
horiz_wall_6_7 = true
horiz_wall_7_7 = true
horiz_wall_8_7 = true
horiz_wall_0_8 = true
horiz_wall_1_8 = true
horiz_wall_2_8 = true
horiz_wall_3_8 = true
horiz_wall_4_8 = true
horiz_wall_5_8 = true
horiz_wall_6_8 = true
horiz_wall_7_8 = true
horiz_wall_8_8 = true
horiz_wall_0_9 = true
horiz_wall_1_9 = true
horiz_wall_2_9 = true
horiz_wall_3_9 = true
horiz_wall_4_9 = true
horiz_wall_5_9 = true
horiz_wall_6_9 = true
horiz_wall_7_9 = true
horiz_wall_8_9 = true

pc0 = true
pc1 = false
pc2 = false
pc3 = false
pc4 = false
pc5 = false
pc6 = false
pc7 = false
pc8 = false
pc9 = false

pr0 = true
pr1 = false
pr2 = false
pr3 = false
pr4 = false
pr5 = false
pr6 = false
pr7 = false
pr8 = false
pr9 = false

facing_north = true
facing_east = false
facing_south = false
facing_west = false

clear()
plant(Entities.Bush)
use_item(Items.Weird_Substance, 100)

while not fully_mapped:
	if measure():
		tc0 = pc0
		tc1 = pc1
		tc2 = pc2
		tc3 = pc3
		tc4 = pc4
		tc5 = pc5
		tc6 = pc6
		tc7 = pc7
		tc8 = pc8
		tc9 = pc9

		tr0 = pr0
		tr1 = pr1
		tr2 = pr2
		tr3 = pr3
		tr4 = pr4
		tr5 = pr5
		tr6 = pr6
		tr7 = pr7
		tr8 = pr8
		tr9 = pr9

	moved = facing_north(alt_move_north, facing_east(alt_move_east, facing_south(alt_move_south, alt_move_west)))()
	moved_north = And(facing_north, moved)
	moved_east = And(facing_east, moved)
	moved_south = And(facing_south, moved)
	moved_west = And(facing_west, moved)

	not_moved_north = moved_north(false, true)
	not_moved_east = moved_east(false, true)
	not_moved_south = moved_south(false, true)
	not_moved_west = moved_west(false, true)

	facing_west_copy = facing_west

	facing_west = Or(moved_north, And(facing_south, Not(moved)))
	facing_south = Or(moved_west, And(facing_east, Not(moved)))
	facing_east = Or(moved_south, And(facing_north, Not(moved)))
	facing_north = Or(moved_east, And(facing_west_copy, Not(moved)))

	x_changed = moved_east(true, moved_west)
	y_changed = moved_north(true, moved_south)

	pc0_copy = pc0
	pc1_copy = pc1
	pc2_copy = pc2
	pc3_copy = pc3
	pc4_copy = pc4
	pc5_copy = pc5
	pc6_copy = pc6
	pc7_copy = pc7
	pc8_copy = pc8
	pc9_copy = pc9

	pr0_copy = pr0
	pr1_copy = pr1
	pr2_copy = pr2
	pr3_copy = pr3
	pr4_copy = pr4
	pr5_copy = pr5
	pr6_copy = pr6
	pr7_copy = pr7
	pr8_copy = pr8
	pr9_copy = pr9

	pc0 = x_changed(moved_east(false, pc1_copy), pc0)
	pc1 = x_changed(moved_east(pc0_copy, pc2_copy), pc1)
	pc2 = x_changed(moved_east(pc1_copy, pc3_copy), pc2)
	pc3 = x_changed(moved_east(pc2_copy, pc4_copy), pc3)
	pc4 = x_changed(moved_east(pc3_copy, pc5_copy), pc4)
	pc5 = x_changed(moved_east(pc4_copy, pc6_copy), pc5)
	pc6 = x_changed(moved_east(pc5_copy, pc7_copy), pc6)
	pc7 = x_changed(moved_east(pc6_copy, pc8_copy), pc7)
	pc8 = x_changed(moved_east(pc7_copy, pc9_copy), pc8)
	pc9 = x_changed(moved_east(pc8_copy, false), pc9)

	pr0 = y_changed(moved_north(false, pr1_copy), pr0)
	pr1 = y_changed(moved_north(pr0_copy, pr2_copy), pr1)
	pr2 = y_changed(moved_north(pr1_copy, pr3_copy), pr2)
	pr3 = y_changed(moved_north(pr2_copy, pr4_copy), pr3)
	pr4 = y_changed(moved_north(pr3_copy, pr5_copy), pr4)
	pr5 = y_changed(moved_north(pr4_copy, pr6_copy), pr5)
	pr6 = y_changed(moved_north(pr5_copy, pr7_copy), pr6)
	pr7 = y_changed(moved_north(pr6_copy, pr8_copy), pr7)
	pr8 = y_changed(moved_north(pr7_copy, pr9_copy), pr8)
	pr9 = y_changed(moved_north(pr8_copy, false), pr9)

	drone_at_0_0 = pc0(pr0, false)
	drone_at_1_0 = pc1(pr0, false)
	drone_at_2_0 = pc2(pr0, false)
	drone_at_3_0 = pc3(pr0, false)
	drone_at_4_0 = pc4(pr0, false)
	drone_at_5_0 = pc5(pr0, false)
	drone_at_6_0 = pc6(pr0, false)
	drone_at_7_0 = pc7(pr0, false)
	drone_at_8_0 = pc8(pr0, false)
	drone_at_9_0 = pc9(pr0, false)
	drone_at_0_1 = pc0(pr1, false)
	drone_at_1_1 = pc1(pr1, false)
	drone_at_2_1 = pc2(pr1, false)
	drone_at_3_1 = pc3(pr1, false)
	drone_at_4_1 = pc4(pr1, false)
	drone_at_5_1 = pc5(pr1, false)
	drone_at_6_1 = pc6(pr1, false)
	drone_at_7_1 = pc7(pr1, false)
	drone_at_8_1 = pc8(pr1, false)
	drone_at_9_1 = pc9(pr1, false)
	drone_at_0_2 = pc0(pr2, false)
	drone_at_1_2 = pc1(pr2, false)
	drone_at_2_2 = pc2(pr2, false)
	drone_at_3_2 = pc3(pr2, false)
	drone_at_4_2 = pc4(pr2, false)
	drone_at_5_2 = pc5(pr2, false)
	drone_at_6_2 = pc6(pr2, false)
	drone_at_7_2 = pc7(pr2, false)
	drone_at_8_2 = pc8(pr2, false)
	drone_at_9_2 = pc9(pr2, false)
	drone_at_0_3 = pc0(pr3, false)
	drone_at_1_3 = pc1(pr3, false)
	drone_at_2_3 = pc2(pr3, false)
	drone_at_3_3 = pc3(pr3, false)
	drone_at_4_3 = pc4(pr3, false)
	drone_at_5_3 = pc5(pr3, false)
	drone_at_6_3 = pc6(pr3, false)
	drone_at_7_3 = pc7(pr3, false)
	drone_at_8_3 = pc8(pr3, false)
	drone_at_9_3 = pc9(pr3, false)
	drone_at_0_4 = pc0(pr4, false)
	drone_at_1_4 = pc1(pr4, false)
	drone_at_2_4 = pc2(pr4, false)
	drone_at_3_4 = pc3(pr4, false)
	drone_at_4_4 = pc4(pr4, false)
	drone_at_5_4 = pc5(pr4, false)
	drone_at_6_4 = pc6(pr4, false)
	drone_at_7_4 = pc7(pr4, false)
	drone_at_8_4 = pc8(pr4, false)
	drone_at_9_4 = pc9(pr4, false)
	drone_at_0_5 = pc0(pr5, false)
	drone_at_1_5 = pc1(pr5, false)
	drone_at_2_5 = pc2(pr5, false)
	drone_at_3_5 = pc3(pr5, false)
	drone_at_4_5 = pc4(pr5, false)
	drone_at_5_5 = pc5(pr5, false)
	drone_at_6_5 = pc6(pr5, false)
	drone_at_7_5 = pc7(pr5, false)
	drone_at_8_5 = pc8(pr5, false)
	drone_at_9_5 = pc9(pr5, false)
	drone_at_0_6 = pc0(pr6, false)
	drone_at_1_6 = pc1(pr6, false)
	drone_at_2_6 = pc2(pr6, false)
	drone_at_3_6 = pc3(pr6, false)
	drone_at_4_6 = pc4(pr6, false)
	drone_at_5_6 = pc5(pr6, false)
	drone_at_6_6 = pc6(pr6, false)
	drone_at_7_6 = pc7(pr6, false)
	drone_at_8_6 = pc8(pr6, false)
	drone_at_9_6 = pc9(pr6, false)
	drone_at_0_7 = pc0(pr7, false)
	drone_at_1_7 = pc1(pr7, false)
	drone_at_2_7 = pc2(pr7, false)
	drone_at_3_7 = pc3(pr7, false)
	drone_at_4_7 = pc4(pr7, false)
	drone_at_5_7 = pc5(pr7, false)
	drone_at_6_7 = pc6(pr7, false)
	drone_at_7_7 = pc7(pr7, false)
	drone_at_8_7 = pc8(pr7, false)
	drone_at_9_7 = pc9(pr7, false)
	drone_at_0_8 = pc0(pr8, false)
	drone_at_1_8 = pc1(pr8, false)
	drone_at_2_8 = pc2(pr8, false)
	drone_at_3_8 = pc3(pr8, false)
	drone_at_4_8 = pc4(pr8, false)
	drone_at_5_8 = pc5(pr8, false)
	drone_at_6_8 = pc6(pr8, false)
	drone_at_7_8 = pc7(pr8, false)
	drone_at_8_8 = pc8(pr8, false)
	drone_at_9_8 = pc9(pr8, false)
	drone_at_0_9 = pc0(pr9, false)
	drone_at_1_9 = pc1(pr9, false)
	drone_at_2_9 = pc2(pr9, false)
	drone_at_3_9 = pc3(pr9, false)
	drone_at_4_9 = pc4(pr9, false)
	drone_at_5_9 = pc5(pr9, false)
	drone_at_6_9 = pc6(pr9, false)
	drone_at_7_9 = pc7(pr9, false)
	drone_at_8_9 = pc8(pr9, false)
	drone_at_9_9 = pc9(pr9, false)

	t_0_0_visited = t_0_0_visited(true, drone_at_0_0)
	t_1_0_visited = t_1_0_visited(true, drone_at_1_0)
	t_2_0_visited = t_2_0_visited(true, drone_at_2_0)
	t_3_0_visited = t_3_0_visited(true, drone_at_3_0)
	t_4_0_visited = t_4_0_visited(true, drone_at_4_0)
	t_5_0_visited = t_5_0_visited(true, drone_at_5_0)
	t_6_0_visited = t_6_0_visited(true, drone_at_6_0)
	t_7_0_visited = t_7_0_visited(true, drone_at_7_0)
	t_8_0_visited = t_8_0_visited(true, drone_at_8_0)
	t_9_0_visited = t_9_0_visited(true, drone_at_9_0)
	t_0_1_visited = t_0_1_visited(true, drone_at_0_1)
	t_1_1_visited = t_1_1_visited(true, drone_at_1_1)
	t_2_1_visited = t_2_1_visited(true, drone_at_2_1)
	t_3_1_visited = t_3_1_visited(true, drone_at_3_1)
	t_4_1_visited = t_4_1_visited(true, drone_at_4_1)
	t_5_1_visited = t_5_1_visited(true, drone_at_5_1)
	t_6_1_visited = t_6_1_visited(true, drone_at_6_1)
	t_7_1_visited = t_7_1_visited(true, drone_at_7_1)
	t_8_1_visited = t_8_1_visited(true, drone_at_8_1)
	t_9_1_visited = t_9_1_visited(true, drone_at_9_1)
	t_0_2_visited = t_0_2_visited(true, drone_at_0_2)
	t_1_2_visited = t_1_2_visited(true, drone_at_1_2)
	t_2_2_visited = t_2_2_visited(true, drone_at_2_2)
	t_3_2_visited = t_3_2_visited(true, drone_at_3_2)
	t_4_2_visited = t_4_2_visited(true, drone_at_4_2)
	t_5_2_visited = t_5_2_visited(true, drone_at_5_2)
	t_6_2_visited = t_6_2_visited(true, drone_at_6_2)
	t_7_2_visited = t_7_2_visited(true, drone_at_7_2)
	t_8_2_visited = t_8_2_visited(true, drone_at_8_2)
	t_9_2_visited = t_9_2_visited(true, drone_at_9_2)
	t_0_3_visited = t_0_3_visited(true, drone_at_0_3)
	t_1_3_visited = t_1_3_visited(true, drone_at_1_3)
	t_2_3_visited = t_2_3_visited(true, drone_at_2_3)
	t_3_3_visited = t_3_3_visited(true, drone_at_3_3)
	t_4_3_visited = t_4_3_visited(true, drone_at_4_3)
	t_5_3_visited = t_5_3_visited(true, drone_at_5_3)
	t_6_3_visited = t_6_3_visited(true, drone_at_6_3)
	t_7_3_visited = t_7_3_visited(true, drone_at_7_3)
	t_8_3_visited = t_8_3_visited(true, drone_at_8_3)
	t_9_3_visited = t_9_3_visited(true, drone_at_9_3)
	t_0_4_visited = t_0_4_visited(true, drone_at_0_4)
	t_1_4_visited = t_1_4_visited(true, drone_at_1_4)
	t_2_4_visited = t_2_4_visited(true, drone_at_2_4)
	t_3_4_visited = t_3_4_visited(true, drone_at_3_4)
	t_4_4_visited = t_4_4_visited(true, drone_at_4_4)
	t_5_4_visited = t_5_4_visited(true, drone_at_5_4)
	t_6_4_visited = t_6_4_visited(true, drone_at_6_4)
	t_7_4_visited = t_7_4_visited(true, drone_at_7_4)
	t_8_4_visited = t_8_4_visited(true, drone_at_8_4)
	t_9_4_visited = t_9_4_visited(true, drone_at_9_4)
	t_0_5_visited = t_0_5_visited(true, drone_at_0_5)
	t_1_5_visited = t_1_5_visited(true, drone_at_1_5)
	t_2_5_visited = t_2_5_visited(true, drone_at_2_5)
	t_3_5_visited = t_3_5_visited(true, drone_at_3_5)
	t_4_5_visited = t_4_5_visited(true, drone_at_4_5)
	t_5_5_visited = t_5_5_visited(true, drone_at_5_5)
	t_6_5_visited = t_6_5_visited(true, drone_at_6_5)
	t_7_5_visited = t_7_5_visited(true, drone_at_7_5)
	t_8_5_visited = t_8_5_visited(true, drone_at_8_5)
	t_9_5_visited = t_9_5_visited(true, drone_at_9_5)
	t_0_6_visited = t_0_6_visited(true, drone_at_0_6)
	t_1_6_visited = t_1_6_visited(true, drone_at_1_6)
	t_2_6_visited = t_2_6_visited(true, drone_at_2_6)
	t_3_6_visited = t_3_6_visited(true, drone_at_3_6)
	t_4_6_visited = t_4_6_visited(true, drone_at_4_6)
	t_5_6_visited = t_5_6_visited(true, drone_at_5_6)
	t_6_6_visited = t_6_6_visited(true, drone_at_6_6)
	t_7_6_visited = t_7_6_visited(true, drone_at_7_6)
	t_8_6_visited = t_8_6_visited(true, drone_at_8_6)
	t_9_6_visited = t_9_6_visited(true, drone_at_9_6)
	t_0_7_visited = t_0_7_visited(true, drone_at_0_7)
	t_1_7_visited = t_1_7_visited(true, drone_at_1_7)
	t_2_7_visited = t_2_7_visited(true, drone_at_2_7)
	t_3_7_visited = t_3_7_visited(true, drone_at_3_7)
	t_4_7_visited = t_4_7_visited(true, drone_at_4_7)
	t_5_7_visited = t_5_7_visited(true, drone_at_5_7)
	t_6_7_visited = t_6_7_visited(true, drone_at_6_7)
	t_7_7_visited = t_7_7_visited(true, drone_at_7_7)
	t_8_7_visited = t_8_7_visited(true, drone_at_8_7)
	t_9_7_visited = t_9_7_visited(true, drone_at_9_7)
	t_0_8_visited = t_0_8_visited(true, drone_at_0_8)
	t_1_8_visited = t_1_8_visited(true, drone_at_1_8)
	t_2_8_visited = t_2_8_visited(true, drone_at_2_8)
	t_3_8_visited = t_3_8_visited(true, drone_at_3_8)
	t_4_8_visited = t_4_8_visited(true, drone_at_4_8)
	t_5_8_visited = t_5_8_visited(true, drone_at_5_8)
	t_6_8_visited = t_6_8_visited(true, drone_at_6_8)
	t_7_8_visited = t_7_8_visited(true, drone_at_7_8)
	t_8_8_visited = t_8_8_visited(true, drone_at_8_8)
	t_9_8_visited = t_9_8_visited(true, drone_at_9_8)
	t_0_9_visited = t_0_9_visited(true, drone_at_0_9)
	t_1_9_visited = t_1_9_visited(true, drone_at_1_9)
	t_2_9_visited = t_2_9_visited(true, drone_at_2_9)
	t_3_9_visited = t_3_9_visited(true, drone_at_3_9)
	t_4_9_visited = t_4_9_visited(true, drone_at_4_9)
	t_5_9_visited = t_5_9_visited(true, drone_at_5_9)
	t_6_9_visited = t_6_9_visited(true, drone_at_6_9)
	t_7_9_visited = t_7_9_visited(true, drone_at_7_9)
	t_8_9_visited = t_8_9_visited(true, drone_at_8_9)
	t_9_9_visited = t_9_9_visited(true, drone_at_9_9)

	vert_wall_0_0 = vert_wall_0_0(drone_at_0_0(not_moved_south, drone_at_0_1(not_moved_north, true)), false)
	vert_wall_1_0 = vert_wall_1_0(drone_at_1_0(not_moved_south, drone_at_1_1(not_moved_north, true)), false)
	vert_wall_2_0 = vert_wall_2_0(drone_at_2_0(not_moved_south, drone_at_2_1(not_moved_north, true)), false)
	vert_wall_3_0 = vert_wall_3_0(drone_at_3_0(not_moved_south, drone_at_3_1(not_moved_north, true)), false)
	vert_wall_4_0 = vert_wall_4_0(drone_at_4_0(not_moved_south, drone_at_4_1(not_moved_north, true)), false)
	vert_wall_5_0 = vert_wall_5_0(drone_at_5_0(not_moved_south, drone_at_5_1(not_moved_north, true)), false)
	vert_wall_6_0 = vert_wall_6_0(drone_at_6_0(not_moved_south, drone_at_6_1(not_moved_north, true)), false)
	vert_wall_7_0 = vert_wall_7_0(drone_at_7_0(not_moved_south, drone_at_7_1(not_moved_north, true)), false)
	vert_wall_8_0 = vert_wall_8_0(drone_at_8_0(not_moved_south, drone_at_8_1(not_moved_north, true)), false)
	vert_wall_9_0 = vert_wall_9_0(drone_at_9_0(not_moved_south, drone_at_9_1(not_moved_north, true)), false)
	vert_wall_0_1 = vert_wall_0_1(drone_at_0_1(not_moved_south, drone_at_0_2(not_moved_north, true)), false)
	vert_wall_1_1 = vert_wall_1_1(drone_at_1_1(not_moved_south, drone_at_1_2(not_moved_north, true)), false)
	vert_wall_2_1 = vert_wall_2_1(drone_at_2_1(not_moved_south, drone_at_2_2(not_moved_north, true)), false)
	vert_wall_3_1 = vert_wall_3_1(drone_at_3_1(not_moved_south, drone_at_3_2(not_moved_north, true)), false)
	vert_wall_4_1 = vert_wall_4_1(drone_at_4_1(not_moved_south, drone_at_4_2(not_moved_north, true)), false)
	vert_wall_5_1 = vert_wall_5_1(drone_at_5_1(not_moved_south, drone_at_5_2(not_moved_north, true)), false)
	vert_wall_6_1 = vert_wall_6_1(drone_at_6_1(not_moved_south, drone_at_6_2(not_moved_north, true)), false)
	vert_wall_7_1 = vert_wall_7_1(drone_at_7_1(not_moved_south, drone_at_7_2(not_moved_north, true)), false)
	vert_wall_8_1 = vert_wall_8_1(drone_at_8_1(not_moved_south, drone_at_8_2(not_moved_north, true)), false)
	vert_wall_9_1 = vert_wall_9_1(drone_at_9_1(not_moved_south, drone_at_9_2(not_moved_north, true)), false)
	vert_wall_0_2 = vert_wall_0_2(drone_at_0_2(not_moved_south, drone_at_0_3(not_moved_north, true)), false)
	vert_wall_1_2 = vert_wall_1_2(drone_at_1_2(not_moved_south, drone_at_1_3(not_moved_north, true)), false)
	vert_wall_2_2 = vert_wall_2_2(drone_at_2_2(not_moved_south, drone_at_2_3(not_moved_north, true)), false)
	vert_wall_3_2 = vert_wall_3_2(drone_at_3_2(not_moved_south, drone_at_3_3(not_moved_north, true)), false)
	vert_wall_4_2 = vert_wall_4_2(drone_at_4_2(not_moved_south, drone_at_4_3(not_moved_north, true)), false)
	vert_wall_5_2 = vert_wall_5_2(drone_at_5_2(not_moved_south, drone_at_5_3(not_moved_north, true)), false)
	vert_wall_6_2 = vert_wall_6_2(drone_at_6_2(not_moved_south, drone_at_6_3(not_moved_north, true)), false)
	vert_wall_7_2 = vert_wall_7_2(drone_at_7_2(not_moved_south, drone_at_7_3(not_moved_north, true)), false)
	vert_wall_8_2 = vert_wall_8_2(drone_at_8_2(not_moved_south, drone_at_8_3(not_moved_north, true)), false)
	vert_wall_9_2 = vert_wall_9_2(drone_at_9_2(not_moved_south, drone_at_9_3(not_moved_north, true)), false)
	vert_wall_0_3 = vert_wall_0_3(drone_at_0_3(not_moved_south, drone_at_0_4(not_moved_north, true)), false)
	vert_wall_1_3 = vert_wall_1_3(drone_at_1_3(not_moved_south, drone_at_1_4(not_moved_north, true)), false)
	vert_wall_2_3 = vert_wall_2_3(drone_at_2_3(not_moved_south, drone_at_2_4(not_moved_north, true)), false)
	vert_wall_3_3 = vert_wall_3_3(drone_at_3_3(not_moved_south, drone_at_3_4(not_moved_north, true)), false)
	vert_wall_4_3 = vert_wall_4_3(drone_at_4_3(not_moved_south, drone_at_4_4(not_moved_north, true)), false)
	vert_wall_5_3 = vert_wall_5_3(drone_at_5_3(not_moved_south, drone_at_5_4(not_moved_north, true)), false)
	vert_wall_6_3 = vert_wall_6_3(drone_at_6_3(not_moved_south, drone_at_6_4(not_moved_north, true)), false)
	vert_wall_7_3 = vert_wall_7_3(drone_at_7_3(not_moved_south, drone_at_7_4(not_moved_north, true)), false)
	vert_wall_8_3 = vert_wall_8_3(drone_at_8_3(not_moved_south, drone_at_8_4(not_moved_north, true)), false)
	vert_wall_9_3 = vert_wall_9_3(drone_at_9_3(not_moved_south, drone_at_9_4(not_moved_north, true)), false)
	vert_wall_0_4 = vert_wall_0_4(drone_at_0_4(not_moved_south, drone_at_0_5(not_moved_north, true)), false)
	vert_wall_1_4 = vert_wall_1_4(drone_at_1_4(not_moved_south, drone_at_1_5(not_moved_north, true)), false)
	vert_wall_2_4 = vert_wall_2_4(drone_at_2_4(not_moved_south, drone_at_2_5(not_moved_north, true)), false)
	vert_wall_3_4 = vert_wall_3_4(drone_at_3_4(not_moved_south, drone_at_3_5(not_moved_north, true)), false)
	vert_wall_4_4 = vert_wall_4_4(drone_at_4_4(not_moved_south, drone_at_4_5(not_moved_north, true)), false)
	vert_wall_5_4 = vert_wall_5_4(drone_at_5_4(not_moved_south, drone_at_5_5(not_moved_north, true)), false)
	vert_wall_6_4 = vert_wall_6_4(drone_at_6_4(not_moved_south, drone_at_6_5(not_moved_north, true)), false)
	vert_wall_7_4 = vert_wall_7_4(drone_at_7_4(not_moved_south, drone_at_7_5(not_moved_north, true)), false)
	vert_wall_8_4 = vert_wall_8_4(drone_at_8_4(not_moved_south, drone_at_8_5(not_moved_north, true)), false)
	vert_wall_9_4 = vert_wall_9_4(drone_at_9_4(not_moved_south, drone_at_9_5(not_moved_north, true)), false)
	vert_wall_0_5 = vert_wall_0_5(drone_at_0_5(not_moved_south, drone_at_0_6(not_moved_north, true)), false)
	vert_wall_1_5 = vert_wall_1_5(drone_at_1_5(not_moved_south, drone_at_1_6(not_moved_north, true)), false)
	vert_wall_2_5 = vert_wall_2_5(drone_at_2_5(not_moved_south, drone_at_2_6(not_moved_north, true)), false)
	vert_wall_3_5 = vert_wall_3_5(drone_at_3_5(not_moved_south, drone_at_3_6(not_moved_north, true)), false)
	vert_wall_4_5 = vert_wall_4_5(drone_at_4_5(not_moved_south, drone_at_4_6(not_moved_north, true)), false)
	vert_wall_5_5 = vert_wall_5_5(drone_at_5_5(not_moved_south, drone_at_5_6(not_moved_north, true)), false)
	vert_wall_6_5 = vert_wall_6_5(drone_at_6_5(not_moved_south, drone_at_6_6(not_moved_north, true)), false)
	vert_wall_7_5 = vert_wall_7_5(drone_at_7_5(not_moved_south, drone_at_7_6(not_moved_north, true)), false)
	vert_wall_8_5 = vert_wall_8_5(drone_at_8_5(not_moved_south, drone_at_8_6(not_moved_north, true)), false)
	vert_wall_9_5 = vert_wall_9_5(drone_at_9_5(not_moved_south, drone_at_9_6(not_moved_north, true)), false)
	vert_wall_0_6 = vert_wall_0_6(drone_at_0_6(not_moved_south, drone_at_0_7(not_moved_north, true)), false)
	vert_wall_1_6 = vert_wall_1_6(drone_at_1_6(not_moved_south, drone_at_1_7(not_moved_north, true)), false)
	vert_wall_2_6 = vert_wall_2_6(drone_at_2_6(not_moved_south, drone_at_2_7(not_moved_north, true)), false)
	vert_wall_3_6 = vert_wall_3_6(drone_at_3_6(not_moved_south, drone_at_3_7(not_moved_north, true)), false)
	vert_wall_4_6 = vert_wall_4_6(drone_at_4_6(not_moved_south, drone_at_4_7(not_moved_north, true)), false)
	vert_wall_5_6 = vert_wall_5_6(drone_at_5_6(not_moved_south, drone_at_5_7(not_moved_north, true)), false)
	vert_wall_6_6 = vert_wall_6_6(drone_at_6_6(not_moved_south, drone_at_6_7(not_moved_north, true)), false)
	vert_wall_7_6 = vert_wall_7_6(drone_at_7_6(not_moved_south, drone_at_7_7(not_moved_north, true)), false)
	vert_wall_8_6 = vert_wall_8_6(drone_at_8_6(not_moved_south, drone_at_8_7(not_moved_north, true)), false)
	vert_wall_9_6 = vert_wall_9_6(drone_at_9_6(not_moved_south, drone_at_9_7(not_moved_north, true)), false)
	vert_wall_0_7 = vert_wall_0_7(drone_at_0_7(not_moved_south, drone_at_0_8(not_moved_north, true)), false)
	vert_wall_1_7 = vert_wall_1_7(drone_at_1_7(not_moved_south, drone_at_1_8(not_moved_north, true)), false)
	vert_wall_2_7 = vert_wall_2_7(drone_at_2_7(not_moved_south, drone_at_2_8(not_moved_north, true)), false)
	vert_wall_3_7 = vert_wall_3_7(drone_at_3_7(not_moved_south, drone_at_3_8(not_moved_north, true)), false)
	vert_wall_4_7 = vert_wall_4_7(drone_at_4_7(not_moved_south, drone_at_4_8(not_moved_north, true)), false)
	vert_wall_5_7 = vert_wall_5_7(drone_at_5_7(not_moved_south, drone_at_5_8(not_moved_north, true)), false)
	vert_wall_6_7 = vert_wall_6_7(drone_at_6_7(not_moved_south, drone_at_6_8(not_moved_north, true)), false)
	vert_wall_7_7 = vert_wall_7_7(drone_at_7_7(not_moved_south, drone_at_7_8(not_moved_north, true)), false)
	vert_wall_8_7 = vert_wall_8_7(drone_at_8_7(not_moved_south, drone_at_8_8(not_moved_north, true)), false)
	vert_wall_9_7 = vert_wall_9_7(drone_at_9_7(not_moved_south, drone_at_9_8(not_moved_north, true)), false)
	vert_wall_0_8 = vert_wall_0_8(drone_at_0_8(not_moved_south, drone_at_0_9(not_moved_north, true)), false)
	vert_wall_1_8 = vert_wall_1_8(drone_at_1_8(not_moved_south, drone_at_1_9(not_moved_north, true)), false)
	vert_wall_2_8 = vert_wall_2_8(drone_at_2_8(not_moved_south, drone_at_2_9(not_moved_north, true)), false)
	vert_wall_3_8 = vert_wall_3_8(drone_at_3_8(not_moved_south, drone_at_3_9(not_moved_north, true)), false)
	vert_wall_4_8 = vert_wall_4_8(drone_at_4_8(not_moved_south, drone_at_4_9(not_moved_north, true)), false)
	vert_wall_5_8 = vert_wall_5_8(drone_at_5_8(not_moved_south, drone_at_5_9(not_moved_north, true)), false)
	vert_wall_6_8 = vert_wall_6_8(drone_at_6_8(not_moved_south, drone_at_6_9(not_moved_north, true)), false)
	vert_wall_7_8 = vert_wall_7_8(drone_at_7_8(not_moved_south, drone_at_7_9(not_moved_north, true)), false)
	vert_wall_8_8 = vert_wall_8_8(drone_at_8_8(not_moved_south, drone_at_8_9(not_moved_north, true)), false)
	vert_wall_9_8 = vert_wall_9_8(drone_at_9_8(not_moved_south, drone_at_9_9(not_moved_north, true)), false)

	horiz_wall_0_0 = horiz_wall_0_0(drone_at_0_0(not_moved_west, drone_at_1_0(not_moved_east, true)), false)
	horiz_wall_1_0 = horiz_wall_1_0(drone_at_1_0(not_moved_west, drone_at_2_0(not_moved_east, true)), false)
	horiz_wall_2_0 = horiz_wall_2_0(drone_at_2_0(not_moved_west, drone_at_3_0(not_moved_east, true)), false)
	horiz_wall_3_0 = horiz_wall_3_0(drone_at_3_0(not_moved_west, drone_at_4_0(not_moved_east, true)), false)
	horiz_wall_4_0 = horiz_wall_4_0(drone_at_4_0(not_moved_west, drone_at_5_0(not_moved_east, true)), false)
	horiz_wall_5_0 = horiz_wall_5_0(drone_at_5_0(not_moved_west, drone_at_6_0(not_moved_east, true)), false)
	horiz_wall_6_0 = horiz_wall_6_0(drone_at_6_0(not_moved_west, drone_at_7_0(not_moved_east, true)), false)
	horiz_wall_7_0 = horiz_wall_7_0(drone_at_7_0(not_moved_west, drone_at_8_0(not_moved_east, true)), false)
	horiz_wall_8_0 = horiz_wall_8_0(drone_at_8_0(not_moved_west, drone_at_9_0(not_moved_east, true)), false)
	horiz_wall_0_1 = horiz_wall_0_1(drone_at_0_1(not_moved_west, drone_at_1_1(not_moved_east, true)), false)
	horiz_wall_1_1 = horiz_wall_1_1(drone_at_1_1(not_moved_west, drone_at_2_1(not_moved_east, true)), false)
	horiz_wall_2_1 = horiz_wall_2_1(drone_at_2_1(not_moved_west, drone_at_3_1(not_moved_east, true)), false)
	horiz_wall_3_1 = horiz_wall_3_1(drone_at_3_1(not_moved_west, drone_at_4_1(not_moved_east, true)), false)
	horiz_wall_4_1 = horiz_wall_4_1(drone_at_4_1(not_moved_west, drone_at_5_1(not_moved_east, true)), false)
	horiz_wall_5_1 = horiz_wall_5_1(drone_at_5_1(not_moved_west, drone_at_6_1(not_moved_east, true)), false)
	horiz_wall_6_1 = horiz_wall_6_1(drone_at_6_1(not_moved_west, drone_at_7_1(not_moved_east, true)), false)
	horiz_wall_7_1 = horiz_wall_7_1(drone_at_7_1(not_moved_west, drone_at_8_1(not_moved_east, true)), false)
	horiz_wall_8_1 = horiz_wall_8_1(drone_at_8_1(not_moved_west, drone_at_9_1(not_moved_east, true)), false)
	horiz_wall_0_2 = horiz_wall_0_2(drone_at_0_2(not_moved_west, drone_at_1_2(not_moved_east, true)), false)
	horiz_wall_1_2 = horiz_wall_1_2(drone_at_1_2(not_moved_west, drone_at_2_2(not_moved_east, true)), false)
	horiz_wall_2_2 = horiz_wall_2_2(drone_at_2_2(not_moved_west, drone_at_3_2(not_moved_east, true)), false)
	horiz_wall_3_2 = horiz_wall_3_2(drone_at_3_2(not_moved_west, drone_at_4_2(not_moved_east, true)), false)
	horiz_wall_4_2 = horiz_wall_4_2(drone_at_4_2(not_moved_west, drone_at_5_2(not_moved_east, true)), false)
	horiz_wall_5_2 = horiz_wall_5_2(drone_at_5_2(not_moved_west, drone_at_6_2(not_moved_east, true)), false)
	horiz_wall_6_2 = horiz_wall_6_2(drone_at_6_2(not_moved_west, drone_at_7_2(not_moved_east, true)), false)
	horiz_wall_7_2 = horiz_wall_7_2(drone_at_7_2(not_moved_west, drone_at_8_2(not_moved_east, true)), false)
	horiz_wall_8_2 = horiz_wall_8_2(drone_at_8_2(not_moved_west, drone_at_9_2(not_moved_east, true)), false)
	horiz_wall_0_3 = horiz_wall_0_3(drone_at_0_3(not_moved_west, drone_at_1_3(not_moved_east, true)), false)
	horiz_wall_1_3 = horiz_wall_1_3(drone_at_1_3(not_moved_west, drone_at_2_3(not_moved_east, true)), false)
	horiz_wall_2_3 = horiz_wall_2_3(drone_at_2_3(not_moved_west, drone_at_3_3(not_moved_east, true)), false)
	horiz_wall_3_3 = horiz_wall_3_3(drone_at_3_3(not_moved_west, drone_at_4_3(not_moved_east, true)), false)
	horiz_wall_4_3 = horiz_wall_4_3(drone_at_4_3(not_moved_west, drone_at_5_3(not_moved_east, true)), false)
	horiz_wall_5_3 = horiz_wall_5_3(drone_at_5_3(not_moved_west, drone_at_6_3(not_moved_east, true)), false)
	horiz_wall_6_3 = horiz_wall_6_3(drone_at_6_3(not_moved_west, drone_at_7_3(not_moved_east, true)), false)
	horiz_wall_7_3 = horiz_wall_7_3(drone_at_7_3(not_moved_west, drone_at_8_3(not_moved_east, true)), false)
	horiz_wall_8_3 = horiz_wall_8_3(drone_at_8_3(not_moved_west, drone_at_9_3(not_moved_east, true)), false)
	horiz_wall_0_4 = horiz_wall_0_4(drone_at_0_4(not_moved_west, drone_at_1_4(not_moved_east, true)), false)
	horiz_wall_1_4 = horiz_wall_1_4(drone_at_1_4(not_moved_west, drone_at_2_4(not_moved_east, true)), false)
	horiz_wall_2_4 = horiz_wall_2_4(drone_at_2_4(not_moved_west, drone_at_3_4(not_moved_east, true)), false)
	horiz_wall_3_4 = horiz_wall_3_4(drone_at_3_4(not_moved_west, drone_at_4_4(not_moved_east, true)), false)
	horiz_wall_4_4 = horiz_wall_4_4(drone_at_4_4(not_moved_west, drone_at_5_4(not_moved_east, true)), false)
	horiz_wall_5_4 = horiz_wall_5_4(drone_at_5_4(not_moved_west, drone_at_6_4(not_moved_east, true)), false)
	horiz_wall_6_4 = horiz_wall_6_4(drone_at_6_4(not_moved_west, drone_at_7_4(not_moved_east, true)), false)
	horiz_wall_7_4 = horiz_wall_7_4(drone_at_7_4(not_moved_west, drone_at_8_4(not_moved_east, true)), false)
	horiz_wall_8_4 = horiz_wall_8_4(drone_at_8_4(not_moved_west, drone_at_9_4(not_moved_east, true)), false)
	horiz_wall_0_5 = horiz_wall_0_5(drone_at_0_5(not_moved_west, drone_at_1_5(not_moved_east, true)), false)
	horiz_wall_1_5 = horiz_wall_1_5(drone_at_1_5(not_moved_west, drone_at_2_5(not_moved_east, true)), false)
	horiz_wall_2_5 = horiz_wall_2_5(drone_at_2_5(not_moved_west, drone_at_3_5(not_moved_east, true)), false)
	horiz_wall_3_5 = horiz_wall_3_5(drone_at_3_5(not_moved_west, drone_at_4_5(not_moved_east, true)), false)
	horiz_wall_4_5 = horiz_wall_4_5(drone_at_4_5(not_moved_west, drone_at_5_5(not_moved_east, true)), false)
	horiz_wall_5_5 = horiz_wall_5_5(drone_at_5_5(not_moved_west, drone_at_6_5(not_moved_east, true)), false)
	horiz_wall_6_5 = horiz_wall_6_5(drone_at_6_5(not_moved_west, drone_at_7_5(not_moved_east, true)), false)
	horiz_wall_7_5 = horiz_wall_7_5(drone_at_7_5(not_moved_west, drone_at_8_5(not_moved_east, true)), false)
	horiz_wall_8_5 = horiz_wall_8_5(drone_at_8_5(not_moved_west, drone_at_9_5(not_moved_east, true)), false)
	horiz_wall_0_6 = horiz_wall_0_6(drone_at_0_6(not_moved_west, drone_at_1_6(not_moved_east, true)), false)
	horiz_wall_1_6 = horiz_wall_1_6(drone_at_1_6(not_moved_west, drone_at_2_6(not_moved_east, true)), false)
	horiz_wall_2_6 = horiz_wall_2_6(drone_at_2_6(not_moved_west, drone_at_3_6(not_moved_east, true)), false)
	horiz_wall_3_6 = horiz_wall_3_6(drone_at_3_6(not_moved_west, drone_at_4_6(not_moved_east, true)), false)
	horiz_wall_4_6 = horiz_wall_4_6(drone_at_4_6(not_moved_west, drone_at_5_6(not_moved_east, true)), false)
	horiz_wall_5_6 = horiz_wall_5_6(drone_at_5_6(not_moved_west, drone_at_6_6(not_moved_east, true)), false)
	horiz_wall_6_6 = horiz_wall_6_6(drone_at_6_6(not_moved_west, drone_at_7_6(not_moved_east, true)), false)
	horiz_wall_7_6 = horiz_wall_7_6(drone_at_7_6(not_moved_west, drone_at_8_6(not_moved_east, true)), false)
	horiz_wall_8_6 = horiz_wall_8_6(drone_at_8_6(not_moved_west, drone_at_9_6(not_moved_east, true)), false)
	horiz_wall_0_7 = horiz_wall_0_7(drone_at_0_7(not_moved_west, drone_at_1_7(not_moved_east, true)), false)
	horiz_wall_1_7 = horiz_wall_1_7(drone_at_1_7(not_moved_west, drone_at_2_7(not_moved_east, true)), false)
	horiz_wall_2_7 = horiz_wall_2_7(drone_at_2_7(not_moved_west, drone_at_3_7(not_moved_east, true)), false)
	horiz_wall_3_7 = horiz_wall_3_7(drone_at_3_7(not_moved_west, drone_at_4_7(not_moved_east, true)), false)
	horiz_wall_4_7 = horiz_wall_4_7(drone_at_4_7(not_moved_west, drone_at_5_7(not_moved_east, true)), false)
	horiz_wall_5_7 = horiz_wall_5_7(drone_at_5_7(not_moved_west, drone_at_6_7(not_moved_east, true)), false)
	horiz_wall_6_7 = horiz_wall_6_7(drone_at_6_7(not_moved_west, drone_at_7_7(not_moved_east, true)), false)
	horiz_wall_7_7 = horiz_wall_7_7(drone_at_7_7(not_moved_west, drone_at_8_7(not_moved_east, true)), false)
	horiz_wall_8_7 = horiz_wall_8_7(drone_at_8_7(not_moved_west, drone_at_9_7(not_moved_east, true)), false)
	horiz_wall_0_8 = horiz_wall_0_8(drone_at_0_8(not_moved_west, drone_at_1_8(not_moved_east, true)), false)
	horiz_wall_1_8 = horiz_wall_1_8(drone_at_1_8(not_moved_west, drone_at_2_8(not_moved_east, true)), false)
	horiz_wall_2_8 = horiz_wall_2_8(drone_at_2_8(not_moved_west, drone_at_3_8(not_moved_east, true)), false)
	horiz_wall_3_8 = horiz_wall_3_8(drone_at_3_8(not_moved_west, drone_at_4_8(not_moved_east, true)), false)
	horiz_wall_4_8 = horiz_wall_4_8(drone_at_4_8(not_moved_west, drone_at_5_8(not_moved_east, true)), false)
	horiz_wall_5_8 = horiz_wall_5_8(drone_at_5_8(not_moved_west, drone_at_6_8(not_moved_east, true)), false)
	horiz_wall_6_8 = horiz_wall_6_8(drone_at_6_8(not_moved_west, drone_at_7_8(not_moved_east, true)), false)
	horiz_wall_7_8 = horiz_wall_7_8(drone_at_7_8(not_moved_west, drone_at_8_8(not_moved_east, true)), false)
	horiz_wall_8_8 = horiz_wall_8_8(drone_at_8_8(not_moved_west, drone_at_9_8(not_moved_east, true)), false)
	horiz_wall_0_9 = horiz_wall_0_9(drone_at_0_9(not_moved_west, drone_at_1_9(not_moved_east, true)), false)
	horiz_wall_1_9 = horiz_wall_1_9(drone_at_1_9(not_moved_west, drone_at_2_9(not_moved_east, true)), false)
	horiz_wall_2_9 = horiz_wall_2_9(drone_at_2_9(not_moved_west, drone_at_3_9(not_moved_east, true)), false)
	horiz_wall_3_9 = horiz_wall_3_9(drone_at_3_9(not_moved_west, drone_at_4_9(not_moved_east, true)), false)
	horiz_wall_4_9 = horiz_wall_4_9(drone_at_4_9(not_moved_west, drone_at_5_9(not_moved_east, true)), false)
	horiz_wall_5_9 = horiz_wall_5_9(drone_at_5_9(not_moved_west, drone_at_6_9(not_moved_east, true)), false)
	horiz_wall_6_9 = horiz_wall_6_9(drone_at_6_9(not_moved_west, drone_at_7_9(not_moved_east, true)), false)
	horiz_wall_7_9 = horiz_wall_7_9(drone_at_7_9(not_moved_west, drone_at_8_9(not_moved_east, true)), false)
	horiz_wall_8_9 = horiz_wall_8_9(drone_at_8_9(not_moved_west, drone_at_9_9(not_moved_east, true)), false)

	fully_mapped = And10(And10(t_0_0_visited, t_1_0_visited, t_2_0_visited, t_3_0_visited, t_4_0_visited, t_5_0_visited, t_6_0_visited, t_7_0_visited, t_8_0_visited, t_9_0_visited),
	And10(t_0_1_visited, t_1_1_visited, t_2_1_visited, t_3_1_visited, t_4_1_visited, t_5_1_visited, t_6_1_visited, t_7_1_visited, t_8_1_visited, t_9_1_visited),
	And10(t_0_2_visited, t_1_2_visited, t_2_2_visited, t_3_2_visited, t_4_2_visited, t_5_2_visited, t_6_2_visited, t_7_2_visited, t_8_2_visited, t_9_2_visited),
	And10(t_0_3_visited, t_1_3_visited, t_2_3_visited, t_3_3_visited, t_4_3_visited, t_5_3_visited, t_6_3_visited, t_7_3_visited, t_8_3_visited, t_9_3_visited),
	And10(t_0_4_visited, t_1_4_visited, t_2_4_visited, t_3_4_visited, t_4_4_visited, t_5_4_visited, t_6_4_visited, t_7_4_visited, t_8_4_visited, t_9_4_visited),
	And10(t_0_5_visited, t_1_5_visited, t_2_5_visited, t_3_5_visited, t_4_5_visited, t_5_5_visited, t_6_5_visited, t_7_5_visited, t_8_5_visited, t_9_5_visited),
	And10(t_0_6_visited, t_1_6_visited, t_2_6_visited, t_3_6_visited, t_4_6_visited, t_5_6_visited, t_6_6_visited, t_7_6_visited, t_8_6_visited, t_9_6_visited),
	And10(t_0_7_visited, t_1_7_visited, t_2_7_visited, t_3_7_visited, t_4_7_visited, t_5_7_visited, t_6_7_visited, t_7_7_visited, t_8_7_visited, t_9_7_visited),
	And10(t_0_8_visited, t_1_8_visited, t_2_8_visited, t_3_8_visited, t_4_8_visited, t_5_8_visited, t_6_8_visited, t_7_8_visited, t_8_8_visited, t_9_8_visited),
	And10(t_0_9_visited, t_1_9_visited, t_2_9_visited, t_3_9_visited, t_4_9_visited, t_5_9_visited, t_6_9_visited, t_7_9_visited, t_8_9_visited, t_9_9_visited))(True, False)

if measure():
	tc0 = pc0
	tc1 = pc1
	tc2 = pc2
	tc3 = pc3
	tc4 = pc4
	tc5 = pc5
	tc6 = pc6
	tc7 = pc7
	tc8 = pc8
	tc9 = pc9

	tr0 = pr0
	tr1 = pr1
	tr2 = pr2
	tr3 = pr3
	tr4 = pr4
	tr5 = pr5
	tr6 = pr6
	tr7 = pr7
	tr8 = pr8
	tr9 = pr9

decode_t = {0:(true,false,false,false,false,false,false,false,false,false),
1:(false,true,false,false,false,false,false,false,false,false),
2:(false,false,true,false,false,false,false,false,false,false),
3:(false,false,false,true,false,false,false,false,false,false),
4:(false,false,false,false,true,false,false,false,false,false),
5:(false,false,false,false,false,true,false,false,false,false),
6:(false,false,false,false,false,false,true,false,false,false),
7:(false,false,false,false,false,false,false,true,false,false),
8:(false,false,false,false,false,false,false,false,true,false),
9:(false,false,false,false,false,false,false,false,false,true)}

same_col = pc0(tc0, pc1(tc1, pc2(tc2, pc3(tc3, pc4(tc4, pc5(tc5, pc6(tc6, pc7(tc7, pc8(tc8, pc9(tc9, false))))))))))
same_row = pr0(tr0, pr1(tr1, pr2(tr2, pr3(tr3, pr4(tr4, pr5(tr5, pr6(tr6, pr7(tr7, pr8(tr8, pr9(tr9, false))))))))))

on_chest = same_col(same_row, false)(True, False)

for maze_iteration in range(299):
	north_detected = false
	east_detected = false
	south_detected = false
	west_detected = false

	while not on_chest:
		drone_found = False

		check_north = south_detected(dud, check_north_wall)()
		check_east = west_detected(dud, check_east_wall)()
		check_south = north_detected(dud, check_south_wall)()
		check_west = east_detected(dud, check_west_wall)()

		not_north_break = check_north(alt_move_north, dud)()(false, true)
		not_north_break(nothing, move)(South)

		not_east_break = check_east(alt_move_east, dud)()(false, true)
		not_east_break(nothing, move)(West)

		not_south_break = check_south(alt_move_south, dud)()(false, true)
		not_south_break(nothing, move)(North)

		not_west_break = check_west(alt_move_west, dud)()(false, true)
		not_west_break(nothing, move)(East)

		vert_wall_0_0 = vert_wall_0_0(drone_at_0_0(not_north_break, drone_at_0_1(not_south_break, true)), false)
		vert_wall_1_0 = vert_wall_1_0(drone_at_1_0(not_north_break, drone_at_1_1(not_south_break, true)), false)
		vert_wall_2_0 = vert_wall_2_0(drone_at_2_0(not_north_break, drone_at_2_1(not_south_break, true)), false)
		vert_wall_3_0 = vert_wall_3_0(drone_at_3_0(not_north_break, drone_at_3_1(not_south_break, true)), false)
		vert_wall_4_0 = vert_wall_4_0(drone_at_4_0(not_north_break, drone_at_4_1(not_south_break, true)), false)
		vert_wall_5_0 = vert_wall_5_0(drone_at_5_0(not_north_break, drone_at_5_1(not_south_break, true)), false)
		vert_wall_6_0 = vert_wall_6_0(drone_at_6_0(not_north_break, drone_at_6_1(not_south_break, true)), false)
		vert_wall_7_0 = vert_wall_7_0(drone_at_7_0(not_north_break, drone_at_7_1(not_south_break, true)), false)
		vert_wall_8_0 = vert_wall_8_0(drone_at_8_0(not_north_break, drone_at_8_1(not_south_break, true)), false)
		vert_wall_9_0 = vert_wall_9_0(drone_at_9_0(not_north_break, drone_at_9_1(not_south_break, true)), false)
		vert_wall_0_1 = vert_wall_0_1(drone_at_0_1(not_north_break, drone_at_0_2(not_south_break, true)), false)
		vert_wall_1_1 = vert_wall_1_1(drone_at_1_1(not_north_break, drone_at_1_2(not_south_break, true)), false)
		vert_wall_2_1 = vert_wall_2_1(drone_at_2_1(not_north_break, drone_at_2_2(not_south_break, true)), false)
		vert_wall_3_1 = vert_wall_3_1(drone_at_3_1(not_north_break, drone_at_3_2(not_south_break, true)), false)
		vert_wall_4_1 = vert_wall_4_1(drone_at_4_1(not_north_break, drone_at_4_2(not_south_break, true)), false)
		vert_wall_5_1 = vert_wall_5_1(drone_at_5_1(not_north_break, drone_at_5_2(not_south_break, true)), false)
		vert_wall_6_1 = vert_wall_6_1(drone_at_6_1(not_north_break, drone_at_6_2(not_south_break, true)), false)
		vert_wall_7_1 = vert_wall_7_1(drone_at_7_1(not_north_break, drone_at_7_2(not_south_break, true)), false)
		vert_wall_8_1 = vert_wall_8_1(drone_at_8_1(not_north_break, drone_at_8_2(not_south_break, true)), false)
		vert_wall_9_1 = vert_wall_9_1(drone_at_9_1(not_north_break, drone_at_9_2(not_south_break, true)), false)
		vert_wall_0_2 = vert_wall_0_2(drone_at_0_2(not_north_break, drone_at_0_3(not_south_break, true)), false)
		vert_wall_1_2 = vert_wall_1_2(drone_at_1_2(not_north_break, drone_at_1_3(not_south_break, true)), false)
		vert_wall_2_2 = vert_wall_2_2(drone_at_2_2(not_north_break, drone_at_2_3(not_south_break, true)), false)
		vert_wall_3_2 = vert_wall_3_2(drone_at_3_2(not_north_break, drone_at_3_3(not_south_break, true)), false)
		vert_wall_4_2 = vert_wall_4_2(drone_at_4_2(not_north_break, drone_at_4_3(not_south_break, true)), false)
		vert_wall_5_2 = vert_wall_5_2(drone_at_5_2(not_north_break, drone_at_5_3(not_south_break, true)), false)
		vert_wall_6_2 = vert_wall_6_2(drone_at_6_2(not_north_break, drone_at_6_3(not_south_break, true)), false)
		vert_wall_7_2 = vert_wall_7_2(drone_at_7_2(not_north_break, drone_at_7_3(not_south_break, true)), false)
		vert_wall_8_2 = vert_wall_8_2(drone_at_8_2(not_north_break, drone_at_8_3(not_south_break, true)), false)
		vert_wall_9_2 = vert_wall_9_2(drone_at_9_2(not_north_break, drone_at_9_3(not_south_break, true)), false)
		vert_wall_0_3 = vert_wall_0_3(drone_at_0_3(not_north_break, drone_at_0_4(not_south_break, true)), false)
		vert_wall_1_3 = vert_wall_1_3(drone_at_1_3(not_north_break, drone_at_1_4(not_south_break, true)), false)
		vert_wall_2_3 = vert_wall_2_3(drone_at_2_3(not_north_break, drone_at_2_4(not_south_break, true)), false)
		vert_wall_3_3 = vert_wall_3_3(drone_at_3_3(not_north_break, drone_at_3_4(not_south_break, true)), false)
		vert_wall_4_3 = vert_wall_4_3(drone_at_4_3(not_north_break, drone_at_4_4(not_south_break, true)), false)
		vert_wall_5_3 = vert_wall_5_3(drone_at_5_3(not_north_break, drone_at_5_4(not_south_break, true)), false)
		vert_wall_6_3 = vert_wall_6_3(drone_at_6_3(not_north_break, drone_at_6_4(not_south_break, true)), false)
		vert_wall_7_3 = vert_wall_7_3(drone_at_7_3(not_north_break, drone_at_7_4(not_south_break, true)), false)
		vert_wall_8_3 = vert_wall_8_3(drone_at_8_3(not_north_break, drone_at_8_4(not_south_break, true)), false)
		vert_wall_9_3 = vert_wall_9_3(drone_at_9_3(not_north_break, drone_at_9_4(not_south_break, true)), false)
		vert_wall_0_4 = vert_wall_0_4(drone_at_0_4(not_north_break, drone_at_0_5(not_south_break, true)), false)
		vert_wall_1_4 = vert_wall_1_4(drone_at_1_4(not_north_break, drone_at_1_5(not_south_break, true)), false)
		vert_wall_2_4 = vert_wall_2_4(drone_at_2_4(not_north_break, drone_at_2_5(not_south_break, true)), false)
		vert_wall_3_4 = vert_wall_3_4(drone_at_3_4(not_north_break, drone_at_3_5(not_south_break, true)), false)
		vert_wall_4_4 = vert_wall_4_4(drone_at_4_4(not_north_break, drone_at_4_5(not_south_break, true)), false)
		vert_wall_5_4 = vert_wall_5_4(drone_at_5_4(not_north_break, drone_at_5_5(not_south_break, true)), false)
		vert_wall_6_4 = vert_wall_6_4(drone_at_6_4(not_north_break, drone_at_6_5(not_south_break, true)), false)
		vert_wall_7_4 = vert_wall_7_4(drone_at_7_4(not_north_break, drone_at_7_5(not_south_break, true)), false)
		vert_wall_8_4 = vert_wall_8_4(drone_at_8_4(not_north_break, drone_at_8_5(not_south_break, true)), false)
		vert_wall_9_4 = vert_wall_9_4(drone_at_9_4(not_north_break, drone_at_9_5(not_south_break, true)), false)
		vert_wall_0_5 = vert_wall_0_5(drone_at_0_5(not_north_break, drone_at_0_6(not_south_break, true)), false)
		vert_wall_1_5 = vert_wall_1_5(drone_at_1_5(not_north_break, drone_at_1_6(not_south_break, true)), false)
		vert_wall_2_5 = vert_wall_2_5(drone_at_2_5(not_north_break, drone_at_2_6(not_south_break, true)), false)
		vert_wall_3_5 = vert_wall_3_5(drone_at_3_5(not_north_break, drone_at_3_6(not_south_break, true)), false)
		vert_wall_4_5 = vert_wall_4_5(drone_at_4_5(not_north_break, drone_at_4_6(not_south_break, true)), false)
		vert_wall_5_5 = vert_wall_5_5(drone_at_5_5(not_north_break, drone_at_5_6(not_south_break, true)), false)
		vert_wall_6_5 = vert_wall_6_5(drone_at_6_5(not_north_break, drone_at_6_6(not_south_break, true)), false)
		vert_wall_7_5 = vert_wall_7_5(drone_at_7_5(not_north_break, drone_at_7_6(not_south_break, true)), false)
		vert_wall_8_5 = vert_wall_8_5(drone_at_8_5(not_north_break, drone_at_8_6(not_south_break, true)), false)
		vert_wall_9_5 = vert_wall_9_5(drone_at_9_5(not_north_break, drone_at_9_6(not_south_break, true)), false)
		vert_wall_0_6 = vert_wall_0_6(drone_at_0_6(not_north_break, drone_at_0_7(not_south_break, true)), false)
		vert_wall_1_6 = vert_wall_1_6(drone_at_1_6(not_north_break, drone_at_1_7(not_south_break, true)), false)
		vert_wall_2_6 = vert_wall_2_6(drone_at_2_6(not_north_break, drone_at_2_7(not_south_break, true)), false)
		vert_wall_3_6 = vert_wall_3_6(drone_at_3_6(not_north_break, drone_at_3_7(not_south_break, true)), false)
		vert_wall_4_6 = vert_wall_4_6(drone_at_4_6(not_north_break, drone_at_4_7(not_south_break, true)), false)
		vert_wall_5_6 = vert_wall_5_6(drone_at_5_6(not_north_break, drone_at_5_7(not_south_break, true)), false)
		vert_wall_6_6 = vert_wall_6_6(drone_at_6_6(not_north_break, drone_at_6_7(not_south_break, true)), false)
		vert_wall_7_6 = vert_wall_7_6(drone_at_7_6(not_north_break, drone_at_7_7(not_south_break, true)), false)
		vert_wall_8_6 = vert_wall_8_6(drone_at_8_6(not_north_break, drone_at_8_7(not_south_break, true)), false)
		vert_wall_9_6 = vert_wall_9_6(drone_at_9_6(not_north_break, drone_at_9_7(not_south_break, true)), false)
		vert_wall_0_7 = vert_wall_0_7(drone_at_0_7(not_north_break, drone_at_0_8(not_south_break, true)), false)
		vert_wall_1_7 = vert_wall_1_7(drone_at_1_7(not_north_break, drone_at_1_8(not_south_break, true)), false)
		vert_wall_2_7 = vert_wall_2_7(drone_at_2_7(not_north_break, drone_at_2_8(not_south_break, true)), false)
		vert_wall_3_7 = vert_wall_3_7(drone_at_3_7(not_north_break, drone_at_3_8(not_south_break, true)), false)
		vert_wall_4_7 = vert_wall_4_7(drone_at_4_7(not_north_break, drone_at_4_8(not_south_break, true)), false)
		vert_wall_5_7 = vert_wall_5_7(drone_at_5_7(not_north_break, drone_at_5_8(not_south_break, true)), false)
		vert_wall_6_7 = vert_wall_6_7(drone_at_6_7(not_north_break, drone_at_6_8(not_south_break, true)), false)
		vert_wall_7_7 = vert_wall_7_7(drone_at_7_7(not_north_break, drone_at_7_8(not_south_break, true)), false)
		vert_wall_8_7 = vert_wall_8_7(drone_at_8_7(not_north_break, drone_at_8_8(not_south_break, true)), false)
		vert_wall_9_7 = vert_wall_9_7(drone_at_9_7(not_north_break, drone_at_9_8(not_south_break, true)), false)
		vert_wall_0_8 = vert_wall_0_8(drone_at_0_8(not_north_break, drone_at_0_9(not_south_break, true)), false)
		vert_wall_1_8 = vert_wall_1_8(drone_at_1_8(not_north_break, drone_at_1_9(not_south_break, true)), false)
		vert_wall_2_8 = vert_wall_2_8(drone_at_2_8(not_north_break, drone_at_2_9(not_south_break, true)), false)
		vert_wall_3_8 = vert_wall_3_8(drone_at_3_8(not_north_break, drone_at_3_9(not_south_break, true)), false)
		vert_wall_4_8 = vert_wall_4_8(drone_at_4_8(not_north_break, drone_at_4_9(not_south_break, true)), false)
		vert_wall_5_8 = vert_wall_5_8(drone_at_5_8(not_north_break, drone_at_5_9(not_south_break, true)), false)
		vert_wall_6_8 = vert_wall_6_8(drone_at_6_8(not_north_break, drone_at_6_9(not_south_break, true)), false)
		vert_wall_7_8 = vert_wall_7_8(drone_at_7_8(not_north_break, drone_at_7_9(not_south_break, true)), false)
		vert_wall_8_8 = vert_wall_8_8(drone_at_8_8(not_north_break, drone_at_8_9(not_south_break, true)), false)
		vert_wall_9_8 = vert_wall_9_8(drone_at_9_8(not_north_break, drone_at_9_9(not_south_break, true)), false)

		horiz_wall_0_0 = horiz_wall_0_0(drone_at_0_0(not_east_break, drone_at_1_0(not_west_break, true)), false)
		horiz_wall_1_0 = horiz_wall_1_0(drone_at_1_0(not_east_break, drone_at_2_0(not_west_break, true)), false)
		horiz_wall_2_0 = horiz_wall_2_0(drone_at_2_0(not_east_break, drone_at_3_0(not_west_break, true)), false)
		horiz_wall_3_0 = horiz_wall_3_0(drone_at_3_0(not_east_break, drone_at_4_0(not_west_break, true)), false)
		horiz_wall_4_0 = horiz_wall_4_0(drone_at_4_0(not_east_break, drone_at_5_0(not_west_break, true)), false)
		horiz_wall_5_0 = horiz_wall_5_0(drone_at_5_0(not_east_break, drone_at_6_0(not_west_break, true)), false)
		horiz_wall_6_0 = horiz_wall_6_0(drone_at_6_0(not_east_break, drone_at_7_0(not_west_break, true)), false)
		horiz_wall_7_0 = horiz_wall_7_0(drone_at_7_0(not_east_break, drone_at_8_0(not_west_break, true)), false)
		horiz_wall_8_0 = horiz_wall_8_0(drone_at_8_0(not_east_break, drone_at_9_0(not_west_break, true)), false)
		horiz_wall_0_1 = horiz_wall_0_1(drone_at_0_1(not_east_break, drone_at_1_1(not_west_break, true)), false)
		horiz_wall_1_1 = horiz_wall_1_1(drone_at_1_1(not_east_break, drone_at_2_1(not_west_break, true)), false)
		horiz_wall_2_1 = horiz_wall_2_1(drone_at_2_1(not_east_break, drone_at_3_1(not_west_break, true)), false)
		horiz_wall_3_1 = horiz_wall_3_1(drone_at_3_1(not_east_break, drone_at_4_1(not_west_break, true)), false)
		horiz_wall_4_1 = horiz_wall_4_1(drone_at_4_1(not_east_break, drone_at_5_1(not_west_break, true)), false)
		horiz_wall_5_1 = horiz_wall_5_1(drone_at_5_1(not_east_break, drone_at_6_1(not_west_break, true)), false)
		horiz_wall_6_1 = horiz_wall_6_1(drone_at_6_1(not_east_break, drone_at_7_1(not_west_break, true)), false)
		horiz_wall_7_1 = horiz_wall_7_1(drone_at_7_1(not_east_break, drone_at_8_1(not_west_break, true)), false)
		horiz_wall_8_1 = horiz_wall_8_1(drone_at_8_1(not_east_break, drone_at_9_1(not_west_break, true)), false)
		horiz_wall_0_2 = horiz_wall_0_2(drone_at_0_2(not_east_break, drone_at_1_2(not_west_break, true)), false)
		horiz_wall_1_2 = horiz_wall_1_2(drone_at_1_2(not_east_break, drone_at_2_2(not_west_break, true)), false)
		horiz_wall_2_2 = horiz_wall_2_2(drone_at_2_2(not_east_break, drone_at_3_2(not_west_break, true)), false)
		horiz_wall_3_2 = horiz_wall_3_2(drone_at_3_2(not_east_break, drone_at_4_2(not_west_break, true)), false)
		horiz_wall_4_2 = horiz_wall_4_2(drone_at_4_2(not_east_break, drone_at_5_2(not_west_break, true)), false)
		horiz_wall_5_2 = horiz_wall_5_2(drone_at_5_2(not_east_break, drone_at_6_2(not_west_break, true)), false)
		horiz_wall_6_2 = horiz_wall_6_2(drone_at_6_2(not_east_break, drone_at_7_2(not_west_break, true)), false)
		horiz_wall_7_2 = horiz_wall_7_2(drone_at_7_2(not_east_break, drone_at_8_2(not_west_break, true)), false)
		horiz_wall_8_2 = horiz_wall_8_2(drone_at_8_2(not_east_break, drone_at_9_2(not_west_break, true)), false)
		horiz_wall_0_3 = horiz_wall_0_3(drone_at_0_3(not_east_break, drone_at_1_3(not_west_break, true)), false)
		horiz_wall_1_3 = horiz_wall_1_3(drone_at_1_3(not_east_break, drone_at_2_3(not_west_break, true)), false)
		horiz_wall_2_3 = horiz_wall_2_3(drone_at_2_3(not_east_break, drone_at_3_3(not_west_break, true)), false)
		horiz_wall_3_3 = horiz_wall_3_3(drone_at_3_3(not_east_break, drone_at_4_3(not_west_break, true)), false)
		horiz_wall_4_3 = horiz_wall_4_3(drone_at_4_3(not_east_break, drone_at_5_3(not_west_break, true)), false)
		horiz_wall_5_3 = horiz_wall_5_3(drone_at_5_3(not_east_break, drone_at_6_3(not_west_break, true)), false)
		horiz_wall_6_3 = horiz_wall_6_3(drone_at_6_3(not_east_break, drone_at_7_3(not_west_break, true)), false)
		horiz_wall_7_3 = horiz_wall_7_3(drone_at_7_3(not_east_break, drone_at_8_3(not_west_break, true)), false)
		horiz_wall_8_3 = horiz_wall_8_3(drone_at_8_3(not_east_break, drone_at_9_3(not_west_break, true)), false)
		horiz_wall_0_4 = horiz_wall_0_4(drone_at_0_4(not_east_break, drone_at_1_4(not_west_break, true)), false)
		horiz_wall_1_4 = horiz_wall_1_4(drone_at_1_4(not_east_break, drone_at_2_4(not_west_break, true)), false)
		horiz_wall_2_4 = horiz_wall_2_4(drone_at_2_4(not_east_break, drone_at_3_4(not_west_break, true)), false)
		horiz_wall_3_4 = horiz_wall_3_4(drone_at_3_4(not_east_break, drone_at_4_4(not_west_break, true)), false)
		horiz_wall_4_4 = horiz_wall_4_4(drone_at_4_4(not_east_break, drone_at_5_4(not_west_break, true)), false)
		horiz_wall_5_4 = horiz_wall_5_4(drone_at_5_4(not_east_break, drone_at_6_4(not_west_break, true)), false)
		horiz_wall_6_4 = horiz_wall_6_4(drone_at_6_4(not_east_break, drone_at_7_4(not_west_break, true)), false)
		horiz_wall_7_4 = horiz_wall_7_4(drone_at_7_4(not_east_break, drone_at_8_4(not_west_break, true)), false)
		horiz_wall_8_4 = horiz_wall_8_4(drone_at_8_4(not_east_break, drone_at_9_4(not_west_break, true)), false)
		horiz_wall_0_5 = horiz_wall_0_5(drone_at_0_5(not_east_break, drone_at_1_5(not_west_break, true)), false)
		horiz_wall_1_5 = horiz_wall_1_5(drone_at_1_5(not_east_break, drone_at_2_5(not_west_break, true)), false)
		horiz_wall_2_5 = horiz_wall_2_5(drone_at_2_5(not_east_break, drone_at_3_5(not_west_break, true)), false)
		horiz_wall_3_5 = horiz_wall_3_5(drone_at_3_5(not_east_break, drone_at_4_5(not_west_break, true)), false)
		horiz_wall_4_5 = horiz_wall_4_5(drone_at_4_5(not_east_break, drone_at_5_5(not_west_break, true)), false)
		horiz_wall_5_5 = horiz_wall_5_5(drone_at_5_5(not_east_break, drone_at_6_5(not_west_break, true)), false)
		horiz_wall_6_5 = horiz_wall_6_5(drone_at_6_5(not_east_break, drone_at_7_5(not_west_break, true)), false)
		horiz_wall_7_5 = horiz_wall_7_5(drone_at_7_5(not_east_break, drone_at_8_5(not_west_break, true)), false)
		horiz_wall_8_5 = horiz_wall_8_5(drone_at_8_5(not_east_break, drone_at_9_5(not_west_break, true)), false)
		horiz_wall_0_6 = horiz_wall_0_6(drone_at_0_6(not_east_break, drone_at_1_6(not_west_break, true)), false)
		horiz_wall_1_6 = horiz_wall_1_6(drone_at_1_6(not_east_break, drone_at_2_6(not_west_break, true)), false)
		horiz_wall_2_6 = horiz_wall_2_6(drone_at_2_6(not_east_break, drone_at_3_6(not_west_break, true)), false)
		horiz_wall_3_6 = horiz_wall_3_6(drone_at_3_6(not_east_break, drone_at_4_6(not_west_break, true)), false)
		horiz_wall_4_6 = horiz_wall_4_6(drone_at_4_6(not_east_break, drone_at_5_6(not_west_break, true)), false)
		horiz_wall_5_6 = horiz_wall_5_6(drone_at_5_6(not_east_break, drone_at_6_6(not_west_break, true)), false)
		horiz_wall_6_6 = horiz_wall_6_6(drone_at_6_6(not_east_break, drone_at_7_6(not_west_break, true)), false)
		horiz_wall_7_6 = horiz_wall_7_6(drone_at_7_6(not_east_break, drone_at_8_6(not_west_break, true)), false)
		horiz_wall_8_6 = horiz_wall_8_6(drone_at_8_6(not_east_break, drone_at_9_6(not_west_break, true)), false)
		horiz_wall_0_7 = horiz_wall_0_7(drone_at_0_7(not_east_break, drone_at_1_7(not_west_break, true)), false)
		horiz_wall_1_7 = horiz_wall_1_7(drone_at_1_7(not_east_break, drone_at_2_7(not_west_break, true)), false)
		horiz_wall_2_7 = horiz_wall_2_7(drone_at_2_7(not_east_break, drone_at_3_7(not_west_break, true)), false)
		horiz_wall_3_7 = horiz_wall_3_7(drone_at_3_7(not_east_break, drone_at_4_7(not_west_break, true)), false)
		horiz_wall_4_7 = horiz_wall_4_7(drone_at_4_7(not_east_break, drone_at_5_7(not_west_break, true)), false)
		horiz_wall_5_7 = horiz_wall_5_7(drone_at_5_7(not_east_break, drone_at_6_7(not_west_break, true)), false)
		horiz_wall_6_7 = horiz_wall_6_7(drone_at_6_7(not_east_break, drone_at_7_7(not_west_break, true)), false)
		horiz_wall_7_7 = horiz_wall_7_7(drone_at_7_7(not_east_break, drone_at_8_7(not_west_break, true)), false)
		horiz_wall_8_7 = horiz_wall_8_7(drone_at_8_7(not_east_break, drone_at_9_7(not_west_break, true)), false)
		horiz_wall_0_8 = horiz_wall_0_8(drone_at_0_8(not_east_break, drone_at_1_8(not_west_break, true)), false)
		horiz_wall_1_8 = horiz_wall_1_8(drone_at_1_8(not_east_break, drone_at_2_8(not_west_break, true)), false)
		horiz_wall_2_8 = horiz_wall_2_8(drone_at_2_8(not_east_break, drone_at_3_8(not_west_break, true)), false)
		horiz_wall_3_8 = horiz_wall_3_8(drone_at_3_8(not_east_break, drone_at_4_8(not_west_break, true)), false)
		horiz_wall_4_8 = horiz_wall_4_8(drone_at_4_8(not_east_break, drone_at_5_8(not_west_break, true)), false)
		horiz_wall_5_8 = horiz_wall_5_8(drone_at_5_8(not_east_break, drone_at_6_8(not_west_break, true)), false)
		horiz_wall_6_8 = horiz_wall_6_8(drone_at_6_8(not_east_break, drone_at_7_8(not_west_break, true)), false)
		horiz_wall_7_8 = horiz_wall_7_8(drone_at_7_8(not_east_break, drone_at_8_8(not_west_break, true)), false)
		horiz_wall_8_8 = horiz_wall_8_8(drone_at_8_8(not_east_break, drone_at_9_8(not_west_break, true)), false)
		horiz_wall_0_9 = horiz_wall_0_9(drone_at_0_9(not_east_break, drone_at_1_9(not_west_break, true)), false)
		horiz_wall_1_9 = horiz_wall_1_9(drone_at_1_9(not_east_break, drone_at_2_9(not_west_break, true)), false)
		horiz_wall_2_9 = horiz_wall_2_9(drone_at_2_9(not_east_break, drone_at_3_9(not_west_break, true)), false)
		horiz_wall_3_9 = horiz_wall_3_9(drone_at_3_9(not_east_break, drone_at_4_9(not_west_break, true)), false)
		horiz_wall_4_9 = horiz_wall_4_9(drone_at_4_9(not_east_break, drone_at_5_9(not_west_break, true)), false)
		horiz_wall_5_9 = horiz_wall_5_9(drone_at_5_9(not_east_break, drone_at_6_9(not_west_break, true)), false)
		horiz_wall_6_9 = horiz_wall_6_9(drone_at_6_9(not_east_break, drone_at_7_9(not_west_break, true)), false)
		horiz_wall_7_9 = horiz_wall_7_9(drone_at_7_9(not_east_break, drone_at_8_9(not_west_break, true)), false)
		horiz_wall_8_9 = horiz_wall_8_9(drone_at_8_9(not_east_break, drone_at_9_9(not_west_break, true)), false)

		t_0_0_spread = false
		t_1_0_spread = false
		t_2_0_spread = false
		t_3_0_spread = false
		t_4_0_spread = false
		t_5_0_spread = false
		t_6_0_spread = false
		t_7_0_spread = false
		t_8_0_spread = false
		t_9_0_spread = false
		t_0_1_spread = false
		t_1_1_spread = false
		t_2_1_spread = false
		t_3_1_spread = false
		t_4_1_spread = false
		t_5_1_spread = false
		t_6_1_spread = false
		t_7_1_spread = false
		t_8_1_spread = false
		t_9_1_spread = false
		t_0_2_spread = false
		t_1_2_spread = false
		t_2_2_spread = false
		t_3_2_spread = false
		t_4_2_spread = false
		t_5_2_spread = false
		t_6_2_spread = false
		t_7_2_spread = false
		t_8_2_spread = false
		t_9_2_spread = false
		t_0_3_spread = false
		t_1_3_spread = false
		t_2_3_spread = false
		t_3_3_spread = false
		t_4_3_spread = false
		t_5_3_spread = false
		t_6_3_spread = false
		t_7_3_spread = false
		t_8_3_spread = false
		t_9_3_spread = false
		t_0_4_spread = false
		t_1_4_spread = false
		t_2_4_spread = false
		t_3_4_spread = false
		t_4_4_spread = false
		t_5_4_spread = false
		t_6_4_spread = false
		t_7_4_spread = false
		t_8_4_spread = false
		t_9_4_spread = false
		t_0_5_spread = false
		t_1_5_spread = false
		t_2_5_spread = false
		t_3_5_spread = false
		t_4_5_spread = false
		t_5_5_spread = false
		t_6_5_spread = false
		t_7_5_spread = false
		t_8_5_spread = false
		t_9_5_spread = false
		t_0_6_spread = false
		t_1_6_spread = false
		t_2_6_spread = false
		t_3_6_spread = false
		t_4_6_spread = false
		t_5_6_spread = false
		t_6_6_spread = false
		t_7_6_spread = false
		t_8_6_spread = false
		t_9_6_spread = false
		t_0_7_spread = false
		t_1_7_spread = false
		t_2_7_spread = false
		t_3_7_spread = false
		t_4_7_spread = false
		t_5_7_spread = false
		t_6_7_spread = false
		t_7_7_spread = false
		t_8_7_spread = false
		t_9_7_spread = false
		t_0_8_spread = false
		t_1_8_spread = false
		t_2_8_spread = false
		t_3_8_spread = false
		t_4_8_spread = false
		t_5_8_spread = false
		t_6_8_spread = false
		t_7_8_spread = false
		t_8_8_spread = false
		t_9_8_spread = false
		t_0_9_spread = false
		t_1_9_spread = false
		t_2_9_spread = false
		t_3_9_spread = false
		t_4_9_spread = false
		t_5_9_spread = false
		t_6_9_spread = false
		t_7_9_spread = false
		t_8_9_spread = false
		t_9_9_spread = false

		while not drone_found:
			t_0_0_spread_copy = t_0_0_spread
			t_1_0_spread_copy = t_1_0_spread
			t_2_0_spread_copy = t_2_0_spread
			t_3_0_spread_copy = t_3_0_spread
			t_4_0_spread_copy = t_4_0_spread
			t_5_0_spread_copy = t_5_0_spread
			t_6_0_spread_copy = t_6_0_spread
			t_7_0_spread_copy = t_7_0_spread
			t_8_0_spread_copy = t_8_0_spread
			t_9_0_spread_copy = t_9_0_spread
			t_0_1_spread_copy = t_0_1_spread
			t_1_1_spread_copy = t_1_1_spread
			t_2_1_spread_copy = t_2_1_spread
			t_3_1_spread_copy = t_3_1_spread
			t_4_1_spread_copy = t_4_1_spread
			t_5_1_spread_copy = t_5_1_spread
			t_6_1_spread_copy = t_6_1_spread
			t_7_1_spread_copy = t_7_1_spread
			t_8_1_spread_copy = t_8_1_spread
			t_9_1_spread_copy = t_9_1_spread
			t_0_2_spread_copy = t_0_2_spread
			t_1_2_spread_copy = t_1_2_spread
			t_2_2_spread_copy = t_2_2_spread
			t_3_2_spread_copy = t_3_2_spread
			t_4_2_spread_copy = t_4_2_spread
			t_5_2_spread_copy = t_5_2_spread
			t_6_2_spread_copy = t_6_2_spread
			t_7_2_spread_copy = t_7_2_spread
			t_8_2_spread_copy = t_8_2_spread
			t_9_2_spread_copy = t_9_2_spread
			t_0_3_spread_copy = t_0_3_spread
			t_1_3_spread_copy = t_1_3_spread
			t_2_3_spread_copy = t_2_3_spread
			t_3_3_spread_copy = t_3_3_spread
			t_4_3_spread_copy = t_4_3_spread
			t_5_3_spread_copy = t_5_3_spread
			t_6_3_spread_copy = t_6_3_spread
			t_7_3_spread_copy = t_7_3_spread
			t_8_3_spread_copy = t_8_3_spread
			t_9_3_spread_copy = t_9_3_spread
			t_0_4_spread_copy = t_0_4_spread
			t_1_4_spread_copy = t_1_4_spread
			t_2_4_spread_copy = t_2_4_spread
			t_3_4_spread_copy = t_3_4_spread
			t_4_4_spread_copy = t_4_4_spread
			t_5_4_spread_copy = t_5_4_spread
			t_6_4_spread_copy = t_6_4_spread
			t_7_4_spread_copy = t_7_4_spread
			t_8_4_spread_copy = t_8_4_spread
			t_9_4_spread_copy = t_9_4_spread
			t_0_5_spread_copy = t_0_5_spread
			t_1_5_spread_copy = t_1_5_spread
			t_2_5_spread_copy = t_2_5_spread
			t_3_5_spread_copy = t_3_5_spread
			t_4_5_spread_copy = t_4_5_spread
			t_5_5_spread_copy = t_5_5_spread
			t_6_5_spread_copy = t_6_5_spread
			t_7_5_spread_copy = t_7_5_spread
			t_8_5_spread_copy = t_8_5_spread
			t_9_5_spread_copy = t_9_5_spread
			t_0_6_spread_copy = t_0_6_spread
			t_1_6_spread_copy = t_1_6_spread
			t_2_6_spread_copy = t_2_6_spread
			t_3_6_spread_copy = t_3_6_spread
			t_4_6_spread_copy = t_4_6_spread
			t_5_6_spread_copy = t_5_6_spread
			t_6_6_spread_copy = t_6_6_spread
			t_7_6_spread_copy = t_7_6_spread
			t_8_6_spread_copy = t_8_6_spread
			t_9_6_spread_copy = t_9_6_spread
			t_0_7_spread_copy = t_0_7_spread
			t_1_7_spread_copy = t_1_7_spread
			t_2_7_spread_copy = t_2_7_spread
			t_3_7_spread_copy = t_3_7_spread
			t_4_7_spread_copy = t_4_7_spread
			t_5_7_spread_copy = t_5_7_spread
			t_6_7_spread_copy = t_6_7_spread
			t_7_7_spread_copy = t_7_7_spread
			t_8_7_spread_copy = t_8_7_spread
			t_9_7_spread_copy = t_9_7_spread
			t_0_8_spread_copy = t_0_8_spread
			t_1_8_spread_copy = t_1_8_spread
			t_2_8_spread_copy = t_2_8_spread
			t_3_8_spread_copy = t_3_8_spread
			t_4_8_spread_copy = t_4_8_spread
			t_5_8_spread_copy = t_5_8_spread
			t_6_8_spread_copy = t_6_8_spread
			t_7_8_spread_copy = t_7_8_spread
			t_8_8_spread_copy = t_8_8_spread
			t_9_8_spread_copy = t_9_8_spread
			t_0_9_spread_copy = t_0_9_spread
			t_1_9_spread_copy = t_1_9_spread
			t_2_9_spread_copy = t_2_9_spread
			t_3_9_spread_copy = t_3_9_spread
			t_4_9_spread_copy = t_4_9_spread
			t_5_9_spread_copy = t_5_9_spread
			t_6_9_spread_copy = t_6_9_spread
			t_7_9_spread_copy = t_7_9_spread
			t_8_9_spread_copy = t_8_9_spread
			t_9_9_spread_copy = t_9_9_spread

			t_0_0_spread = tc0(tr0, false)(true, t_0_1_spread_copy(vert_wall_0_0, true)(t_1_0_spread_copy(horiz_wall_0_0(false, true), false), true))
			t_1_0_spread = tc1(tr0, false)(true, t_1_1_spread_copy(vert_wall_1_0, true)(t_2_0_spread_copy(horiz_wall_1_0, true)(t_0_0_spread_copy(horiz_wall_0_0(false, true), false), true), true))
			t_2_0_spread = tc2(tr0, false)(true, t_2_1_spread_copy(vert_wall_2_0, true)(t_3_0_spread_copy(horiz_wall_2_0, true)(t_1_0_spread_copy(horiz_wall_1_0(false, true), false), true), true))
			t_3_0_spread = tc3(tr0, false)(true, t_3_1_spread_copy(vert_wall_3_0, true)(t_4_0_spread_copy(horiz_wall_3_0, true)(t_2_0_spread_copy(horiz_wall_2_0(false, true), false), true), true))
			t_4_0_spread = tc4(tr0, false)(true, t_4_1_spread_copy(vert_wall_4_0, true)(t_5_0_spread_copy(horiz_wall_4_0, true)(t_3_0_spread_copy(horiz_wall_3_0(false, true), false), true), true))
			t_5_0_spread = tc5(tr0, false)(true, t_5_1_spread_copy(vert_wall_5_0, true)(t_6_0_spread_copy(horiz_wall_5_0, true)(t_4_0_spread_copy(horiz_wall_4_0(false, true), false), true), true))
			t_6_0_spread = tc6(tr0, false)(true, t_6_1_spread_copy(vert_wall_6_0, true)(t_7_0_spread_copy(horiz_wall_6_0, true)(t_5_0_spread_copy(horiz_wall_5_0(false, true), false), true), true))
			t_7_0_spread = tc7(tr0, false)(true, t_7_1_spread_copy(vert_wall_7_0, true)(t_8_0_spread_copy(horiz_wall_7_0, true)(t_6_0_spread_copy(horiz_wall_6_0(false, true), false), true), true))
			t_8_0_spread = tc8(tr0, false)(true, t_8_1_spread_copy(vert_wall_8_0, true)(t_9_0_spread_copy(horiz_wall_8_0, true)(t_7_0_spread_copy(horiz_wall_7_0(false, true), false), true), true))
			t_9_0_spread = tc9(tr0, false)(true, t_9_1_spread_copy(vert_wall_9_0, true)(t_8_0_spread_copy(horiz_wall_8_0(false, true), false), true))

			t_0_1_spread = tc0(tr1, false)(true, t_0_2_spread_copy(vert_wall_0_1, true)(t_1_1_spread_copy(horiz_wall_0_1, true)(t_0_0_spread_copy(vert_wall_0_0(false, true), false), true), true))
			t_1_1_spread = tc1(tr1, false)(true, t_1_2_spread_copy(vert_wall_1_1, true)(t_2_1_spread_copy(horiz_wall_1_1, true)(t_1_0_spread_copy(vert_wall_1_0, true)(t_0_1_spread_copy(horiz_wall_0_1(false, true), false), true), true), true))
			t_2_1_spread = tc2(tr1, false)(true, t_2_2_spread_copy(vert_wall_2_1, true)(t_3_1_spread_copy(horiz_wall_2_1, true)(t_2_0_spread_copy(vert_wall_2_0, true)(t_1_1_spread_copy(horiz_wall_1_1(false, true), false), true), true), true))
			t_3_1_spread = tc3(tr1, false)(true, t_3_2_spread_copy(vert_wall_3_1, true)(t_4_1_spread_copy(horiz_wall_3_1, true)(t_3_0_spread_copy(vert_wall_3_0, true)(t_2_1_spread_copy(horiz_wall_2_1(false, true), false), true), true), true))
			t_4_1_spread = tc4(tr1, false)(true, t_4_2_spread_copy(vert_wall_4_1, true)(t_5_1_spread_copy(horiz_wall_4_1, true)(t_4_0_spread_copy(vert_wall_4_0, true)(t_3_1_spread_copy(horiz_wall_3_1(false, true), false), true), true), true))
			t_5_1_spread = tc5(tr1, false)(true, t_5_2_spread_copy(vert_wall_5_1, true)(t_6_1_spread_copy(horiz_wall_5_1, true)(t_5_0_spread_copy(vert_wall_5_0, true)(t_4_1_spread_copy(horiz_wall_4_1(false, true), false), true), true), true))
			t_6_1_spread = tc6(tr1, false)(true, t_6_2_spread_copy(vert_wall_6_1, true)(t_7_1_spread_copy(horiz_wall_6_1, true)(t_6_0_spread_copy(vert_wall_6_0, true)(t_5_1_spread_copy(horiz_wall_5_1(false, true), false), true), true), true))
			t_7_1_spread = tc7(tr1, false)(true, t_7_2_spread_copy(vert_wall_7_1, true)(t_8_1_spread_copy(horiz_wall_7_1, true)(t_7_0_spread_copy(vert_wall_7_0, true)(t_6_1_spread_copy(horiz_wall_6_1(false, true), false), true), true), true))
			t_8_1_spread = tc8(tr1, false)(true, t_8_2_spread_copy(vert_wall_8_1, true)(t_9_1_spread_copy(horiz_wall_8_1, true)(t_8_0_spread_copy(vert_wall_8_0, true)(t_7_1_spread_copy(horiz_wall_7_1(false, true), false), true), true), true))
			t_9_1_spread = tc9(tr1, false)(true, t_9_2_spread_copy(vert_wall_9_1, true)(t_9_0_spread_copy(vert_wall_9_0, true)(t_8_1_spread_copy(horiz_wall_8_1(false, true), false), true), true))

			t_0_2_spread = tc0(tr2, false)(true, t_0_3_spread_copy(vert_wall_0_2, true)(t_1_2_spread_copy(horiz_wall_0_2, true)(t_0_1_spread_copy(vert_wall_0_1(false, true), false), true), true))
			t_1_2_spread = tc1(tr2, false)(true, t_1_3_spread_copy(vert_wall_1_2, true)(t_2_2_spread_copy(horiz_wall_1_2, true)(t_1_1_spread_copy(vert_wall_1_1, true)(t_0_2_spread_copy(horiz_wall_0_2(false, true), false), true), true), true))
			t_2_2_spread = tc2(tr2, false)(true, t_2_3_spread_copy(vert_wall_2_2, true)(t_3_2_spread_copy(horiz_wall_2_2, true)(t_2_1_spread_copy(vert_wall_2_1, true)(t_1_2_spread_copy(horiz_wall_1_2(false, true), false), true), true), true))
			t_3_2_spread = tc3(tr2, false)(true, t_3_3_spread_copy(vert_wall_3_2, true)(t_4_2_spread_copy(horiz_wall_3_2, true)(t_3_1_spread_copy(vert_wall_3_1, true)(t_2_2_spread_copy(horiz_wall_2_2(false, true), false), true), true), true))
			t_4_2_spread = tc4(tr2, false)(true, t_4_3_spread_copy(vert_wall_4_2, true)(t_5_2_spread_copy(horiz_wall_4_2, true)(t_4_1_spread_copy(vert_wall_4_1, true)(t_3_2_spread_copy(horiz_wall_3_2(false, true), false), true), true), true))
			t_5_2_spread = tc5(tr2, false)(true, t_5_3_spread_copy(vert_wall_5_2, true)(t_6_2_spread_copy(horiz_wall_5_2, true)(t_5_1_spread_copy(vert_wall_5_1, true)(t_4_2_spread_copy(horiz_wall_4_2(false, true), false), true), true), true))
			t_6_2_spread = tc6(tr2, false)(true, t_6_3_spread_copy(vert_wall_6_2, true)(t_7_2_spread_copy(horiz_wall_6_2, true)(t_6_1_spread_copy(vert_wall_6_1, true)(t_5_2_spread_copy(horiz_wall_5_2(false, true), false), true), true), true))
			t_7_2_spread = tc7(tr2, false)(true, t_7_3_spread_copy(vert_wall_7_2, true)(t_8_2_spread_copy(horiz_wall_7_2, true)(t_7_1_spread_copy(vert_wall_7_1, true)(t_6_2_spread_copy(horiz_wall_6_2(false, true), false), true), true), true))
			t_8_2_spread = tc8(tr2, false)(true, t_8_3_spread_copy(vert_wall_8_2, true)(t_9_2_spread_copy(horiz_wall_8_2, true)(t_8_1_spread_copy(vert_wall_8_1, true)(t_7_2_spread_copy(horiz_wall_7_2(false, true), false), true), true), true))
			t_9_2_spread = tc9(tr2, false)(true, t_9_3_spread_copy(vert_wall_9_2, true)(t_9_1_spread_copy(vert_wall_9_1, true)(t_8_2_spread_copy(horiz_wall_8_2(false, true), false), true), true))

			t_0_3_spread = tc0(tr3, false)(true, t_0_4_spread_copy(vert_wall_0_3, true)(t_1_3_spread_copy(horiz_wall_0_3, true)(t_0_2_spread_copy(vert_wall_0_2(false, true), false), true), true))
			t_1_3_spread = tc1(tr3, false)(true, t_1_4_spread_copy(vert_wall_1_3, true)(t_2_3_spread_copy(horiz_wall_1_3, true)(t_1_2_spread_copy(vert_wall_1_2, true)(t_0_3_spread_copy(horiz_wall_0_3(false, true), false), true), true), true))
			t_2_3_spread = tc2(tr3, false)(true, t_2_4_spread_copy(vert_wall_2_3, true)(t_3_3_spread_copy(horiz_wall_2_3, true)(t_2_2_spread_copy(vert_wall_2_2, true)(t_1_3_spread_copy(horiz_wall_1_3(false, true), false), true), true), true))
			t_3_3_spread = tc3(tr3, false)(true, t_3_4_spread_copy(vert_wall_3_3, true)(t_4_3_spread_copy(horiz_wall_3_3, true)(t_3_2_spread_copy(vert_wall_3_2, true)(t_2_3_spread_copy(horiz_wall_2_3(false, true), false), true), true), true))
			t_4_3_spread = tc4(tr3, false)(true, t_4_4_spread_copy(vert_wall_4_3, true)(t_5_3_spread_copy(horiz_wall_4_3, true)(t_4_2_spread_copy(vert_wall_4_2, true)(t_3_3_spread_copy(horiz_wall_3_3(false, true), false), true), true), true))
			t_5_3_spread = tc5(tr3, false)(true, t_5_4_spread_copy(vert_wall_5_3, true)(t_6_3_spread_copy(horiz_wall_5_3, true)(t_5_2_spread_copy(vert_wall_5_2, true)(t_4_3_spread_copy(horiz_wall_4_3(false, true), false), true), true), true))
			t_6_3_spread = tc6(tr3, false)(true, t_6_4_spread_copy(vert_wall_6_3, true)(t_7_3_spread_copy(horiz_wall_6_3, true)(t_6_2_spread_copy(vert_wall_6_2, true)(t_5_3_spread_copy(horiz_wall_5_3(false, true), false), true), true), true))
			t_7_3_spread = tc7(tr3, false)(true, t_7_4_spread_copy(vert_wall_7_3, true)(t_8_3_spread_copy(horiz_wall_7_3, true)(t_7_2_spread_copy(vert_wall_7_2, true)(t_6_3_spread_copy(horiz_wall_6_3(false, true), false), true), true), true))
			t_8_3_spread = tc8(tr3, false)(true, t_8_4_spread_copy(vert_wall_8_3, true)(t_9_3_spread_copy(horiz_wall_8_3, true)(t_8_2_spread_copy(vert_wall_8_2, true)(t_7_3_spread_copy(horiz_wall_7_3(false, true), false), true), true), true))
			t_9_3_spread = tc9(tr3, false)(true, t_9_4_spread_copy(vert_wall_9_3, true)(t_9_2_spread_copy(vert_wall_9_2, true)(t_8_3_spread_copy(horiz_wall_8_3(false, true), false), true), true))

			t_0_4_spread = tc0(tr4, false)(true, t_0_5_spread_copy(vert_wall_0_4, true)(t_1_4_spread_copy(horiz_wall_0_4, true)(t_0_3_spread_copy(vert_wall_0_3(false, true), false), true), true))
			t_1_4_spread = tc1(tr4, false)(true, t_1_5_spread_copy(vert_wall_1_4, true)(t_2_4_spread_copy(horiz_wall_1_4, true)(t_1_3_spread_copy(vert_wall_1_3, true)(t_0_4_spread_copy(horiz_wall_0_4(false, true), false), true), true), true))
			t_2_4_spread = tc2(tr4, false)(true, t_2_5_spread_copy(vert_wall_2_4, true)(t_3_4_spread_copy(horiz_wall_2_4, true)(t_2_3_spread_copy(vert_wall_2_3, true)(t_1_4_spread_copy(horiz_wall_1_4(false, true), false), true), true), true))
			t_3_4_spread = tc3(tr4, false)(true, t_3_5_spread_copy(vert_wall_3_4, true)(t_4_4_spread_copy(horiz_wall_3_4, true)(t_3_3_spread_copy(vert_wall_3_3, true)(t_2_4_spread_copy(horiz_wall_2_4(false, true), false), true), true), true))
			t_4_4_spread = tc4(tr4, false)(true, t_4_5_spread_copy(vert_wall_4_4, true)(t_5_4_spread_copy(horiz_wall_4_4, true)(t_4_3_spread_copy(vert_wall_4_3, true)(t_3_4_spread_copy(horiz_wall_3_4(false, true), false), true), true), true))
			t_5_4_spread = tc5(tr4, false)(true, t_5_5_spread_copy(vert_wall_5_4, true)(t_6_4_spread_copy(horiz_wall_5_4, true)(t_5_3_spread_copy(vert_wall_5_3, true)(t_4_4_spread_copy(horiz_wall_4_4(false, true), false), true), true), true))
			t_6_4_spread = tc6(tr4, false)(true, t_6_5_spread_copy(vert_wall_6_4, true)(t_7_4_spread_copy(horiz_wall_6_4, true)(t_6_3_spread_copy(vert_wall_6_3, true)(t_5_4_spread_copy(horiz_wall_5_4(false, true), false), true), true), true))
			t_7_4_spread = tc7(tr4, false)(true, t_7_5_spread_copy(vert_wall_7_4, true)(t_8_4_spread_copy(horiz_wall_7_4, true)(t_7_3_spread_copy(vert_wall_7_3, true)(t_6_4_spread_copy(horiz_wall_6_4(false, true), false), true), true), true))
			t_8_4_spread = tc8(tr4, false)(true, t_8_5_spread_copy(vert_wall_8_4, true)(t_9_4_spread_copy(horiz_wall_8_4, true)(t_8_3_spread_copy(vert_wall_8_3, true)(t_7_4_spread_copy(horiz_wall_7_4(false, true), false), true), true), true))
			t_9_4_spread = tc9(tr4, false)(true, t_9_5_spread_copy(vert_wall_9_4, true)(t_9_3_spread_copy(vert_wall_9_3, true)(t_8_4_spread_copy(horiz_wall_8_4(false, true), false), true), true))

			t_0_5_spread = tc0(tr5, false)(true, t_0_6_spread_copy(vert_wall_0_5, true)(t_1_5_spread_copy(horiz_wall_0_5, true)(t_0_4_spread_copy(vert_wall_0_4(false, true), false), true), true))
			t_1_5_spread = tc1(tr5, false)(true, t_1_6_spread_copy(vert_wall_1_5, true)(t_2_5_spread_copy(horiz_wall_1_5, true)(t_1_4_spread_copy(vert_wall_1_4, true)(t_0_5_spread_copy(horiz_wall_0_5(false, true), false), true), true), true))
			t_2_5_spread = tc2(tr5, false)(true, t_2_6_spread_copy(vert_wall_2_5, true)(t_3_5_spread_copy(horiz_wall_2_5, true)(t_2_4_spread_copy(vert_wall_2_4, true)(t_1_5_spread_copy(horiz_wall_1_5(false, true), false), true), true), true))
			t_3_5_spread = tc3(tr5, false)(true, t_3_6_spread_copy(vert_wall_3_5, true)(t_4_5_spread_copy(horiz_wall_3_5, true)(t_3_4_spread_copy(vert_wall_3_4, true)(t_2_5_spread_copy(horiz_wall_2_5(false, true), false), true), true), true))
			t_4_5_spread = tc4(tr5, false)(true, t_4_6_spread_copy(vert_wall_4_5, true)(t_5_5_spread_copy(horiz_wall_4_5, true)(t_4_4_spread_copy(vert_wall_4_4, true)(t_3_5_spread_copy(horiz_wall_3_5(false, true), false), true), true), true))
			t_5_5_spread = tc5(tr5, false)(true, t_5_6_spread_copy(vert_wall_5_5, true)(t_6_5_spread_copy(horiz_wall_5_5, true)(t_5_4_spread_copy(vert_wall_5_4, true)(t_4_5_spread_copy(horiz_wall_4_5(false, true), false), true), true), true))
			t_6_5_spread = tc6(tr5, false)(true, t_6_6_spread_copy(vert_wall_6_5, true)(t_7_5_spread_copy(horiz_wall_6_5, true)(t_6_4_spread_copy(vert_wall_6_4, true)(t_5_5_spread_copy(horiz_wall_5_5(false, true), false), true), true), true))
			t_7_5_spread = tc7(tr5, false)(true, t_7_6_spread_copy(vert_wall_7_5, true)(t_8_5_spread_copy(horiz_wall_7_5, true)(t_7_4_spread_copy(vert_wall_7_4, true)(t_6_5_spread_copy(horiz_wall_6_5(false, true), false), true), true), true))
			t_8_5_spread = tc8(tr5, false)(true, t_8_6_spread_copy(vert_wall_8_5, true)(t_9_5_spread_copy(horiz_wall_8_5, true)(t_8_4_spread_copy(vert_wall_8_4, true)(t_7_5_spread_copy(horiz_wall_7_5(false, true), false), true), true), true))
			t_9_5_spread = tc9(tr5, false)(true, t_9_6_spread_copy(vert_wall_9_5, true)(t_9_4_spread_copy(vert_wall_9_4, true)(t_8_5_spread_copy(horiz_wall_8_5(false, true), false), true), true))

			t_0_6_spread = tc0(tr6, false)(true, t_0_7_spread_copy(vert_wall_0_6, true)(t_1_6_spread_copy(horiz_wall_0_6, true)(t_0_5_spread_copy(vert_wall_0_5(false, true), false), true), true))
			t_1_6_spread = tc1(tr6, false)(true, t_1_7_spread_copy(vert_wall_1_6, true)(t_2_6_spread_copy(horiz_wall_1_6, true)(t_1_5_spread_copy(vert_wall_1_5, true)(t_0_6_spread_copy(horiz_wall_0_6(false, true), false), true), true), true))
			t_2_6_spread = tc2(tr6, false)(true, t_2_7_spread_copy(vert_wall_2_6, true)(t_3_6_spread_copy(horiz_wall_2_6, true)(t_2_5_spread_copy(vert_wall_2_5, true)(t_1_6_spread_copy(horiz_wall_1_6(false, true), false), true), true), true))
			t_3_6_spread = tc3(tr6, false)(true, t_3_7_spread_copy(vert_wall_3_6, true)(t_4_6_spread_copy(horiz_wall_3_6, true)(t_3_5_spread_copy(vert_wall_3_5, true)(t_2_6_spread_copy(horiz_wall_2_6(false, true), false), true), true), true))
			t_4_6_spread = tc4(tr6, false)(true, t_4_7_spread_copy(vert_wall_4_6, true)(t_5_6_spread_copy(horiz_wall_4_6, true)(t_4_5_spread_copy(vert_wall_4_5, true)(t_3_6_spread_copy(horiz_wall_3_6(false, true), false), true), true), true))
			t_5_6_spread = tc5(tr6, false)(true, t_5_7_spread_copy(vert_wall_5_6, true)(t_6_6_spread_copy(horiz_wall_5_6, true)(t_5_5_spread_copy(vert_wall_5_5, true)(t_4_6_spread_copy(horiz_wall_4_6(false, true), false), true), true), true))
			t_6_6_spread = tc6(tr6, false)(true, t_6_7_spread_copy(vert_wall_6_6, true)(t_7_6_spread_copy(horiz_wall_6_6, true)(t_6_5_spread_copy(vert_wall_6_5, true)(t_5_6_spread_copy(horiz_wall_5_6(false, true), false), true), true), true))
			t_7_6_spread = tc7(tr6, false)(true, t_7_7_spread_copy(vert_wall_7_6, true)(t_8_6_spread_copy(horiz_wall_7_6, true)(t_7_5_spread_copy(vert_wall_7_5, true)(t_6_6_spread_copy(horiz_wall_6_6(false, true), false), true), true), true))
			t_8_6_spread = tc8(tr6, false)(true, t_8_7_spread_copy(vert_wall_8_6, true)(t_9_6_spread_copy(horiz_wall_8_6, true)(t_8_5_spread_copy(vert_wall_8_5, true)(t_7_6_spread_copy(horiz_wall_7_6(false, true), false), true), true), true))
			t_9_6_spread = tc9(tr6, false)(true, t_9_7_spread_copy(vert_wall_9_6, true)(t_9_5_spread_copy(vert_wall_9_5, true)(t_8_6_spread_copy(horiz_wall_8_6(false, true), false), true), true))

			t_0_7_spread = tc0(tr7, false)(true, t_0_8_spread_copy(vert_wall_0_7, true)(t_1_7_spread_copy(horiz_wall_0_7, true)(t_0_6_spread_copy(vert_wall_0_6(false, true), false), true), true))
			t_1_7_spread = tc1(tr7, false)(true, t_1_8_spread_copy(vert_wall_1_7, true)(t_2_7_spread_copy(horiz_wall_1_7, true)(t_1_6_spread_copy(vert_wall_1_6, true)(t_0_7_spread_copy(horiz_wall_0_7(false, true), false), true), true), true))
			t_2_7_spread = tc2(tr7, false)(true, t_2_8_spread_copy(vert_wall_2_7, true)(t_3_7_spread_copy(horiz_wall_2_7, true)(t_2_6_spread_copy(vert_wall_2_6, true)(t_1_7_spread_copy(horiz_wall_1_7(false, true), false), true), true), true))
			t_3_7_spread = tc3(tr7, false)(true, t_3_8_spread_copy(vert_wall_3_7, true)(t_4_7_spread_copy(horiz_wall_3_7, true)(t_3_6_spread_copy(vert_wall_3_6, true)(t_2_7_spread_copy(horiz_wall_2_7(false, true), false), true), true), true))
			t_4_7_spread = tc4(tr7, false)(true, t_4_8_spread_copy(vert_wall_4_7, true)(t_5_7_spread_copy(horiz_wall_4_7, true)(t_4_6_spread_copy(vert_wall_4_6, true)(t_3_7_spread_copy(horiz_wall_3_7(false, true), false), true), true), true))
			t_5_7_spread = tc5(tr7, false)(true, t_5_8_spread_copy(vert_wall_5_7, true)(t_6_7_spread_copy(horiz_wall_5_7, true)(t_5_6_spread_copy(vert_wall_5_6, true)(t_4_7_spread_copy(horiz_wall_4_7(false, true), false), true), true), true))
			t_6_7_spread = tc6(tr7, false)(true, t_6_8_spread_copy(vert_wall_6_7, true)(t_7_7_spread_copy(horiz_wall_6_7, true)(t_6_6_spread_copy(vert_wall_6_6, true)(t_5_7_spread_copy(horiz_wall_5_7(false, true), false), true), true), true))
			t_7_7_spread = tc7(tr7, false)(true, t_7_8_spread_copy(vert_wall_7_7, true)(t_8_7_spread_copy(horiz_wall_7_7, true)(t_7_6_spread_copy(vert_wall_7_6, true)(t_6_7_spread_copy(horiz_wall_6_7(false, true), false), true), true), true))
			t_8_7_spread = tc8(tr7, false)(true, t_8_8_spread_copy(vert_wall_8_7, true)(t_9_7_spread_copy(horiz_wall_8_7, true)(t_8_6_spread_copy(vert_wall_8_6, true)(t_7_7_spread_copy(horiz_wall_7_7(false, true), false), true), true), true))
			t_9_7_spread = tc9(tr7, false)(true, t_9_8_spread_copy(vert_wall_9_7, true)(t_9_6_spread_copy(vert_wall_9_6, true)(t_8_7_spread_copy(horiz_wall_8_7(false, true), false), true), true))

			t_0_8_spread = tc0(tr8, false)(true, t_0_9_spread_copy(vert_wall_0_8, true)(t_1_8_spread_copy(horiz_wall_0_8, true)(t_0_7_spread_copy(vert_wall_0_7(false, true), false), true), true))
			t_1_8_spread = tc1(tr8, false)(true, t_1_9_spread_copy(vert_wall_1_8, true)(t_2_8_spread_copy(horiz_wall_1_8, true)(t_1_7_spread_copy(vert_wall_1_7, true)(t_0_8_spread_copy(horiz_wall_0_8(false, true), false), true), true), true))
			t_2_8_spread = tc2(tr8, false)(true, t_2_9_spread_copy(vert_wall_2_8, true)(t_3_8_spread_copy(horiz_wall_2_8, true)(t_2_7_spread_copy(vert_wall_2_7, true)(t_1_8_spread_copy(horiz_wall_1_8(false, true), false), true), true), true))
			t_3_8_spread = tc3(tr8, false)(true, t_3_9_spread_copy(vert_wall_3_8, true)(t_4_8_spread_copy(horiz_wall_3_8, true)(t_3_7_spread_copy(vert_wall_3_7, true)(t_2_8_spread_copy(horiz_wall_2_8(false, true), false), true), true), true))
			t_4_8_spread = tc4(tr8, false)(true, t_4_9_spread_copy(vert_wall_4_8, true)(t_5_8_spread_copy(horiz_wall_4_8, true)(t_4_7_spread_copy(vert_wall_4_7, true)(t_3_8_spread_copy(horiz_wall_3_8(false, true), false), true), true), true))
			t_5_8_spread = tc5(tr8, false)(true, t_5_9_spread_copy(vert_wall_5_8, true)(t_6_8_spread_copy(horiz_wall_5_8, true)(t_5_7_spread_copy(vert_wall_5_7, true)(t_4_8_spread_copy(horiz_wall_4_8(false, true), false), true), true), true))
			t_6_8_spread = tc6(tr8, false)(true, t_6_9_spread_copy(vert_wall_6_8, true)(t_7_8_spread_copy(horiz_wall_6_8, true)(t_6_7_spread_copy(vert_wall_6_7, true)(t_5_8_spread_copy(horiz_wall_5_8(false, true), false), true), true), true))
			t_7_8_spread = tc7(tr8, false)(true, t_7_9_spread_copy(vert_wall_7_8, true)(t_8_8_spread_copy(horiz_wall_7_8, true)(t_7_7_spread_copy(vert_wall_7_7, true)(t_6_8_spread_copy(horiz_wall_6_8(false, true), false), true), true), true))
			t_8_8_spread = tc8(tr8, false)(true, t_8_9_spread_copy(vert_wall_8_8, true)(t_9_8_spread_copy(horiz_wall_8_8, true)(t_8_7_spread_copy(vert_wall_8_7, true)(t_7_8_spread_copy(horiz_wall_7_8(false, true), false), true), true), true))
			t_9_8_spread = tc9(tr8, false)(true, t_9_9_spread_copy(vert_wall_9_8, true)(t_9_7_spread_copy(vert_wall_9_7, true)(t_8_8_spread_copy(horiz_wall_8_8(false, true), false), true), true))

			t_0_9_spread = tc0(tr9, false)(true, t_1_9_spread_copy(horiz_wall_0_9, true)(t_0_8_spread_copy(vert_wall_0_8(false, true), false), true))
			t_1_9_spread = tc1(tr9, false)(true, t_2_9_spread_copy(horiz_wall_1_9, true)(t_1_8_spread_copy(vert_wall_1_8, true)(t_0_9_spread_copy(horiz_wall_0_9(false, true), false), true), true))
			t_2_9_spread = tc2(tr9, false)(true, t_3_9_spread_copy(horiz_wall_2_9, true)(t_2_8_spread_copy(vert_wall_2_8, true)(t_1_9_spread_copy(horiz_wall_1_9(false, true), false), true), true))
			t_3_9_spread = tc3(tr9, false)(true, t_4_9_spread_copy(horiz_wall_3_9, true)(t_3_8_spread_copy(vert_wall_3_8, true)(t_2_9_spread_copy(horiz_wall_2_9(false, true), false), true), true))
			t_4_9_spread = tc4(tr9, false)(true, t_5_9_spread_copy(horiz_wall_4_9, true)(t_4_8_spread_copy(vert_wall_4_8, true)(t_3_9_spread_copy(horiz_wall_3_9(false, true), false), true), true))
			t_5_9_spread = tc5(tr9, false)(true, t_6_9_spread_copy(horiz_wall_5_9, true)(t_5_8_spread_copy(vert_wall_5_8, true)(t_4_9_spread_copy(horiz_wall_4_9(false, true), false), true), true))
			t_6_9_spread = tc6(tr9, false)(true, t_7_9_spread_copy(horiz_wall_6_9, true)(t_6_8_spread_copy(vert_wall_6_8, true)(t_5_9_spread_copy(horiz_wall_5_9(false, true), false), true), true))
			t_7_9_spread = tc7(tr9, false)(true, t_8_9_spread_copy(horiz_wall_7_9, true)(t_7_8_spread_copy(vert_wall_7_8, true)(t_6_9_spread_copy(horiz_wall_6_9(false, true), false), true), true))
			t_8_9_spread = tc8(tr9, false)(true, t_9_9_spread_copy(horiz_wall_8_9, true)(t_8_8_spread_copy(vert_wall_8_8, true)(t_7_9_spread_copy(horiz_wall_7_9(false, true), false), true), true))
			t_9_9_spread = tc9(tr9, false)(true, t_9_8_spread_copy(vert_wall_9_8, true)(t_8_9_spread_copy(horiz_wall_8_9(false, true), false), true))

			north_detected = check_north(dud, check_north_spread)()

			east_detected = check_east(dud, check_east_spread)()

			south_detected = check_south(dud, check_south_spread)()

			west_detected = check_west(dud, check_west_spread)()

			drone_found = north_detected(true, east_detected(true, south_detected(true, west_detected)))(True, False)

		east_detected = east_detected(north_detected(false, true), false)
		south_detected = south_detected(north_detected(false, east_detected(false, true)), false)
		west_detected = west_detected(north_detected(false, east_detected(false, south_detected(false, true))), false)

		north_detected(move, nothing)(North)
		east_detected(move, nothing)(East)
		south_detected(move, nothing)(South)
		west_detected(move, nothing)(West)

		x_changed = east_detected(true, west_detected)
		y_changed = north_detected(true, south_detected)

		pc0_copy = pc0
		pc1_copy = pc1
		pc2_copy = pc2
		pc3_copy = pc3
		pc4_copy = pc4
		pc5_copy = pc5
		pc6_copy = pc6
		pc7_copy = pc7
		pc8_copy = pc8
		pc9_copy = pc9

		pr0_copy = pr0
		pr1_copy = pr1
		pr2_copy = pr2
		pr3_copy = pr3
		pr4_copy = pr4
		pr5_copy = pr5
		pr6_copy = pr6
		pr7_copy = pr7
		pr8_copy = pr8
		pr9_copy = pr9

		pc0 = x_changed(east_detected(false, pc1_copy), pc0)
		pc1 = x_changed(east_detected(pc0_copy, pc2_copy), pc1)
		pc2 = x_changed(east_detected(pc1_copy, pc3_copy), pc2)
		pc3 = x_changed(east_detected(pc2_copy, pc4_copy), pc3)
		pc4 = x_changed(east_detected(pc3_copy, pc5_copy), pc4)
		pc5 = x_changed(east_detected(pc4_copy, pc6_copy), pc5)
		pc6 = x_changed(east_detected(pc5_copy, pc7_copy), pc6)
		pc7 = x_changed(east_detected(pc6_copy, pc8_copy), pc7)
		pc8 = x_changed(east_detected(pc7_copy, pc9_copy), pc8)
		pc9 = x_changed(east_detected(pc8_copy, false), pc9)

		pr0 = y_changed(north_detected(false, pr1_copy), pr0)
		pr1 = y_changed(north_detected(pr0_copy, pr2_copy), pr1)
		pr2 = y_changed(north_detected(pr1_copy, pr3_copy), pr2)
		pr3 = y_changed(north_detected(pr2_copy, pr4_copy), pr3)
		pr4 = y_changed(north_detected(pr3_copy, pr5_copy), pr4)
		pr5 = y_changed(north_detected(pr4_copy, pr6_copy), pr5)
		pr6 = y_changed(north_detected(pr5_copy, pr7_copy), pr6)
		pr7 = y_changed(north_detected(pr6_copy, pr8_copy), pr7)
		pr8 = y_changed(north_detected(pr7_copy, pr9_copy), pr8)
		pr9 = y_changed(north_detected(pr8_copy, false), pr9)

		drone_at_0_0 = pc0(pr0, false)
		drone_at_1_0 = pc1(pr0, false)
		drone_at_2_0 = pc2(pr0, false)
		drone_at_3_0 = pc3(pr0, false)
		drone_at_4_0 = pc4(pr0, false)
		drone_at_5_0 = pc5(pr0, false)
		drone_at_6_0 = pc6(pr0, false)
		drone_at_7_0 = pc7(pr0, false)
		drone_at_8_0 = pc8(pr0, false)
		drone_at_9_0 = pc9(pr0, false)
		drone_at_0_1 = pc0(pr1, false)
		drone_at_1_1 = pc1(pr1, false)
		drone_at_2_1 = pc2(pr1, false)
		drone_at_3_1 = pc3(pr1, false)
		drone_at_4_1 = pc4(pr1, false)
		drone_at_5_1 = pc5(pr1, false)
		drone_at_6_1 = pc6(pr1, false)
		drone_at_7_1 = pc7(pr1, false)
		drone_at_8_1 = pc8(pr1, false)
		drone_at_9_1 = pc9(pr1, false)
		drone_at_0_2 = pc0(pr2, false)
		drone_at_1_2 = pc1(pr2, false)
		drone_at_2_2 = pc2(pr2, false)
		drone_at_3_2 = pc3(pr2, false)
		drone_at_4_2 = pc4(pr2, false)
		drone_at_5_2 = pc5(pr2, false)
		drone_at_6_2 = pc6(pr2, false)
		drone_at_7_2 = pc7(pr2, false)
		drone_at_8_2 = pc8(pr2, false)
		drone_at_9_2 = pc9(pr2, false)
		drone_at_0_3 = pc0(pr3, false)
		drone_at_1_3 = pc1(pr3, false)
		drone_at_2_3 = pc2(pr3, false)
		drone_at_3_3 = pc3(pr3, false)
		drone_at_4_3 = pc4(pr3, false)
		drone_at_5_3 = pc5(pr3, false)
		drone_at_6_3 = pc6(pr3, false)
		drone_at_7_3 = pc7(pr3, false)
		drone_at_8_3 = pc8(pr3, false)
		drone_at_9_3 = pc9(pr3, false)
		drone_at_0_4 = pc0(pr4, false)
		drone_at_1_4 = pc1(pr4, false)
		drone_at_2_4 = pc2(pr4, false)
		drone_at_3_4 = pc3(pr4, false)
		drone_at_4_4 = pc4(pr4, false)
		drone_at_5_4 = pc5(pr4, false)
		drone_at_6_4 = pc6(pr4, false)
		drone_at_7_4 = pc7(pr4, false)
		drone_at_8_4 = pc8(pr4, false)
		drone_at_9_4 = pc9(pr4, false)
		drone_at_0_5 = pc0(pr5, false)
		drone_at_1_5 = pc1(pr5, false)
		drone_at_2_5 = pc2(pr5, false)
		drone_at_3_5 = pc3(pr5, false)
		drone_at_4_5 = pc4(pr5, false)
		drone_at_5_5 = pc5(pr5, false)
		drone_at_6_5 = pc6(pr5, false)
		drone_at_7_5 = pc7(pr5, false)
		drone_at_8_5 = pc8(pr5, false)
		drone_at_9_5 = pc9(pr5, false)
		drone_at_0_6 = pc0(pr6, false)
		drone_at_1_6 = pc1(pr6, false)
		drone_at_2_6 = pc2(pr6, false)
		drone_at_3_6 = pc3(pr6, false)
		drone_at_4_6 = pc4(pr6, false)
		drone_at_5_6 = pc5(pr6, false)
		drone_at_6_6 = pc6(pr6, false)
		drone_at_7_6 = pc7(pr6, false)
		drone_at_8_6 = pc8(pr6, false)
		drone_at_9_6 = pc9(pr6, false)
		drone_at_0_7 = pc0(pr7, false)
		drone_at_1_7 = pc1(pr7, false)
		drone_at_2_7 = pc2(pr7, false)
		drone_at_3_7 = pc3(pr7, false)
		drone_at_4_7 = pc4(pr7, false)
		drone_at_5_7 = pc5(pr7, false)
		drone_at_6_7 = pc6(pr7, false)
		drone_at_7_7 = pc7(pr7, false)
		drone_at_8_7 = pc8(pr7, false)
		drone_at_9_7 = pc9(pr7, false)
		drone_at_0_8 = pc0(pr8, false)
		drone_at_1_8 = pc1(pr8, false)
		drone_at_2_8 = pc2(pr8, false)
		drone_at_3_8 = pc3(pr8, false)
		drone_at_4_8 = pc4(pr8, false)
		drone_at_5_8 = pc5(pr8, false)
		drone_at_6_8 = pc6(pr8, false)
		drone_at_7_8 = pc7(pr8, false)
		drone_at_8_8 = pc8(pr8, false)
		drone_at_9_8 = pc9(pr8, false)
		drone_at_0_9 = pc0(pr9, false)
		drone_at_1_9 = pc1(pr9, false)
		drone_at_2_9 = pc2(pr9, false)
		drone_at_3_9 = pc3(pr9, false)
		drone_at_4_9 = pc4(pr9, false)
		drone_at_5_9 = pc5(pr9, false)
		drone_at_6_9 = pc6(pr9, false)
		drone_at_7_9 = pc7(pr9, false)
		drone_at_8_9 = pc8(pr9, false)
		drone_at_9_9 = pc9(pr9, false)

		same_col = pc0(tc0, pc1(tc1, pc2(tc2, pc3(tc3, pc4(tc4, pc5(tc5, pc6(tc6, pc7(tc7, pc8(tc8, pc9(tc9, false))))))))))
		same_row = pr0(tr0, pr1(tr1, pr2(tr2, pr3(tr3, pr4(tr4, pr5(tr5, pr6(tr6, pr7(tr7, pr8(tr8, pr9(tr9, false))))))))))

		on_chest = same_col(same_row, false)(True, False)

	on_chest = False

	if measure():
		tx, ty = measure()

		tc0, tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9 = decode_t[tx]
		tr0, tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9 = decode_t[ty]

		use_item(Items.Weird_Substance, 100)

harvest()
