# Cactus
This is a collection of cactus scripts that are used to farm cactus. Cactus will be reworked in the upcoming update so the corner strats will be obsolete. Post update cactus strat will be planting and sorting the entire farm.

## Nice to know
- cactus can be harvested before it is fully grown


## Benchmarks
These benchmarks are without preplanting. Preplanting adds an additional 4k items/min.
Current record is 47.5k items/min by @Danielrab with 6 cactus strat but i cant reproduce it. He also said he will publish it as soon as the update is out.

| file          | items/min | setup time | seed efficiency |
| ------------- | --------- | ---------- | --------------- |
| cacti3.py     | 29.5k     | 0s         | 33.3%           |
| cacti6dict.py | 34.7k     | 182.34s    | 50%             |
| inner.py      | 18.4k     | <0.3s      | 90%+            |


## cacti3.py
This script plants 3 cactus in the corner without moving the player.

## cacti6dict.py + cacti6dict-helper.py
This script plants 6 cactus in the corner like this:
```plaintext
1
4 2
3 5 6
```
This should be the fastest way to plant cactus, but im still missing some optimizations. no.1 uses functions instead of a precalculated dict so idk. Also heard someting about moving cactus West on position 4.

## inner.py
This script plants the entire farm and then sorts the inner cactus. (world size - 2). There is probably a better moving pattern to use + scanning is not optimized. more of a proof of concept.
