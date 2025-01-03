# move-to.py
clear()
# True Random Number Generator
# https://www.random.org/
SPOTS = [
	(5,0),(2,0),(3,5),(8,9),(6,6),(6,6),
	(3,0),(4,7),(9,7),(5,3),(7,9),(9,4),
	(6,7),(4,4),(2,6),(1,5),(6,8),(2,0),
	(0,1),(4,2),(8,7),(4,7),(8,2),(6,4),
	(2,7),(5,8),(0,2),(8,0),(0,8),(6,6),
]
run_ops = get_tick_count()

for pos in SPOTS:
	x,y = pos
	move_to(x,y)
	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_tick_count() - run_ops - 32800 - 240 - 1 # minus mandatory operations (164 moves, verify position, for loop)
quick_print("move-to.py, ops:", run_ops)


# navi-to-dict.py
clear()
boot_time = get_time()
move_x, move_y = loadData(get_world_size())
boot_time = get_time() - boot_time

run_ops = get_tick_count()

for pos in SPOTS:

	x, y = pos
	navi_to_dict(x, y)

	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_tick_count() - run_ops - 32800 - 240 - 1
quick_print("navi-to-dict.py, Setup time:", str(boot_time), ", ops:", run_ops)


# navi-to-list.py
clear()
boot_time = get_time()
move_x, move_y = loadDataList(get_world_size())
boot_time = get_time() - boot_time

run_ops = get_tick_count()

for pos in SPOTS:

	x, y = pos
	navi_to_list(x, y)

	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_tick_count() - run_ops - 32800 - 240 - 1
quick_print("navi-to-list.py, Setup time:", str(boot_time), ", ops:", run_ops)


# navi-to-list.py - known positions
clear()
boot_time = get_time()
move_x = (
	(),
	[East],
	(East, East),
	(East, East, East),
	(East, East, East, East),
	(West, West, West, West, West),
	(West, West, West, West),
	(West, West, West),
	(West, West),
	[West],
)
move_y = (
	(),
	[North],
	(North, North),
	(North, North, North),
	(North, North, North, North),
	(South, South, South, South, South),
	(South, South, South, South),
	(South, South, South),
	(South, South),
	[South],
)
boot_time = get_time() - boot_time

run_ops = get_tick_count()
tx = 0
ty = 0

for pos in SPOTS:

	x, y = pos
	navi_to_list(x, y, tx, ty)
	tx = x
	ty = y

	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_tick_count() - run_ops - 32800 - 240 - 1
quick_print("navi-to-list.py - known positions, Setup time:", str(boot_time), ", ops:", run_ops)


# navi-pos-to-pos.py
clear()
boot_time = get_time()
navi_to_pos = generate_path_map(get_world_size())
boot_time = get_time() - boot_time

run_ops = get_tick_count()

for pos in SPOTS:
	for moves in navi_to_pos[(get_pos_x(),get_pos_y())][pos]:
		move(moves)
	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_tick_count() - run_ops - 32800 - 240 - 1
quick_print("navi-pos-to-pos.py, Setup time:", str(boot_time), ", ops:", run_ops)


# navi-pos-to-pos-func.py
clear()
boot_time = get_time()
navi_to_func_pos = generate_path_func_map(get_world_size())
boot_time = get_time() - boot_time

run_ops = get_tick_count()

for pos in SPOTS:
	navi_to_func_pos[(get_pos_x(),get_pos_y())][pos]()
	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_tick_count() - run_ops - 32800 - 240 - 1
quick_print("navi-pos-to-pos-func.py, Setup time:", str(boot_time), ", ops:", run_ops)



# gen-move-to.py
clear()
boot_time = get_time()
move_to = gen_move_to()
boot_time = get_time() - boot_time

run_ops = get_tick_count()

for pos in SPOTS:
	x,y = pos
	move_to(x, y)
	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break
run_ops = get_tick_count() - run_ops - 32800 - 240 - 1
quick_print("gen-move-to.py, Setup time:", str(boot_time), ", ops:", run_ops)
