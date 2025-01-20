# ...existing code...
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bubble_sort_by_f(neighbors, costs, goal):
    # Einfaches Bubble-Sort
    n = len(neighbors)
    for i in range(n):
        for j in range(0, n - i - 1):
            f_j = costs[neighbors[j]] + 1 + manhattan_distance(neighbors[j], goal)
            f_j1 = costs[neighbors[j+1]] + 1 + manhattan_distance(neighbors[j+1], goal)
            if f_j > f_j1:
                temp = neighbors[j]
                neighbors[j] = neighbors[j+1]
                neighbors[j+1] = temp

def debug_display(current, candidate):
    print("Expanding node:", current, "-> Checking candidate:", candidate)

def recursive_astar(grid, current, goal, g_cost, visited):
    if current == goal:
        return [current]
    visited.add(current)
    neighbors = get_neighbors(current)
    valid_neighbors = []
    for n in neighbors:
        if n not in visited and not is_wall(grid, n):
            g_cost[n] = g_cost[current] + 1
            valid_neighbors.append(n)
    bubble_sort_by_f(valid_neighbors, g_cost, goal)
    for next_node in valid_neighbors:
        debug_display(current, next_node)
        path = recursive_astar(grid, next_node, goal, g_cost, visited)
        if path:
            return [current] + path
    return []
# ...existing code...
