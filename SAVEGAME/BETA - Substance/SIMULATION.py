file = "sub35"
compare = "f0"
sim_items = {
	Items.Carrot             : 1000000000,
}
speedup = 256
seed = -1
timings = []
altTimings = []

while True:
	seed = randint(0, 99999999)
	time = simulate(file, Unlocks, sim_items, {}, seed, speedup)
	timings.append(time)
	if compare:
		time2 = simulate(compare, Unlocks, sim_items, {}, seed, speedup)
		altTimings.append(time2)
		avg = sum(timings) / len(timings)
		avg2 = sum(altTimings) / len(altTimings)
		if avg < avg2:
			quick_print("Original version is faster")
		else:
			quick_print("Alternative version is faster")
		quick_print("Original:", avg, "Alternative:", avg2)
	else:
		quick_print("min", min(timings), "max", max(timings), "avg", sum(timings) / len(timings))