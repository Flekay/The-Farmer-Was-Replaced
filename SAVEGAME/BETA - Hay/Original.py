set_world_size(5)
MOVES = generate_moves_light()
grid = [
	[Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass],
	[Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass],
	[Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass],
	[Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass],
	[Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass, Entities.Grass],
]
grid0 = grid[0]
grid1 = grid[1]
grid2 = grid[2]
grid3 = grid[3]
grid4 = grid[4]
contin = True

init_move_0()

for _ in range(37):
	default_move_0()

for dir in MOVES:
	ent = get_entity_type()
	if ent == Entities.Grass or ent == Entities.Tree:
		harvest()
		plant(Entities.Bush)
	move(dir)

while num_items(Items.Hay) < 100000:
	if Entities.Bush in get_companion():
		use_item(Items.Fertilizer)
		use_item(Items.Weird_Substance)
	harvest()
	
quick_print(num_items(Items.Fertilizer))