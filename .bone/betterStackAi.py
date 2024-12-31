clear()
betterStack()
def betterStack():
    change_hat(Hats.Dinosaur_Hat)
    state = {'length': 98, 'apple': measure()}
    switch_length = 50

    def mowe(direction):
        mov = move(direction)
        measurement = measure()
        if measurement:
            state['length'] -= 1
            state['apple'] = measurement
        return mov

    mowe(East)
    mowe(East)
    mowe(North)
    mowe(North)

    positions = {
        'pos1': {
            'apple_positions': [(0, 2), (0, 3), (1, 2), (1, 3)],
            'primary_moves': [North],
            'alternate_moves': [West, West, North, East, East]
        },
        'pos2': {
            'apple_positions': [(0, 4), (0, 5), (1, 4), (1, 5)],
            'primary_moves': [North],
            'alternate_moves': [West, West, North, East, East]
        },
        'pos3': {
            'apple_positions': [(3, 5), (3, 6), (4, 5), (4, 6)],
            'primary_moves': [North],
            'alternate_moves': [East, East, North, West, West]
        },
        'pos4': {
            'apple_positions': [(0, 6), (0, 7), (0, 8), (0, 9), (1, 6), (1, 7), (1, 8), (1, 9)],
            'primary_moves': [North],
            'alternate_moves': [West, West, North, North, North, East, South, South, East]
        },
        'pos5': {
            'apple_positions': [(2, 8), (2, 9), (3, 8), (3, 9)],
            'primary_moves': [East],
            'alternate_moves': [North, North, East, South, South]
        },
        'pos6': {
            'apple_positions': [(4, 8), (4, 9), (5, 8), (5, 9)],
            'primary_moves': [East],
            'alternate_moves': [North, North, East, South, South]
        },
        'pos7': {
            'apple_positions': [(5, 6), (5, 5), (6, 6), (6, 5)],
            'primary_moves': [East],
            'alternate_moves': [South, South, East, North, North]
        },
        'pos8': {
            'apple_positions': [(6, 8), (6, 9), (7, 8), (7, 9), (8, 8), (8, 9), (9, 8), (9, 9)],
            'primary_moves': [East],
            'alternate_moves': [North, North, East, East, East, South, West, West, South]
        },
        'pos9': {
            'apple_positions': [(8, 6), (8, 7), (9, 6), (9, 7)],
            'primary_moves': [South],
            'alternate_moves': [East, East, South, West, West]
        },
        'pos10': {
            'apple_positions': [(8, 4), (8, 5), (9, 4), (9, 5)],
            'primary_moves': [South],
            'alternate_moves': [East, East, South, West, West]
        },
        'pos11': {
            'apple_positions': [(6, 3), (6, 4), (5, 3), (5, 4)],
            'primary_moves': [South],
            'alternate_moves': [West, West, South, East, East]
        },
        'pos12': {
            'apple_positions': [(8, 0), (8, 1), (8, 2), (8, 3), (9, 0), (9, 1), (9, 2), (9, 3)],
            'primary_moves': [South],
            'alternate_moves': [East, East, South, South, South, West, North, North, West]
        },
        'pos13': {
            'apple_positions': [(6, 0), (6, 1), (7, 0), (7, 1)],
            'primary_moves': [West],
            'alternate_moves': [South, South, West, North, North]
        },
        'pos14': {
            'apple_positions': [(4, 0), (4, 1), (5, 0), (5, 1)],
            'primary_moves': [West],
            'alternate_moves': [South, South, West, North, North]
        },
        'pos15': {
            'apple_positions': [(4, 3), (4, 4), (3, 3), (3, 4)],
            'primary_moves': [West],
            'alternate_moves': [North, North, West, South, South]
        },
        'pos16': {
            'apple_positions': [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)],
            'primary_moves': [West],
            'alternate_moves': [South, South, West, West, West, North, East, East, North]
        }
    }

    for pos_data in positions.values():
        if state['apple'] in pos_data['apple_positions'] or state['length'] < switch_length:
            if state['apple']:
                for dir in pos_data['alternate_moves']:
                    mowe(dir)
        else:
            for dir in pos_data['primary_moves']:
                if state['apple']:
                    mowe(dir)

    while state['length'] > 0:
        state['length'] -= 1  # Prevent infinite loop
    clear()
