clear()
betterStack()
def betterStack():
	change_hat(Hats.Dinosaur_Hat)
	apple = measure()
	apple_dict = {0: apple}
	length_dict = {0: 99}
	switch_length = 56
	def mowe(dir):
		measureing = measure()
		if measureing:
			length_dict[0] -= 1
			apple_dict[0] = measureing
		mov = move(dir)
		return mov
	mowe(East)
	mowe(East)
	mowe(North)
	mowe(North)



	ax2y2 = [(0, 2), (0, 3), (1, 2), (1, 3)]
	def x2y2():
		if apple in ax2y2 or length_dict[0] < switch_length or not mowe(North):
			mowe(West)
			mowe(West)
			mowe(North)
			mowe(East)
			mowe(East)
		return x2y3
	def x2y3():
		mowe(North)
		return x2y4
	ax2y4= [(0, 4), (0, 5), (1, 4), (1, 5)]
	def x2y4():
		if apple in ax2y4 or length_dict[0] < switch_length or not mowe(North):
			mowe(West)
			mowe(West)
			mowe(North)
			mowe(East)
			mowe(East)
		return x2y5
	ix2y5 = [(3, 5), (3, 6), (4, 5), (4, 6)]
	def x2y5():
		if apple in ix2y5 or length_dict[0] < switch_length or not mowe(North):
			mowe(East)
			mowe(East)
			mowe(North)
			mowe(West)
			mowe(West)
		return x2y6
	ax2y6 = [(0, 6), (0, 7), (0, 8), (0, 9), (1, 6), (1, 7), (1, 8), (1, 9)]
	def x2y6():
		if apple in ax2y6 or length_dict[0] < switch_length or not mowe(North):
			mowe(West)
			mowe(West)
			mowe(North)
			mowe(North)
			mowe(North)
			mowe(East)
			mowe(South)
			mowe(South)
			mowe(East)
		return x2y7

	ax2y7 = [(2, 8), (2, 9), (3, 8), (3, 9)]
	def x2y7():
		if apple in ax2y7 or length_dict[0] < switch_length or not mowe(East):
			mowe(North)
			mowe(North)
			mowe(East)
			mowe(South)
			mowe(South)
		return x3y7
	def x3y7():
		mowe(East)
		return x4y7
	ax4y7 = [(4, 8), (4, 9), (5, 8), (5, 9)]
	def x4y7():
		if apple in ax4y7 or length_dict[0] < switch_length or not mowe(East):
			mowe(North)
			mowe(North)
			mowe(East)
			mowe(South)
			mowe(South)
		return x5y7
	ix5y7 = [(5, 6), (5, 5), (6, 6), (6, 5)]
	def x5y7():
		if apple in ix5y7 or length_dict[0] < switch_length or not mowe(East):
			mowe(South)
			mowe(South)
			mowe(East)
			mowe(North)
			mowe(North)
		return x6y7
	ax6y7 = [(6, 8), (6, 9), (7, 8), (7, 9), (8, 8), (8, 9), (9, 8), (9, 9)]
	def x6y7():
		if apple in ax6y7 or length_dict[0] < switch_length or not mowe(East):
			mowe(North)
			mowe(North)
			mowe(East)
			mowe(East)
			mowe(East)
			mowe(South)
			mowe(West)
			mowe(West)
			mowe(South)
		return x7y7

	ax7y7 = [(8, 6), (8, 7), (9, 6), (9, 7)]
	def x7y7():
		if apple in ax7y7 or length_dict[0] < switch_length or not mowe(South):
			mowe(East)
			mowe(East)
			mowe(South)
			mowe(West)
			mowe(West)
		return x7y6
	def x7y6():
		mowe(South)
		return x7y5
	ax7y5 = [(8, 4), (8, 5), (9, 4), (9, 5)]
	def x7y5():
		if apple in ax7y5 or length_dict[0] < switch_length or not mowe(South):
			mowe(East)
			mowe(East)
			mowe(South)
			mowe(West)
			mowe(West)
		return x7y4
	ix7y4 = [(6, 3), (6, 4), (5, 3), (5, 4)]
	def x7y4():
		if apple in ix7y4 or length_dict[0] < switch_length or not mowe(South):
			mowe(West)
			mowe(West)
			mowe(South)
			mowe(East)
			mowe(East)
		return x7y3
	ax7y3 = [(8, 0), (8, 1), (8, 2), (8, 3), (9, 0), (9, 1), (9, 2), (9, 3)]
	def x7y3():
		if apple in ax7y3 or length_dict[0] < switch_length or not mowe(South):
			mowe(East)
			mowe(East)
			mowe(South)
			mowe(South)
			mowe(South)
			mowe(West)
			mowe(North)
			mowe(North)
			mowe(West)
		return x7y2

	ax7y2 = [(6, 0), (6, 1), (7, 0), (7, 1)]
	def x7y2():
		if apple in ax7y2 or length_dict[0] < switch_length or not mowe(West):
			mowe(South)
			mowe(South)
			mowe(West)
			mowe(North)
			mowe(North)
		return x6y2
	def x6y2():
		mowe(West)
		return x5y2
	ax5y2 = [(4, 0), (4, 1), (5, 0), (5, 1)]
	def x5y2():
		if apple in ax5y2 or length_dict[0] < switch_length or not mowe(West):
			mowe(South)
			mowe(South)
			mowe(West)
			mowe(North)
			mowe(North)
		return x4y2
	ix4y2 = [(4, 3), (4, 4), (3, 3), (3, 4)]
	def x4y2():
		if apple in ix4y2 or length_dict[0] < switch_length or not mowe(West):
			mowe(North)
			mowe(North)
			mowe(West)
			mowe(South)
			mowe(South)
		return x3y2
	ax3y2 = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]
	def x3y2():
		if apple in ax3y2 or length_dict[0] < switch_length or not mowe(West):
			mowe(South)
			mowe(South)
			mowe(West)
			mowe(West)
			mowe(West)
			mowe(North)
			mowe(East)
			mowe(East)
			mowe(North)
		return x2y2



	dir = x2y2
	while length_dict[0] > 0:
		dir = dir()
		apple = apple_dict[0]
	clear()
