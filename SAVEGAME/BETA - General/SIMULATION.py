filename = [
	"SwedishChef",
]
sim_items = {
	Items.Hay                : 1000000000,
	Items.Wood               : 1000000000,
	Items.Carrot             : 1000000000,
	Items.Pumpkin            : 1000000000,
	Items.Power              : 1000000000,
	Items.Cactus             : 1000000000,
	Items.Gold               : 1000000000,
	Items.Fertilizer         : 1000000000,
	Items.Water              : 1000000000,
}
speedup = 256
seed = -1
time = simulate(filename[0], Unlocks, sim_items, {}, seed, speedup)
quick_print(time)