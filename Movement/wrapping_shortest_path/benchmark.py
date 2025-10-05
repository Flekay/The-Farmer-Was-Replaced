from string import string

# Randomly generated test positions
SPOTS = (
	(5,0),(2,0),(3,5),(8,9),(6,6),(6,6),
	(3,0),(4,7),(9,7),(5,3),(7,9),(9,4),
	(6,7),(4,4),(2,6),(1,5),(6,8),(2,0),
	(0,1),(4,2),(8,7),(4,7),(8,2),(6,4),
	(2,7),(5,8),(0,2),(8,0),(0,8),(6,6),
)

names = []
files = []
timings = []

# movement/wrapping_shortest_path/gen_move_to.py
boot_time = get_time()
import gen_move_to
timings.append(get_time() - boot_time)
files.append(gen_move_to.move_to)
names.append("gen_move_to.py")

# movement/wrapping_shortest_path/move_to.py
boot_time = get_time()
import move_to
timings.append(get_time() - boot_time)
files.append(move_to.move_to)
names.append("move_to.py")

# movement/wrapping_shortest_path/navi_to_deltalist.py
boot_time = get_time()
import navi_to_deltalist
timings.append(get_time() - boot_time)
files.append(navi_to_deltalist.move_to)
names.append("navi_to_deltalist.py")

# movement/wrapping_shortest_path/navi_to_dict.py
boot_time = get_time()
import navi_to_dict
timings.append(get_time() - boot_time)
files.append(navi_to_dict.move_to)
names.append("navi_to_dict.py")

# movement/wrapping_shortest_path/navi_to_list.py
boot_time = get_time()
import navi_to_list
timings.append(get_time() - boot_time)
files.append(navi_to_list.move_to)
names.append("navi_to_list.py")


# Run tests for x,y based movement
for i in range(len(files)):
	move_to = files[i]
	clear()
	run_ops = get_tick_count()

	for pos in SPOTS:
		x,y = pos
		move_to(x,y)
		if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
			quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
			break

	# minus mandatory operations (164 moves, verify position, for loop)
	run_ops = get_tick_count() - run_ops - 32800 - 240 - 1
	quick_print(names[i], "Booted in", string(timings[i]), "seconds and ran in", run_ops, "operations")












names = []
files = []
timings = []

# movement/wrapping_shortest_path/navi_pos_to_pos_func.py
boot_time = get_time()
import navi_pos_to_pos_func
timings.append(get_time() - boot_time)
files.append(navi_pos_to_pos_func.move_to_pos)
names.append("navi_pos_to_pos_func.py")

# movement/wrapping_shortest_path/navi_pos_to_pos.py
boot_time = get_time()
import navi_pos_to_pos
timings.append(get_time() - boot_time)
files.append(navi_pos_to_pos.move_to_pos)
names.append("navi_pos_to_pos.py")


# Run tests for position based movement
for i in range(len(files)):
	move_to = files[i]
	clear()
	run_ops = get_tick_count()

	for pos in SPOTS:
		move_to(pos, (get_pos_x(), get_pos_y()))
		if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
			quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
			break

	# minus mandatory operations (164 moves, verify position, for loop)
	run_ops = get_tick_count() - run_ops - 32800 - 240 - 1
	quick_print(names[i], "Booted in", string(timings[i]), "seconds and ran in", run_ops, "operations")
