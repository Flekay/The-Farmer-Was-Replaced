# Polyculture Hay
This is a script that are used to farm hay using polyculture. Current record is 173,0k items/min.

## Benchmarks
| file        | items/min | note |
| ----------- | --------- | ---- |
| static.py   | 144k      |      |
| preplant.py | 157k      |      |

## static.py
This script just spams fertilizer and harvest in the middle of a bush field. Heavily luck based. preplanting might be better, but i accidentally deleted that script and i'm too lazy to rewrite it. It's also very luck based.

## preplant.py + harvest_polyhay.py
thanks to @karne for the harvest_polyhay function.
This is the impelementation of preplanting/harvesting i accidentally deleted. It has a lower max items/min than static.py, but it's average is a lot higher. 177203 items/min is the current record.
