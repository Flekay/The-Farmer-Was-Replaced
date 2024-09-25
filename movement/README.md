# Movement
This folder contains movement related functions. These functions are used to move the player to a specific position or to the next tile in the path. The prefix `move` is used for functions that calculate the movement on the fly, while the prefix `navi` is used for functions that calculate the movement beforehand.


## Benchmark

### benchmark-destination.py | move to a specific position
| file                       | setup time | ops per bench | ops per move |
| -------------------------- | ---------- | ------------- | ------------ |
| navi-to-pos.py             | 9.3369s    |  539          |  3.2865      |
| navi-to-func.py            | 7.3332s    | 1414          |  8,6219      |
| navi-to.py                 | 0.8305s    | 1583          |  9,6524      |
| move-to.py                 | 0s         | 1594          |  9,7195      |


### benchmark-loop.py | traverse the map
| file                        | setup time | ops per map | ops per move |
| --------------------------- | ---------- | ----------- | ------------ |
| navi-map.py                 | 0.0744s    |  338        |  3.38        |
| navi-to-next-tile.py        | 0.0624s    |  991        |  9.91        |
| move-to-next-tile.py inline | 0s         | 1002        | 10.02        |
| move-to-next-tile.py        | 0s         | 1113        | 11.13        |


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
