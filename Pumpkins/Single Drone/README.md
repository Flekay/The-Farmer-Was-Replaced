# Pumpkin
This is a collection of pumpkin scripts that are used to farm pumpkins.

## functions

### oneshot.py
This script is a one-shot script that will plant and harvest pumpkins in a single run.

### rerun.py
This script will only plant in the first run and then plant, fertilize and harvest in the second run.

### schindler.py
This script will keep planting pumpkins until every tile is filled.

### tiny.py
This script just runs and harvests at the same time.

## Benchmarks
| file         | items/min | fertilizer |
| -----------  | --------- | ---------- |
| rerun.py     |  67.9k    | low        |
| oneshot.py   |  37.5k    | high       |
| schindler.py |  55k      | no         |
| tiny.py      |  32.2k    | no         |
