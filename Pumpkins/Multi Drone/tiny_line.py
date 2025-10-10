from for_all_sync import for_all

required_pumkins = 200000000
#                200 000 000


def drone():
	# inital till and plant
	for _ in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		move(North)

	# main loop until we have enough pumpkins
	while num_items(Items.Pumpkin) < required_pumkins:

		# ensure pumpkin are fully grown and atleast 2x2
		if measure() == measure(North):
			harvest()

		# simple planting and watering logic
		if plant(Entities.Pumpkin) and get_water() < 0.2:
			use_item(Items.Water)
		move(North)



if __name__ == "__main__":
	for_all(drone)
	