def SMx0y0a(goal_idx, length, snake_body, position_function_dict):
	move(North)
	return SMx0y1a
def SMx0y1a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(1, goal_idx)
	if (path_distance(6, goal_idx) < default_distance) and move(North):
		return SMx0y2a
	move(East)
	return SMx1y1a
def SMx1y1a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(2, goal_idx)
	if (path_distance(5, goal_idx) < default_distance) and move(North):
		return SMx1y2a
	if (path_distance(99, goal_idx) < default_distance) and move(South):
		return SMx1y0a
	move(East)
	return SMx2y1a
def SMx2y1a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(3, goal_idx)
	if (path_distance(98, goal_idx) < default_distance) and move(South):
		return SMx2y0a
	if (path_distance(96, goal_idx) < default_distance) and move(East):
		return SMx3y1a
	move(North)
	return SMx2y2a
def SMx2y2a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(4, goal_idx)
	if (path_distance(9, goal_idx) < default_distance) and move(North):
		return SMx2y3a
	if (path_distance(95, goal_idx) < default_distance) and move(East):
		return SMx3y2a
	move(West)
	return SMx1y2a
def SMx1y2a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(5, goal_idx)
	if (path_distance(8, goal_idx) < default_distance) and move(North):
		return SMx1y3a
	if (path_distance(2, goal_idx) < default_distance) and move(South):
		return SMx1y1a
	move(West)
	return SMx0y2a
def SMx0y2a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(6, goal_idx)
	if (path_distance(1, goal_idx) < default_distance) and move(South):
		return SMx0y1a
	move(North)
	return SMx0y3a
def SMx0y3a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(7, goal_idx)
	if (path_distance(12, goal_idx) < default_distance) and move(North):
		return SMx0y4a
	move(East)
	return SMx1y3a
def SMx1y3a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(8, goal_idx)
	if (path_distance(11, goal_idx) < default_distance) and move(North):
		return SMx1y4a
	if (path_distance(5, goal_idx) < default_distance) and move(South):
		return SMx1y2a
	move(East)
	return SMx2y3a
def SMx2y3a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(9, goal_idx)
	if (path_distance(4, goal_idx) < default_distance) and move(South):
		return SMx2y2a
	if (path_distance(94, goal_idx) < default_distance) and move(East):
		return SMx3y3a
	move(North)
	return SMx2y4a
def SMx2y4a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(10, goal_idx)
	if (path_distance(15, goal_idx) < default_distance) and move(North):
		return SMx2y5a
	if (path_distance(93, goal_idx) < default_distance) and move(East):
		return SMx3y4a
	move(West)
	return SMx1y4a
def SMx1y4a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(11, goal_idx)
	if (path_distance(14, goal_idx) < default_distance) and move(North):
		return SMx1y5a
	if (path_distance(8, goal_idx) < default_distance) and move(South):
		return SMx1y3a
	move(West)
	return SMx0y4a
def SMx0y4a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(12, goal_idx)
	if (path_distance(7, goal_idx) < default_distance) and move(South):
		return SMx0y3a
	move(North)
	return SMx0y5a
def SMx0y5a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(13, goal_idx)
	if (path_distance(22, goal_idx) < default_distance) and move(North):
		return SMx0y6a
	move(East)
	return SMx1y5a
def SMx1y5a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(14, goal_idx)
	if (path_distance(21, goal_idx) < default_distance) and move(North):
		return SMx1y6a
	if (path_distance(11, goal_idx) < default_distance) and move(South):
		return SMx1y4a
	move(East)
	return SMx2y5a
def SMx2y5a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(15, goal_idx)
	if (path_distance(20, goal_idx) < default_distance) and move(North):
		return SMx2y6a
	if (path_distance(10, goal_idx) < default_distance) and move(South):
		return SMx2y4a
	move(East)
	return SMx3y5a
def SMx3y5a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(16, goal_idx)
	if (path_distance(19, goal_idx) < default_distance) and move(North):
		return SMx3y6a
	if (path_distance(93, goal_idx) < default_distance) and move(South):
		return SMx3y4a
	move(East)
	return SMx4y5a
