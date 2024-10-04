# Sunflower / Power


## Benchmarks
| file          | items/min |
| ------------- | --------- |
| power-fart.py |      5380 |
| power-hash.py |      3470 |
| power-path.py |      3640 |
| power-runs.py |      2600 |
| power-spam.py |      6200 |
| power-till.py |      1020 |
| CYR.py        |       552 |


## power-fart.py
This plants 7s sunflowers everywere. Then waters and harvests them.

## power-hash.py
This adds all sunflowers to single dictionary and then harvests 90% of them before planting new ones.

## power-path.py
This calculates the fastest path between sunflowers using nerest neighbour algorithm. This is about 5-10% faster than harvesting in planting order. You can test it yourself by uncommenting the "sub optimal pathing" part and commenting the "optimal pathing" part.

## power-runs.py
This replants directly after harvesting.

## power-spam.py
This just boringsly spams sunflowers without moving.

## power-till.py
This harvests only 15s sunflowers.

## CYR.py
This script tries to get the highest possible sunflowers per minute per character.
Currently 185 characters excluding clear() = 59900/185 = ~323,78 sunflowers per minute per character
