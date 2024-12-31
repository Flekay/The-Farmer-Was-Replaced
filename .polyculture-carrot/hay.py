clear()
#set_world_size(5)
MOVES = generate_moves()
companions = {}
contin = True
items = 0


for dir in MOVES:
	till()
	coords = (get_pos_x(), get_pos_y())
	if coords in companions:
		plant(companions.pop(coords))
		move(dir)
	else:
		# while get_companion()[0] == Entities.Carrot:
		# 	harvest()
		plant(Entities.Carrot)
		use_item(Items.Water)
		companion, pos = get_companion()
		companions[pos] = companion
		move(dir)

for _ in range(36):
	for dir in MOVES:
		coords = (get_pos_x(), get_pos_y())
		if coords in companions:
			comp = companions.pop(coords)
			if get_entity_type() == comp:
				move(dir)
			else:
				harvest()
				plant(comp)
				move(dir)
		else:
			harvest()
			# while get_companion()[0] == Entities.Carrot:
			# 	harvest()
			plant(Entities.Carrot)
			companion, pos = get_companion()
			companions[pos] = companion
			move(dir)

while contin:
	for dir in MOVES:
		coords = (get_pos_x(), get_pos_y())
		if coords in companions:
			comp = companions.pop(coords)
			if get_entity_type() == comp:
				move(dir)
			else:
				harvest()
				plant(comp)
				move(dir)
		else:
			harvest()
			if num_items(Items.Carrot) > 99250:
				contin = False
				break
			# while get_companion()[0] == Entities.Carrot:
			# 	harvest()
			plant(Entities.Carrot)
			companion, pos = get_companion()
			companions[pos] = companion
			move(dir)


# garenteed to harvest at least 750 hay
for dir in MOVES:
	if get_entity_type() == Entities.Carrot:
		harvest()
		if num_items(Items.Carrot) > 100000:
			break
	move(dir)
