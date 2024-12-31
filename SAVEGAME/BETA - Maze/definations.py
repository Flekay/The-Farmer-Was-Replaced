
def true(a, b):
	return a

def false(a, b):
	return b

def nop(n0=None, n1=None, n2=None, n3=None, n4=None, n5=None, n6=None, n7=None, n8=None, n9=None):
	return true

def scan_north(tile, index, dist):
	if move(North):
		dist += 1
		DIST_TO_BASE[index] = dist
		DIR_TO_BASE[index] = South
		tile(true, false, false, false, dist)
		move(South)
		return true
	return false

def scan_east(tile, index, dist):
	if move(East):
		dist += 1
		DIST_TO_BASE[index] = dist
		DIR_TO_BASE[index] = West
		tile(false, true, false, false, dist)
		move(West)
		return true
	return false

def scan_south(tile, index, dist):
	if move(South):
		dist += 1
		DIST_TO_BASE[index] = dist
		DIR_TO_BASE[index] = North
		tile(false, false, true, false, dist)
		move(North)
		return true
	return false

def scan_west(tile, index, dist):
	if move(West):
		dist += 1
		DIST_TO_BASE[index] = dist
		DIR_TO_BASE[index] = East
		tile(false, false, false, true, dist)
		move(East)
		return true
	return false
	