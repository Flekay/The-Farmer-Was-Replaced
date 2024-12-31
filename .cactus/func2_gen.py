import os

MOVES = [
	"North", "East", "North", "East", "North", "East", "North", "East", "North", "East",
	"North", "East", "North", "East", "North", "East", "North", "West", "South", "West",
	"South", "West", "South", "West", "South", "West", "South", "West", "South", "West",
	"South", "West", "North", "East", "North", "East", "North", "East", "North", "East",
	"North", "East", "North", "East", "North", "West", "South", "West", "South", "West",
	"South", "West", "South", "West", "South", "West", "North", "East", "North", "East",
	"North", "East", "North", "East", "North", "West", "South", "West", "South", "West",
	"South", "West", "North", "East", "North", "East", "North", "West", "South", "West",
	"North", "West", "South", "West", "South", "West", "South", "West", "South", "West",
	"South", "West", "South", "West", "South", "West", "South", "West", "South", "East",
	"North", "East", "North", "East", "North", "East", "North", "East", "North", "East",
	"North", "East", "North", "East", "South", "West", "South", "West", "South", "West",
	"South", "West", "South", "West", "South", "West", "South", "East", "North", "East",
	"North", "East", "North", "East", "North", "East", "North", "East", "South", "West",
	"South", "West", "South", "West", "South", "West", "South", "East", "North", "East",
	"North", "East", "North", "East", "South", "West", "South", "West", "South", "East",
	"North", "East", "South", "East",
]

# MOVES = [
# 	"North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "West", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "North", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "West", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "North", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "West", "West", "South", "West", "South", "West", "South", "West", "South", "North", "North", "East", "North", "East", "North", "East", "West", "West", "South", "West", "South", "North", "North", "East", "West", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "East", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "South", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "East", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "East", "North", "South", "South", "West", "South", "West", "South", "West", "South", "West", "South", "West", "East", "East", "North", "East", "North", "East", "North", "East", "North", "South", "South", "West", "South", "West", "South", "West", "East", "East", "North", "East", "North", "South", "South", "West", "East", "East",
# ]
world_size = 10
directions = {
	"North": [0, 1],
	"East": [1, 0],
	"South": [0, -1],
	"West": [-1, 0]
}

def neighbour_pos(pos):
	x, y = pos
	list = []
	list.append(((x - 1) % world_size, y))
	list.append(((x + 1) % world_size, y))
	list.append((x, (y - 1) % world_size))
	list.append((x, (y + 1) % world_size))
	return list
neighbour_order = ["West", "East", "South", "North"]

last_visit = {}
pos = [0, 0]
i = 0
for dir in MOVES:
	x,y = pos
	neighbours = neighbour_pos(pos)
	last_visit[tuple(pos)] = i
	for neighbour in neighbours:
		last_visit[neighbour] = i
	pos[0] = (pos[0] + directions[dir][0]) % world_size
	pos[1] = (pos[1] + directions[dir][1]) % world_size
	i += 1

pos_dir = {}
pos = [0, 0]
i = 0
for dir in MOVES:
	pos_dir[tuple(pos)] = MOVES[i]
	pos[0] = (pos[0] + directions[dir][0]) % world_size
	pos[1] = (pos[1] + directions[dir][1]) % world_size
	i += 1



# replant_2d = [0,0,0,0,1,1,2,3,4,5,5,6,6,7,8,8,9,9,9,9]
replant_2d = [0,0,0,0,0,1,1,2,3,4,5,6,7,8,8,9,9,9,9,9]
sorting_func = {
	"North": "NorthSort",
	"East": "EastSort",
	"South": "SouthSort",
	"West": "WestSort",
	"EastNorth": "NorthEastSort",
	"EastSouth": "SouthEastSort",
	"WestSouth": "SouthWestSort",
	"WestNorth": "NorthWestSort",
	"SouthNorth": "NorthSouthSort", # doesn't exist
	"WestEast": "EastWestSort", # doesn't exist
	"EastSouthNorth": "NorthEastSouthSort",
	"WestEastSouth": "EastSouthWestSort",
	"WestSouthNorth": "SouthWestNorthSort",
	"WestEastNorth": "WestNorthEastSort",
	"WestEastSouthNorth": "simple_swap",
	"": False
}


def get_neighbours(pos, visited):
	sorting_func_name = ""
	x,y = pos
	west = (x - 1, y)
	east = (x + 1, y)
	north = (x, y + 1)
	south = (x, y - 1)
	if x > 0 and west in visited:
		sorting_func_name += "West"
	if x < world_size - 1 and east in visited:
		sorting_func_name += "East"
	if y > 0 and south in visited:
		sorting_func_name += "South"
	if y < world_size - 1 and north in visited:
		sorting_func_name += "North"
	return sorting_func[sorting_func_name]


functions = []
output_file = "state_machine.py"
pos = [0, 0]
visited = set()
replant_tolerance = 4
i = 0

def replant_9(index):
	funcns = []
	if replant_2d[index] - replant_tolerance > 0:
		funcns.append(f"\twhile measure() < {replant_2d[index] - replant_tolerance}:")
		funcns.append(f"\t\ttill()")
		funcns.append(f"\t\ttill()")
		funcns.append(f"\t\tplant(Entities.Cactus)")
	return funcns

def replant_0(index):
	funcns = []
	if replant_2d[index] + replant_tolerance < 9:
		funcns.append(f"\twhile measure() > {replant_2d[index] + replant_tolerance}:")
		funcns.append(f"\t\ttill()")
		funcns.append(f"\t\ttill()")
		funcns.append(f"\t\tplant(Entities.Cactus)")
	return funcns


for dir in MOVES:
	# print(pos)
	till = True if tuple(pos) not in visited else False
	next_dir = True if i+1 < len(MOVES) else False
	neighbours = get_neighbours(pos, visited)
	neighbours_pos = neighbour_pos(pos)
	replant_index = pos[0] + pos[1]
	replant_func = replant_0 if replant_index < world_size - 1 else replant_9
	functions.append(f"def cacti2_move_{i}(grid0, grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9):")
	if till:
		functions.append(f"\ttill()")
		functions.append(f"\tplant(Entities.Cactus)")
		functions += replant_func(replant_index)
		visited.add(tuple(pos))
	if neighbours:
		functions.append(f"\t{neighbours}()")
	for neighbour in neighbours_pos:
		if last_visit[neighbour] == i:
			measure = neighbour_order[neighbours_pos.index(neighbour)]
			# functions.append(f"\tgrid[{neighbour[0]}][{neighbour[1]}] = measure({measure})")
			functions.append(f"\tgrid{neighbour[0]}[{neighbour[1]}] = measure({measure})")
	if next_dir:
		functions.append(f"\tmove({dir})")
		functions.append(f"\tcacti2_move_{i+1}(grid0, grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9)")
	else:
		# functions.append(f"\tgrid[{pos[0]}][{pos[1]}] = measure()")
		functions.append(f"\tgrid{pos[0]}[{pos[1]}] = measure()")
		functions.append(f"\tmove({dir})")
	pos[0] = (pos[0] + directions[dir][0]) % world_size
	pos[1] = (pos[1] + directions[dir][1]) % world_size
	i += 1




# Write to file
with open(os.path.join(os.path.dirname(__file__), output_file), "w") as f:
	f.write("\n".join(functions))
