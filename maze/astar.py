clear()
astar()
def astar(itr = [300]):
	plant(Entities.Bush)
	tot = get_world_size()*num_unlocked(Unlocks.Mazes)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance,tot)
	southWall = set()
	westWall = set()
	vis = set()
	treasure = [1]


	def Ndfs(val):
		if move(North):
			val = val + 10
			southWall.add(val)
			if(val not in vis):
				vis.add(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Ndfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Wdfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Edfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
			move(South)

	def Sdfs(val):
		if move(South):
			southWall.add(val)
			val = val - 10
			if(val not in vis):
				vis.add(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Sdfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Wdfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Edfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
			move(North)

	def Edfs(val):
		if move(East):
			val = val + 1
			westWall.add(val)
			if(val not in vis):
				vis.add(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Sdfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Ndfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Edfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
			move(West)

	def Wdfs(val):
		if move(West):
			westWall.add(val)
			val = val - 1
			if(val not in vis):
				vis.add(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Sdfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Ndfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
				Wdfs(val)
				if(get_entity_type() == Entities.Treasure):
					itr[0] = itr[0] - 1
					treasure[0] = measure()
					use_item(Items.Weird_Substance,tot)
			move(East)


	val = get_pos_x()+10*get_pos_y()

	if(get_entity_type() == Entities.Treasure):
		itr[0] = itr[0] - 1
		treasure[0] = measure()
		use_item(Items.Weird_Substance,tot)
	Edfs(val)
	if(get_entity_type() == Entities.Treasure):
		itr[0] = itr[0] - 1
		treasure[0] = measure()
		use_item(Items.Weird_Substance,tot)
	Wdfs(val)
	if(get_entity_type() == Entities.Treasure):
		itr[0] = itr[0] - 1
		treasure[0] = measure()
		use_item(Items.Weird_Substance,tot)
	Ndfs(val)
	if(get_entity_type() == Entities.Treasure):
		itr[0] = itr[0] - 1
		treasure[0] = measure()
		use_item(Items.Weird_Substance,tot)
	Sdfs(val)
	if(get_entity_type() == Entities.Treasure):
		itr[0] = itr[0] - 1
		treasure[0] = measure()
		use_item(Items.Weird_Substance,tot)

	x,y = treasure[0]
	dronex = get_pos_x()
	droney = get_pos_y()

	def N(val):
		if val + 10 in southWall and val + 10 not in map:
			val = val + 10
			map[val] = South
			if val == droneval:
				return True
			nxt.append((val,rEN))
			nxt.append((val,rWN))
			return N(val)
		return False

	def rN(val):
		if val in southWall and val - 10 not in map:
			val = val - 10
			map[val] = North
			nxt.append((val,rN))
			nxt.append((val,rEN))
			nxt.append((val,rWN))
		return False


	def S(val):
		if val in southWall and val - 10 not in map:
			val = val - 10
			map[val] = North
			if val == droneval:
				return True
			nxt.append((val,rES))
			nxt.append((val,rWS))
			return S(val)
		return False

	def rS(val):
		if val + 10 in southWall and val + 10 not in map:
			val = val + 10
			map[val] = South
			nxt.append((val,rS))
			nxt.append((val,rES))
			nxt.append((val,rWS))
		return False

	def E(val):
		if val + 1 in westWall and val + 1 not in map:
			val = val + 1
			map[val] = West
			if val == droneval:
				return True
			nxt.append((val,rNE))
			nxt.append((val,rSE))
			return E(val)
		return False

	def rE(val):
		if val in westWall and val - 1 not in map:
			val = val - 1
			map[val] = East
			nxt.append((val,rE))
			nxt.append((val,rNE))
			nxt.append((val,rSE))
		return False

	def W(val):
		if val in westWall and val - 1 not in map:
			val = val - 1
			map[val] = East
			if val == droneval:
				return True
			nxt.append((val,rNW))
			nxt.append((val,rSW))
			return W(val)
		return False

	def rW(val):
		if val + 1 in westWall and val + 1 not in map:
			val = val + 1
			map[val] = West
			nxt.append((val,rW))
			nxt.append((val,rNW))
			nxt.append((val,rSW))
		return False

	def NE(val):
		if val + 10 in southWall and val + 10 not in map:
			val = val + 10
			map[val] = South
			nxt.append((val,rEN))
			if(val/10 >= droney):
				nxt.append(val,rSE)
				return E(val)
			else:
				return NE(val) or EN(val)
		return False

	def rNE(val):
		if val in southWall and val - 10 not in map:
			val = val - 10
			map[val] = North
			nxt.append((val,rNE))
			nxt.append((val,rEN))
			return EN(val)
		return False

	def EN(val):
		if val + 1 in westWall and val + 1 not in map:
			val = val + 1
			map[val] = West
			nxt.append((val,rNE))
			if(val % 10 >= dronex):
				nxt.append((val,rWN))
				return N(val)
			else:
				return EN(val) or NE(val)
		return False

	def rEN(val):
		if val + 1 in westWall and val + 1 not in map:
			val = val + 1
			map[val] = East
			nxt.append((val,rNE))
			nxt.append((val,rEN))
			return NE(val)
		return False

	def SE(val):
		if val in southWall and val - 10 not in map:
			val = val - 10
			map[val] = North
			nxt.append((val,rES))
			if(val/10 <= droney):
				nxt.append(val,rNE)
				return E(val)
			else:
				return SE(val) or ES(val)
		return False

	def rSE(val):
		if val + 10 in southWall and val + 10 not in map:
			val = val + 10
			map[val] = South
			nxt.append((val,rSE))
			nxt.append((val,rES))
			return ES(val)
		return False

	def ES(val):
		if val + 1 in westWall and val + 1 not in map:
			val = val + 1
			map[val] = West
			nxt.append((val,rSW))
			if(val % 10 >= dronex):
				nxt.append(val,rWS)
				return S(val)
			else:
				return ES(val) or SE(val)
		return False

	def rES(val):
		if val in westWall and val - 1 not in map:
			val = val - 1
			map[val] = East
			nxt.append((val,rSE))
			nxt.append((val,rES))
			return SE(val)
		return False

	def NW(val):
		if val + 10 in southWall and val + 10 not in map:
			val = val + 10
			map[val] = South
			nxt.append((val,rWN))
			if(val/10 >= droney):
				nxt.append((val,rSW))
				return W(val)
			else:
				return NW(val) or WN(val)
		return False

	def rNW(val):
		if val in southWall and val - 10 not in map:
			val = val - 10
			map[val] = North
			nxt.append((val,rNW))
			nxt.append((val,rWN))
			return WN(val)
		return False

	def WN(val):
		if val in westWall and val - 1 not in map:
			val = val - 1
			map[val] = East
			nxt.append((val,rNW))
			if(val % 10 <= dronex):
				nxt.append((val,rEN))
				return N(val)
			else:
				return WN(val) or NW(val)
		return False

	def rWN(val):
		if val + 1 in westWall and val + 1 not in map:
			val = val + 1
			map[val] = West
			nxt.append((val,rWN))
			nxt.append((val,rNW))
			return NW(val)
		return False

	def SW(val):
		if val in southWall and val - 10 not in map:
			val = val - 10
			map[val] = North
			nxt.append((val,rWS))
			if(val/10 <= droney):
				nxt.append((val,rNW))
				return W(val)
			else:
				return SW(val) or WS(val)
		return False

	def rSW(val):
		if val + 10 in southWall and val + 10 not in map:
			val = val + 10
			map[val] = South
			nxt.append((val,rSW))
			nxt.append((val,rWS))
			return WS(val)
		return False

	def WS(val):
		if val in westWall and val - 1 not in map:
			val = val - 1
			map[val] = East
			nxt.append((val,rSW))
			if(val % 10 <= dronex):
				nxt.append((val,rES))
				return S(val)
			else:
				return WS(val) or SW(val)
		return False

	def rWS(val):
		if val + 1 in westWall and val + 1 not in map:
			val = val + 1
			map[val] = West
			nxt.append((val,rWS))
			nxt.append((val,rSW))
			return SW(val)
		return False


	for i in range(itr[0]):
		if i:
			dronex = x
			droney = y
			x,y = measure()
			use_item(Items.Weird_Substance,tot)

		val = x + 10*y
		droneval = dronex + 10 * droney
		nxt = []
		map = {val:False}

		if dronex > x:#E
			if droney > y:#N
				nxt.append((val,rNE))
				nxt.append((val,rEN))
				if not EN(val):
					NE(val)
			elif droney < y:#S
				nxt.append((val,rSE))
				nxt.append((val,rES))
				if not ES(val):
					SE(val)
			else:
				nxt.append((val,rE))
				nxt.append((val,rNE))
				nxt.append((val,rSE))
				E(val)
		elif dronex < x:#W
			if droney > y:#N
				nxt.append((val,rNW))
				nxt.append((val,rWN))
				if not WN(val):
					NW(val)
			elif droney < y:#S
				nxt.append((val,rSW))
				nxt.append((val,rWS))
				if not WS(val):
					SW(val)
			else:
				nxt.append((val,rW))
				nxt.append((val,rNW))
				nxt.append((val,rSW))
				W(val)
		else:
			if droney > y:#N
				nxt.append((val,rN))
				nxt.append((val,rEN))
				nxt.append((val,rWN))
				N(val)
			elif droney < y:#S
				nxt.append((val,rS))
				nxt.append((val,rES))
				nxt.append((val,rWS))
				S(val)
			else:
				move("???")


		while droneval not in map:
			quick_print(nxt)
			cur = nxt
			nxt = []
			for v in cur:
				val,f = v
				if (f(val)):
					break

		dir = map[droneval]

		dval = {North: +10, South: -10, East: +1, West: - 1}

		while(dir):
			if val not in southWall and move(South):
				move(North)
				southWall.add(val)
			if val + 10 not in southWall and move(North):
				move(South)
				southWall.add(val + 10)
			if val not in westWall and move(West):
				move(East)
				westWall.add(val)
			if val + 1 not in westWall and move(East):
				move(West)
				westWall.add(val + 1)
			move(dir)
			val = val + dval[dir]

	harvest()
