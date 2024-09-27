MOVES = generate_moves()

clear()
# till all
for direction in MOVES:
	till()
	move(direction)

def tiny():
	# prewater
	for direction in MOVES:
		while get_water() != 1:
			use_item(Items.Water_Tank)
		move(direction)

	time = get_time()
	for _ in range(22): # 60 seconds
		# plant
		for direction in MOVES:
			harvest()
			plant(Entities.Pumpkin)
			move(direction)
	quick_print("Time: ", get_time() - time)

while True:
	tiny()
	