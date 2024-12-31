# sorting_func = {
# 	"North": NorthSort,
# 	"East": EastSort,
# 	"South": SouthSort,
# 	"West": WestSort,
# 	"NorthEast": NorthEastSort,
# 	"SouthEast": SouthEastSort,
# 	"SouthWest": SouthWestSort,
# 	"NorthWest": NorthWestSort,
# 	"NorthSouth": NorthSouthSort,
# 	"EastWest": EastWestSort,
# 	"NorthEastSouth": NorthEastSouthSort,
# 	"EastSouthWest": EastSouthWestSort,
# 	"SouthWestNorth": SouthWestNorthSort,
# 	"WestNorthEast": WestNorthEastSort,
# 	"simple_swap": simple_swap,
# }

def simple_swap():
	if measure(West) > measure():
		swap(West)
	if measure(North) < measure():
		swap(North)
	if measure(South) > measure():
		swap(South)
	if measure(East) < measure():
		swap(East)
	if measure(West) > measure():
		swap(West)
	if measure(North) < measure():
		swap(North)
	if measure(South) > measure():
		swap(South)
	if measure(East) < measure():
		swap(East)

def NorthSort():
	if measure(North) < measure():
		swap(North)

def EastSort():
	if measure(East) < measure():
		swap(East)

def SouthSort():
	if measure(South) > measure():
		swap(South)

def WestSort():
	if measure(West) > measure():
		swap(West)

def NorthEastSort():
	if measure(North) < measure():
		swap(North)
	if measure(East) < measure():
		swap(East)
	if measure(North) < measure():
		swap(North)

def SouthEastSort():
	if measure(South) > measure():
		swap(South)
	if measure(East) < measure():
		swap(East)
	if measure(South) > measure():
		swap(South)

def SouthWestSort():
	if measure(South) > measure():
		swap(South)
	if measure(West) > measure():
		swap(West)
	if measure(South) > measure():
		swap(South)

def NorthWestSort():
	if measure(North) < measure():
		swap(North)
	if measure(West) > measure():
		swap(West)
	if measure(North) < measure():
		swap(North)

def NorthSouthSort():
	if measure(North) < measure():
		swap(North)
	if measure(South) > measure():
		swap(South)
	if measure(North) < measure():
		swap(North)

def EastWestSort():
	if measure(East) < measure():
		swap(East)
	if measure(West) > measure():
		swap(West)
	if measure(East) < measure():
		swap(East)

def NorthEastSouthSort():
	if measure(North) < measure():
		swap(North)
	if measure(East) < measure():
		swap(East)
	if measure(South) > measure():
		swap(South)
	if measure(North) < measure():
		swap(North)
	if measure(East) < measure():
		swap(East)
	if measure(South) > measure():
		swap(South)

def EastSouthWestSort():
	if measure(East) < measure():
		swap(East)
	if measure(South) > measure():
		swap(South)
	if measure(West) > measure():
		swap(West)
	if measure(East) < measure():
		swap(East)
	if measure(South) > measure():
		swap(South)
	if measure(West) > measure():
		swap(West)

def SouthWestNorthSort():
	if measure(South) > measure():
		swap(South)
	if measure(West) > measure():
		swap(West)
	if measure(North) < measure():
		swap(North)
	if measure(South) > measure():
		swap(South)
	if measure(West) > measure():
		swap(West)
	if measure(North) < measure():
		swap(North)

def WestNorthEastSort():
	if measure(West) > measure():
		swap(West)
	if measure(North) < measure():
		swap(North)
	if measure(East) < measure():
		swap(East)
	if measure(West) > measure():
		swap(West)
	if measure(North) < measure():
		swap(North)
	if measure(East) < measure():
		swap(East)
