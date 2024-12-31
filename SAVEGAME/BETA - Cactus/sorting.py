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
	current_measure = measure()
	west_measure = measure(West)
	north_measure = measure(North)
	south_measure = measure(South)
	east_measure = measure(East)
	temp_measure = None
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
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
	current_measure = measure()
	east_measure = measure(East)
	north_measure = measure(North)
	temp_measure = None
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)

def SouthEastSort():
	current_measure = measure()
	east_measure = measure(East)
	south_measure = measure(South)
	temp_measure = None
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)

def SouthWestSort():
	current_measure = measure()
	south_measure = measure(South)
	west_measure = measure(West)
	temp_measure = None
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)


def NorthWestSort():
	current_measure = measure()
	north_measure = measure(North)
	west_measure = measure(West)
	temp_measure = None
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)

def NorthSouthSort():
	current_measure = measure()
	north_measure = measure(North)
	south_measure = measure(South)
	temp_measure = None
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)

def EastWestSort():
	current_measure = measure()
	east_measure = measure(East)
	west_measure = measure(West)
	temp_measure = None
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)

def NorthEastSouthSort():
	current_measure = measure()
	north_measure = measure(North)
	east_measure = measure(East)
	south_measure = measure(South)
	temp_measure = None
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)


def EastSouthWestSort():
	current_measure = measure()
	east_measure = measure(East)
	south_measure = measure(South)
	west_measure = measure(West)
	temp_measure = None
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)

def SouthWestNorthSort():
	current_measure = measure()
	south_measure = measure(South)
	west_measure = measure(West)
	north_measure = measure(North)
	temp_measure = None
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)
	if south_measure > current_measure:
		temp_measure = south_measure
		south_measure = current_measure
		current_measure = temp_measure
		swap(South)
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)

def WestNorthEastSort():
	current_measure = measure()
	west_measure = measure(West)
	north_measure = measure(North)
	east_measure = measure(East)
	temp_measure = None
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)
	if west_measure > current_measure:
		temp_measure = west_measure
		west_measure = current_measure
		current_measure = temp_measure
		swap(West)
	if north_measure < current_measure:
		temp_measure = north_measure
		north_measure = current_measure
		current_measure = temp_measure
		swap(North)
	if east_measure < current_measure:
		temp_measure = east_measure
		east_measure = current_measure
		current_measure = temp_measure
		swap(East)
		