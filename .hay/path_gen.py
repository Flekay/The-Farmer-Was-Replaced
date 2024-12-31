import os

def generate_moves(world_size):
	moves = []
	pos_x = 0
	pos_y = 0
	for i in range(world_size**2):
		if pos_x % world_size == pos_y % world_size:
			pos_x -= 1
			moves.append("West")
		else:
			pos_y += 1
			moves.append("North")
	return moves

# Replace static MOVES with generated ones
world_size = 5
MOVES = generate_moves(world_size)
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

	functions.append(f"def move_{i}(func):")
	functions.append(f"\tfunc({current_x}, {current_y}, {step_index})")

	if i + 1 < len(MOVES):
		functions.append(f"\tmove({dir})")
		functions.append(f"\tmove_{i+1}(func)")
	else:
		functions.append(f"\tmove({dir})")

	# Update position for next iteration
	pos[0] = (pos[0] + directions[dir][0]) % world_size
	pos[1] = (pos[1] + directions[dir][1]) % world_size
	i += 1




# Write to file
with open(os.path.join(os.path.dirname(__file__), "stateMachine.py"), "w") as f:
	f.write("\n".join(functions))




# func(x, y, x*10 + y)
# def move_0(func):
# 	func(0, 0, 0)
# 	move(dir)
# 	move_1(func)
