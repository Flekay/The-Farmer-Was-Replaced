# Iterative Depth-First Search (DFS) for Maze Exploration
# Explores the maze iteratively using an explicit stack of directional cursors
# to prevent recursion limits. Checks neighbor coordinates before moving to
# avoid re-entering visited tiles (saving 400 ticks per redundant probe).
# Backtracks when dead ends are reached and harvests the treasure upon arrival.

DIRECTION = (North, East, South, West)
OPPOSITE = (South, West, North, East)
WORLD_SIZE = get_world_size()
AMOUNT = WORLD_SIZE * num_unlocked(Unlocks.Mazes)

clear()

# Generate the maze
plant(Entities.Bush)
use_item(Items.Weird_Substance, AMOUNT)

visited = {(get_pos_x(), get_pos_y())}
stack = [0]
backtrack = []

while get_entity_type() != Entities.Treasure:
	if stack[-1] == 4:
		stack.pop()
		if len(backtrack) == 0:
			break
		move(backtrack.pop())
	else:
		index = stack[-1]
		stack[-1] = index + 1
		direction = DIRECTION[index]

		if can_move(direction):
			x = get_pos_x()
			y = get_pos_y()

			if index == 0:
				y = (y + 1) % WORLD_SIZE
			elif index == 1:
				x = (x + 1) % WORLD_SIZE
			elif index == 2:
				y = (y - 1) % WORLD_SIZE
			else:
				x = (x - 1) % WORLD_SIZE

			position = (x, y)
			if position not in visited and move(direction):
				visited.add(position)
				backtrack.append(OPPOSITE[index])
				stack.append(0)

if get_entity_type() == Entities.Treasure:
	harvest()
