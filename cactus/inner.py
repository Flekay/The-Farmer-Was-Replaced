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
        plant(CACTUS)
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
CACTUS = Entities.Cactus
INNER_MOVES = INNER_MOVES + INNER_INNER_MOVES_REV + INNER_INNER_MOVES + INNER_MOVES_REV
clear()
till_all()
for i in range(999999999):
	cactus()
