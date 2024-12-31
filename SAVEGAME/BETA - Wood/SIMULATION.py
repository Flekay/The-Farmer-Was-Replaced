filename = "sub"
sim_items = {
	Items.Power              : 1000000000,
}
speedup = 1
seed = -1
time = simulate(filename, Unlocks, sim_items, {}, seed, speedup)
quick_print(time)