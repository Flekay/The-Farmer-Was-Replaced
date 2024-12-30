# map-adv.py
clear()
boot_time = get_tick_count()
MOVES = generate_moves()
boot_time = get_tick_count() - boot_time

run_ops = get_tick_count()
for direction in MOVES:
	till()
	move(direction)
run_ops = get_tick_count() - run_ops - 40000
quick_print("map-adv.py, Setup time:", boot_time, ", ops:", run_ops)


# map-inline.py
clear()
SIZE = get_world_size()
boot_time = get_tick_count()
MOVES = generate_moves_inline()
boot_time = get_tick_count() - boot_time

run_ops = get_tick_count()
for _ in range(SIZE):
	for direction in MOVES:
		till()
		move(direction)
run_ops = get_tick_count() - run_ops - 40000
quick_print("map-inline.py, Setup time:", boot_time, ", ops:", run_ops)


# map-light.py
clear()
boot_time = get_tick_count()
MOVES = generate_moves_light()
boot_time = get_tick_count() - boot_time

run_ops = get_tick_count()
for direction in MOVES:
	till()
	move(direction)
run_ops = get_tick_count() - run_ops - 40000
quick_print("map-light.py, Setup time:", boot_time, ", ops:", run_ops)


# move-to-next-tile.py
clear()
SIZE = get_world_size()**2
run_ops = get_tick_count()
for i in range(SIZE):
	till()
	move_to_next_tile()
run_ops = get_tick_count() - run_ops - 40000
quick_print("move-to-next-tile.py, ops:", run_ops)


# navi-to-next-tile.py
clear()
SIZE = get_world_size()**2
boot_time = get_tick_count()
next_tile = navi_to_next_tile()
boot_time = get_tick_count() - boot_time

run_ops = get_tick_count()
for i in range(SIZE):
	till()
	move(next_tile[get_pos_x()][get_pos_y()])
run_ops = get_tick_count() - run_ops - 40000
quick_print("navi-to-next-tile.py, Setup time:", boot_time, ", Run time:", run_ops)
