import os

def generate_bfs_functions():
	directions = ['north', 'east', 'south', 'west']
	grid_size = 10

	for x in range(grid_size):
		for y in range(grid_size):
			function_name = f"bfs_{x}_{y}"
			bDirList = []

			# Generate move checks for each direction
			move_checks = []
			for i, d in enumerate(directions):
				next_x, next_y = x, y
				if d == 'north': next_y += 1
				elif d == 'east': next_x += 1
				elif d == 'south': next_y -= 1
				elif d == 'west': next_x -= 1

				opposite_dir = directions[(i + 2) % 4]
				if 0 <= next_x < grid_size and 0 <= next_y < grid_size:
					bDirList.append(f"b{d.capitalize()}")
					move_checks.append(
						f"	b{d.capitalize()} = lb{opposite_dir.capitalize()}(nop, bfs_{d})(bfs_{next_x}_{next_y})")
				else:
					bDirList.append("false")

			# Generate function code
			params = ", ".join([f"lb{d.capitalize()}" for d in directions])
			func_code = f"""def {function_name}({params}):
{chr(10).join(move_checks)}
	grid{x}[{y}] = [{", ".join(bDirList)}]"""
			yield func_code

def write_bfs_functions_to_file(filename):
	with open(os.path.join(os.path.dirname(__file__), filename), 'w') as file:
		for function_code in generate_bfs_functions():
			file.write(function_code + "\n")

write_bfs_functions_to_file('generated_bfs_functions.py')






grid = {}
grid[0] = {}
grid[1] = {}
grid[2] = {}
grid[3] = {}
grid[4] = {}
grid[5] = {}
grid[6] = {}
grid[7] = {}
grid[8] = {}
grid[9] = {}
grid0 = grid[0]
grid1 = grid[1]
grid2 = grid[2]
grid3 = grid[3]
grid4 = grid[4]
grid5 = grid[5]
grid6 = grid[6]
grid7 = grid[7]
grid8 = grid[8]
grid9 = grid[9]

# grid = {0:{7:[true,true,false,false],8:[true,false,true,false],9:[false,true,true,false],6:[false,false,true,false],5:[true,true,false,false],4:[false,true,true,false],0:[false,true,false,false],1:[true,true,false,false],2:[true,false,true,false],3:[true,true,true,false]},1:{8:[false,true,false,false],6:[true,true,false,false],7:[false,false,true,true],9:[false,true,false,true],5:[false,false,true,true],4:[true,false,false,true],2:[false,false,true,false],0:[true,true,false,true],1:[true,false,true,true],3:[false,true,false,true]},2:{8:[false,false,true,true],7:[true,true,false,false],4:[true,false,false,false],5:[false,true,true,false],6:[false,true,false,true],9:[false,true,false,true],0:[false,true,false,true],3:[false,true,false,true],2:[false,true,true,false],1:[true,true,false,false]},3:{7:[false,true,false,true],5:[true,false,false,true],6:[false,false,true,true],9:[false,false,true,true],8:[true,true,false,false],4:[false,false,true,false],0:[false,false,false,true],3:[true,false,true,true],2:[true,false,false,true],1:[false,true,false,true]},4:{7:[false,false,true,true],8:[true,false,false,true],9:[false,true,true,false],6:[true,true,true,false],5:[true,false,true,false],1:[false,false,true,true],0:[true,true,false,false],2:[true,true,false,false],3:[true,false,true,false],4:[true,false,true,false]},5:{9:[false,true,false,true],8:[false,true,true,false],7:[true,false,true,false],6:[true,false,false,true],0:[false,true,false,true],5:[false,true,false,false],4:[false,true,true,false],3:[true,true,false,false],1:[true,true,false,false],2:[false,false,true,true]},6:{9:[false,false,true,true],8:[true,false,false,true],0:[false,true,false,true],7:[false,true,true,false],6:[true,false,true,false],5:[true,false,true,true],4:[true,false,false,true],3:[false,false,true,true],2:[true,false,true,false],1:[true,false,false,true]},7:{6:[false,false,true,false],5:[true,false,true,false],4:[true,false,true,false],3:[true,false,true,false],2:[true,false,true,false],1:[true,false,true,false],0:[true,true,false,true],9:[false,true,true,false],8:[true,false,true,false],7:[true,false,false,true]},8:{8:[false,false,true,false],0:[true,true,false,true],1:[false,true,true,false],2:[true,true,false,false],3:[true,false,true,false],4:[true,false,true,false],5:[false,true,true,false],6:[true,true,false,false],7:[true,true,true,false],9:[false,true,false,true]},9:{4:[false,false,true,false],3:[true,false,true,false],0:[false,false,false,true],1:[true,false,false,true],2:[true,false,true,true],5:[true,false,false,true],6:[false,false,true,true],7:[true,false,false,true],8:[true,false,true,false],9:[false,false,true,true]}}



def bfs_north(pos, dist):
	pos = TILE_NORTH[pos]
	if dist < DIST_TO_BASE[pos]:
		DIST_TO_BASE[pos] = dist
		DIR_TO_BASE[pos] = South
		pro_max_bfs(pos, dist)

def bfs_east(pos, dist):
	pos = TILE_EAST[pos]
	if dist < DIST_TO_BASE[pos]:
		DIST_TO_BASE[pos] = dist
		DIR_TO_BASE[pos] = West
		pro_max_bfs(pos, dist)


def bfs_south(pos, dist):
	pos = TILE_SOUTH[pos]
	if dist < DIST_TO_BASE[pos]:
		DIST_TO_BASE[pos] = dist
		DIR_TO_BASE[pos] = North
		pro_max_bfs(pos, dist)

def bfs_west(pos, dist):
	pos = TILE_WEST[pos]
	if dist < DIST_TO_BASE[pos]:
		DIST_TO_BASE[pos] = dist
		DIR_TO_BASE[pos] = East
		pro_max_bfs(pos, dist)

def pro_max_bfs(pos, dist):
	for func in PATH[pos]:
		func(pos, dist+1)





DIST_TO_BASE = {}
DIR_TO_BASE = {}

def true(a, b):
	return a

def false(a, b):
	return b

def bfs_4_4(dist=999):
	# tile = grid4[4] # 4:4:[true,false,true,false] # true = path, false = wall
	# index = 4*10 + 4
