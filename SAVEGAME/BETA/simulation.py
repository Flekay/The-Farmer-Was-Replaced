filename = [
	"SwedishChef",
	"farm_cacti_once",
	"farm_cacti_twice",
	"f3",
]
filename = [
	"noOpt",
	"preSort",
]
filename = [
	"preSort1000",
	"preSort99",
	"preSort93",
]
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
speedup = 2
seed = 831051
timings = []
simulate(filename[0], Unlocks, sim_items, sim_globals, seed, speedup)
for file in filename:
	time = simulate(file, Unlocks, sim_items, sim_globals, seed, speedup)
	#time = simulate(file, Unlocks, sim_items, sim_globals, seed, speedup)
	timings.append(time)


quick_print("")
quick_print(timings)
quick_print("")
# fastest name
for i in range(len(timings)):
	if timings[i] == min(timings):
		quick_print(filename[i], "is the fastest at", timings[i])
quick_print("")
# slowest
for i in range(len(timings)):
	if timings[i] == max(timings):
		quick_print(filename[i], "is the slowest at", timings[i])