def SMx4y5a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(17, goal_idx)
	if (path_distance(92, goal_idx) < default_distance) and move(South):
		return SMx4y4a
	if (path_distance(42, goal_idx) < default_distance) and move(East):
		return SMx5y5a
	move(North)
	return SMx4y6a
def SMx4y6a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(18, goal_idx)
	if (path_distance(35, goal_idx) < default_distance) and move(North):
		return SMx4y7a
	if (path_distance(41, goal_idx) < default_distance) and move(East):
		return SMx5y6a
	move(West)
	return SMx3y6a
def SMx3y6a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(19, goal_idx)
	if (path_distance(34, goal_idx) < default_distance) and move(North):
		return SMx3y7a
	if (path_distance(16, goal_idx) < default_distance) and move(South):
		return SMx3y5a
	move(West)
	return SMx2y6a
def SMx2y6a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(20, goal_idx)
	if (path_distance(29, goal_idx) < default_distance) and move(North):
		return SMx2y7a
	if (path_distance(15, goal_idx) < default_distance) and move(South):
		return SMx2y5a
	move(West)
	return SMx1y6a
def SMx1y6a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(21, goal_idx)
	if (path_distance(28, goal_idx) < default_distance) and move(North):
		return SMx1y7a
	if (path_distance(14, goal_idx) < default_distance) and move(South):
		return SMx1y5a
	move(West)
	return SMx0y6a
def SMx0y6a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(22, goal_idx)
	if (path_distance(13, goal_idx) < default_distance) and move(South):
		return SMx0y5a
	move(North)
	return SMx0y7a
def SMx0y7a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(23, goal_idx)
	if (path_distance(28, goal_idx) < default_distance) and move(East):
		return SMx1y7a
	move(North)
	return SMx0y8a
def SMx0y8a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(24, goal_idx)
	if (path_distance(27, goal_idx) < default_distance) and move(East):
		return SMx1y8a
	move(North)
	return SMx0y9a
def SMx0y9a(goal_idx, length, snake_body, position_function_dict):
	move(East)
	return SMx1y9a
def SMx1y9a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(26, goal_idx)
	if (path_distance(31, goal_idx) < default_distance) and move(East):
		return SMx2y9a
	move(South)
	return SMx1y8a
def SMx1y8a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(27, goal_idx)
	if (path_distance(30, goal_idx) < default_distance) and move(East):
		return SMx2y8a
	if (path_distance(24, goal_idx) < default_distance) and move(West):
		return SMx0y8a
	move(South)
	return SMx1y7a
def SMx1y7a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(28, goal_idx)
	if (path_distance(21, goal_idx) < default_distance) and move(South):
		return SMx1y6a
	if (path_distance(23, goal_idx) < default_distance) and move(West):
		return SMx0y7a
	move(East)
	return SMx2y7a
def SMx2y7a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(29, goal_idx)
	if (path_distance(20, goal_idx) < default_distance) and move(South):
		return SMx2y6a
	if (path_distance(34, goal_idx) < default_distance) and move(East):
		return SMx3y7a
	move(North)
	return SMx2y8a
def SMx2y8a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(30, goal_idx)
	if (path_distance(33, goal_idx) < default_distance) and move(East):
		return SMx3y8a
	if (path_distance(27, goal_idx) < default_distance) and move(West):
		return SMx1y8a
	move(North)
	return SMx2y9a
def SMx2y9a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(31, goal_idx)
	if (path_distance(26, goal_idx) < default_distance) and move(West):
		return SMx1y9a
	move(East)
	return SMx3y9a
def SMx3y9a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(32, goal_idx)
	if (path_distance(37, goal_idx) < default_distance) and move(East):
		return SMx4y9a
	move(South)
	return SMx3y8a
def SMx3y8a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(33, goal_idx)
	if (path_distance(36, goal_idx) < default_distance) and move(East):
		return SMx4y8a
	if (path_distance(30, goal_idx) < default_distance) and move(West):
		return SMx2y8a
	move(South)
	return SMx3y7a
