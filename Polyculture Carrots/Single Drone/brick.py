EVODD = (True, False, True, False, True, False, True, False, True, False)
clear()
for _ in range(get_world_size()/2):
	for _ in range(get_world_size()):
		till()
		plant(Entities.Carrot)
		companion, (x, y) = get_companion()
		while companion != Entities.Grass or EVODD[x]:
			harvest()
			plant(Entities.Carrot)
			companion, (x, y) = get_companion()
		move(North)
	move(East)
	move(East)

def replant_row():
	for _ in range(get_world_size()):
		use_item(Items.Water)
		# while not can_harvest():
		# 	pass
		harvest()
		plant(Entities.Carrot)
		companion, _ = get_companion()
		while companion != Entities.Grass:
			harvest()
			plant(Entities.Carrot)
			companion, _ = get_companion()
		move(North)
	move(East)
	move(East)

def remove_row():
	for _ in range(get_world_size()):
		while not can_harvest():
			pass
		harvest()
		till()
		move(North)
	move(East)
	move(East)



replant_row()
remove_row()
remove_row()
replant_row()
remove_row()



def replant_row2():
	for _ in range(get_world_size()):
		if get_water() < 0.75:
			use_item(Items.Water)
		# while not can_harvest():
		# 	if get_water() < 0.25:
		# 		use_item(Items.Water)
		if not can_harvest():
			if num_items(Items.Fertilizer):
				use_item(Items.Fertilizer)
			else:
				move(North)
				continue
		harvest()
		plant(Entities.Carrot)
		companion, _ = get_companion()
		while companion != Entities.Grass:
			harvest()
			plant(Entities.Carrot)
			companion, _ = get_companion()
		move(North)

switch = True
while num_items(Items.Carrot) < 100000:
	if switch:
		replant_row2()
		move(West)
		move(West)
		move(West)
		move(West)
	else:
		replant_row2()
		move(East)
		move(East)
		move(East)
		move(East)
	switch = not switch
