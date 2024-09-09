# move-to.py
clear()
# True Random Number Generator
# https://www.random.org/
SPOTS = [
	(5,0),(2,0),(3,5),(8,9),(6,6),(6,6),
	(3,0),(4,7),(9,7),(5,3),(7,9),(9,4),
	(6,7),(4,4),(2,6),(1,5),(6,8),(2,0),
	(0,1),(4,2),(8,7),(4,7),(8,2),(6,4),
	(2,7),(5,8),(0,2),(8,0),(0,8),(6,6)
]
run_ops = get_op_count()

for pos in SPOTS:
	move_to_pos(pos)
	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_op_count() - run_ops - 32800 - 450 - 3 # minus mandatory operations (164 moves, verify position, op count)
quick_print("move_to_pos, ops:", run_ops)


# navi-to.py
clear()
boot_time = get_time()
move_x2, move_y2 = loadData(get_world_size())
boot_time = get_time() - boot_time

run_ops = get_op_count()

for pos in SPOTS:

	# this is the same as
	pos_x, pos_y = pos
	navi_to(pos_x, pos_y)
	# this
	navi_to_pos(pos)

	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_op_count() - run_ops - 32800 - 450 - 3
quick_print("navi-map.py, Setup time:", str(boot_time), ", ops:", run_ops)


# navi-to-pos.py
clear()
boot_time = get_time()
navi_to_pos = generate_path_map(get_world_size())
boot_time = get_time() - boot_time
current_pos = (get_pos_x(), get_pos_y())

run_ops = get_op_count()

for pos in SPOTS:
	for moves in navi_to_pos[current_pos][pos]:
		move(moves)
	current_pos = pos
	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_op_count() - run_ops - 32800 - 450 - 3
quick_print("navi-map.py, Setup time:", str(boot_time), ", ops:", run_ops)


# navi-to-func.py
clear()
boot_time = get_time()
navi_to_func_pos = generate_path_func_map(get_world_size())
boot_time = get_time() - boot_time
current_pos = (get_pos_x(), get_pos_y())

run_ops = get_op_count()

for pos in SPOTS:
	navi_to_func_pos[current_pos][pos]()
	current_pos = pos
	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_op_count() - run_ops - 32800 - 450 - 3
quick_print("navi-map.py, Setup time:", str(boot_time), ", ops:", run_ops)
