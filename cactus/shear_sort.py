# any move_to function can be used.
# /movement/wrapping_shortest_path/navi_to_list.py
from navi_to_deltalist import *

world_size = get_world_size()
def shear_sort(grid):
	# Row phase: snake-order sort on each row.
	for i in range(world_size):
		if i % 2 == 0:
			changed = True
			while changed:
				changed = False
				# Even row: ascending (South → North, i.e. increasing j)
				for j in range(world_size):
					if j<world_size - 1:
						if grid[i][j] > grid[i][j+1]:
							navi_to_deltalist(i, j)
							swap(North)  # swap with neighbor at (i, j+1)
							grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]
							changed = True
					if i<world_size - 1:
						if grid[i][j] > grid[i+1][j]:
							navi_to_deltalist(i, j)
							swap(East)  # swap with neighbor at (i+1, j)
							grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
							changed = True
		else:
			changed = True
			while changed:
				changed = False
				# Odd row: descending (North → South, i.e. decreasing j)
				for j in range(world_size-1, 0, -1):
					if j>0:
						if grid[i][j] < grid[i][j-1]:
							navi_to_deltalist(i, j)
							swap(South)  # swap with neighbor at (i, j-1)
							grid[i][j], grid[i][j-1] = grid[i][j-1], grid[i][j]
							changed = True
					if i<world_size - 1:
						if grid[i][j] > grid[i+1][j]:
							navi_to_deltalist(i, j)
							swap(East)  # swap with neighbor at (i+1, j)
							grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
							changed = True

	# Column phase: sort each column in ascending order (West → East, i.e. increasing i)
	for j in range(world_size):
		changed = True
		while changed:
			changed = False
			for i in range(world_size - 1):
				if grid[i][j] > grid[i+1][j]:
					navi_to_deltalist(i, j)
					swap(East)  # swap with neighbor at (i+1, j)
					grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
					changed = True
	return grid