def SMx3y7a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(34, goal_idx)
	if (path_distance(19, goal_idx) < default_distance) and move(South):
		return SMx3y6a
	if (path_distance(29, goal_idx) < default_distance) and move(West):
		return SMx2y7a
	move(East)
	return SMx4y7a
def SMx4y7a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(35, goal_idx)
	if (path_distance(18, goal_idx) < default_distance) and move(South):
		return SMx4y6a
	if (path_distance(40, goal_idx) < default_distance) and move(East):
		return SMx5y7a
	move(North)
	return SMx4y8a
def SMx4y8a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(36, goal_idx)
	if (path_distance(39, goal_idx) < default_distance) and move(East):
		return SMx5y8a
	if (path_distance(33, goal_idx) < default_distance) and move(West):
		return SMx3y8a
	move(North)
	return SMx4y9a
def SMx4y9a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(37, goal_idx)
	if (path_distance(32, goal_idx) < default_distance) and move(West):
		return SMx3y9a
	move(East)
	return SMx5y9a
def SMx5y9a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(38, goal_idx)
	if (path_distance(47, goal_idx) < default_distance) and move(East):
		return SMx6y9a
	move(South)
	return SMx5y8a
def SMx5y8a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(39, goal_idx)
	if (path_distance(46, goal_idx) < default_distance) and move(East):
		return SMx6y8a
	if (path_distance(36, goal_idx) < default_distance) and move(West):
		return SMx4y8a
	move(South)
	return SMx5y7a
def SMx5y7a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(40, goal_idx)
	if (path_distance(45, goal_idx) < default_distance) and move(East):
		return SMx6y7a
	if (path_distance(35, goal_idx) < default_distance) and move(West):
		return SMx4y7a
	move(South)
	return SMx5y6a
def SMx5y6a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(41, goal_idx)
	if (path_distance(44, goal_idx) < default_distance) and move(East):
		return SMx6y6a
	if (path_distance(18, goal_idx) < default_distance) and move(West):
		return SMx4y6a
	move(South)
	return SMx5y5a
def SMx5y5a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(42, goal_idx)
	if (path_distance(67, goal_idx) < default_distance) and move(South):
		return SMx5y4a
	if (path_distance(17, goal_idx) < default_distance) and move(West):
		return SMx4y5a
	move(East)
	return SMx6y5a
def SMx6y5a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(43, goal_idx)
	if (path_distance(66, goal_idx) < default_distance) and move(South):
		return SMx6y4a
	if (path_distance(60, goal_idx) < default_distance) and move(East):
		return SMx7y5a
	move(North)
	return SMx6y6a
def SMx6y6a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(44, goal_idx)
	if (path_distance(59, goal_idx) < default_distance) and move(East):
		return SMx7y6a
	if (path_distance(41, goal_idx) < default_distance) and move(West):
		return SMx5y6a
	move(North)
	return SMx6y7a
def SMx6y7a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(45, goal_idx)
	if (path_distance(54, goal_idx) < default_distance) and move(East):
		return SMx7y7a
	if (path_distance(40, goal_idx) < default_distance) and move(West):
		return SMx5y7a
	move(North)
	return SMx6y8a
def SMx6y8a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(46, goal_idx)
	if (path_distance(53, goal_idx) < default_distance) and move(East):
		return SMx7y8a
	if (path_distance(39, goal_idx) < default_distance) and move(West):
		return SMx5y8a
	move(North)
	return SMx6y9a
def SMx6y9a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(47, goal_idx)
	if (path_distance(38, goal_idx) < default_distance) and move(West):
		return SMx5y9a
	move(East)
	return SMx7y9a
def SMx7y9a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(48, goal_idx)
	if (path_distance(53, goal_idx) < default_distance) and move(South):
		return SMx7y8a
	move(East)
	return SMx8y9a
def SMx8y9a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(49, goal_idx)
	if (path_distance(52, goal_idx) < default_distance) and move(South):
		return SMx8y8a
	move(East)
	return SMx9y9a
