clear()
move_to(4,4)
MOVES = generate_moves()

for direction in MOVES:
	plant(Entities.Bush)
	move(direction)
harvest()

while True:
	if Entities.Bush in get_companion():
		use_item(Items.Fertilizer)
	harvest()
