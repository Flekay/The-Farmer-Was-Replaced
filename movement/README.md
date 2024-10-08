# Movement
This folder contains movement related functions. These functions are used to move the player to a specific position or to the next tile in the path. The prefix `move` is used for functions that calculate the movement on the fly, while the prefix `navi` is used for functions that calculate the movement beforehand.


## Benchmark

### benchmark-destination.py | move to a specific position
| file                       | setup time | ops per bench | ops per move |
| -------------------------- | ---------- | ------------- | ------------ |
| navi-to-pos.py             | 9.4829s    |  539          |  3.2865      |
| navi-to-func.py            | 10.1986s   |  540          |  3,2926      |
| navi-to.py                 | 0.0806s    |  869          |  5.2987      |
| move-to.py                 | 0s         | 1769          | 10.7865      |
| goto.py                    | 0s         | 1241          |  6.204       |


### benchmark-loop.py | traverse the map
| file                        | setup time | ops per map |
| --------------------------- | ---------- | ----------- |
| navi-map.py                 | 0.0944s    | 301         |
| move-to-next-tile.py inline | 0s         | 903         |
| navi-to-next-tile.py        | 0.0090s    | 903         |
| move-to-next-tile.py        | 0s         | 1003        |


## move to a specific position

### navi-to-pos.py
This script pre-calculates the moves form each position to each position. You can also dump the compiled functions to a file which will reduce the setup time to ~5.3s.

### navi-to-func.py
Slighly modified version of けろびー code.
This script pre-calculates the moves form each position to each position. Similar to navi-to-pos.py but uses functions instead of a dictionary. You can also dump the compiled functions to a file which will reduce the setup time to ~2.4s.

### navi-to.py
This script pre-calculates the moves form each x,y coordinate to each x,y coordinate.

### move-to.py
This script calculates the moves to a specific position on the fly. Wraps around the map if shorter.

### goto.py
This script calculates the moves to a specific position on the fly. Does not wrap around the map.


## traverse the map

### navi-map.py
This script pre-calculates the moves to the next tile for each tile. Not position aware.

### navi-world.py
This script pre-calculates the moves to the next tile for each tile. Withouth using world wraping. Currently only works for even sized maps.

### move-to-next-tile.py
This script calculates the moves to the next tile on the fly. Always follows the same path.

### navi-to-next-tile.py
This script pre-calculates the moves to the next tile for each tile. Always follows the same path.

### move-to-next-tile.py inline
This script calculates the moves to the next tile on the fly. Always follows the same path. Inline version of move-to-next-tile.py.
