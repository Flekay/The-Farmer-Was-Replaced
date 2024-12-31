guys()
def guys(itr = [50]):
	# move to the center/base
	for dir in range(get_world_size()//2):
		move(North)
		move(East)

	# setup variables
	base = get_pos_x() * 11
	USED_SUBSTANCE = get_world_size()*num_unlocked(Unlocks.Mazes)
	southWall = set()
	westWall = set()
	northWall = set()
	eastWall = set()
	treasure = {}
	dist_to_base = {base:0}
	dir_to_base = {base:None}
	direction_values = {North: +10, South: -10, East: +1, West: - 1}
	OPP = {North: South, South: North, East: West, West: East}

	# setup the maze
	plant(Entities.Bush)
	use_item(Items.Weird_Substance,USED_SUBSTANCE)
	till()

	def Ndfs(val,dist):
		if measure():
			itr[0] -= 1
			treasure[0] = measure()
			use_item(Items.Weird_Substance,USED_SUBSTANCE)
		southWall.add(val)
		if val not in dist_to_base:
			dist_to_base[val] = dist
			dir_to_base[val] = South
			if move(West):
				westWall.add(val)
				Wdfs(val-1,dist + 1)
			if move(East):
				eastWall.add(val)
				Edfs(val+1,dist + 1)
			if move(North):
				northWall.add(val)
				Ndfs(val+10,dist + 1)
		move(South)
		if measure():
			itr[0] -= 1
			treasure[0] = measure()
			use_item(Items.Weird_Substance,USED_SUBSTANCE)

	def Sdfs(val,dist):
		if measure():
			itr[0] -= 1
			treasure[0] = measure()
			use_item(Items.Weird_Substance,USED_SUBSTANCE)
		northWall.add(val)
		if val not in dist_to_base:
			dist_to_base[val] = dist
			dir_to_base[val] = North
			if move(East):
				eastWall.add(val)
				Edfs(val+1,dist + 1)
			if move(West):
				westWall.add(val)
				Wdfs(val-1,dist + 1)
			if move(South):
				southWall.add(val)
				Sdfs(val-10,dist + 1)
		move(North)
		if measure():
			itr[0] -= 1
			treasure[0] = measure()
			use_item(Items.Weird_Substance,USED_SUBSTANCE)

	def Edfs(val,dist):
		if measure():
			itr[0] -= 1
			treasure[0] = measure()
			use_item(Items.Weird_Substance,USED_SUBSTANCE)
		westWall.add(val)
		if val not in dist_to_base:
			dist_to_base[val] = dist
			dir_to_base[val] = West
			if move(North):
				northWall.add(val)
				Ndfs(val+10,dist + 1)
			if move(South):
				southWall.add(val)
				Sdfs(val-10,dist + 1)
			if move(East):
				eastWall.add(val)
				Edfs(val+1,dist + 1)
		move(West)
		if measure():
			itr[0] -= 1
			treasure[0] = measure()
			use_item(Items.Weird_Substance,USED_SUBSTANCE)

	def Wdfs(val,dist):
		if measure():
			itr[0] -= 1
			treasure[0] = measure()
			use_item(Items.Weird_Substance,USED_SUBSTANCE)
		eastWall.add(val)
		if val not in dist_to_base:
			dist_to_base[val] = dist
			dir_to_base[val] = East
			if move(South):
				southWall.add(val)
				Sdfs(val-10,dist + 1)
			if move(North):
				northWall.add(val)
				Ndfs(val+10,dist + 1)
			if move(West):
				westWall.add(val)
				Wdfs(val-1,dist + 1)
		move(East)
		if measure():
			itr[0] -= 1
			treasure[0] = measure()
			use_item(Items.Weird_Substance,USED_SUBSTANCE)

	def Nbfs(val,dist):
		if(dist < dist_to_base[val]):
			dist_to_base[val] = dist
			dir_to_base[val] = South
			if val in northWall:
				Nbfs(val+10,dist+1)
			if val in eastWall:
				Ebfs(val+1,dist+1)
			if val in westWall:
				Wbfs(val-1,dist+1)

	def Sbfs(val,dist):
		if(dist < dist_to_base[val]):
			dist_to_base[val] = dist
			dir_to_base[val] = North
			if val in southWall:
				Sbfs(val-10,dist+1)
			if val in eastWall:
				Ebfs(val+1,dist+1)
			if val in westWall:
				Wbfs(val-1,dist+1)

	def Ebfs(val,dist):
		if(dist < dist_to_base[val]):
			dist_to_base[val] = dist
			dir_to_base[val] = West
			if val in northWall:
				Nbfs(val+10,dist+1)
			if val in southWall:
				Sbfs(val-10,dist+1)
			if val in eastWall:
				Ebfs(val+1,dist+1)

	def Wbfs(val,dist):
		if(dist < dist_to_base[val]):
			dist_to_base[val] = dist
			dir_to_base[val] = East
			if val in northWall:
				Nbfs(val+10,dist+1)
			if val in southWall:
				Sbfs(val-10,dist+1)
			if val in westWall:
				Wbfs(val-1,dist+1)

	# dfs scan the maze
	if move(North):
		northWall.add(base)
		southWall.add(base+10)
		Ndfs(base+10,1)
	if move(East):
		eastWall.add(base)
		westWall.add(base+1)
		Edfs(base+1,1)
	if move(South):
		northWall.add(base-10)
		southWall.add(base)
		Sdfs(base-10,1)
	if move(West):
		eastWall.add(base-1)
		westWall.add(base)
		Wdfs(base-1,1)

	#timings
	timings = []
	time = get_time()

	# first maze solve
	x,y = treasure[0]
	val = x + 10 * y
	droneval = val
	tpath = [0]
	while val != base:
		dir = dir_to_base[val]
		tpath.append(dir)
		val += direction_values[dir]
	for step in tpath[:0:-1]:
		move(OPP[step])

	# loop through the maze
	for i in range(itr[0] - 1):
		#timings
		timings.append(((get_time() - time)*100))
		time = get_time()

		dpath = tpath
		gpath = [i]

		x,y = measure()
		use_item(Items.Weird_Substance,USED_SUBSTANCE)
		val = x + 10 * y
		while val != base:
			dir = dir_to_base[val]
			gpath.append(dir)
			val += direction_values[dir]

		tpath = gpath + []

		while dpath[-1] == gpath[-1]:
			gpath.pop()
			dpath.pop()

		dpath.pop(0)
		for dir in dpath:
			if i % 2:
				move(dir)
			else:
				move(dir)
				#droneval += direction_values[dir]
				droneval = get_pos_x() + 10 * get_pos_y()
				if droneval not in northWall and move(North):
					nval = droneval + 10
					northWall.add(droneval)
					southWall.add(nval)
					Nbfs(nval,dist_to_base[droneval ] + 1)
					Sbfs(droneval ,dist_to_base[nval] + 1)
					move(South)
				if droneval not in southWall and move(South):
					nval = droneval - 10
					southWall.add(droneval)
					northWall.add(nval)
					Sbfs(nval, dist_to_base[droneval] + 1)
					Nbfs(droneval, dist_to_base[nval] + 1)
					move(North)
				if droneval not in eastWall and move(East):
					nval = droneval + 1
					eastWall.add(droneval)
					westWall.add(nval)
					Ebfs(nval, dist_to_base[droneval] + 1)
					Wbfs(droneval, dist_to_base[nval] + 1)
					move(West)
				if droneval not in westWall and move(West):
					nval = droneval - 1
					westWall.add(droneval)
					eastWall.add(nval)
					Wbfs(nval, dist_to_base[droneval] + 1)
					Ebfs(droneval, dist_to_base[nval] + 1)
					move(East)


		for dir in gpath[:0:-1]:
			if i % 2:
				move(OPP[dir])
			else:
				opdir = OPP[dir]
				move(opdir)
				#droneval += direction_values[opdir]
				droneval = get_pos_x() + 10 * get_pos_y()
				if droneval not in northWall and move(North):
					nval = droneval + 10
					northWall.add(droneval)
					southWall.add(nval)
					Nbfs(nval,dist_to_base[droneval ] + 1)
					Sbfs(droneval ,dist_to_base[nval] + 1)
					move(South)
				if droneval not in southWall and move(South):
					nval = droneval - 10
					southWall.add(droneval)
					northWall.add(nval)
					Sbfs(nval, dist_to_base[droneval] + 1)
					Nbfs(droneval, dist_to_base[nval] + 1)
					move(North)
				if droneval not in eastWall and move(East):
					nval = droneval + 1
					eastWall.add(droneval)
					westWall.add(nval)
					Ebfs(nval, dist_to_base[droneval] + 1)
					Wbfs(droneval, dist_to_base[nval] + 1)
					move(West)
				if droneval not in westWall and move(West):
					nval = droneval - 1
					westWall.add(droneval)
					eastWall.add(nval)
					Wbfs(nval, dist_to_base[droneval] + 1)
					Ebfs(droneval, dist_to_base[nval] + 1)
					move(East)
	harvest()
	quick_print(timings)
