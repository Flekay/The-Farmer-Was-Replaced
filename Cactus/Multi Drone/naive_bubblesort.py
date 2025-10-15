def zero_zero():
	for i in range(get_pos_y()):
		move(South)
	
	for i in range(get_pos_x()):
		move(West)

def sort_vert():
	sorted = False
	while not sorted:
		sorted = True
		for i in range(get_world_size()):
			s = measure()
			if s > measure(North) and get_pos_y() != get_world_size() - 1:
				swap(North)
				sorted = False
			elif s < measure(South) and get_pos_y() != 0:
				swap(South)
				sorted = False
		
			move(North)

def plant_cacti():
	for i in range(get_world_size()):
		till()
		plant(Entities.Cactus)
		move(North)

def sort_hor():
	sorted = False
	while not sorted:
		sorted = True
		for i in range(get_world_size()):
			s = measure()
			if s > measure(East) and get_pos_x() != get_world_size() - 1:
				swap(East)
				sorted = False
			elif s < measure(West) and get_pos_x() != 0:
				swap(West)
				sorted = False
			
			move(East)

# =======
# ==Run==
# =======

def run():
	clear()

	for i in range(min([get_world_size(), max_drones()])):
		drone = spawn_drone(plant_cacti)
		move(East)
	
	if get_world_size() >= max_drones():
		move(West)
		plant_cacti()
		move(North)
		
	wait_for(drone)
	drones = []
	zero_zero()

	for i in range(min([get_world_size(), max_drones()])):
		drones.append(spawn_drone(sort_vert))
		move(East)
		
	if get_world_size() >= max_drones():
		move(West)
		sort_vert()

	for drone in drones:
		if drone == None:
			continue
		
		wait_for(drone)
	
	drones = []
	zero_zero()

	for i in range(min([get_world_size(), max_drones()])):
		drones.append(spawn_drone(sort_hor))
		move(North)
	if get_world_size() < max_drones():
		move(South)
		sort_hor()

	for drone in drones:
		if drone == None:
			continue
		
		wait_for(drone)
	
	harvest()
	
while True:
	run()
