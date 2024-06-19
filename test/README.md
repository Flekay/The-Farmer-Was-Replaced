## Failed / Inefficient scripts
list of incomplete, inefficient or non-working scripts. So you don't have to waste time on them.


## POWER
### powerTill()
`powerTill()` is a function that uses the `till()` on sunflowers until a level 15 petal spawns. The idea behind this was to harvest only one sunflower at a time, to always have the maximum yield bonus. However, the function is not efficient enough to be used in a speedrun.
- produces ~120 power / second
- high seed cost

### powerFart()
`powerFart()` only plants sunflowers with petal level 7 and then harvests and fertilizes the last planted sunflower. Only ment to be used to push the power stat to the max.
- produces ~1013 power / second
- high fertilizer cost

### powerSkip()
`powerSkip()` is the most promising approach to farm power. It skips level 7 petals. But i want to add the option to fertilize the sunflowers to not loose the waiting for growth time, before replacing the old function.
- produces ~5% more power than `farmpower()`

## BONES
### farmBoneHard()
`farmBoneHard()` is the same as `farmBone()` but hardcoded. It is a bit faster than `farmBone()` but still far from world record(19.2k bones / minute).