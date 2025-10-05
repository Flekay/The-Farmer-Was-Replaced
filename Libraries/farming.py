help        = "https://github.com/Flekay/The-Farmer-Was-Replaced/tree/main/general/farming"
constants   = "[]"
functions   = "[batch_func, batch_harvest, batch_plant, batch_till, batch_water]"

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

# Visits all tiles and harvests them.
def batch_harvest():
	ws = get_world_size()
	MOVES = [East, North, North]
	for _ in range(ws-3):
		MOVES.append(North)
	for _ in MOVES:
		for direction in MOVES:
			harvest()
			move(direction)

# Visit each tile and plants a given entity.
#
# Arguments:
#	entity (entity): the entity to plant
#
# Example:
#	batch_plant(Entities.Carrot)
def batch_plant(entity):
	ws = get_world_size()
	MOVES = [East, North, North]
	for _ in range(ws-3):
		MOVES.append(North)
	for _ in MOVES:
		for direction in MOVES:
			plant(entity)
			move(direction)

# Visits all tiles and tills them.
def batch_till():
	ws = get_world_size()
	MOVES = [East, North, North]
	for _ in range(ws-3):
		MOVES.append(North)
	for _ in MOVES:
		for direction in MOVES:
			till()
			move(direction)

# Visits all tiles and waters them to a certain threshold.
def batch_water(threshold=0.5):
	ws = get_world_size()
	MOVES = [East, North, North]
	for _ in range(ws-3):
		MOVES.append(North)
	for _ in MOVES:
		for direction in MOVES:
			use_item(Item.Water)
			move(direction)

