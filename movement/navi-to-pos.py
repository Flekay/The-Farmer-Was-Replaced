def get_shortest_path(start, end, size, hws):
    path = []

    dx = (end[0] - start[0] + hws) % size - hws
    dy = (end[1] - start[1] + hws) % size - hws

    for i in range(dx):
        path.append(East)
    for i in range(-dx):
        path.append(West)
    for i in range(dy):
        path.append(North)
    for i in range(-dy):
        path.append(South)

    return path

def generate_path_map(size=get_world_size()):
    hws = size // 2
    possible_tuples = []
    for i in range(size):
        for j in range(size):
            possible_tuples.append((i, j))
    # Generate a nested dictionary structure for efficient path lookup
    map_paths = {}
    for start in possible_tuples:
        map_paths[start] = {}
        for end in possible_tuples:
            if start == end:
                map_paths[start][end] = []
            else:
                map_paths[start][end] = get_shortest_path(start, end, size, hws)
    return map_paths