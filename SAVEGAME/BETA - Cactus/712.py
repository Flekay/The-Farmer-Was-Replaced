MOVES = generate_moves()
clear()
for direction in MOVES:
	till()
	move(direction)

ws = get_world_size()
ws_range = range(ws)
moves = [
	North,East,North,East,North,East,North,East,North,East,
	North,East,North,East,North,North,North,North,North,North,
	North,North,North,West,West,South,West,South,West,South,
	West,South,West,South,East,East,North,East,East,North,
	East,North,North,North,North,North,West,South,West,South,
	West,South,South,West,North,North,North,North,East,East,
	South,West,South,West,West,South,South,South,East,East,
	South,West,South,East,East,East,North,East,North,West,
	North,North,North,North,North,North,North,North,East,
	South,South,South,East,East,South,South,South,South,West,
	South,East,South,South,West,North,West,West,West,South,
	West,South,South,East,North,East,South,East,East,North,
	East,East,East,South,South,East,South,South,South,East,
	East,North,North,North,East,South,South,South,South,West,
	West,North,North,North,North,North,North,North,West,North,
	West,West,West,North,North,North,West,West,South,West,South,
]


while True:
	move_to(0,0)

	# Combined till, plant and initial sort
	for x in ws_range:
		for y in ws_range:
			# Till and plant
			plant(Entities.Cactus)

			# Initial sort
			valid_simple_swap()
			move(North)
		move(East)

	for dir in moves:
		move(dir)
		simple_swap()
		
	harvest()