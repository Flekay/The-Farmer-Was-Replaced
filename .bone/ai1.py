clear()
betterStack()
def betterStack():
    change_hat(Hats.Dinosaur_Hat)
    apple = measure()
    length = 98
    switch_length = 50

    def mowe(direction):
        mov = move(direction)
        measurement = measure()
        if measurement:
            nonlocal length, apple
            length -= 1
            apple = measurement
        return mov

    mowe(East)
    mowe(East)
    mowe(North)
    mowe(North)

    # Define positions and movements in a list
    positions = [
        ([(0, 2), (0, 3), (1, 2), (1, 3)], [North], [West, West, North, East, East]),
        ([(0, 4), (0, 5), (1, 4), (1, 5)], [North], [West, West, North, East, East]),
        ([(3, 5), (3, 6), (4, 5), (4, 6)], [North], [East, East, North, West, West]),
        ([(0, 6), (0, 7), (0, 8), (0, 9), (1, 6), (1, 7), (1, 8), (1, 9)], [North], [West, West, North, North, North, East, South, South, East]),
        ([(2, 8), (2, 9), (3, 8), (3, 9)], [East], [North, North, East, South, South]),
        ([(4, 8), (4, 9), (5, 8), (5, 9)], [East], [North, North, East, South, South]),
        ([(5, 6), (5, 5), (6, 6), (6, 5)], [East], [South, South, East, North, North]),
        ([(6, 8), (6, 9), (7, 8), (7, 9), (8, 8), (8, 9), (9, 8), (9, 9)], [East], [North, North, East, East, East, South, West, West, South]),
        ([(8, 6), (8, 7), (9, 6), (9, 7)], [South], [East, East, South, West, West]),
        ([(8, 4), (8, 5), (9, 4), (9, 5)], [South], [East, East, South, West, West]),
        ([(6, 3), (6, 4), (5, 3), (5, 4)], [South], [West, West, South, East, East]),
        ([(8, 0), (8, 1), (8, 2), (8, 3), (9, 0), (9, 1), (9, 2), (9, 3)], [South], [East, East, South, South, South, West, North, North, West]),
        ([(6, 0), (6, 1), (7, 0), (7, 1)], [West], [South, South, West, North, North]),
        ([(4, 0), (4, 1), (5, 0), (5, 1)], [West], [South, South, West, North, North]),
        ([(4, 3), (4, 4), (3, 3), (3, 4)], [West], [North, North, West, South, South]),
        ([(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)], [West], [South, South, West, West, West, North, East, East, North])
    ]

    for apple_positions, primary_moves, alternate_moves in positions:
        if apple in apple_positions or length < switch_length or not all(mowe(dir) for dir in primary_moves):
            for dir in alternate_moves:
                mowe(dir)

    while length > 0:
        pass
    clear()
