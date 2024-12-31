def default_move_0():
	comp = grid0[0]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid0[0] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(West)
	default_move_1()
def default_move_1():
	comp = grid0[4]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid0[4] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_2()
def default_move_2():
	comp = grid1[4]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid1[4] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_3()
def default_move_3():
	comp = grid2[4]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid2[4] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_4()
def default_move_4():
	comp = grid3[4]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid3[4] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_5()
def default_move_5():
	comp = grid4[4]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid4[4] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(West)
	default_move_6()
def default_move_6():
	comp = grid4[3]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid4[3] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_7()
def default_move_7():
	comp = grid0[3]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid0[3] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_8()
def default_move_8():
	comp = grid1[3]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid1[3] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_9()
def default_move_9():
	comp = grid2[3]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid2[3] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_10()
def default_move_10():
	comp = grid3[3]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid3[3] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(West)
	default_move_11()
def default_move_11():
	comp = grid3[2]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid3[2] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_12()
def default_move_12():
	comp = grid4[2]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid4[2] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_13()
def default_move_13():
	comp = grid0[2]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid0[2] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_14()
def default_move_14():
	comp = grid1[2]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid1[2] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_15()
def default_move_15():
	comp = grid2[2]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid2[2] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(West)
	default_move_16()
def default_move_16():
	comp = grid2[1]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid2[1] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_17()
def default_move_17():
	comp = grid3[1]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid3[1] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_18()
def default_move_18():
	comp = grid4[1]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid4[1] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_19()
def default_move_19():
	comp = grid0[1]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid0[1] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_20()
def default_move_20():
	comp = grid1[1]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid1[1] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(West)
	default_move_21()
def default_move_21():
	comp = grid1[0]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid1[0] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_22()
def default_move_22():
	comp = grid2[0]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid2[0] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_23()
def default_move_23():
	comp = grid3[0]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid3[0] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)
	default_move_24()
def default_move_24():
	comp = grid4[0]
	if comp != Entities.Grass:
		if get_entity_type() == comp:
			o=0
		else:
			harvest()
			plant(comp)
		grid4[0] = Entities.Grass
	else:
		harvest()
		while get_companion()[0] == Entities.Carrot:
			harvest()
		companion, (x, y) = get_companion()
		grid[y][x] = companion
	move(North)