from for_all_sync import for_all
from move_y import move_y

required_pumkins = 200000000
#                200 000 000

def main_farming_loop(initial_plant=False):
		# inital till and plant
		for _ in range(get_world_size()):
			if initial_plant:
				till()
			plant(Entities.Pumpkin)
			move(North)

		# check for dead pumkins and replant
		dead_pumpkins = []
		for _ in range(get_world_size()):
			if not can_harvest():
				plant(Entities.Pumpkin)
				dead_pumpkins.append(get_pos_y())
			move(North)

		# replant dead pumpkins until all fully grown
		while len(dead_pumpkins) > 3:
			for y in dead_pumpkins:
				move_y(y)
				if can_harvest():
					dead_pumpkins.remove(y)
				elif not get_entity_type():
					return
				else:
					plant(Entities.Pumpkin)
					if get_water() < 0.2:
						use_item(Items.Water)

		for y in dead_pumpkins:
			move_y(y)
			use_item(Items.Water,2)
			while not can_harvest():
				use_item(Items.Fertilizer)
				if not get_entity_type():
					return
				plant(Entities.Pumpkin)

def helper_drone():
	# main loop until we have enough pumpkins
	initial_plant = True
	while num_items(Items.Pumpkin) < required_pumkins:

		main_farming_loop(initial_plant)
		initial_plant = False

		# row is fully grown, wait for main drone to harvest
		while get_entity_type():
			pass

def main_drone():
	# main loop until we have enough pumpkins
	initial_plant = True
	while num_items(Items.Pumpkin) < required_pumkins:

		main_farming_loop(initial_plant)
		initial_plant = False

		# row is fully grown, wait for main drone to harvest
		while measure() != measure(West):
			pass

		list(range(10)) # race condition workaround

		# harvest mega pumpkin
		harvest()


if __name__ == "__main__":
	for_all((
		main_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
		helper_drone,
	))
