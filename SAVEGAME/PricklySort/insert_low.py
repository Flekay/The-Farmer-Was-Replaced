def insert_low(x, y, cur, measures, size):

	# Case 1
	if x and y:
		left = measures[x - 1][y]
		down = measures[x][y - 1]
		swapping = cur < left or cur < down

		# Swap not necessary
		if not swapping:
			return

		move_to(x,y,size)
		while swapping:

			# Swap with largest and update measures
			if left > down:
				swap(West)
				measures[x][y] = left
				x -= 1
				measures[x][y] = cur

				do_swaps_high(x+1, y, measures, size)

				# Follow case 2 if we hit edge
				if not x:
					break

				left = measures[x - 1][y]
				down = measures[x][y - 1]

				# No need to move if we are not swapping
				swapping = cur < left or cur < down
				if not swapping:
					return

				move(West)


			# Down is largest
			else:
				swap(South)
				measures[x][y] = down
				y -= 1
				measures[x][y] = cur

				do_swaps_high(x, y+1, measures, size)

				# Follow case 3 if we hit edge
				if not y:
					break

				left = measures[x - 1][y]
				down = measures[x][y - 1]
				swapping = cur < left or cur < down

				# No need to move if we are not swapping
				if not swapping:
					return

				move(South)

	# Case 2
	if x:
		left = measures[x - 1][y]
		swapping = cur < left

		# Swap not necessary
		if not swapping:
			return

		move_to(x,y,size)
		while swapping:
			swap(West)
			measures[x][y] = left
			x -= 1
			measures[x][y] = cur

			do_swaps_high(x+1, y, measures, size)

			# Hit corner
			if not x:
				return

			left = measures[x - 1][y]
			swapping = cur < left

			# No need to move if we are not swapping
			if not swapping:
				return

			move(West)

	# Case 3
	if y:
		down = measures[x][y - 1]
		swapping = cur < down

		# Swap not necessary
		if not swapping:
			return

		move_to(x,y,size)
		while swapping:
			swap(South)
			measures[x][y] = down
			y -= 1
			measures[x][y] = cur

			do_swaps_high(x, y+1, measures, size)

			# Hit corner
			if not y:
				return

			down = measures[x][y - 1]
			swapping = cur < down

			# No need to move if we are not swapping
			if not swapping:
				return

			move(South)
			