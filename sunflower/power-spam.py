clear()
MOVES = generate_moves()
move_to(4,4)

# pre plant
for direction in MOVES:
	till()
	while measure() != 7:
		harvest()
		plant(Entities.Sunflower)
	move(direction)

# spam
harvest()
while True:
	if get_water() < 0.8:
		use_item(Items.Water_Tank)
	plant(Entities.Sunflower)
	while not can_harvest():
		use_item(Items.Fertilizer)
	use_item(Items.Weird_Substance)
	harvest()
	