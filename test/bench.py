
# Setup for your function
# ws = get_world_size()
# move_x2, move_y2 = loadData()

def bench():
    clear()
    # True Random Number Generator
    # https://www.random.org/
    spots = [
        (5,0),(2,0),(3,5),(8,9),(6,6),(6,6),
        (3,0),(4,7),(9,7),(5,3),(7,9),(9,4),
        (6,7),(4,4),(2,6),(1,5),(6,8),(2,0),
        (0,1),(4,2),(8,7),(4,7),(8,2),(6,4),
        (2,7),(5,8),(0,2),(8,0),(0,8),(6,6)
    ]
    startOp = get_op_count()
    startTime = get_time()
    for pos in spots:

        # Call your moveTo function here
        x, y = pos # uncomment if needed
        moveTo(x, y)

        if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
            quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
            break
    quick_print("@username | op:", get_op_count() - startOp - 8, " | time:", str(get_time() - startTime))
bench()