import os

MOVES = ["North","East","East","East","East","North","West","West","West","West","North","East","East","East","East","North","West","West","West","West","North","East","East","East","East","North","West","West","West","West","North","East","East","East","East","North","West","West","West","West","North","East","East","East","East","East","East","East","East","East","South","West","West","West","West","South","East","East","East","East","South","West","West","West","West","South","East","East","East","East","South","West","West","West","West","South","East","East","East","East","South","West","West","West","West","South","East","East","East","East","South","West","West","West","West","West","West","West","West","West"]
world_size = 10
directions = {
	"North": [0, 1],
	"East": [1, 0],
	"South": [0, -1],
	"West": [-1, 0]
}

functions = []
pos = [0, 0]
i = 0

for dir in MOVES:
	current_x = pos[0]
	current_y = pos[1]
	step_index = current_x * 10 + current_y


	functions.append(f"def move_{i}():")

	if i + 1 < len(MOVES):
		functions.append(f"\tmove({dir})")
		functions.append(f"\ttill()")
		functions.append(f"\tmove_{i+1}()")
	else:
		functions.append(f"\tmove({dir})")
		functions.append(f"\ttill()")

	# Update position for next iteration
	pos[0] = (pos[0] + directions[dir][0]) % world_size
	pos[1] = (pos[1] + directions[dir][1]) % world_size
	i += 1

# Write to file
with open(os.path.join(os.path.dirname(__file__), "mighty_moves.py"), "w") as f:
	f.write("\n".join(functions))
