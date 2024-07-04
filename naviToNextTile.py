def loadNaviToNextTile(size=get_world_size()):
    if size == 3:
        return [
            [East, North, North],
            [East, West, South],
            [North, North, West]
        ]
    if size == 4:
        return [
            [North, North, North, East],
            [West, East, South, South],
            [West, North, North, East],
            [West, South, South, South]
        ]
    if size == 5:
        return [
            [North, East, North, East, North],
            [East, South, West, East, West],
            [North, North, West, East, West],
            [East, South, South, South, West],
            [North, North, North, North, West]
        ]
    if size == 6:
        return [
            [East, South, South, South, South, South],
            [East, North, North, East, North, West],
            [East, West, East, South, West, South],
            [East, West, North, North, North, West],
            [East, West, South, South, South, South],
            [North, North, North, North, North, West]
        ]
    if size == 7:
        return [
            [North, North, North, North, North, North, East],
            [West, South, South, South, South, South, East],
            [North, North, North, North, East, West, East],
            [West, East, South, South, East, West, East],
            [West, North, East, West, East, West, East],
            [West, South, South, West, East, West, East],
            [North, North, North, West, North, West, North]
        ]
    if size == 8:
        return [
            [North, North, North, North, North, North, North, East],
            [West, East, South, South, South, South, South, East],
            [West, East, North, North, North, East, West, East],
            [West, East, West, South, South, East, West, East],
            [West, North, North, North, West, East, West, East],
            [West, South, South, South, South, South, West, East],
            [North, North, North, North, North, North, West, East],
            [West, South, South, South, South, South, South, South]
        ]
    if size == 9:
        return [
            [North, North, North, North, North, North, North, North, East],
            [West, South, East, South, South, South, South, South, South],
            [North, West, North, North, North, North, North, North, East],
            [West, South, South, South, East, South, South, South, South],
            [North, North, North, West, North, North, North, North, East],
            [West, South, South, South, South, South, East, South, South],
            [North, North, North, North, North, West, North, North, East],
            [West, South, South, South, South, South, South, South, East],
            [North, North, North, North, North, North, North, West, North]
        ]
    if size == 10:
        return [
            [North, North, North, North, North, North, North, North, North, East],
            [West, East, South, South, South, South, South, South, South, East],
            [West, East, North, East, North, East, North, East, West, East],
            [West, East, West, East, West, East, West, East, West, East],
            [West, South, West, North, West, North, West, North, West, East],
            [North, East, West, East, South, East, South, East, South, East],
            [West, East, West, East, West, East, West, East, West, East],
            [West, East, West, South, West, South, West, South, West, East],
            [West, North, North, North, North, North, North, North, West, East],
            [West, South, South, South, South, South, South, South, South, South]
        ]
    

def generate_moves(ws = get_world_size()):
    moves = []
    moves_row = []
    for i in range(ws-1):
        moves_row.append(East)
    moves_row.append(North)
    for i in range(ws):
        moves += moves_row
    return moves

# this global is generated once per run
# moves = generate_moves()
# for dir in moves:
#     move(dir)



# set_farm_size(3)
# set_execution_speed(7)
NaviToNextTile = loadNaviToNextTile()

def bench():
    clear()
    startOp = get_op_count()
    startTime = get_time()
    for i in range(get_world_size()**2):
        till()

        # smaller code than moveToNextTile but requires setup
        # same ops and time as inline moveToNextTile
        move(NaviToNextTile[get_pos_x()][get_pos_y()])

    quick_print("@username | op:", get_op_count() - startOp - 8,
                " | time:", str(get_time() - startTime - 0.0008))
bench()