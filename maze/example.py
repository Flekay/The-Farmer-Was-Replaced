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
