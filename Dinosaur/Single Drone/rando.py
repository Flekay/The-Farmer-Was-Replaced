clear()
rando()
def rando():
	change_hat(Hats.Dinosaur_Hat)

	def try_move(directions):
		dir = directions.pop(random() * len(directions))
		if move(dir):
			return False
		elif directions:
			return try_move(directions)
		else:
			return True

	while True:
		if try_move([North, South, West, East]):
			break
	clear()
