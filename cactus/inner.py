def first_scan():
    for i in range(4):
        if measure(West) != None and  measure(West) > measure():
            swap(West)
        if measure(South) != None and measure(South)  > measure():
            swap(South)
        if measure(North) != None and measure(North) < measure():
            swap(North)
        if measure(East) != None and measure(East) < measure():
            swap(East)

def simple_scan():
    for i in range(4):
        if measure(West) > measure():
            swap(West)
        if measure(South)  > measure():
            swap(South)
        if measure(North) < measure():
            swap(North)
        if measure(East) < measure():
            swap(East)

def till_all():
    for dir in MOVES:
        till()
        move(dir)

def cactus():
    for dir in MOVES:
        plant(Entities.Cactus)
        first_scan()
        move(dir)
    move(North)
    move(East)
    for dir in INNER_MOVES:
        simple_scan()
        move(dir)
    move(South)
    move(West)
    harvest()

def generate_world_moves(
		n = get_world_size()**2,
		world_size = get_world_size(),
		pos_x = 0,
		pos_y = 0
	):
	moves = []
	if n > world_size**2:
		world_moves = generate_world_moves(world_size**2, world_size, pos_x, pos_y)
		for i in range(n // world_size**2):
			moves += world_moves
		n %= world_size**2

	if world_size % 2 == 0:
		for i in range(n):
			if pos_x == 0 and pos_y < world_size - 1:
				pos_y += 1
				moves.append(North)
			elif pos_y % 2 == 0 and pos_x != 1:
				pos_x -= 1
				moves.append(West)
			elif pos_y % 2 != 0 and pos_x != world_size - 1:
				pos_x += 1
				moves.append(East)
			elif pos_x == 1 and pos_y == 0:
				pos_x -= 1
				moves.append(West)
			else:
				pos_y -= 1
				moves.append(South)
	else:
		print("Odd world size not supported yet")
	return moves


OPPOSITE = {North: South, South: North, East: West, West: East}
INNER_WORLD_SIZE = get_world_size() - 2
MOVES = generate_moves()
INNER_MOVES = generate_world_moves(INNER_WORLD_SIZE**2, INNER_WORLD_SIZE)
# INNER_MOVES = generate_moves()
INNER_MOVES_REV = []
for dir in INNER_MOVES[::-1]:
    INNER_MOVES_REV.append(OPPOSITE[dir])
INNER_INNER_MOVES = INNER_MOVES + []
INNER_INNER_MOVES_REV = INNER_MOVES_REV + []
for i in range(INNER_WORLD_SIZE):
    INNER_INNER_MOVES.pop(0)
    INNER_INNER_MOVES_REV.pop(-1)
INNER_MOVES = INNER_MOVES + INNER_INNER_MOVES_REV + INNER_INNER_MOVES + INNER_MOVES_REV
clear()
till_all()
while True:
	cactus()