def SMx9y9a(goal_idx, length, snake_body, position_function_dict):
	move(South)
	return SMx9y8a
def SMx9y8a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(51, goal_idx)
	if (path_distance(56, goal_idx) < default_distance) and move(South):
		return SMx9y7a
	move(West)
	return SMx8y8a
def SMx8y8a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(52, goal_idx)
	if (path_distance(49, goal_idx) < default_distance) and move(North):
		return SMx8y9a
	if (path_distance(55, goal_idx) < default_distance) and move(South):
		return SMx8y7a
	move(West)
	return SMx7y8a
def SMx7y8a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(53, goal_idx)
	if (path_distance(48, goal_idx) < default_distance) and move(North):
		return SMx7y9a
	if (path_distance(46, goal_idx) < default_distance) and move(West):
		return SMx6y8a
	move(South)
	return SMx7y7a
def SMx7y7a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(54, goal_idx)
	if (path_distance(59, goal_idx) < default_distance) and move(South):
		return SMx7y6a
	if (path_distance(45, goal_idx) < default_distance) and move(West):
		return SMx6y7a
	move(East)
	return SMx8y7a
def SMx8y7a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(55, goal_idx)
	if (path_distance(52, goal_idx) < default_distance) and move(North):
		return SMx8y8a
	if (path_distance(58, goal_idx) < default_distance) and move(South):
		return SMx8y6a
	move(East)
	return SMx9y7a
def SMx9y7a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(56, goal_idx)
	if (path_distance(51, goal_idx) < default_distance) and move(North):
		return SMx9y8a
	move(South)
	return SMx9y6a
def SMx9y6a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(57, goal_idx)
	if (path_distance(62, goal_idx) < default_distance) and move(South):
		return SMx9y5a
	move(West)
	return SMx8y6a
def SMx8y6a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(58, goal_idx)
	if (path_distance(55, goal_idx) < default_distance) and move(North):
		return SMx8y7a
	if (path_distance(61, goal_idx) < default_distance) and move(South):
		return SMx8y5a
	move(West)
	return SMx7y6a
def SMx7y6a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(59, goal_idx)
	if (path_distance(54, goal_idx) < default_distance) and move(North):
		return SMx7y7a
	if (path_distance(44, goal_idx) < default_distance) and move(West):
		return SMx6y6a
	move(South)
	return SMx7y5a
def SMx7y5a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(60, goal_idx)
	if (path_distance(65, goal_idx) < default_distance) and move(South):
		return SMx7y4a
	if (path_distance(43, goal_idx) < default_distance) and move(West):
		return SMx6y5a
	move(East)
	return SMx8y5a
def SMx8y5a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(61, goal_idx)
	if (path_distance(58, goal_idx) < default_distance) and move(North):
		return SMx8y6a
	if (path_distance(64, goal_idx) < default_distance) and move(South):
		return SMx8y4a
	move(East)
	return SMx9y5a
def SMx9y5a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(62, goal_idx)
	if (path_distance(57, goal_idx) < default_distance) and move(North):
		return SMx9y6a
	move(South)
	return SMx9y4a
def SMx9y4a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(63, goal_idx)
	if (path_distance(72, goal_idx) < default_distance) and move(South):
		return SMx9y3a
	move(West)
	return SMx8y4a
def SMx8y4a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(64, goal_idx)
	if (path_distance(61, goal_idx) < default_distance) and move(North):
		return SMx8y5a
	if (path_distance(71, goal_idx) < default_distance) and move(South):
		return SMx8y3a
	move(West)
	return SMx7y4a
def SMx7y4a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(65, goal_idx)
	if (path_distance(60, goal_idx) < default_distance) and move(North):
		return SMx7y5a
	if (path_distance(70, goal_idx) < default_distance) and move(South):
		return SMx7y3a
	move(West)
	return SMx6y4a
def SMx6y4a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(66, goal_idx)
	if (path_distance(43, goal_idx) < default_distance) and move(North):
		return SMx6y5a
	if (path_distance(69, goal_idx) < default_distance) and move(South):
		return SMx6y3a
	move(West)
	return SMx5y4a
