def SMx0y0(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((0, 0))
	move(North)
	return SMx0y1
def SMx0y1(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((0, 1))
	tail_distance = path_distance(1, position_function_dict[snake_body[0]])
	food_distance = path_distance(1, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(1, 6) <= cutting_amount:
		move(North)
		return SMx0y2
	move(East)
	return SMx1y1
def SMx1y1(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((1, 1))
	tail_distance = path_distance(2, position_function_dict[snake_body[0]])
	food_distance = path_distance(2, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(2, 5) <= cutting_amount:
		move(North)
		return SMx1y2
	if path_distance(2, 99) <= cutting_amount:
		move(South)
		return SMx1y0
	move(East)
	return SMx2y1
def SMx2y1(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((2, 1))
	tail_distance = path_distance(3, position_function_dict[snake_body[0]])
	food_distance = path_distance(3, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(3, 98) <= cutting_amount:
		move(South)
		return SMx2y0
	if path_distance(3, 96) <= cutting_amount:
		move(East)
		return SMx3y1
	move(North)
	return SMx2y2
def SMx2y2(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((2, 2))
	tail_distance = path_distance(4, position_function_dict[snake_body[0]])
	food_distance = path_distance(4, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(4, 9) <= cutting_amount:
		move(North)
		return SMx2y3
	if path_distance(4, 95) <= cutting_amount:
		move(East)
		return SMx3y2
	move(West)
	return SMx1y2
def SMx1y2(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((1, 2))
	tail_distance = path_distance(5, position_function_dict[snake_body[0]])
	food_distance = path_distance(5, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(5, 8) <= cutting_amount:
		move(North)
		return SMx1y3
	if path_distance(5, 2) <= cutting_amount:
		move(South)
		return SMx1y1
	move(West)
	return SMx0y2
def SMx0y2(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((0, 2))
	tail_distance = path_distance(6, position_function_dict[snake_body[0]])
	food_distance = path_distance(6, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(6, 1) <= cutting_amount:
		move(South)
		return SMx0y1
	move(North)
	return SMx0y3
def SMx0y3(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((0, 3))
	tail_distance = path_distance(7, position_function_dict[snake_body[0]])
	food_distance = path_distance(7, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(7, 12) <= cutting_amount:
		move(North)
		return SMx0y4
	move(East)
	return SMx1y3
def SMx1y3(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((1, 3))
	tail_distance = path_distance(8, position_function_dict[snake_body[0]])
	food_distance = path_distance(8, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(8, 11) <= cutting_amount:
		move(North)
		return SMx1y4
	if path_distance(8, 5) <= cutting_amount:
		move(South)
		return SMx1y2
	move(East)
	return SMx2y3
def SMx2y3(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((2, 3))
	tail_distance = path_distance(9, position_function_dict[snake_body[0]])
	food_distance = path_distance(9, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(9, 4) <= cutting_amount:
		move(South)
		return SMx2y2
	if path_distance(9, 94) <= cutting_amount:
		move(East)
		return SMx3y3
	move(North)
	return SMx2y4
def SMx2y4(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((2, 4))
	tail_distance = path_distance(10, position_function_dict[snake_body[0]])
	food_distance = path_distance(10, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(10, 15) <= cutting_amount:
		move(North)
		return SMx2y5
	if path_distance(10, 93) <= cutting_amount:
		move(East)
		return SMx3y4
	move(West)
	return SMx1y4
def SMx1y4(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((1, 4))
	tail_distance = path_distance(11, position_function_dict[snake_body[0]])
	food_distance = path_distance(11, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(11, 14) <= cutting_amount:
		move(North)
		return SMx1y5
	if path_distance(11, 8) <= cutting_amount:
		move(South)
		return SMx1y3
	move(West)
	return SMx0y4
def SMx0y4(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((0, 4))
	tail_distance = path_distance(12, position_function_dict[snake_body[0]])
	food_distance = path_distance(12, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(12, 7) <= cutting_amount:
		move(South)
		return SMx0y3
	move(North)
	return SMx0y5
def SMx0y5(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((0, 5))
	tail_distance = path_distance(13, position_function_dict[snake_body[0]])
	food_distance = path_distance(13, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(13, 22) <= cutting_amount:
		move(North)
		return SMx0y6
	move(East)
	return SMx1y5
def SMx1y5(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((1, 5))
	tail_distance = path_distance(14, position_function_dict[snake_body[0]])
	food_distance = path_distance(14, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(14, 21) <= cutting_amount:
		move(North)
		return SMx1y6
	if path_distance(14, 11) <= cutting_amount:
		move(South)
		return SMx1y4
	move(East)
	return SMx2y5
def SMx2y5(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((2, 5))
	tail_distance = path_distance(15, position_function_dict[snake_body[0]])
	food_distance = path_distance(15, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(15, 20) <= cutting_amount:
		move(North)
		return SMx2y6
	if path_distance(15, 10) <= cutting_amount:
		move(South)
		return SMx2y4
	move(East)
	return SMx3y5
def SMx3y5(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((3, 5))
	tail_distance = path_distance(16, position_function_dict[snake_body[0]])
	food_distance = path_distance(16, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(16, 19) <= cutting_amount:
		move(North)
		return SMx3y6
	if path_distance(16, 93) <= cutting_amount:
		move(South)
		return SMx3y4
	move(East)
	return SMx4y5
def SMx4y5(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((4, 5))
	tail_distance = path_distance(17, position_function_dict[snake_body[0]])
	food_distance = path_distance(17, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(17, 92) <= cutting_amount:
		move(South)
		return SMx4y4
	if path_distance(17, 42) <= cutting_amount:
		move(East)
		return SMx5y5
	move(North)
	return SMx4y6
def SMx4y6(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((4, 6))
	tail_distance = path_distance(18, position_function_dict[snake_body[0]])
	food_distance = path_distance(18, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(18, 35) <= cutting_amount:
		move(North)
		return SMx4y7
	if path_distance(18, 41) <= cutting_amount:
		move(East)
		return SMx5y6
	move(West)
	return SMx3y6
def SMx3y6(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((3, 6))
	tail_distance = path_distance(19, position_function_dict[snake_body[0]])
	food_distance = path_distance(19, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(19, 34) <= cutting_amount:
		move(North)
		return SMx3y7
	if path_distance(19, 16) <= cutting_amount:
		move(South)
		return SMx3y5
	move(West)
	return SMx2y6
def SMx2y6(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((2, 6))
	tail_distance = path_distance(20, position_function_dict[snake_body[0]])
	food_distance = path_distance(20, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(20, 29) <= cutting_amount:
		move(North)
		return SMx2y7
	if path_distance(20, 15) <= cutting_amount:
		move(South)
		return SMx2y5
	move(West)
	return SMx1y6
def SMx1y6(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((1, 6))
	tail_distance = path_distance(21, position_function_dict[snake_body[0]])
	food_distance = path_distance(21, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(21, 28) <= cutting_amount:
		move(North)
		return SMx1y7
	if path_distance(21, 14) <= cutting_amount:
		move(South)
		return SMx1y5
	move(West)
	return SMx0y6
def SMx0y6(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((0, 6))
	tail_distance = path_distance(22, position_function_dict[snake_body[0]])
	food_distance = path_distance(22, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(22, 13) <= cutting_amount:
		move(South)
		return SMx0y5
	move(North)
	return SMx0y7
def SMx0y7(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((0, 7))
	tail_distance = path_distance(23, position_function_dict[snake_body[0]])
	food_distance = path_distance(23, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(23, 28) <= cutting_amount:
		move(East)
		return SMx1y7
	move(North)
	return SMx0y8
def SMx0y8(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((0, 8))
	tail_distance = path_distance(24, position_function_dict[snake_body[0]])
	food_distance = path_distance(24, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(24, 27) <= cutting_amount:
		move(East)
		return SMx1y8
	move(North)
	return SMx0y9
def SMx0y9(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((0, 9))
	move(East)
	return SMx1y9
def SMx1y9(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((1, 9))
	tail_distance = path_distance(26, position_function_dict[snake_body[0]])
	food_distance = path_distance(26, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(26, 31) <= cutting_amount:
		move(East)
		return SMx2y9
	move(South)
	return SMx1y8
def SMx1y8(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((1, 8))
	tail_distance = path_distance(27, position_function_dict[snake_body[0]])
	food_distance = path_distance(27, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(27, 30) <= cutting_amount:
		move(East)
		return SMx2y8
	if path_distance(27, 24) <= cutting_amount:
		move(West)
		return SMx0y8
	move(South)
	return SMx1y7
def SMx1y7(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((1, 7))
	tail_distance = path_distance(28, position_function_dict[snake_body[0]])
	food_distance = path_distance(28, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(28, 21) <= cutting_amount:
		move(South)
		return SMx1y6
	if path_distance(28, 23) <= cutting_amount:
		move(West)
		return SMx0y7
	move(East)
	return SMx2y7
def SMx2y7(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((2, 7))
	tail_distance = path_distance(29, position_function_dict[snake_body[0]])
	food_distance = path_distance(29, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(29, 20) <= cutting_amount:
		move(South)
		return SMx2y6
	if path_distance(29, 34) <= cutting_amount:
		move(East)
		return SMx3y7
	move(North)
	return SMx2y8
def SMx2y8(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((2, 8))
	tail_distance = path_distance(30, position_function_dict[snake_body[0]])
	food_distance = path_distance(30, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(30, 33) <= cutting_amount:
		move(East)
		return SMx3y8
	if path_distance(30, 27) <= cutting_amount:
		move(West)
		return SMx1y8
	move(North)
	return SMx2y9
def SMx2y9(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((2, 9))
	tail_distance = path_distance(31, position_function_dict[snake_body[0]])
	food_distance = path_distance(31, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(31, 26) <= cutting_amount:
		move(West)
		return SMx1y9
	move(East)
	return SMx3y9
def SMx3y9(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((3, 9))
	tail_distance = path_distance(32, position_function_dict[snake_body[0]])
	food_distance = path_distance(32, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(32, 37) <= cutting_amount:
		move(East)
		return SMx4y9
	move(South)
	return SMx3y8
def SMx3y8(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((3, 8))
	tail_distance = path_distance(33, position_function_dict[snake_body[0]])
	food_distance = path_distance(33, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(33, 36) <= cutting_amount:
		move(East)
		return SMx4y8
	if path_distance(33, 30) <= cutting_amount:
		move(West)
		return SMx2y8
	move(South)
	return SMx3y7
def SMx3y7(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((3, 7))
	tail_distance = path_distance(34, position_function_dict[snake_body[0]])
	food_distance = path_distance(34, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(34, 19) <= cutting_amount:
		move(South)
		return SMx3y6
	if path_distance(34, 29) <= cutting_amount:
		move(West)
		return SMx2y7
	move(East)
	return SMx4y7
def SMx4y7(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((4, 7))
	tail_distance = path_distance(35, position_function_dict[snake_body[0]])
	food_distance = path_distance(35, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(35, 18) <= cutting_amount:
		move(South)
		return SMx4y6
	if path_distance(35, 40) <= cutting_amount:
		move(East)
		return SMx5y7
	move(North)
	return SMx4y8
def SMx4y8(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((4, 8))
	tail_distance = path_distance(36, position_function_dict[snake_body[0]])
	food_distance = path_distance(36, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(36, 39) <= cutting_amount:
		move(East)
		return SMx5y8
	if path_distance(36, 33) <= cutting_amount:
		move(West)
		return SMx3y8
	move(North)
	return SMx4y9
def SMx4y9(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((4, 9))
	tail_distance = path_distance(37, position_function_dict[snake_body[0]])
	food_distance = path_distance(37, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(37, 32) <= cutting_amount:
		move(West)
		return SMx3y9
	move(East)
	return SMx5y9
def SMx5y9(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((5, 9))
	tail_distance = path_distance(38, position_function_dict[snake_body[0]])
	food_distance = path_distance(38, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(38, 47) <= cutting_amount:
		move(East)
		return SMx6y9
	move(South)
	return SMx5y8
def SMx5y8(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((5, 8))
	tail_distance = path_distance(39, position_function_dict[snake_body[0]])
	food_distance = path_distance(39, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(39, 46) <= cutting_amount:
		move(East)
		return SMx6y8
	if path_distance(39, 36) <= cutting_amount:
		move(West)
		return SMx4y8
	move(South)
	return SMx5y7
def SMx5y7(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((5, 7))
	tail_distance = path_distance(40, position_function_dict[snake_body[0]])
	food_distance = path_distance(40, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(40, 45) <= cutting_amount:
		move(East)
		return SMx6y7
	if path_distance(40, 35) <= cutting_amount:
		move(West)
		return SMx4y7
	move(South)
	return SMx5y6
def SMx5y6(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((5, 6))
	tail_distance = path_distance(41, position_function_dict[snake_body[0]])
	food_distance = path_distance(41, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(41, 44) <= cutting_amount:
		move(East)
		return SMx6y6
	if path_distance(41, 18) <= cutting_amount:
		move(West)
		return SMx4y6
	move(South)
	return SMx5y5
def SMx5y5(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((5, 5))
	tail_distance = path_distance(42, position_function_dict[snake_body[0]])
	food_distance = path_distance(42, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(42, 67) <= cutting_amount:
		move(South)
		return SMx5y4
	if path_distance(42, 17) <= cutting_amount:
		move(West)
		return SMx4y5
	move(East)
	return SMx6y5
def SMx6y5(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((6, 5))
	tail_distance = path_distance(43, position_function_dict[snake_body[0]])
	food_distance = path_distance(43, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(43, 66) <= cutting_amount:
		move(South)
		return SMx6y4
	if path_distance(43, 60) <= cutting_amount:
		move(East)
		return SMx7y5
	move(North)
	return SMx6y6
def SMx6y6(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((6, 6))
	tail_distance = path_distance(44, position_function_dict[snake_body[0]])
	food_distance = path_distance(44, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(44, 59) <= cutting_amount:
		move(East)
		return SMx7y6
	if path_distance(44, 41) <= cutting_amount:
		move(West)
		return SMx5y6
	move(North)
	return SMx6y7
def SMx6y7(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((6, 7))
	tail_distance = path_distance(45, position_function_dict[snake_body[0]])
	food_distance = path_distance(45, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(45, 54) <= cutting_amount:
		move(East)
		return SMx7y7
	if path_distance(45, 40) <= cutting_amount:
		move(West)
		return SMx5y7
	move(North)
	return SMx6y8
def SMx6y8(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((6, 8))
	tail_distance = path_distance(46, position_function_dict[snake_body[0]])
	food_distance = path_distance(46, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(46, 53) <= cutting_amount:
		move(East)
		return SMx7y8
	if path_distance(46, 39) <= cutting_amount:
		move(West)
		return SMx5y8
	move(North)
	return SMx6y9
def SMx6y9(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((6, 9))
	tail_distance = path_distance(47, position_function_dict[snake_body[0]])
	food_distance = path_distance(47, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(47, 38) <= cutting_amount:
		move(West)
		return SMx5y9
	move(East)
	return SMx7y9
def SMx7y9(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((7, 9))
	tail_distance = path_distance(48, position_function_dict[snake_body[0]])
	food_distance = path_distance(48, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(48, 53) <= cutting_amount:
		move(South)
		return SMx7y8
	move(East)
	return SMx8y9
def SMx8y9(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((8, 9))
	tail_distance = path_distance(49, position_function_dict[snake_body[0]])
	food_distance = path_distance(49, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(49, 52) <= cutting_amount:
		move(South)
		return SMx8y8
	move(East)
	return SMx9y9
def SMx9y9(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((9, 9))
	move(South)
	return SMx9y8
def SMx9y8(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((9, 8))
	tail_distance = path_distance(51, position_function_dict[snake_body[0]])
	food_distance = path_distance(51, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(51, 56) <= cutting_amount:
		move(South)
		return SMx9y7
	move(West)
	return SMx8y8
def SMx8y8(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((8, 8))
	tail_distance = path_distance(52, position_function_dict[snake_body[0]])
	food_distance = path_distance(52, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(52, 49) <= cutting_amount:
		move(North)
		return SMx8y9
	if path_distance(52, 55) <= cutting_amount:
		move(South)
		return SMx8y7
	move(West)
	return SMx7y8