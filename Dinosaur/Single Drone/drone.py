clear()
change_hat(Hats.Dinosaur_Hat)
apple_x, apple_y = measure()
flipX = True
flipY = True
drone_x = 0
drone_y = 0
length = 0

# Early apples
while length < 50:

	if flipX: # <- check if X is even or odd
		if flipY: # <- check if Y is even or odd
			# South or East
			if apple_y < drone_y:
				if move(South):
					flipY = not flipY
					drone_y -= 1
				else:
					move(East)
					flipX = not flipX
					drone_x += 1
			else:
				if move(East):
					flipX = not flipX
					drone_x += 1
				else:
					move(South)
					flipY = not flipY
					drone_y -= 1
		else:
			# South or West
			if apple_x < drone_x:
				if move(West):
					flipX = not flipX
					drone_x -= 1
				else:
					move(South)
					flipY = not flipY
					drone_y -= 1
			else:
				if move(South):
					flipY = not flipY
					drone_y -= 1
				else:
					move(West)
					flipX = not flipX
					drone_x -= 1
	else:
		if flipY:
			# North or East
			if apple_x > drone_x:
				if move(East):
					flipX = not flipX
					drone_x += 1
				else:
					move(North)
					flipY = not flipY
					drone_y += 1
			else:
				if move(North):
					flipY = not flipY
					drone_y += 1
				else:
					move(East)
					flipX = not flipX
					drone_x += 1
		else:
			# North or West
			if apple_y > drone_y:
				if move(North):
					flipY = not flipY
					drone_y += 1
				else:
					move(West)
					flipX = not flipX
					drone_x -= 1
			else:
				if move(West):
					flipX = not flipX
					drone_x -= 1
				else:
					move(North)
					flipY = not flipY
					drone_y += 1

	m = measure()
	if m:
		apple_x, apple_y = m
		length += 1


# generate almighty circle list
almighty = []
visited = set((drone_x,drone_y))
while len(almighty) < 100:
	if flipX:
		if flipY:
			new_x = drone_x + 1
			if (new_x, drone_y) not in visited and move(East):
				flipX = not flipX
				drone_x = new_x
				almighty.append(East)
			elif move(South):
				# move(South)
				flipY = not flipY
				drone_y -= 1
				almighty.append(South)
		else:
			new_x = drone_x - 1
			if (new_x, drone_y) not in visited and move(West):
				flipX = not flipX
				drone_x = new_x
				almighty.append(West)
			elif move(South):
				# move(South)
				flipY = not flipY
				drone_y -= 1
				almighty.append(South)
	else:
		if flipY:
			new_x = drone_x + 1
			if (new_x, drone_y) not in visited and move(East):
				flipX = not flipX
				drone_x = new_x
				almighty.append(East)
			elif move(North):
				# move(North)
				flipY = not flipY
				drone_y += 1
				almighty.append(North)
		else:
			new_y = drone_y + 1
			if (drone_x, new_y) not in visited and move(North):
				flipY = not flipY
				drone_y = new_y
				almighty.append(North)
			elif move(West):
				# move(West)
				flipX = not flipX
				drone_x -= 1
				almighty.append(West)
	pos = (get_pos_x(), get_pos_y())
	if pos in visited:
		almighty.pop()
	else:
		visited.add(pos)

# loop through almighty circle list
contin = True
while contin:
	for direction in almighty:
		if not move(direction):
			contin = False
			break

clear()
