def high_insertion(x, y, cur, measures, size, sm1):
	sm1 = size - 1

	# Case 1
	if x < sm1 and y < sm1:
		right = measures[x + 1][y]
		up = measures[x][y + 1]
		swapping = cur > right or cur > up

		# Swap not necessary
		if not swapping:
			return

		move_to(x,y,size)
		while swapping:

			# Swap with smallest and update measures
			if right < up:
				swap(East)
				measures[x][y] = right
				x += 1
				measures[x][y] = cur

				do_swaps_lower(x-1, y, measures, size, sm1)

				# Follow case 2 if we hit edge
				if x == sm1:
					break

				right = measures[x + 1][y]
				up = measures[x][y + 1]
				swapping = cur > right or cur > up

				# No need to move if we are not swapping
				if not swapping:
					return

				move(East)


			# Up is smallest
			else:
				swap(North)
				measures[x][y] = up
				y += 1
				measures[x][y] = cur

				do_swaps_lower(x, y-1, measures, size, sm1)

				# Follow case 3 if we hit edge
				if y == sm1:
					break

				right = measures[x + 1][y]
				up = measures[x][y + 1]
				swapping = cur > right or cur > up

				# No need to move if we are not swapping
				if not swapping:
					return

				move(North)

	# Case 2
	if x < sm1:
		right = measures[x + 1][y]
		swapping = cur > right

		# Swap not necessary
		if not swapping:
			return

		move_to(x,y,size)
		while swapping:
			swap(East)
			measures[x][y] = right
			x += 1
			measures[x][y] = cur

			do_swaps_lower(x-1, y, measures, size, sm1)

			# Hit corner
			if x == sm1:
				return

			right = measures[x + 1][y]
			swapping = cur > right

			# No need to move if we are not swapping
			if not swapping:
				return

			move(East)

	# Case 3
	if y < sm1:
		up = measures[x][y + 1]
		swapping = cur > up

		# Swap not necessary
		if not swapping:
			return

		move_to(x,y,size)
		while swapping:
			swap(North)
			measures[x][y] = up
			y += 1
			measures[x][y] = cur

			do_swaps_lower(x, y-1, measures, size, sm1)

			# Hit corner
			if y == sm1:
				return

			up = measures[x][y + 1]
			swapping = cur > up

			# No need to move if we are not swapping
			if not swapping:
				return

			move(North)
			