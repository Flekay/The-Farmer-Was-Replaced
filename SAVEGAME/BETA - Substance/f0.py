clear()
while 1:
	if can_harvest():
		harvest()
	else:
		move(North)