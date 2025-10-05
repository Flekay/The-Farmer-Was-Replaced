# Visit each tile, and execute a given function
#
# Arguments:
#	func: function to execute on each tile
#
# Example:
#	def custom_func():
#		till()
#		plant(Entities.Carrot)
#		while get_water() < 1:
#			use_item(Item.Water)
#	batch_func(custom_func)
def batch_func(func):
	ws = get_world_size()
	MOVES = [East, North, North]
	for _ in range(ws-3):
		MOVES.append(North)
	for _ in MOVES:
		for direction in MOVES:
			func()
			move(direction)
