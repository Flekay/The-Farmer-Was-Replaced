# Iterative Depth-First Search (DFS) for Maze Exploration
# Explores the maze iteratively using an explicit stack of directions to avoid
# recursion overhead and depth limits. Backtracks when dead ends are reached,
# tracks visited coordinates to prevent cycles, and harvests the treasure.

OPPOSITE = {North: South, South: North, East: West, West: East}
DIRECTIONS = (North, East, South, West)
AMOUNT = get_world_size() * num_unlocked(Unlocks.Mazes)

clear()

# Generate the maze
plant(Entities.Bush)
use_item(Items.Weird_Substance, AMOUNT)

visited = {(get_pos_x(), get_pos_y())}
stack = []

while get_entity_type() != Entities.Treasure:
	moved = False
	for d in DIRECTIONS:
		if move(d):
			pos = (get_pos_x(), get_pos_y())
			if pos in visited:
				move(OPPOSITE[d])
			else:
				visited.add(pos)
				stack.append(OPPOSITE[d])
				moved = True
				break

	if not moved:
		if len(stack) == 0:
			break
		move(stack.pop())

if get_entity_type() == Entities.Treasure:
	harvest()
