## Failed / Inefficient scripts
list of incomplete, inefficient or non-working scripts. So you don't have to waste time on them.

## BENCHMARK 

### bench
`bench()` simple function to test the performance `moveTo()` functions.

## POWER
### powerTill()
`powerTill()` is a function that uses the `till()` on sunflowers until a level 15 petal spawns. The idea behind this was to harvest only one sunflower at a time, to always have the maximum yield bonus. However, the function is not efficient enough to be used in a speedrun.
- produces ~120 power / second
- high seed consumption

### powerFart()
`powerFart()` only plants sunflowers with petal level 7 and then harvests and fertilizes the last planted sunflower. Only ment to be used to push the power stat to the max.
- produces ~1013 power / second
- high fertilizer consumption

### powerSkip()
`powerSkip()` is the most promising approach to farm power. It skips level 7 petals. But i want to add the option to fertilize the sunflowers to not loose the waiting for growth time, before replacing the old function.
- produces ~5% more power than `farmpower()`

## pumpkin

### pumpkinFart()
`pumpkinFart()` is a single round of planting and harvesting pumpkins. Just for testing purposes.
- produces 120k pumpkins / 60s
- netto 92k pumpkins / 60s
- high fertilizer consumption

### pumpkinReRun()
`pumpkinReRun()` plants in the first round. pumpkinFarts() the second round. Just for testing purposes. Almost identical to `pumpkinFart()` but with way less fertilizer consumption.
- produces 120k pumpkins / 60s
- netto 121k pumpkins / 60s

### pumpkinFarmStats()
`pumpkinFarmStats()` is a function to maximize the pumpkin yield. Without looking at the fertilizer consumption. Maybe with some optimization or luck it could produce 140k pumpkins / 60s.
- produces +130k pumpkins / 60s
- just for stats

### pumpkinNoFart()
`pumpkinNoFart()` is a function to maximize the pumpkin yield. Without using the fertilizer. Might be useful for speedruns. Not optimized yet.
- produces 50k pumpkins / 60s
- 100% netto
- Not optimized

### pumpkinTiny()
`pumpkinTiny()` plants in the first round. harvests in the second round. Terrible performance. But maybe good enough to finance the first fertilizer in a speedrun.
- netto 15k pumpkins / 60s


## BONES

### blackCocks()
`blackCocks()` this function pre plants black dinos and harvests them.
- produces +20k bones / 60s
- not viable for speedrun

### mixedCocks()
`mixedCocks()` this function pre plants all dinos and harvests them.
- produces less bones than `blackCocks()`
- not viable for speedrun