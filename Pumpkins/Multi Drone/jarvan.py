ws = 29
set_world_size(ws)
from move_to import move_to_pos, move_to

required_pumkins = 200000000
#                200 000 000

def spawn_all(funcs):
	def drone(i):
		power = 1
		while i + power < len(funcs):
			if power > i:
				spawn_drone(drone_funcs[i + power])
			power = power * 2
		funcs[i]()

	drone_funcs = []
	x = 0
	while x < len(funcs):
		def make_drone(index):
			def d():
				drone(index)
			return d
		drone_funcs.append(make_drone(x))
		x = x + 1

	drone(0)

starting_positions = (
	(0,0),(5,0),(10,0),(15,0),(20,0),(25,0),
	(0,5),(5,5),(10,5),(15,5),(20,5),(25,5),
	(0,10),(5,10),(10,10),(20,10),
	(25,10),(0,15),(5,15),(10,20),
	(20,15),(25,15),(0,20),(5,20),
	(20,20),(25,20),(0,25),(5,25),
	(10,25),(15,25),(20,25),(25,25),
	# (15,15),(15,10),(10,15)(15,20),
)
moves = (
	North, North, North, East,
	South, South, East,
	North, North, East,
	South, South, South, West,
	West, West
)
root = (0,0)

def drone_gen():
	drones = []
	for spawn_pos in starting_positions:
		def make_drone(position):
			def drone():
				start = root
				while num_items(Items.Pumpkin) < required_pumkins:
					move_to_pos(position, start, ws)
					fasf = (get_pos_x(), get_pos_y())
					if position != fasf:
						[[]]=[]
					initial = get_ground_type() == Grounds.Grassland
					# Initial planting
					for move_dir in moves:
						if initial:
							till()
						plant(Entities.Pumpkin)
						move(move_dir)

					# check for dead pumpkins
					dead_pumpkins = []
					for move_dir in moves:
						if not can_harvest():
							dead_pumpkins.append((get_pos_x(), get_pos_y()))
						plant(Entities.Pumpkin)
						if get_water() < 0.2:
							use_item(Items.Water)
						move(move_dir)


					# replant dead pumpkins until all fully grown
					while len(dead_pumpkins) > 3:
						for pos in dead_pumpkins:
							x,y = pos
							move_to(x,y)
							if can_harvest():
								dead_pumpkins.remove(pos)
							else:
								plant(Entities.Pumpkin)
								if get_water() < 0.2:
									use_item(Items.Water)

					for pos in dead_pumpkins:
						x,y = pos
						move_to(x,y)
						use_item(Items.Water,2)
						while not can_harvest():
							use_item(Items.Fertilizer)
							plant(Entities.Pumpkin)
					start = pos
					harvest()
			return drone
		drones.append(make_drone(spawn_pos))
	return drones


if __name__ == "__main__":
	spawn_all(drone_gen())
