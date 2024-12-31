file = "f2"
compare = ""
sim_items = {
	Items.Power             : 1000000000,
	Items.Pumpkin           : 1000000000,
}

speedup = 256
seed = -1
timings = []
altTimings = []
sim_globals = {
	"switch" : 0
}

for i in range(1):
	seed = randint(0, 99999999)
	#seed = 17426740
	#quick_print(seed)
	sim_globals = {
		"switch" : i
	}
	time = simulate(file, Unlocks, sim_items, sim_globals, seed, speedup)
	quick_print(i//1, time, seed)
	continue
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