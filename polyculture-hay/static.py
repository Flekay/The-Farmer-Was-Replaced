clear()
move_to(4,4)
ENTITY = {Entities.Tree, Entities.Carrots}
FERTILIZER = Items.Fertilizer

for x in range(10):
	for y in range(10):
		plant(Entities.Bush)
		move(East)
	move(North)
harvest()

for i in range(0,1,0):
	while get_companion()[0] in ENTITY:
		harvest()
	use_item(FERTILIZER)
	harvest()