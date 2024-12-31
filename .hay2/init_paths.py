def init_move_0():
	comp = grid0[0]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(West)
	init_move_1()
def init_move_1():
	comp = grid0[4]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_2()
def init_move_2():
	comp = grid1[4]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_3()
def init_move_3():
	comp = grid2[4]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_4()
def init_move_4():
	comp = grid3[4]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_5()
def init_move_5():
	comp = grid4[4]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(West)
	init_move_6()
def init_move_6():
	comp = grid4[3]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_7()
def init_move_7():
	comp = grid0[3]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_8()
def init_move_8():
	comp = grid1[3]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_9()
def init_move_9():
	comp = grid2[3]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_10()
def init_move_10():
	comp = grid3[3]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(West)
	init_move_11()
def init_move_11():
	comp = grid3[2]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_12()
def init_move_12():
	comp = grid4[2]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_13()
def init_move_13():
	comp = grid0[2]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_14()
def init_move_14():
	comp = grid1[2]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_15()
def init_move_15():
	comp = grid2[2]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(West)
	init_move_16()
def init_move_16():
	comp = grid2[1]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_17()
def init_move_17():
	comp = grid3[1]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_18()
def init_move_18():
	comp = grid4[1]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_19()
def init_move_19():
	comp = grid0[1]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_20()
def init_move_20():
	comp = grid1[1]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(West)
	init_move_21()
def init_move_21():
	comp = grid1[0]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_22()
def init_move_22():
	comp = grid2[0]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_23()
def init_move_23():
	comp = grid3[0]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	init_move_24()
def init_move_24():
	comp = grid4[0]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)