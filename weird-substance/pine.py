clear()
move_to(4,4)
till()
use_item(Items.Water_Tank)
use_item(Items.Water_Tank)
use_item(Items.Water_Tank)

# spam trees
while True:
	use_item(Items.Water_Tank)
	for i in range(888): # get_water <= 0.78
		plant(Entities.Tree)
		if Entities.Grass in get_companion():
			use_item(Items.Fertilizer)
		harvest()
