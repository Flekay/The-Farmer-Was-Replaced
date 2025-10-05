MOVES = generate_moves()

clear()
# till all
for direction in MOVES:
	till()
	move(direction)

def rerun():
	# prewater
	for direction in MOVES:
		while get_water() != 1:
			use_item(Items.Water)
		move(direction)

	for _ in range(15): # 60 seconds

		# plant
		for direction in MOVES:
			plant(Entities.Pumpkin)
			move(direction)

		# plant missing
		for direction in MOVES:
			while not can_harvest():
				plant(Entities.Pumpkin)
				use_item(Items.Fertilizer)
			move(direction)
		harvest()


while True:
	rerun()
