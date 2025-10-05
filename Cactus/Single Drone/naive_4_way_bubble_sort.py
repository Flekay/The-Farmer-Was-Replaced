def simple_swaping():
	current_measure = measure()
	west_measure = measure(West)
	north_measure = measure(North)
	south_measure = measure(South)
	east_measure = measure(East)
	temp_measure = None
	swapped = False
	while True:
		if current_measure < west_measure and swap(West):
			temp_measure = west_measure
			west_measure = current_measure
			current_measure = temp_measure
			swapped = True
			continue
		if current_measure < south_measure and swap(South):
			temp_measure = south_measure
			south_measure = current_measure
			current_measure = temp_measure
			swapped = True
			continue
		if current_measure > east_measure and swap(East):
			temp_measure = east_measure
			east_measure = current_measure
			current_measure = temp_measure
			swapped = True
			continue
		if current_measure > north_measure and swap(North):
			temp_measure = north_measure
			north_measure = current_measure
			current_measure = temp_measure
			swapped = True
			continue
		break
	return swapped

_OPP = {North: South, South: North, East: West, West: East}
def naive_4_way_bubble_sort(grid=None):

	moves = list()
	for y in range(get_world_size()):
		for x in range(get_world_size()-1):
			if y % 2:
				moves.append(West)
			else:
				moves.append(East)
		moves.append(North)
	moves.pop()

	moves2 = list()
	for i in range(len(moves)-1, -1, -1):
		moves2.append(_OPP[moves[i]])

	moves3 = list()
	for x in range(get_world_size()):
		for y in range(get_world_size()-1):
			if x % 2:
				moves3.append(South)
			else:
				moves3.append(North)
		moves3.append(East)
	moves3.pop()

	moves4 = list()
	for i in range(len(moves3)-1, -1, -1):
		moves4.append(_OPP[moves3[i]])

	DIR = [moves, moves2, moves3, moves4]
	unfinished = True
	i = 0
	while unfinished:
		unfinished = False
		simple_swaping()
		for dir in DIR[i]:
			move(dir)
			if simple_swaping():
				unfinished = True
		i = (i + 1) % len(DIR)
