# Bones
This is a collection of bones scripts that are used to farm dinos.

## Nice to know
- Dinos can be harvested before they are fully grown

## Benchmarks
| file           | items/min | setup time | note |
| -------------- | --------- | ---------- | ---- |
| abomination.py | 20.9k     | 30s        | best for stats and speedruns |
| farm_bone.py   | 20.8k     | 0s         | easy to use |

## abomination.py
Created by: @Danielrab
This file contains a function factory that creates functions that can be used to farm dinos very efficiently at the cost of readability, maintainability, and sanity.

## farm_bone.py
This file contains a function that can be used to farm dinos efficiently.

### farm_bone(num_bone=2000)
Farms the specified number of bones.

### pre_plant()
pre plants to get a nice boost at the start of the run. Only relevant for stat runs.

### setup_bone()
tills the field in the most efficient way possible after a clear.