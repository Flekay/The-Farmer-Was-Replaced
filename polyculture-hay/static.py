clear()
move_to(4,4)
MOVES = generate_moves()
FERTILIZER = Items.Fertilizer
BUSH = Entities.Bush
BUSH_SET = {Entities.Bush}
ENTITY = {Entities.Tree, Entities.Carrots}

for direction in MOVES:
	plant(BUSH)
	move(direction)
harvest()

# version 1 by @Danielrab
for i in range(0,1,0):
	if get_companion()[0] in BUSH_SET:
		use_item(FERTILIZER)
	harvest()

# version 2
for i in range(0,1,0):
	while get_companion()[0] in ENTITY:
		harvest()
	use_item(FERTILIZER)
	harvest()

# version 3
# 1 op faster if companion is a bush
# but slower if companion is a tree or carrots
for i in range(0,1,0):
	while BUSH in get_companion():
		use_item(FERTILIZER)
		harvest()
	harvest()
