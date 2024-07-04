def farm_bone(num_bone=2000):
	bone = num_items(Items.Bones)
	EGG = Items.Egg

	# Functions for black dino
	def swap_black():
		swap(North)
		operations[0] = shuffle_black

	def shuffle_black():
		move(North)
		swap(North)
		swap(South)
		swap(East)
		move(South)
		operations[0] = swap_black2
	
	def swap_black2():
		swap(North)
		operations[0] = harvest_black

	def harvest_black():
		harvest()
		operations[0] = swap_black

	# Functions for brown dino
	def swap_brown():
		swap(East)
		operations[1] = shuffle_brown

	def shuffle_brown():
		move(East)
		swap(East)
		swap(West)
		swap(South)
		move(West)
		operations[1] = swap_brown2
	
	def swap_brown2():  
		swap(East)
		operations[1] = harvest_brown

	def harvest_brown():
		harvest()
		operations[1] = swap_brown

	# Functions for white dino
	def swap_white():
		swap(South)
		operations[2] = shuffle_white

	def shuffle_white():
		move(South)
		swap(South)
		swap(North)
		swap(West)
		move(North)
		operations[2] = swap_white2
	
	def swap_white2():
		swap(South)
		operations[2] = harvest_white

	def harvest_white():
		harvest()
		operations[2] = swap_white

	# Functions for grey dino
	def swap_grey():
		swap(West)
		operations[3] = shuffle_grey

	def shuffle_grey():
		move(West)
		swap(West)
		swap(East)
		swap(North)
		move(East)
		operations[3] = swap_grey2
	
	def swap_grey2():
		swap(West)
		operations[3] = harvest_grey

	def harvest_grey():
		harvest()
		operations[3] = swap_grey

	operations = [swap_black, swap_brown, swap_white, swap_grey]

	# Setup 
	# setup_bone()
	# pre_plant()

	# Main loop
	while num_items(Items.Bones) < num_bone + bone:
		use_item(EGG)
		operations[measure()]()

# outside functions because probably not needed in a speedrun
def setup_bone():
	clear()
	move(North)
	move(North)
	move(East)
	move(East)
	till()
	move(North)
	move(North)
	till()
	move(South)
	till()
	move(East)
	till()
	move(South)
	move(East)
	till()
	move(West)
	till()
	move(South)
	till()
	move(West)
	move(South)
	till()
	move(North)
	till()
	move(West)
	till()
	move(North)
	move(West)
	till()
	move(East)
	till()
	move(North)
	till()
	move(East)
	move(South)

def pre_plant():
	for i in range(get_world_size()**2):
		till()
		while measure() != 0:
			harvest()
			use_item(Items.Egg)
		move_to_next_tile()
	move_to(2,2)