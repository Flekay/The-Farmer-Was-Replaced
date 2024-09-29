# Cactus
This is a collection of cactus scripts that are used to farm cactus.

## Benchmarks
| file           | items/min | setup time |
| -------------- | --------- | ---------- |
| inner.py       | 537k      | <0.3s      |
| oneshot.py     | 190k      | 0s         |
| SwedishChef.py | 500k      | 0s         |


## inner.py
This script plants the entire farm and then sorts the inner cactus. (world size - 2). There is probably a better moving pattern to use + scanning is not optimized. more of a proof of concept.

## oneshot.py
This script plants the entire farm in one go, with only 1 growing stage.

## SwedishChef.py
made by @SwedishChef
This script plants the entire farm and then sorts the cactus.
