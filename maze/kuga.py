#===============================================================================
## Configurations
CATEGORY = "early"           # early, mid, late, speedrun
MAZE_COUNT = 100             # minimum 100 for leaderboard submission
TRIM = True                  # Shifts current window to the right
ONLY_PRINT_HIGHSCORE = True  # Only print if it's a new highscore
PRINT_CURRENT_LAPS = True    # Print the current laps for each maze
MINUTES_TO_RUN = 10          # Run for at least this many minutes


#===============================================================================
## Initialization code goes here!
# This code is run once at the start of the run
BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer
OPEN = 'O' # Open direction will remain open
WALL = 'W' # Wall can open and need to be checked
BORDER = 'B' # Fixed border. Will never open, no need to check
directions = [North, East, South, West]
back       = [South, West, North, East]
move_x     = [0,     +1,   0,     -1]
move_y     = [+1,    0,    -1,    0]
s = get_world_size()
l = s - 1
treasure = [None]
maze = {} # a map of lists with OPEN, WALL or BORDER for each dir.


#===============================================================================
## DO NOT CHANGE
LEADERBOARDS = {
	# "name":     [chest_count, size]
	"early":      [         20,   10],
	"mid":        [        100,   10],
	"late":       [        300,   10],
	"speedrun":   [        151,    8],
}
SIZE_NAME = "(" + str(LEADERBOARDS[CATEGORY][1],0) + "x" + str(LEADERBOARDS[CATEGORY][1],0) + ")"
NAME = CATEGORY + " maze 1x" + str(LEADERBOARDS[CATEGORY][0],0) + SIZE_NAME
CHEST_COUNT = LEADERBOARDS[CATEGORY][0]
SIZE = LEADERBOARDS[CATEGORY][1]
EXPECTED_GOLD = CHEST_COUNT * (SIZE ** 2) * num_unlocked(Unlocks.Mazes)
OPS = 400 * (1 + min(num_unlocked(Unlocks.Speed), 20)) * (1 + (num_items(Items.Power) > 0))
SPACER = ""
for i in range(22):
	SPACER += "~"
SPACER_HS = SPACER + " NEW HIGHSCORE " + SPACER
SPACER = SPACER + "~~~~~~~~~~~~~~~" + SPACER
maze_stats = {"window": [], "highscore": {"average": 9999, "median": 9999, "min": 9999, "max": 0}}
lap_count = 0
runtime = get_time()
set_farm_size(SIZE)
while get_time() - runtime < MINUTES_TO_RUN * 60:
	for i in range(MAZE_COUNT):
		lap_count += 1
#===============================================================================
		#===============================================================================
		## Reset code goes here!
		# This code is run before each maze
		# and does not count towards the timer


		#===============================================================================
		## DO NOT CHANGE
		gold_at_start = num_items(Items.Gold)
		timer_start = get_op_count()
		clear()
		#===============================================================================
		## Maze solving code here!
		# you can use a function
		# or write your code directly here
		do_maze(CHEST_COUNT)


		#===============================================================================
		## DO NOT CHANGE
		lap_time = (get_op_count() - timer_start) / OPS
		actual_gold = num_items(Items.Gold) - gold_at_start
		if actual_gold != EXPECTED_GOLD:
			quick_print("Expected to get", EXPECTED_GOLD, "gold, actually got", actual_gold, "gold.")
			break
		else:
			maze_stats["window"].append(lap_time)
			while TRIM and len(maze_stats["window"]) > MAZE_COUNT:
				maze_stats["window"].pop(0)
			maze_window_stats = {
				"min": min(maze_stats["window"]),
				"max": max(maze_stats["window"]),
				"median": median(maze_stats["window"]),
				"average": average(maze_stats["window"])
			}
			if ONLY_PRINT_HIGHSCORE:
				new_highscore = False
			else:
				new_highscore = True

			if lap_time < maze_stats["highscore"]["min"]:
				maze_stats["highscore"]["min"] = lap_time
				new_highscore = True
			if lap_time > maze_stats["highscore"]["max"]:
				maze_stats["highscore"]["max"] = lap_time
				new_highscore = True
			if maze_window_stats["median"] < maze_stats["highscore"]["median"]:
				maze_stats["highscore"]["median"] = maze_window_stats["median"]
				new_highscore = True
			if maze_window_stats["average"] < maze_stats["highscore"]["average"]:
				maze_stats["highscore"]["average"] = maze_window_stats["average"]
				new_highscore = True

			if (new_highscore and lap_count > MAZE_COUNT) or (lap_count == MAZE_COUNT):
				if new_highscore and ONLY_PRINT_HIGHSCORE:
					quick_print(SPACER_HS)
				else:
					quick_print(SPACER)
				quick_print(NAME, "mazes", len(maze_stats["window"]), "of", MAZE_COUNT, "(" + str(lap_count,0) + " laps)")
				quick_print("Highscores:")
				if TRIM:
					quick_print("Best Average per Window:", str(maze_stats["highscore"]["average"]) + "s")
					quick_print("Best Median per Window:", str(maze_stats["highscore"]["median"]) + "s")
				else:
					quick_print("Average:", str(maze_window_stats["average"]) + "s")
					quick_print("Median:", str(maze_window_stats["median"]) + "s")
				quick_print("Best Lap Time:", str(maze_stats["highscore"]["min"]) + "s")
				quick_print("Worst lap Time:", str(maze_stats["highscore"]["max"]) + "s")

				quick_print(SPACER)
				quick_print("Current Window:")
				if PRINT_CURRENT_LAPS:
					quick_print("Laps:", maze_stats["window"])
				quick_print(maze_window_stats)
				quick_print(SPACER)
		#===============================================================================
		## Reset code or custom statistics code goes here!


