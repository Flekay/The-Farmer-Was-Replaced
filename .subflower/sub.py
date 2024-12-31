files = [
	"sub34",
]
sim_items = {
	Items.Carrot             : 1000000000,
}
speedup = 25600
seed = -1
timings = {}
for file in files:
	timings[file] = []
sim_globals = {}

while True:
	# Randomize seed
	seed = randint(0, 99999999)

	# Run simulation for each file
	for file in files:
		time = simulate(file, Unlocks, sim_items, sim_globals, seed, speedup)
		timings[file].append(time)

	# generate output string
	string = ""
	fastest_name = ""
	fastest_time = 999999999
	for file in files:
		avg = sum(timings[file]) / len(timings[file])
		if avg < fastest_time:
			fastest_time = avg
			fastest_name = file
		string += file + ": " + strtime(avg) + " "
	if len(files) > 1:
		prefix_string = "Fastest: " + fastest_name + " "
		quick_print(prefix_string + string)
	else:
		quick_print("avg",strtime(avg),"current",strtime(time))
