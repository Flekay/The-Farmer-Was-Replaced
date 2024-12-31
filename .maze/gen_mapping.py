import os

def generate_scan_functions():
	directions = ['north', 'east', 'south', 'west']
	grid_size = 10

	for x in range(grid_size):
		for y in range(grid_size):
			function_name = f"scan_{x}_{y}"
			bDirList = []
			index = x + 10 * y

			# Generate move checks for each direction
			move_checks = []
			for i, d in enumerate(directions):
				next_x, next_y = x, y
				if d == 'north': next_y += 1
				elif d == 'east': next_x += 1
				elif d == 'south': next_y -= 1
				elif d == 'west': next_x -= 1

				opposite_dir = directions[(i + 2) % 4]
				if 0 <= next_x < grid_size and 0 <= next_y < grid_size:
					bDirList.append(f"b{d.capitalize()}")
					move_checks.append(
						f"	b{d.capitalize()} = lb{opposite_dir.capitalize()}(nop, scan_{d})(scan_{next_x}_{next_y}, {next_x + 10 * next_y}, dist)")
				else:
					bDirList.append("false")

			# Generate function code
			params = ", ".join([f"lb{d.capitalize()}" for d in directions])
			func_code = f"""def {function_name}({params}, dist):
{chr(10).join(move_checks)}
	if measure():
		TREASURE_POS[0] = {index}
	grid{x}[{y}] = [{", ".join(bDirList)}]"""
			yield func_code

def write_scan_functions_to_file(filename):
	with open(os.path.join(os.path.dirname(__file__), filename), 'w') as file:
		for function_code in generate_scan_functions():
			file.write(function_code + "\n")

write_scan_functions_to_file('generated_scan_functions.py')