#===============================================================================
## Helper functions
def do_maze(iterations=100):
	# setup the maze!
	plant(BUSH)
	while get_entity_type() == BUSH:
		use_item(FERTILIZER)

	# scout the maze
	scout_maze()

	# navi the maze x times
	for i in range(iterations-1):
		navi_maze()
		treasure[0] = measure()

		# recycle treasure
		while measure():
			use_item(FERTILIZER)
	navi_maze()
	harvest()

def scout_tile(recursive = False):
    pos = (get_pos_x(), get_pos_y())
    for i in range(len(directions)):
        if maze[pos][i] == WALL: # Try if open.
            if move(directions[i]):
                maze[pos][i] = OPEN
                probed_tile = (get_pos_x(), get_pos_y())
                maze[probed_tile][(i+2)%4] = OPEN
                if recursive:
                    scout_tile(recursive)
                move(back[i])
    if Entities.Treasure == get_entity_type():
        treasure[0] = pos

def scout_maze():
    # Init maze
    for x in range(s):
        for y in range(s):
                      #  [North, East, South, West]
            maze[(x,y)] = [WALL, WALL, WALL, WALL]
            if y == 0: # bottom row
                maze[(x,y)][2] = BORDER
            elif y == l: # top row
                maze[(x,y)][0] = BORDER
            if x == 0: # left column
                maze[(x,y)][3] = BORDER
            elif x == l: # right column
                maze[(x,y)][1] = BORDER
    treasure[0] = None
    scout_tile(True)

def navi_maze():
    # Check for disappeared wall in start position!
    scout_tile(False)

    start = ((get_pos_x(), get_pos_y()))
    frontier = [start]
    came_from = {start:None} # Stores path (with direction) A--B[1]-->B[0]
    came_from_dir = {start:None}

    # A* to fill came_from
    while len(frontier) != 0:
        current = frontier.pop()
        for i in range(len(directions)):
            if maze[current][i] != OPEN:
                continue # We can go that way
            next = ((current[0]+move_x[i])%s, (current[1]+move_y[i])%s)
            if next not in came_from:
                came_from[next] = current
                came_from_dir[next] = directions[i]
                if next == treasure[0]:
                    # We found goal. Break loops
                    frontier = []
                    break
                frontier.insert(0, next)

    # draw_maze(maze, start, treasure[0], came_from, came_from_dir)

    # Follow the path back
    current = treasure[0]
    path = []
    while current != start:
        path.append(came_from_dir[current])
        current = came_from[current]
    path = reverse(path)

    # Start moving
    for d in path:
        move(d)
        # Check for disappeared walls while we are moving
        scout_tile(False)
        # TODO we could replan once we find a new open path
