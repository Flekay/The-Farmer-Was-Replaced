clear()
for _ in range(get_world_size()):
	till()
	plant(Entities.Carrot)
	companion, (x, y) = get_companion()
	while companion != Entities.Grass or not x:
		harvest()
		plant(Entities.Carrot)
		companion, (x, y) = get_companion()
	use_item(Items.Water)
	move(North)

while num_items(Items.Carrot) < 100000:
	if get_water() < 0.9:
		use_item(Items.Water)
	if not can_harvest():
		move(North)
		continue
	harvest()
	plant(Entities.Carrot)
	companion, (x, y) = get_companion()
	while companion != Entities.Grass or not x:
		harvest()
		plant(Entities.Carrot)
		companion, (x, y) = get_companion()
	move(North)
