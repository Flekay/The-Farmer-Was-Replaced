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

# globals bfs
BASE = (4, 4)
PATH = init_path()
DIR_TO_BASE = {BASE: None}
DIST_TO_BASE = init_dist_to_base()
queuepos = []
queued = {}

# globals scan
WALL = init_wall()
PATH = init_path()
TREASURE_POS = {0: BASE}
FERTILIZER = Items.Fertilizer
TILE_NORTH = tile_north()
TILE_EAST = tile_east()
TILE_SOUTH = tile_south()
TILE_WEST = tile_west()

# globals path
DPOS = generate_dpos()

def generate_dpos():
	dpos = {}
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			dpos[(x, y)] = {North: (x, y + 1), South: (x, y - 1), East: (x + 1, y), West: (x - 1, y)}
	return dpos

# globals pro-max
OPP = {North: South, East: West, South: North, West: East}
BUSH = Entities.Bush

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
		PATH = init_path()
		WALL = init_wall()
		DIST_TO_BASE = init_dist_to_base()
		DIR_TO_BASE = {BASE: None}
		TREASURE_POS = {0: BASE}


		#===============================================================================
		## DO NOT CHANGE
		gold_at_start = num_items(Items.Gold)
		timer_start = get_tick_count()
		clear()
		#===============================================================================
		## Build maze
		move_to_pos(BASE)
		plant(BUSH)
		while get_entity_type() == BUSH:
			use_item(FERTILIZER)

		## Maze solving code here!
		pro_max(CHEST_COUNT)

		#===============================================================================
		## DO NOT CHANGE
		lap_time = (get_tick_count() - timer_start) / OPS
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
## Helper functions go here!


def pro_max(iterations=300):
	# Map the maze
	scan_north()
	scan_east()
	scan_south()
	scan_west()
	pro_max_bfs(BASE)


	# Solve the maze
	goal = TREASURE_POS[0]
	gpath = []
	ddpath = []
	dir = DIR_TO_BASE[goal]
	while dir:
		gpath.insert(0, OPP[dir])
		ddpath.append(dir)
		goal = DPOS[goal][dir]
		dir = DIR_TO_BASE[goal]

	# Follow the goal path backward
	for step in gpath:
		move(step)

	for i in range(iterations - 1):
		# Compute paths from drone to base
		dpath = ddpath
		# Recycle treasure
		goal = measure()
		while measure():
			use_item(FERTILIZER)
		# Compute paths from goal to base
		gpath = []
		dir = DIR_TO_BASE[goal]
		while dir:
			gpath.append(dir)
			goal = DPOS[goal][dir]
			dir = DIR_TO_BASE[goal]
		ddpath = gpath + []
		# Cancel the final moves if they're the same
		while dpath and gpath and dpath[-1] == gpath[-1]:
			gpath.pop()
			dpath.pop()
		# Follow the drone path forward
		for step in dpath:
			move(step)
			for func in WALL[get_pos_x(), get_pos_y()]:
				func()
		# Follow the goal path backward
		for step in gpath[::-1]:
			move(OPP[step])
			for func in WALL[get_pos_x(), get_pos_y()]:
				func()
	# Harvest the treasure
	harvest()
