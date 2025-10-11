clear()
set_world_size(5)
ws = get_world_size()
substance = ws * 2**(num_unlocked(Unlocks.Mazes)-1)
goal = 9863168
rr = range(ws)

def drone_search():
	while num_items(Items.Gold) < goal:
		while use_item(Items.Weird_Substance, substance):
			continue
		if get_entity_type() == Entities.Treasure:
			if not use_item(Items.Weird_Substance, substance):
				harvest()
				plant(Entities.Bush)
				use_item(Items.Weird_Substance,substance)


for i in rr:
	for j in rr:
		spawn_drone(drone_search)
		move(North)
	move(East)
plant(Entities.Bush)
use_item(Items.Weird_Substance,substance)
