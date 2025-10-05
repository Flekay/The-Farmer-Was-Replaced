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
use_item(Items.Water)
use_item(Items.Water)
use_item(Items.Water)
while True:
	use_item(Items.Water)
	for _ in range(562): # get_water <= 0.76
		plant(Entities.Sunflower)
		use_item(Items.Fertilizer)
		use_item(Items.Weird_Substance)
		harvest()
