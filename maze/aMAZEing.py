from github import *

# init code here
BUSH = Entities.Bush
FERTILIZER = Items.Fertilizer

trade(Items.Fertilizer, 100)
gold_at_start = num_items(Items.Gold)
clear()

test = {
                             # mazes, resets, size
    'Development':              [  5,  20,  5],
    'Early Maze Leaderboard Q': [  3,  20, 10],
    'Early Maze Leaderboard':   [100,  20, 10],
    'Speedrun Leaderboard':     [  1, 151,  8],
}
CURRENT = 'Early Maze Leaderboard Qg'
MAZES = test[CURRENT][0]
RESETS = test[CURRENT][1]
SIZE = test[CURRENT][2]

set_farm_size(SIZE)
quick_print(CURRENT, MAZES, 'x', RESETS, '(', SIZE , 'x', SIZE, ')')

timings = []
timer_start = get_time()

#===============================================================================

def get_maze():
    while get_entity_type() != Entities.Hedge:
        if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Bush:
            use_item(Items.Fertilizer)
        else:
            harvest()
            plant(Entities.Bush) # takes 3.2 and 4.8 s
            use_item(Items.Fertilizer) # -2s
            use_item(Items.Fertilizer) # -2s
            use_item(Items.Fertilizer) # -2s or to hedge

def scout_maze():
    map = {}
    tiles_left = get_world_size()**2
    direction = 0
    directions = [North, East, South, West]
    back       = [South, West, North, East]
    treasure = None

    while tiles_left > 0:
        pos = (get_pos_x(), get_pos_y())
        if get_entity_type() == Entities.Treasure:
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
    directions = [North, East, South, West]
    move_x     = [0,     +1,   0,     -1]
    move_y     = [+1,    0,    -1,    0]
    backwards =  [South, West, North, East]
    s = get_world_size()

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
            next = ((current[0]+move_x[i])%s, (current[1]+move_y[i])%s)
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
    path = reverse(path)

    # Start moving
    for d in path:
        move(d)
        # Check for disappeared walls while we are moving
        for i in range(len(directions)):
            if maze[get_pos_x(), get_pos_y()][i] == True:
                # Wall was here
                if move(directions[i]):
                    maze[(get_pos_x(), get_pos_y())][(i+2)%4] = False # Wall is gone
                    move(backwards[i])
                    maze[(get_pos_x(), get_pos_y())][i] = False # Wall is gone


for h in range(MAZES):
    time = get_time()
    get_maze()
    maze, treasure = scout_maze()
    for r in range(RESETS):
        navi_maze(maze, treasure)
        treasure = measure()
        get_maze()
    navi_maze(maze, treasure)
    harvest()
    time = get_time() - time
    insort(timings, time)

#===============================================================================

harvest()
lap_time = get_time() - timer_start
if num_items(Items.Gold) - gold_at_start != 150000:
    quick_print("Insufficient Gold, better luck next time :)")
quick_print(
    "# aMAZEing",
    "min:", str(timings[0]),
    "max:", str(timings[-1]),
    "median:", str(median(timings)),
    "avg:", str(average(timings)),
    "time:", str(time)
)
