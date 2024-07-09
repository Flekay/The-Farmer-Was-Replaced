clear()
move_to(4,4)
MOVES = generate_moves()
ENTITY = {Entities.Tree, Entities.Carrots}
FERTILIZER = Items.Fertilizer
BUSH = Entities.Bush

for direction in MOVES:
	plant(BUSH)
	move(direction)
harvest()

for i in range(0,1,0):
	while get_companion()[0] in ENTITY:
		harvest()
	use_item(FERTILIZER)
	harvest()