def SMx5y4a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(67, goal_idx)
	if (path_distance(42, goal_idx) < default_distance) and move(North):
		return SMx5y5a
	if (path_distance(92, goal_idx) < default_distance) and move(West):
		return SMx4y4a
	move(South)
	return SMx5y3a
def SMx5y3a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(68, goal_idx)
	if (path_distance(85, goal_idx) < default_distance) and move(South):
		return SMx5y2a
	if (path_distance(91, goal_idx) < default_distance) and move(West):
		return SMx4y3a
	move(East)
	return SMx6y3a
def SMx6y3a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(69, goal_idx)
	if (path_distance(66, goal_idx) < default_distance) and move(North):
		return SMx6y4a
	if (path_distance(84, goal_idx) < default_distance) and move(South):
		return SMx6y2a
	move(East)
	return SMx7y3a
def SMx7y3a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(70, goal_idx)
	if (path_distance(65, goal_idx) < default_distance) and move(North):
		return SMx7y4a
	if (path_distance(79, goal_idx) < default_distance) and move(South):
		return SMx7y2a
	move(East)
	return SMx8y3a
def SMx8y3a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(71, goal_idx)
	if (path_distance(64, goal_idx) < default_distance) and move(North):
		return SMx8y4a
	if (path_distance(78, goal_idx) < default_distance) and move(South):
		return SMx8y2a
	move(East)
	return SMx9y3a
def SMx9y3a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(72, goal_idx)
	if (path_distance(63, goal_idx) < default_distance) and move(North):
		return SMx9y4a
	move(South)
	return SMx9y2a
def SMx9y2a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(73, goal_idx)
	if (path_distance(78, goal_idx) < default_distance) and move(West):
		return SMx8y2a
	move(South)
	return SMx9y1a
def SMx9y1a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(74, goal_idx)
	if (path_distance(77, goal_idx) < default_distance) and move(West):
		return SMx8y1a
	move(South)
	return SMx9y0a
def SMx9y0a(goal_idx, length, snake_body, position_function_dict):
	move(West)
	return SMx8y0a
def SMx8y0a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(76, goal_idx)
	if (path_distance(81, goal_idx) < default_distance) and move(West):
		return SMx7y0a
	move(North)
	return SMx8y1a
def SMx8y1a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(77, goal_idx)
	if (path_distance(74, goal_idx) < default_distance) and move(East):
		return SMx9y1a
	if (path_distance(80, goal_idx) < default_distance) and move(West):
		return SMx7y1a
	move(North)
	return SMx8y2a
def SMx8y2a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(78, goal_idx)
	if (path_distance(71, goal_idx) < default_distance) and move(North):
		return SMx8y3a
	if (path_distance(73, goal_idx) < default_distance) and move(East):
		return SMx9y2a
	move(West)
	return SMx7y2a
def SMx7y2a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(79, goal_idx)
	if (path_distance(70, goal_idx) < default_distance) and move(North):
		return SMx7y3a
	if (path_distance(84, goal_idx) < default_distance) and move(West):
		return SMx6y2a
	move(South)
	return SMx7y1a
def SMx7y1a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(80, goal_idx)
	if (path_distance(77, goal_idx) < default_distance) and move(East):
		return SMx8y1a
	if (path_distance(83, goal_idx) < default_distance) and move(West):
		return SMx6y1a
	move(South)
	return SMx7y0a
def SMx7y0a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(81, goal_idx)
	if (path_distance(76, goal_idx) < default_distance) and move(East):
		return SMx8y0a
	move(West)
	return SMx6y0a
def SMx6y0a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(82, goal_idx)
	if (path_distance(87, goal_idx) < default_distance) and move(West):
		return SMx5y0a
	move(North)
	return SMx6y1a
def SMx6y1a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(83, goal_idx)
	if (path_distance(80, goal_idx) < default_distance) and move(East):
		return SMx7y1a
	if (path_distance(86, goal_idx) < default_distance) and move(West):
		return SMx5y1a
	move(North)
	return SMx6y2a
