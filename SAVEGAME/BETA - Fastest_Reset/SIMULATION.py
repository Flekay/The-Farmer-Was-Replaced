filename = "main"
speedup = 256
empty = {}

for itr in range(10**305):
	seed = randint(0, 99999999)
	time = simulate(filename, {}, {}, {}, seed, speedup)
	#time = simulate(filename, empty, empty, empty, seed, speedup)
	if not time:
		continue
	quick_print(adjust_length(itr, 4), adjust_length(seed, 16), strtime(time))
		