def for_all(func):
	rr = range(get_world_size()-1)
	def row():
		for _ in rr:
			func()
			move(North)
		func()
	for _ in rr:
		spawn_drone(row)
		move(East)
	row()
