sim_items = {
	Items.Hay                : 1000000000,
	Items.Wood               : 1000000000,
	Items.Carrot             : 1000000000,
	Items.Pumpkin            : 1000000000,
	Items.Power              : 1000000000,
	Items.Cactus             : 1000000000,
	Items.Bone               : 1000000000,
	Items.Weird_Substance    : 1000000000,
	Items.Gold               : 1000000000,
	Items.Fertilizer         : 1000000000,
	Items.Water              : 1000000000,
}
moves = [
    North,East,North,East,North,East,North,East,North,East,
    North,East,North,East,North,North,North,North,North,North,
    North,North,North,West,West,South,West,South,West,South,
    West,South,West,South,East,East,North,East,East,North,
    East,North,North,North,North,North,West,South,West,South,
    West,South,South,West,North,North,North,North,East,East,
    South,West,South,West,West,South,South,South,East,East,
    South,West,South,East,East,East,North,East,North,West,
    North,North,North,North,North,North,North,North,East,
    South,South,South,East,East,South,South,South,South,West,
    South,East,South,South,West,North,West,West,West,South,
    West,South,South,East,North,East,South,East,East,North,
    East,East,East,South,South,East,South,South,South,East,
    East,North,North,North,East,South,South,South,South,West,
    West,North,North,North,North,North,North,North,West,North,
    West,West,West,North,North,North,West,West,South,West,South,
    West,West,West,South,West,North,North,West,North,North,North,
    North,North,East,South,South,South,East,South,East,South,
    East,North,East,North,East,East,East,North,West,West,North,
    North,North,North,West,North,East,North,East,East,East,East,
    North,North,North,North,North,North,North,North,North,North,
    North,North,West,West,West,South,East,East,North,North,East,
    North,North,North,North,East,North,East,East,South,South,East,
    East,East,East,East,South,North,North,North,East,North
]
speedup = 255
seed = 831051
for i in range(len(moves)):
	i = i + 166
	sim_globals = {
		"moves" : moves[:i],
		"index":i
	}
	ime2 = simulate("preSort1000", Unlocks, sim_items, sim_globals, seed, speedup)
	#quick_print(i, ":", time, time2)