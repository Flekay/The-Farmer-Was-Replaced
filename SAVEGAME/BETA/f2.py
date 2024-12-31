filename = "f0"
sim_unlocks = Unlocks
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
sim_globals = {"a" : 13}
seed = 58008
speedup = 256
run_time = simulate(
		filename, sim_unlocks,
		sim_items, sim_globals, seed, speedup
	)