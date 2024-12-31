set_world_size(3)

plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(East)
plant(Entities.Bush)
move(East)
plant(Entities.Bush)
move(South)
plant(Entities.Bush)
move(South)
plant(Entities.Bush)
move(West)
plant(Entities.Bush)
move(North)
harvest()

while num_items(Items.Hay) < 100000:
	if Entities.Bush in get_companion():
		if num_items(Items.Fertilizer) > 1:
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
		else:
			while not can_harvest():
				use_item(Items.Water)
	harvest()