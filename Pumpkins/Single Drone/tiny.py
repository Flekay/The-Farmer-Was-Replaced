# movement/loop_around/map_light.py
from map_light import MOVES

clear()
# Till the entire field and plant initial pumpkins
for dir in MOVES:
	till()
	plant(Entities.Pumpkin)
	move(dir)

# Main farming loop
while True:
	for dir in MOVES:
		if can_harvest():
			harvest()
		else:
			plant(Entities.Pumpkin)
		move(dir)
