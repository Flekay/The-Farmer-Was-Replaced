file = "sub4"
sim_items = {
	Items.Power              : 1000000000,
}
speedup = 256
seed = -1
time = simulate(file, Unlocks, sim_items, {}, seed, speedup)
quick_print(time)