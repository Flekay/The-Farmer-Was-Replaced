# Pumpkin
This is a collection of pumpkin scripts that are used to farm pumpkins.

## Benchmarks
| file         | items/min | fertilizer |
| -----------  | --------- | ---------- |
| rerun.py     | 140k      | low        |
| oneshot.py   | 130k      | high       |
| CYR.py       | 120k      | high       |
| schindler.py | 110k      | no         |
| tiny.py      | 30k       | no         |


## oneshot.py
This script is a one-shot script that will plant and harvest pumpkins in a single run.

## rerun.py
This script will only plant in the first run and then plant, fertilize and harvest in the second run.

## schindler.py
This script will keep planting pumpkins until every tile is filled. It has a list of all missing tiles.

## tiny.py
This script just runs and harvests at the same time. Ain't nobody got time for gigant pumpkins.

## CYR.py
This script tries to get the highest possible pumpkins per minute per character.
Currently 193 characters excluding clear() = 120k/193 = 621.76 pumpkins per minute per character
