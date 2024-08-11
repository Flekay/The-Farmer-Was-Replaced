# Cactus
This is a collection of cactus scripts that are used to farm cactus. Cactus will be reworked in the upcoming update so the corner strats will be obsolete. Post update cactus strat will be planting and sorting the entire farm.

## Nice to know
- cactus can be harvested before it is fully grown


## Benchmarks
These benchmarks are without preplanting. Preplanting adds an additional 4k items/min.
Current record is 47.5k items/min by @Danielrab with 6 cactus strat but i cant reproduce it. He also said he will publish it as soon as the update is out.

| file           | items/min | setup time | seed efficiency |
| -------------- | --------- | ---------- | --------------- |
| cacti3.py      | 29.5k     | 0s         | 33.3%           |
| cacti6dict.py  | 34.7k     | 182.34s    | 50%             |
| cacti6.py      | 38.7k     | 0s         | 50%             |
| inner.py       | 18.4k     | <0.3s      | 90%+            |
| oneshot.py     | 8k        | 0s         | 10%             |
| SwedishChef.py | 20k       | 0s         | 100%            |


## cacti3.py
This script plants 3 cactus in the corner without moving the player.
```plaintext
2
1 3
```

## cacti6dict.py + cacti6dict-helper.py
This script plants 6 cactus in the corner like this:
```plaintext
1
3 2
4 5 6
```

## cacti6.py
made by @Josh
This script uses the 6 cactus strat but without the dictionary.


## inner.py
This script plants the entire farm and then sorts the inner cactus. (world size - 2). There is probably a better moving pattern to use + scanning is not optimized. more of a proof of concept.


## oneshot.py
This script plants the entire farm in one go, with only 1 growing stage.
