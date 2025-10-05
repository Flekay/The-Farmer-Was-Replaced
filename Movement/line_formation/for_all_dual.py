def for_all(func):
	world_size = get_world_size()
	rr = range(world_size - 1)
	hws = world_size // 2
	rr2 = range(1, hws)

	def row():
		for _ in rr:
			func()
			move(North)
		func()

	def second_spawner():
		for i in rr2:
			def worker_drone():
				for _ in range(hws - i):
					move(East)
				row()
			spawn_drone(worker_drone)
		row()

	spawn_drone(second_spawner)
	move(West)

	for i in rr2:
		def worker_drone():
			for _ in range(hws - i):
				move(West)
			row()
		spawn_drone(worker_drone)

	row()
	move(North)
