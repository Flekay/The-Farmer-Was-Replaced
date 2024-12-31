file = "sub2"
sim_items = {
	Items.Power              : 1000000000,
	Items.Hay                : 1000000000,
	Items.Wood               : 1000000000,
}
speedup = 2
seed = -1
timings = []
while True:
	time = simulate(file, Unlocks, sim_items, {}, seed, speedup)
	timings.append(time)
	quick_print("min", str(min(timings)), "max", str(max(timings)), "avg", str(sum(timings) / len(timings)))
	