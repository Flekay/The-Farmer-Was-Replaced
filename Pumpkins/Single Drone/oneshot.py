MOVES = generate_moves()

clear()
for direction in MOVES:
	till()
	move(direction)

while True:
	for direction in MOVES:
		while not can_harvest():
			plant(Entities.Pumpkin)
			use_item(Items.Fertilizer)
		move(direction)
	harvest()
