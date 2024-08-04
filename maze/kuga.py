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
	maze, treasure = scout_maze()

	# navi the maze x times
	for i in range(iterations-1):
		navi_maze(maze, treasure)
		treasure = measure()

		# recycle treasure
		while measure():
			use_item(FERTILIZER)
	navi_maze(maze, treasure)
	harvest()

def scout_maze():
	map = {}
	tiles_left  = get_world_size()**2
	direction   = 0
	directions  = [North, East, South, West]
	back        = [South, West, North, East]
	treasure    = None

	while tiles_left > 0:
		pos = (get_pos_x(), get_pos_y())
		if measure():
			treasure = pos
		if not pos in map:
			map[pos] = []
			for i in range(len(directions)):
				is_open = move(directions[i])
				if is_open:
					move(back[i])
				# quick_print('Scanning', directions[i], 'is wall:', not is_open)
				map[pos].append(not is_open)
			tiles_left -= 1
		for next in [1, 0, 3, 2]:
			new = (direction + next) % 4 # 4 directions
			if move([North, East, South, West][new]):
				direction = new
				break
	return map, treasure

def navi_maze(maze, treasure):
	directions  = [North, East, South, West]
	move_x      = [0,     +1,   0,     -1]
	move_y      = [+1,    0,    -1,    0]
	backwards   =  [South, West, North, East]
	world_size  = get_world_size()

	# Check for disappeared wall in start position!
	for i in range(len(directions)):
		if maze[(get_pos_x(), get_pos_y())][i] == True:
			# Wall was here
			if move(directions[i]):
				maze[(get_pos_x(), get_pos_y())][(i+2)%4] = False # Wall is gone
				move(backwards[i])
				maze[(get_pos_x(), get_pos_y())][i] = False # Wall is gone

	start = ((get_pos_x(), get_pos_y()))
	frontier = [start]
	came_from = {start:None} # Stores path (with direction) A--B[1]-->B[0]
	came_from_dir = {start:None}

	# A* to fill came_from
	while len(frontier) != 0:
		current = frontier.pop()
		for i in range(len(directions)):
			if maze[current][i] == True:
				continue # We still cannot go that way
			next = ((current[0]+move_x[i])%world_size, (current[1]+move_y[i])%world_size)
			if next not in came_from:
				frontier.insert(0, next)
				came_from[next] = current
				came_from_dir[next] = directions[i]
	# draw_maze(maze, start, treasure, came_from, came_from_dir)

	# Follow the path back
	current = treasure
	path = []
	while current != start:
		path.append(came_from_dir[current])
		current = came_from[current]

	# Start moving
	for d in path[::-1]:
		move(d)
		# Check for disappeared walls while we are moving
		for i in range(len(directions)):
			if maze[get_pos_x(), get_pos_y()][i] == True:
				# Wall was here
				if move(directions[i]):
					maze[(get_pos_x(), get_pos_y())][(i+2)%4] = False # Wall is gone
					move(backwards[i])
					maze[(get_pos_x(), get_pos_y())][i] = False # Wall is gone
					
