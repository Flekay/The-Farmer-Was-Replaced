clear()

while True:
	if can_harvest():
		harvest()
	move(North)
