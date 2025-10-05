def wait():
	while num_drones() > 1:
		continue

def row():
	for _ in range(get_world_size()):
		till()
		move(North)


# for_all.py
clear()
# movement/line_formation/for_all.py
from for_all import for_all

runtime = get_tick_count()
for_all(row)
runtime = get_tick_count() - runtime

wait_time = get_tick_count()
wait()
wait_time = get_tick_count() - wait_time
quick_print("for_all.py, Runtime:", runtime, ", wait time:", wait_time)



# for_all_dual.py
clear()
# movement/line_formation/for_all_dual.py
from for_all_dual import for_all

runtime = get_tick_count()
for_all(row)
runtime = get_tick_count() - runtime

wait_time = get_tick_count()
wait()
wait_time = get_tick_count() - wait_time
quick_print("for_all_dual.py, Runtime:", runtime, ", wait time:", wait_time)
