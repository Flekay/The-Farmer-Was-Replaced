# navi-map.py
clear()
moveto(4,4)
boot_time = get_time()
MOVES = generate_moves()
boot_time = get_time() - boot_time

run_ops = get_op_count()
for direction in MOVES:
	till()
	move(direction)
run_ops = get_op_count() - run_ops - 3 - 40000
quick_print("navi-map.py, Setup time:", str(boot_time), ", ops:", run_ops)


# move-to-next-tile.py
clear()
SIZE = get_world_size()**2
run_ops = get_op_count()
for i in range(SIZE):
	till()
	move_to_next_tile()
run_ops = get_op_count() - run_ops - 3 - 40000
quick_print("move-to-next-tile.py, ops:", run_ops)

# move-to-next-tile.py inline
clear()
SIZE = get_world_size()**2
run_ops = get_op_count()
for i in range(SIZE):
	till()
	if get_pos_x() == get_pos_y():
		move(West)
	else:
		move(North)
run_ops = get_op_count() - run_ops - 3 - 40000
quick_print("move-to-next-tile.py inline, ops:", run_ops)


# navi-to-next-tile.py
clear()
SIZE = get_world_size()**2
boot_time = get_time()
next_tile = navi_to_next_tile()
boot_time = get_time() - boot_time

run_ops = get_op_count()
for i in range(SIZE):
	till()
	move(next_tile[get_pos_x()][get_pos_y()])
run_ops = get_op_count() - run_ops - 3 - 40000
quick_print("navi-to-next-tile.py, Setup time:", str(boot_time), ", Run time:", run_ops)
