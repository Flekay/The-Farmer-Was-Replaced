#min 29.1613 max 31.6816 avg 30.2619
set_world_size(5)
MOVES = generate_moves()
companions = {}
contin = True


move_0(init_run)

for _ in range(35):
	move_0(default_run)

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
			if num_items(Items.Hay) > 99250:
				contin = False
				break
			while get_companion()[0] == Entities.Carrot:
				harvest()
			companion, pos = get_companion()
			companions[pos] = companion
			move(dir)


# garenteed to harvest at least 750 hay
for dir in MOVES:
	if get_entity_type() == Entities.Grass:
		harvest()
		if num_items(Items.Hay) > 100000:
			break
	move(dir)
	