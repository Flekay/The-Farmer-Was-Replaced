def almighty(ws=get_world_size()):
	path = []
	def stack(width):
		STACK = []
		for _ in range(width):
			STACK.append(East)
		STACK.append(South)
		for _ in range(width):
			STACK.append(West)
		return STACK
	def zigzag(width):
		even = [North, West]
		odd = [South, West]
		ZIGZAG = []
		for i in range(width):
			if i % 2:
				ZIGZAG += odd
			else:
				ZIGZAG += even
		return ZIGZAG

	STACK = stack(ws-2)
	if ws % 2:
		shared_path = []
		path1 = []
		path2 = []
		for _ in range(ws-2):
			shared_path.append(North)
		shared_path.append(East)
		for _ in range(ws//2-1):
			shared_path += STACK
			shared_path.append(South)
		for _ in range(ws-2):
			shared_path.append(East)
		shared_path += [South, South, West]
		shared_path += zigzag(ws-3)

		path1 = [North] + shared_path + [North, West]
		path2 = shared_path + [West]
		path = path1 + path2
	else:
		for _ in range(ws-1):
			path.append(North)
		path.append(East)
		for _ in range(ws//2-1):
			path += STACK
			path.append(South)
		path += STACK
		path.append(West)
	return path


clear()
MOVES = almighty()
change_hat(Hats.Dinosaur_Hat)
while True:
	for dir in MOVES:
		if not move(dir):
			change_hat(Hats.Dinosaur_Hat)
