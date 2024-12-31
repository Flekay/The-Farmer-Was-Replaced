
def SMx7y8(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((7, 8))
	tail_distance = path_distance(53, position_function_dict[snake_body[0]])
	food_distance = path_distance(53, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(53, 48) <= cutting_amount:
		move(North)
		return SMx7y9
	if path_distance(53, 46) <= cutting_amount:
		move(West)
		return SMx6y8
	move(South)
	return SMx7y7
def SMx7y7(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((7, 7))
	tail_distance = path_distance(54, position_function_dict[snake_body[0]])
	food_distance = path_distance(54, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(54, 59) <= cutting_amount:
		move(South)
		return SMx7y6
	if path_distance(54, 45) <= cutting_amount:
		move(West)
		return SMx6y7
	move(East)
	return SMx8y7
def SMx8y7(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((8, 7))
	tail_distance = path_distance(55, position_function_dict[snake_body[0]])
	food_distance = path_distance(55, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(55, 52) <= cutting_amount:
		move(North)
		return SMx8y8
	if path_distance(55, 58) <= cutting_amount:
		move(South)
		return SMx8y6
	move(East)
	return SMx9y7
def SMx9y7(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((9, 7))
	tail_distance = path_distance(56, position_function_dict[snake_body[0]])
	food_distance = path_distance(56, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(56, 51) <= cutting_amount:
		move(North)
		return SMx9y8
	move(South)
	return SMx9y6
def SMx9y6(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((9, 6))
	tail_distance = path_distance(57, position_function_dict[snake_body[0]])
	food_distance = path_distance(57, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(57, 62) <= cutting_amount:
		move(South)
		return SMx9y5
	move(West)
	return SMx8y6
def SMx8y6(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((8, 6))
	tail_distance = path_distance(58, position_function_dict[snake_body[0]])
	food_distance = path_distance(58, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(58, 55) <= cutting_amount:
		move(North)
		return SMx8y7
	if path_distance(58, 61) <= cutting_amount:
		move(South)
		return SMx8y5
	move(West)
	return SMx7y6
def SMx7y6(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((7, 6))
	tail_distance = path_distance(59, position_function_dict[snake_body[0]])
	food_distance = path_distance(59, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(59, 54) <= cutting_amount:
		move(North)
		return SMx7y7
	if path_distance(59, 44) <= cutting_amount:
		move(West)
		return SMx6y6
	move(South)
	return SMx7y5
def SMx7y5(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((7, 5))
	tail_distance = path_distance(60, position_function_dict[snake_body[0]])
	food_distance = path_distance(60, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(60, 65) <= cutting_amount:
		move(South)
		return SMx7y4
	if path_distance(60, 43) <= cutting_amount:
		move(West)
		return SMx6y5
	move(East)
	return SMx8y5
def SMx8y5(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((8, 5))
	tail_distance = path_distance(61, position_function_dict[snake_body[0]])
	food_distance = path_distance(61, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(61, 58) <= cutting_amount:
		move(North)
		return SMx8y6
	if path_distance(61, 64) <= cutting_amount:
		move(South)
		return SMx8y4
	move(East)
	return SMx9y5
def SMx9y5(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((9, 5))
	tail_distance = path_distance(62, position_function_dict[snake_body[0]])
	food_distance = path_distance(62, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(62, 57) <= cutting_amount:
		move(North)
		return SMx9y6
	move(South)
	return SMx9y4
def SMx9y4(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((9, 4))
	tail_distance = path_distance(63, position_function_dict[snake_body[0]])
	food_distance = path_distance(63, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(63, 72) <= cutting_amount:
		move(South)
		return SMx9y3
	move(West)
	return SMx8y4
def SMx8y4(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((8, 4))
	tail_distance = path_distance(64, position_function_dict[snake_body[0]])
	food_distance = path_distance(64, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(64, 61) <= cutting_amount:
		move(North)
		return SMx8y5
	if path_distance(64, 71) <= cutting_amount:
		move(South)
		return SMx8y3
	move(West)
	return SMx7y4
def SMx7y4(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((7, 4))
	tail_distance = path_distance(65, position_function_dict[snake_body[0]])
	food_distance = path_distance(65, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(65, 60) <= cutting_amount:
		move(North)
		return SMx7y5
	if path_distance(65, 70) <= cutting_amount:
		move(South)
		return SMx7y3
	move(West)
	return SMx6y4
def SMx6y4(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((6, 4))
	tail_distance = path_distance(66, position_function_dict[snake_body[0]])
	food_distance = path_distance(66, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(66, 43) <= cutting_amount:
		move(North)
		return SMx6y5
	if path_distance(66, 69) <= cutting_amount:
		move(South)
		return SMx6y3
	move(West)
	return SMx5y4
def SMx5y4(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((5, 4))
	tail_distance = path_distance(67, position_function_dict[snake_body[0]])
	food_distance = path_distance(67, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(67, 42) <= cutting_amount:
		move(North)
		return SMx5y5
	if path_distance(67, 92) <= cutting_amount:
		move(West)
		return SMx4y4
	move(South)
	return SMx5y3
def SMx5y3(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((5, 3))
	tail_distance = path_distance(68, position_function_dict[snake_body[0]])
	food_distance = path_distance(68, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(68, 85) <= cutting_amount:
		move(South)
		return SMx5y2
	if path_distance(68, 91) <= cutting_amount:
		move(West)
		return SMx4y3
	move(East)
	return SMx6y3
def SMx6y3(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((6, 3))
	tail_distance = path_distance(69, position_function_dict[snake_body[0]])
	food_distance = path_distance(69, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(69, 66) <= cutting_amount:
		move(North)
		return SMx6y4
	if path_distance(69, 84) <= cutting_amount:
		move(South)
		return SMx6y2
	move(East)
	return SMx7y3
def SMx7y3(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((7, 3))
	tail_distance = path_distance(70, position_function_dict[snake_body[0]])
	food_distance = path_distance(70, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(70, 65) <= cutting_amount:
		move(North)
		return SMx7y4
	if path_distance(70, 79) <= cutting_amount:
		move(South)
		return SMx7y2
	move(East)
	return SMx8y3
def SMx8y3(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((8, 3))
	tail_distance = path_distance(71, position_function_dict[snake_body[0]])
	food_distance = path_distance(71, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(71, 64) <= cutting_amount:
		move(North)
		return SMx8y4
	if path_distance(71, 78) <= cutting_amount:
		move(South)
		return SMx8y2
	move(East)
	return SMx9y3
def SMx9y3(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((9, 3))
	tail_distance = path_distance(72, position_function_dict[snake_body[0]])
	food_distance = path_distance(72, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(72, 63) <= cutting_amount:
		move(North)
		return SMx9y4
	move(South)
	return SMx9y2
def SMx9y2(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((9, 2))
	tail_distance = path_distance(73, position_function_dict[snake_body[0]])
	food_distance = path_distance(73, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(73, 78) <= cutting_amount:
		move(West)
		return SMx8y2
	move(South)
	return SMx9y1
def SMx9y1(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((9, 1))
	tail_distance = path_distance(74, position_function_dict[snake_body[0]])
	food_distance = path_distance(74, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(74, 77) <= cutting_amount:
		move(West)
		return SMx8y1
	move(South)
	return SMx9y0
def SMx9y0(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((9, 0))
	move(West)
	return SMx8y0
def SMx8y0(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((8, 0))
	tail_distance = path_distance(76, position_function_dict[snake_body[0]])
	food_distance = path_distance(76, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(76, 81) <= cutting_amount:
		move(West)
		return SMx7y0
	move(North)
	return SMx8y1
def SMx8y1(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((8, 1))
	tail_distance = path_distance(77, position_function_dict[snake_body[0]])
	food_distance = path_distance(77, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(77, 74) <= cutting_amount:
		move(East)
		return SMx9y1
	if path_distance(77, 80) <= cutting_amount:
		move(West)
		return SMx7y1
	move(North)
	return SMx8y2
def SMx8y2(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((8, 2))
	tail_distance = path_distance(78, position_function_dict[snake_body[0]])
	food_distance = path_distance(78, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(78, 71) <= cutting_amount:
		move(North)
		return SMx8y3
	if path_distance(78, 73) <= cutting_amount:
		move(East)
		return SMx9y2
	move(West)
	return SMx7y2
def SMx7y2(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((7, 2))
	tail_distance = path_distance(79, position_function_dict[snake_body[0]])
	food_distance = path_distance(79, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(79, 70) <= cutting_amount:
		move(North)
		return SMx7y3
	if path_distance(79, 84) <= cutting_amount:
		move(West)
		return SMx6y2
	move(South)
	return SMx7y1
def SMx7y1(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((7, 1))
	tail_distance = path_distance(80, position_function_dict[snake_body[0]])
	food_distance = path_distance(80, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(80, 77) <= cutting_amount:
		move(East)
		return SMx8y1
	if path_distance(80, 83) <= cutting_amount:
		move(West)
		return SMx6y1
	move(South)
	return SMx7y0
def SMx7y0(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((7, 0))
	tail_distance = path_distance(81, position_function_dict[snake_body[0]])
	food_distance = path_distance(81, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(81, 76) <= cutting_amount:
		move(East)
		return SMx8y0
	move(West)
	return SMx6y0
def SMx6y0(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((6, 0))
	tail_distance = path_distance(82, position_function_dict[snake_body[0]])
	food_distance = path_distance(82, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(82, 87) <= cutting_amount:
		move(West)
		return SMx5y0
	move(North)
	return SMx6y1
def SMx6y1(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((6, 1))
	tail_distance = path_distance(83, position_function_dict[snake_body[0]])
	food_distance = path_distance(83, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(83, 80) <= cutting_amount:
		move(East)
		return SMx7y1
	if path_distance(83, 86) <= cutting_amount:
		move(West)
		return SMx5y1
	move(North)
	return SMx6y2
def SMx6y2(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((6, 2))
	tail_distance = path_distance(84, position_function_dict[snake_body[0]])
	food_distance = path_distance(84, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(84, 69) <= cutting_amount:
		move(North)
		return SMx6y3
	if path_distance(84, 79) <= cutting_amount:
		move(East)
		return SMx7y2
	move(West)
	return SMx5y2
def SMx5y2(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((5, 2))
	tail_distance = path_distance(85, position_function_dict[snake_body[0]])
	food_distance = path_distance(85, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(85, 68) <= cutting_amount:
		move(North)
		return SMx5y3
	if path_distance(85, 90) <= cutting_amount:
		move(West)
		return SMx4y2
	move(South)
	return SMx5y1
def SMx5y1(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((5, 1))
	tail_distance = path_distance(86, position_function_dict[snake_body[0]])
	food_distance = path_distance(86, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(86, 83) <= cutting_amount:
		move(East)
		return SMx6y1
	if path_distance(86, 89) <= cutting_amount:
		move(West)
		return SMx4y1
	move(South)
	return SMx5y0
def SMx5y0(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((5, 0))
	tail_distance = path_distance(87, position_function_dict[snake_body[0]])
	food_distance = path_distance(87, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(87, 82) <= cutting_amount:
		move(East)
		return SMx6y0
	move(West)
	return SMx4y0
def SMx4y0(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((4, 0))
	tail_distance = path_distance(88, position_function_dict[snake_body[0]])
	food_distance = path_distance(88, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(88, 97) <= cutting_amount:
		move(West)
		return SMx3y0
	move(North)
	return SMx4y1
def SMx4y1(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((4, 1))
	tail_distance = path_distance(89, position_function_dict[snake_body[0]])
	food_distance = path_distance(89, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(89, 86) <= cutting_amount:
		move(East)
		return SMx5y1
	if path_distance(89, 96) <= cutting_amount:
		move(West)
		return SMx3y1
	move(North)
	return SMx4y2
def SMx4y2(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((4, 2))
	tail_distance = path_distance(90, position_function_dict[snake_body[0]])
	food_distance = path_distance(90, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(90, 85) <= cutting_amount:
		move(East)
		return SMx5y2
	if path_distance(90, 95) <= cutting_amount:
		move(West)
		return SMx3y2
	move(North)
	return SMx4y3
def SMx4y3(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((4, 3))
	tail_distance = path_distance(91, position_function_dict[snake_body[0]])
	food_distance = path_distance(91, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(91, 68) <= cutting_amount:
		move(East)
		return SMx5y3
	if path_distance(91, 94) <= cutting_amount:
		move(West)
		return SMx3y3
	move(North)
	return SMx4y4
def SMx4y4(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((4, 4))
	tail_distance = path_distance(92, position_function_dict[snake_body[0]])
	food_distance = path_distance(92, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(92, 17) <= cutting_amount:
		move(North)
		return SMx4y5
	if path_distance(92, 67) <= cutting_amount:
		move(East)
		return SMx5y4
	move(West)
	return SMx3y4
def SMx3y4(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((3, 4))
	tail_distance = path_distance(93, position_function_dict[snake_body[0]])
	food_distance = path_distance(93, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(93, 16) <= cutting_amount:
		move(North)
		return SMx3y5
	if path_distance(93, 10) <= cutting_amount:
		move(West)
		return SMx2y4
	move(South)
	return SMx3y3
def SMx3y3(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((3, 3))
	tail_distance = path_distance(94, position_function_dict[snake_body[0]])
	food_distance = path_distance(94, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(94, 91) <= cutting_amount:
		move(East)
		return SMx4y3
	if path_distance(94, 9) <= cutting_amount:
		move(West)
		return SMx2y3
	move(South)
	return SMx3y2
def SMx3y2(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((3, 2))
	tail_distance = path_distance(95, position_function_dict[snake_body[0]])
	food_distance = path_distance(95, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(95, 90) <= cutting_amount:
		move(East)
		return SMx4y2
	if path_distance(95, 4) <= cutting_amount:
		move(West)
		return SMx2y2
	move(South)
	return SMx3y1
def SMx3y1(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((3, 1))
	tail_distance = path_distance(96, position_function_dict[snake_body[0]])
	food_distance = path_distance(96, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(96, 89) <= cutting_amount:
		move(East)
		return SMx4y1
	if path_distance(96, 3) <= cutting_amount:
		move(West)
		return SMx2y1
	move(South)
	return SMx3y0
def SMx3y0(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((3, 0))
	tail_distance = path_distance(97, position_function_dict[snake_body[0]])
	food_distance = path_distance(97, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(97, 88) <= cutting_amount:
		move(East)
		return SMx4y0
	move(West)
	return SMx2y0
def SMx2y0(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((2, 0))
	tail_distance = path_distance(98, position_function_dict[snake_body[0]])
	food_distance = path_distance(98, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(98, 3) <= cutting_amount:
		move(North)
		return SMx2y1
	move(West)
	return SMx1y0
def SMx1y0(goal_idx, length, snake_body, position_function_dict):
	snake_body.append((1, 0))
	tail_distance = path_distance(99, position_function_dict[snake_body[0]])
	food_distance = path_distance(99, goal_idx)
	cutting_amount = tail_distance - length
	if food_distance < cutting_amount:
		cutting_amount = food_distance
	if path_distance(99, 2) <= cutting_amount:
		move(North)
		return SMx1y1
	move(West)
	return SMx0y0
	