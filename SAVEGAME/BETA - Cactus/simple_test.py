clear()
set_world_size(3)
MOVES = generate_moves()
move_to(1,1)

# 0. Preplant
for direction in MOVES:
	till()
	plant(Entities.Cactus)
	move(direction)
	
	
EastWestSort()
	
simple_verify()