# Cactus
This is a collection of cactus scripts that are used to farm cactus. Cactus will be reworked in the upcoming update so the corner strats will be obsolete. Post update cactus strat will be planting and sorting the entire farm.

## Nice to know
- cactus can be harvested before it is fully grown


## Benchmarks
These benchmarks are without preplanting. Preplanting adds an additional 4k items/min.
Current record is 47.5k items/min by @Danielrab with 6 cactus strat but i cant reproduce it. He also said he will publish it as soon as the update is out.

| file           | items/min | setup time | seed efficiency |
| -------------- | --------- | ---------- | --------------- |
| inner.py       | 537k      | <0.3s      | 90%+            |
| oneshot.py     | 190k      | 0s         | 10%             |
| SwedishChef.py | 500k      | 0s         | 100%            |


## inner.py
This script plants the entire farm and then sorts the inner cactus. (world size - 2). There is probably a better moving pattern to use + scanning is not optimized. more of a proof of concept.


## oneshot.py
This script plants the entire farm in one go, with only 1 growing stage.

## SwedishChef.py
made by @SwedishChef
This script plants the entire farm and then sorts the cactus.
