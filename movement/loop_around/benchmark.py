# map_adv.py
clear()
boot_time = get_tick_count()
# movement/loop_around/map_adv.py
from map_adv import MOVES
boot_time = get_tick_count() - boot_time

run_ops = get_tick_count()
for direction in MOVES:
	till()
	move(direction)
run_ops = get_tick_count() - run_ops - 40000
quick_print("map_adv.py, Setup time:", boot_time, ", ops:", run_ops)


# map_inline.py
clear()
SIZE = get_world_size()
boot_time = get_tick_count()
# movement/loop_around/map_inline.py
from map_inline import MOVES
boot_time = get_tick_count() - boot_time

run_ops = get_tick_count()
for _ in range(SIZE):
	for direction in MOVES:
		till()
		move(direction)
run_ops = get_tick_count() - run_ops - 40000
quick_print("map_inline.py, Setup time:", boot_time, ", ops:", run_ops)


# map_light.py
clear()
boot_time = get_tick_count()
# movement/loop_around/map_light.py
from map_light import MOVES
boot_time = get_tick_count() - boot_time

run_ops = get_tick_count()
for direction in MOVES:
	till()
	move(direction)
run_ops = get_tick_count() - run_ops - 40000
quick_print("map_light.py, Setup time:", boot_time, ", ops:", run_ops)


# move_to_next_tile.py
clear()
boot_time = get_tick_count()
# movement/loop_around/move_to_next_tile.py
from move_to_next_tile import move_to_next_tile
boot_time = get_tick_count() - boot_time
SIZE = get_world_size()**2
run_ops = get_tick_count()
for i in range(SIZE):
	till()
	move_to_next_tile()
run_ops = get_tick_count() - run_ops - 40000
quick_print("move_to_next_tile.py, Setup time:", boot_time, ", ops:", run_ops)


# navi_to_next_tile.py
clear()
boot_time = get_tick_count()
# movement/loop_around/navi_to_next_tile.py
from navi_to_next_tile import navi_to_next_tile
boot_time = get_tick_count() - boot_time
SIZE = get_world_size()**2
run_ops = get_tick_count()
for i in range(SIZE):
	till()
	navi_to_next_tile()
run_ops = get_tick_count() - run_ops - 40000
quick_print("navi_to_next_tile.py, Setup time:", boot_time, ", ops:", run_ops)
