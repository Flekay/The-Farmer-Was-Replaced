import os

def generate_moves(world_size):
	moves = []
	pos_x = 0
	pos_y = 0
	for i in range(world_size**2):
		if pos_x % world_size == pos_y % world_size:
			pos_x -= 1
			moves.append("West")
		else:
			pos_y += 1
			moves.append("North")
	return moves

# Replace static MOVES with generated ones
world_size = 5
MOVES = generate_moves(world_size)
directions = {
	"North": [0, 1],
	"East": [1, 0],
	"South": [0, -1],
	"West": [-1, 0]
}

functions = []
pos = [0, 0]
i = 0

for dir in MOVES:
	current_x = pos[0]
	current_y = pos[1]
	step_index = current_x * 10 + current_y

	# def init_run():
	# 	comp = grid0[0]
	# 	if comp != Entities.Grass:
	# 		plant(comp)
	# 	else:
	# 		while get_companion()[0] == Entities.Carrot:
	# 			harvest()
	# 		companion, pos = get_companion()
	# 		x, y = pos
	# 		grid[y][x] = companion

	functions.append(f"def init_move_{i}():")
	functions.append(f"\tcomp = grid{current_y}[{current_x}]")
	functions.append(f"\tif comp != Entities.Grass:")
	functions.append(f"\t\tplant(comp)")
	functions.append(f"\telse:")
	functions.append(f"\t\twhile get_companion()[0] == Entities.Carrot:")
	functions.append(f"\t\t\tharvest()")
	functions.append(f"\t\tcompanion, (x, y) = get_companion()")
	functions.append(f"\t\tgrid[y][x] = companion")

	if i + 1 < len(MOVES):
		functions.append(f"\tmove({dir})")
		functions.append(f"\tinit_move_{i+1}()")
	else:
		functions.append(f"\tmove({dir})")

	# Update position for next iteration
	pos[0] = (pos[0] + directions[dir][0]) % world_size
	pos[1] = (pos[1] + directions[dir][1]) % world_size
	i += 1




# Write to file
with open(os.path.join(os.path.dirname(__file__), "init_paths.py"), "w") as f:
	f.write("\n".join(functions))




# grid = [
# 	[Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass],
# 	[Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass],
# 	[Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass],
# 	[Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass],
# 	[Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass],
# ]
# grid0 = grid[0]
# grid1 = grid[1]
# grid2 = grid[2]
# grid3 = grid[3]
# grid4 = grid[4]

# def init_run(x,y,i):
# 	coords = (x,y)
# 	if coords in companions:
# 		plant(companions.pop(coords))
# 		#move(dir)
# 	else:
# 		while get_companion()[0] == Entities.Carrot:
# 			harvest()
# 		companion, pos = get_companion()
# 		companions[pos] = companion
# 		#move(dir)


def init_run():
	comp = grid0[0]
	if comp != Entities.Grass:
		plant(comp)
	else:
		while get_companion()[0] == Entities.Carrot:
			harvest()
		# companion, pos = get_companion()
		# x, y = pos
		companion, (x, y) = get_companion()
		grid[y][x] = companion
