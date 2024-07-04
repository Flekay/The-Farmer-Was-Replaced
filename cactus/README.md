# Cactus
This is a collection of cactus scripts that are used to farm cactus.

## Nice to know
- cactus can be harvested before it is fully grown


## Benchmarks
These benchmarks are without preplanting. Preplanting adds an additional 4k items/min.
Current record is 44.0k items/min with 6 cactus strat but i cant reproduce it.

| file          | items/min | setup time | seed efficiency |
| ------------- | --------- | ---------- | --------------- |
| cacti3.py     | 29.5k     | 0s         | 33.3%           |
| cacti6dict.py | 34.7k     | 182.34s    | 50%             |


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