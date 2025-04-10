clear()
change_hat(Hats.Dinosaur_Hat)
apple_x, apple_y = measure()
flipX = True
flipY = True
x = 0
y = 0
length = 0

# Early apples
while length < 50:

	if flipX: # <- check if X is even or odd
		if flipY: # <- check if Y is even or odd
			# South or East
			if apple_y < y:
				if move(South):
					flipY = not flipY
					y -= 1
				else:
					move(East)
					flipX = not flipX
					x += 1
			else:
				if move(East):
					flipX = not flipX
					x += 1
				else:
					move(South)
					flipY = not flipY
					y -= 1
		else:
			# South or West
			if apple_x < x:
				if move(West):
					flipX = not flipX
					x -= 1
				else:
					move(South)
					flipY = not flipY
					y -= 1
			else:
				if move(South):
					flipY = not flipY
					y -= 1
				else:
					move(West)
					flipX = not flipX
					x -= 1
	else:
		if flipY:
			# North or East
			if apple_x > x:
				if move(East):
					flipX = not flipX
					x += 1
				else:
					move(North)
					flipY = not flipY
					y += 1
			else:
				if move(North):
					flipY = not flipY
					y += 1
				else:
					move(East)
					flipX = not flipX
					x += 1
		else:
			# North or West
			if apple_y > y:
				if move(North):
					flipY = not flipY
					y += 1
				else:
					move(West)
					flipX = not flipX
					x -= 1
			else:
				if move(West):
					flipX = not flipX
					x -= 1
				else:
					move(North)
					flipY = not flipY
					y += 1

	m = measure()
	if m:
		apple_x, apple_y = m
		length += 1


# generate almighty circle list
almighty = []
visited = set((x,y))
while len(almighty) < 100:
	if flipX:
		if flipY:
			new_x = x + 1
			if (new_x, y) not in visited and move(East):
				flipX = not flipX
				x = new_x
				almighty.append(East)
			elif move(South):
				# move(South)
				flipY = not flipY
				y -= 1
				almighty.append(South)
		else:
			new_x = x - 1
			if (new_x, y) not in visited and move(West):
				flipX = not flipX
				x = new_x
				almighty.append(West)
			elif move(South):
				# move(South)
				flipY = not flipY
				y -= 1
				almighty.append(South)
	else:
		if flipY:
			new_x = x + 1
			if (new_x, y) not in visited and move(East):
				flipX = not flipX
				x = new_x
				almighty.append(East)
			elif move(North):
				# move(North)
				flipY = not flipY
				y += 1
				almighty.append(North)
		else:
			new_y = y + 1
			if (x, new_y) not in visited and move(North):
				flipY = not flipY
				y = new_y
				almighty.append(North)
			elif move(West):
				# move(West)
				flipX = not flipX
				x -= 1
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
