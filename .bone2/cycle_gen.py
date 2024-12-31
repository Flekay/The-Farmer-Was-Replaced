import random

def generate_random_hamiltonian_cycle(width, height):
    # Generate initial Hamiltonian cycle using the serpentine pattern
    path = []
    for y in range(height):
        row = list(range(width))
        if y % 2 == 1:
            row.reverse()
        for x in row:
            path.append((x, y))
    # Close the cycle
    path.append(path[0])

    # Apply random transformations
    if random.choice([True, False]):
        path.reverse()
    if random.choice([True, False]):
        # Rotate 90 degrees
        path = [(y, width - 1 - x) for x, y in path]
        width, height = height, width
    if random.choice([True, False]):
        # Flip horizontally
        path = [(width - 1 - x, y) for x, y in path]
    if random.choice([True, False]):
        # Flip vertically
        path = [(x, height - 1 - y) for x, y in path]

    # Convert positions to directions
    directions = []
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        if x2 == x1 and y2 == y1 - 1:
            directions.append("North")
        elif x2 == x1 + 1 and y2 == y1:
            directions.append("East")
        elif x2 == x1 and y2 == y1 + 1:
            directions.append("South")
        elif x2 == x1 - 1 and y2 == y1:
            directions.append("West")
    print("ALMIGHTY = [")
    for direction in directions:
        print(f"\t{direction},")
    print("]")


if __name__ == "__main__":
    generate_random_hamiltonian_cycle(10, 10)
