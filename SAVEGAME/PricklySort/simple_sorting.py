def simple_swaping():
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


def NorthSorting():
	if measure(North) < measure():
		swap(North)

def EastSorting():
	if measure(East) < measure():
		swap(East)

def SouthSorting():
	if measure(South) > measure():
		swap(South)

def WestSorting():
	if measure(West) > measure():
		swap(West)

def NorthEastSorting():
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

def SouthEastSorting():
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

def SouthWestSorting():
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


def NorthWestSorting():
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

def NorthSouthSorting():
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

def EastWestSorting():
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

def NorthEastSouthSorting():
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


def EastSouthWestSorting():
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

def SouthWestNorthSorting():
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

def WestNorthEastSorting():
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
		