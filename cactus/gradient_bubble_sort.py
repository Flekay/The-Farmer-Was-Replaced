# any move_to function can be used.
# /movement/wrapping_shortest_path/navi_to_list.py
from navi_to_list import *

def gradient_bubble_sort(grid):
	rr = range(get_world_size())
	wsm1 = get_world_size() - 1
	global_changed = True
	while global_changed:
		global_changed = False
		for x in rr:
			gridx = grid[x]
			for y in rr:
				# Swap with right neighbor if needed.
				yp1 = y + 1
				if y < wsm1 and gridx[y] > gridx[yp1]:
					temp = gridx[y]
					gridx[y] = gridx[yp1]
					gridx[yp1] = temp

					global_changed = True
					navi_to_list(x, y)
					swap(North)
					offset = y - 1
					offset2 = y
					while offset2 and gridx[offset2] < gridx[offset]:
						navi_to_list(x, offset2)
						swap(South)
						temp = gridx[offset2]
						gridx[offset2] = gridx[offset]
						gridx[offset] = temp

						offset += 1
						offset2 += 1
				# Swap with bottom neighbor if needed.
				xp1 = x + 1
				if x < wsm1:
					gridxp1 = grid[xp1]
				else:
					continue
				if gridx[y] > gridxp1[y]:
					# use temp variable to swap
					temp = gridx[y]
					gridx[y] = gridxp1[y]
					gridxp1[y] = temp

					global_changed = True
					navi_to_list(x, y)
					swap(East)
					offset = x - 1
					offset2 = x
					while offset2 and grid[offset2][y] < grid[offset][y]:
						navi_to_list(offset2, y)
						swap(West)
						gridoffset = grid[offset]
						gridoffset2 = grid[offset2]
						temp = gridoffset2[y]
						gridoffset2[y] = gridoffset[y]
						gridoffset[y] = temp

						offset += 1
						offset2 += 1
