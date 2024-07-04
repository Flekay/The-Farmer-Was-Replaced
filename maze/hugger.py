def hugger(farmAmount):
	while num_items(Items.Gold) < farmAmount:
		# Spawn Maze
		clear()
		plant(Entities.Bush)
		while get_entity_type() == Entities.Bush:
			if num_items(Items.Fertilizer) < 1:
				trade(Items.Fertilizer)
			use_item(Items.Fertilizer)
				
		# Traverse Maze
		PosY = 0
		PosX = 0
		dir = [South, East, North, West]
		currDir = 0
		newDir = 0
		while get_entity_type() != Entities.Treasure:
			if get_pos_x() == PosX and get_pos_y() == PosY:
				currDir+=1
				if currDir == 4:
					currDir = 0
				PosX = get_pos_x()
				PosY = get_pos_y()
				move(dir[currDir])
			else:
				PosX = get_pos_x()
				PosY = get_pos_y()
				if currDir-1 >= 0:
					newDir = currDir-1
					move(dir[newDir])
				else:
					newDir = 3
					move(dir[newDir])
				if get_pos_x() != PosX or get_pos_y() != PosY:
					currDir = newDir
				else:
					move(dir[currDir])

		# Harvest Treasure
		harvest()