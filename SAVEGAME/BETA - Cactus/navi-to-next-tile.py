def navi_to_next_tile(size=get_world_size()):
	if size == 3:
		return [
			[East, North, North],
			[East, West, South],
			[North, North, West]
		]
	if size == 4:
		return [
			[North, North, North, East],
			[West, East, South, South],
			[West, North, North, East],
			[West, South, South, South]
		]
	if size == 5:
		return [
			[North, East, North, East, North],
			[East, South, West, East, West],
			[North, North, West, East, West],
			[East, South, South, South, West],
			[North, North, North, North, West]
		]
	if size == 6:
		return [
			[East, South, South, South, South, South],
			[East, North, North, East, North, West],
			[East, West, East, South, West, South],
			[East, West, North, North, North, West],
			[East, West, South, South, South, South],
			[North, North, North, North, North, West]
		]
	if size == 7:
		return [
			[North, North, North, North, North, North, East],
			[West, South, South, South, South, South, East],
			[North, North, North, North, East, West, East],
			[West, East, South, South, East, West, East],
			[West, North, East, West, East, West, East],
			[West, South, South, West, East, West, East],
			[North, North, North, West, North, West, North]
		]
	if size == 8:
		return [
			[North, North, North, North, North, North, North, East],
			[West, East, South, South, South, South, South, East],
			[West, East, North, North, North, East, West, East],
			[West, East, West, South, South, East, West, East],
			[West, North, North, North, West, East, West, East],
			[West, South, South, South, South, South, West, East],
			[North, North, North, North, North, North, West, East],
			[West, South, South, South, South, South, South, South]
		]
	if size == 9:
		return [
			[North, North, North, North, North, North, North, North, East],
			[West, South, East, South, South, South, South, South, South],
			[North, West, North, North, North, North, North, North, East],
			[West, South, South, South, East, South, South, South, South],
			[North, North, North, West, North, North, North, North, East],
			[West, South, South, South, South, South, East, South, South],
			[North, North, North, North, North, West, North, North, East],
			[West, South, South, South, South, South, South, South, East],
			[North, North, North, North, North, North, North, West, North]
		]
	if size == 10:
		return [
			[North, North, North, North, North, North, North, North, North, East],
			[West, East, South, South, South, South, South, South, South, East],
			[West, East, North, East, North, East, North, East, West, East],
			[West, East, West, East, West, East, West, East, West, East],
			[West, South, West, North, West, North, West, North, West, East],
			[North, East, West, East, South, East, South, East, South, East],
			[West, East, West, East, West, East, West, East, West, East],
			[West, East, West, South, West, South, West, South, West, East],
			[West, North, North, North, North, North, North, North, West, East],
			[West, South, South, South, South, South, South, South, South, South]
		]