# general/string/string.py
from string import string
# goto.py
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
boot_time = get_time()
# movement/non_wrapping_shortest_path/goto.py
from goto import goto
boot_time = get_time() - boot_time
run_ops = get_tick_count()

for pos in SPOTS:
	x, y = pos
	goto(x, y)
	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_tick_count() - run_ops - 32800 - 240 - 1
quick_print("goto.py, Setup time:", string(boot_time), ", ops:", run_ops)


# goto-local.py
clear()
boot_time = get_time()
# movement/non_wrapping_shortest_path/goto_local.py
from runto_local import *
boot_time = get_time() - boot_time

run_ops = get_tick_count()

for pos in SPOTS:

	runto(pos)

	if get_pos_x() != pos[0] or get_pos_y() != pos[1]:
		quick_print("Target missed! Expected:", pos, "Actual:", (get_pos_x(), get_pos_y()))
		break

run_ops = get_tick_count() - run_ops - 32800 - 240 - 1
quick_print("runto-local.py, Setup time:", string(boot_time), ", ops:", run_ops)
