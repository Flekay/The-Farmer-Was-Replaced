# pro-max  41411 + 988
# this     40725 + 32
clear()
move_to(4,4)
plant(Entities.Bush)
use_item(Items.Weird_Substance, 100)

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
TREASURE_POS = {}
DIST_TO_BASE = {}
DIST_TO_BASE[44] = 0
DIR_TO_BASE = {}
DIR_TO_BASE[44] = False
direction_values = {North: +10, South: -10, East: +1, West: - 1}
OPP = {North: South, South: North, East: West, West: East}
gpath = []
tpath = [0]
dpath = []

# scan the map
scan_4_4(false, false, false, false, 0)

# Solve the maze
goal = TREASURE_POS[0]
dir = DIR_TO_BASE[goal]
while dir:
	tpath.append(dir)
	goal += direction_values[dir]
	dir = DIR_TO_BASE[goal]

# Follow the goal path backward
for step in tpath[:0:-1]:
	move(OPP[step])

for i in range(299):
	dpath = tpath
	gpath = [i]

	x,y = measure()
	goal = x + 10 * y
	use_item(Items.Weird_Substance, 100)

	dir = DIR_TO_BASE[goal]
	while dir:
		gpath.append(dir)
		goal += direction_values[dir]
		dir = DIR_TO_BASE[goal]

	tpath = gpath + []

	while dpath[-1] == gpath[-1]:
		gpath.pop()
		dpath.pop()

	dpath.pop(0)
	for dir in dpath:
		move(dir)

	for dir in gpath[:0:-1]:
		move(OPP[dir])
harvest()