clear()
set_world_size(6)
for _ in range(5):
	for _ in range(get_world_size()):
		plant(Entities.Bush)
		move(East)
	move(North)


while num_items(Items.Hay) < 100000:
	if get_water() < 0.475:
		use_item(Items.Water)

	if can_harvest():
		harvest()
		companion, (x, y) = get_companion()
		while y > 4 or companion != Entities.Bush:
			harvest()
			companion, (x, y) = get_companion()
	move(West)
	