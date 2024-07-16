clear()
move_to(4,4)
MOVES = generate_moves()
FERTILIZER = Items.Fertilizer
BUSH = Entities.Bush

for direction in MOVES:
	plant(BUSH)
	move(direction)
harvest()

for i in range(0,1,0):
	while BUSH in get_companion():
		use_item(FERTILIZER)
		harvest()
	harvest()