def SMx6y2a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(84, goal_idx)
	if (path_distance(69, goal_idx) < default_distance) and move(North):
		return SMx6y3a
	if (path_distance(79, goal_idx) < default_distance) and move(East):
		return SMx7y2a
	move(West)
	return SMx5y2a
def SMx5y2a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(85, goal_idx)
	if (path_distance(68, goal_idx) < default_distance) and move(North):
		return SMx5y3a
	if (path_distance(90, goal_idx) < default_distance) and move(West):
		return SMx4y2a
	move(South)
	return SMx5y1a
def SMx5y1a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(86, goal_idx)
	if (path_distance(83, goal_idx) < default_distance) and move(East):
		return SMx6y1a
	if (path_distance(89, goal_idx) < default_distance) and move(West):
		return SMx4y1a
	move(South)
	return SMx5y0a
def SMx5y0a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(87, goal_idx)
	if (path_distance(82, goal_idx) < default_distance) and move(East):
		return SMx6y0a
	move(West)
	return SMx4y0a
def SMx4y0a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(88, goal_idx)
	if (path_distance(97, goal_idx) < default_distance) and move(West):
		return SMx3y0a
	move(North)
	return SMx4y1a
def SMx4y1a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(89, goal_idx)
	if (path_distance(86, goal_idx) < default_distance) and move(East):
		return SMx5y1a
	if (path_distance(96, goal_idx) < default_distance) and move(West):
		return SMx3y1a
	move(North)
	return SMx4y2a
def SMx4y2a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(90, goal_idx)
	if (path_distance(85, goal_idx) < default_distance) and move(East):
		return SMx5y2a
	if (path_distance(95, goal_idx) < default_distance) and move(West):
		return SMx3y2a
	move(North)
	return SMx4y3a
def SMx4y3a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(91, goal_idx)
	if (path_distance(68, goal_idx) < default_distance) and move(East):
		return SMx5y3a
	if (path_distance(94, goal_idx) < default_distance) and move(West):
		return SMx3y3a
	move(North)
	return SMx4y4a
def SMx4y4a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(92, goal_idx)
	if (path_distance(17, goal_idx) < default_distance) and move(North):
		return SMx4y5a
	if (path_distance(67, goal_idx) < default_distance) and move(East):
		return SMx5y4a
	move(West)
	return SMx3y4a
def SMx3y4a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(93, goal_idx)
	if (path_distance(16, goal_idx) < default_distance) and move(North):
		return SMx3y5a
	if (path_distance(10, goal_idx) < default_distance) and move(West):
		return SMx2y4a
	move(South)
	return SMx3y3a
def SMx3y3a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(94, goal_idx)
	if (path_distance(91, goal_idx) < default_distance) and move(East):
		return SMx4y3a
	if (path_distance(9, goal_idx) < default_distance) and move(West):
		return SMx2y3a
	move(South)
	return SMx3y2a
def SMx3y2a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(95, goal_idx)
	if (path_distance(90, goal_idx) < default_distance) and move(East):
		return SMx4y2a
	if (path_distance(4, goal_idx) < default_distance) and move(West):
		return SMx2y2a
	move(South)
	return SMx3y1a
def SMx3y1a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(96, goal_idx)
	if (path_distance(89, goal_idx) < default_distance) and move(East):
		return SMx4y1a
	if (path_distance(3, goal_idx) < default_distance) and move(West):
		return SMx2y1a
	move(South)
	return SMx3y0a
def SMx3y0a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(97, goal_idx)
	if (path_distance(88, goal_idx) < default_distance) and move(East):
		return SMx4y0a
	move(West)
	return SMx2y0a
def SMx2y0a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(98, goal_idx)
	if (path_distance(3, goal_idx) < default_distance) and move(North):
		return SMx2y1a
	move(West)
	return SMx1y0a
def SMx1y0a(goal_idx, length, snake_body, position_function_dict):
	default_distance = path_distance(99, goal_idx)
	if (path_distance(2, goal_idx) < default_distance) and move(North):
		return SMx1y1a
	move(West)
	return SMx0y0a
