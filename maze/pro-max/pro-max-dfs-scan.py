# Global variables
ws = get_world_size()
PATH = {}
WALL = {}
for x in range(ws):
    for y in range(ws):
        PATH[(x, y)] = set()
        WALL[(x, y)] = {North, East, South, West}
TREASURE_POS = {0: (0, 0)}
FERTILIZER = Items.Fertilizer
VISITED = set()


def get_adjacent_positions(pos):
    x, y = pos
    return [
        ((x, y+1), North, South),  # North
        ((x+1, y), East, West),    # East
        ((x, y-1), South, North),  # South
        ((x-1, y), West, East)     # West
    ]

def dfs_explore(current_pos):
    VISITED.add(current_pos)

    if measure():
        # TREASURE_POS[0] = current_pos
        # Optionally, harvest treasure here
        # while measure():
        #     use_item(FERTILIZER)

        TREASURE_POS[0] = measure()
        while measure():
            use_item(FERTILIZER)

    for adjacent in get_adjacent_positions(current_pos):
        next_pos, direction, opposite = adjacent
        if next_pos not in VISITED and move(direction):
            # Update WALL and PATH
            WALL[current_pos].remove(direction)
            WALL[next_pos].remove(opposite)
            PATH[current_pos].add(direction)
            PATH[next_pos].add(opposite)

            # Recursive exploration
            dfs_explore(next_pos)

            # Backtrack
            move(opposite)


# Main execution
ops = get_op_count()
dfs_explore((get_pos_x(), get_pos_y()))
quick_print("DFS scan completed in", get_op_count() - ops, "operations")
