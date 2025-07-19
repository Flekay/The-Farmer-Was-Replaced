border = get_world_size()
area = border * border

# Sort current field cell
def CellSort(x, y):
	
	Sorted = False
	LocalSorted = False
	
	# Try to sort until can't sort anything
	while not LocalSorted:
		CurHeight = measure()
		
		if (CurHeight < measure(West)) and (x != 0):
			swap(West)
			Sorted = True
			continue
		if (CurHeight < measure(South)) and (y != 0):
			swap(South)
			Sorted = True
			continue
		if (CurHeight > measure(East)) and (x != (border - 1)):
			swap(East)
			Sorted = True
			continue
		if (CurHeight > measure(North)) and (y != (border - 1)):
			swap(North)
			Sorted = True
			continue
			
		LocalSorted = True
		
	return Sorted

# Move up in zigzag mode and sort
def DoSortingUp():

	def GoUp(x, y):
		IsEven = ((y % 2) == 0)
		
		if IsEven:
			if (x < (border - 1)):
				move(East)
				x += 1
				return x, y
		else:
			if (x > 0):
				move(West)
				x -= 1
				return x, y
				
		if (y < (border - 1)):
			move(North)
			y += 1
			
		return x, y
	
	SortedCount = 0
	x, y = 0, 0
	
	for _ in range(area):
		if CellSort(x, y):
			SortedCount += 1
		x, y = GoUp(x, y)
			
	return SortedCount

# Move down in zigzag mode and sort
def DoSortingDown():
	
	def GoDown(x, y):
		IsEven = ((y % 2) == 0)
		
		if not IsEven:
			if (x < (border - 1)):
				move(East)
				x += 1
				return x, y
		else:
			if (x > 0):
				move(West)
				x -= 1
				return x, y
				
		if (y > 0):
			move(South)
			y -= 1
			
		return x, y
		
	SortedCount = 0
	x, y = 0, border - 1
	
	for _ in range(area):
		if CellSort(x, y):
			SortedCount += 1
		x, y = GoDown(x, y)

	return SortedCount

# This algorithm gives a result of ~16.2 s for a 10x10 field (without pre-sort while planting)
# The algorithm is not the most optimal, since it makes useless passes over the already sorted bottom and top rows each iteration
def DoCocktailSort():
	while True:
		# If one of the two methods returns 0, it means that the field is sorted
		if DoSortingUp() == 0:
			return
		if DoSortingDown() == 0:
			return