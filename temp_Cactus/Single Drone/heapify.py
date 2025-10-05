def heapify(cacti, x, y, nextDir=None):
	cactix = cacti[x]
	current_val = cactix[y]
	dir = None
	tx = x
	ty = y
	new_val = 0

	# Check left neighbor once.
	if x > 0:
		left = x - 1
		left_val = cacti[left][y]
		if left_val > current_val:
			dir = West
			tx = left
			new_val = left_val

	# Check bottom neighbor once.
	if y > 0:
		bottom = y - 1
		bottom_val = cactix[bottom]
		if bottom_val > current_val:
			if not dir:
				dir = South
				ty = bottom
				new_val = bottom_val
			# If both neighbors are candidates and values differ, pick the higher.
			elif bottom_val > left_val:
				dir = South
				tx = x
				ty = bottom
				new_val = bottom_val
			# If values are equal, keep candidate from left as per original behavior.

	if not dir:
		return

	if nextDir:
		move(nextDir)

	# Swap using the chosen candidate.
	swap(dir)
	cactix[y] = new_val
	cacti[tx][ty] = current_val
	heapify(cacti, tx, ty, dir)

def rectCoords(n = get_world_size()):
	res = []
	for i in range(n):
		for j in range(n):
			res.append((i, j))
	res.remove((0,0))
	return res
