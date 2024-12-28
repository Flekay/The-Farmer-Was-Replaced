# Movement
This folder contains movement related functions. These functions are used to move the player to a specific position or to the next tile in the path. The prefix `move` is used for functions that calculate the movement on the fly, while the prefix `navi` is used for functions that calculate the movement beforehand.


## Benchmark

### benchmark-destination.py | move to a specific position
| file                       | setup time | ops per bench |
| -------------------------- | ---------- | ------------- |
| move-to.py                 |          - |           660 |
| navi-to.py                 |    0.0915s |           360 |
| navi-to-list.py            |    0.0303s |           300 |
| navi-to-pos.py             |    6.6732s |           240 |
| navi-to-func.py            |    4.8067s |           241 |
| gen-move-to.py             |    0.0049s |           450 |


### benchmark-loop.py | traverse the map
| file                        | setup ops  | ops per map |
| --------------------------- | ---------- | ----------- |
| navi-map.py                 |        609 |           1 |
| navi-map-light.py           |        116 |           1 |
| navi-map-inline.py          |         14 |          12 |
| move-to-next-tile.py        |          - |         402 |
| navi-to-next-tile.py        |        127 |         402 |


## move to a specific position

### navi-to-pos.py
This script pre-calculates the moves form each position to each position. You can also dump the compiled functions to a file which will reduce the setup time to ~5.3s.

### navi-to-func.py
Slighly modified version of けろびー code.
This script pre-calculates the moves form each position to each position. Similar to navi-to-pos.py but uses functions instead of a dictionary. You can also dump the compiled functions to a file which will reduce the setup time to ~2.4s.

### navi-to.py
This script pre-calculates the moves form each x,y coordinate to each x,y coordinate.

### navi-to-list.py
This script is the same as navi-to.py but uses a list instead of a dictionary. Setup time can potentially be reduced by using navi-to-pos.py's generator method.

### move-to.py
This script calculates the moves to a specific position on the fly. Wraps around the map if shorter.

### goto.py
This script calculates the moves to a specific position on the fly. Does not wrap around the map.

### gen-move-to.py
This script only exists because @ThatMerlinGuy insisted on having a not completely hard-coded version of move-to.py. It generates a function with inlined worldsize.


## traverse the map

### navi-map.py
This script pre-calculates the moves to the next tile for each tile. Not position aware.

### navi-map-light.py
This is a light version of navi-map.py. It cannot start from a specific position and does not support custom path lengths.

### navi-world.py
This script pre-calculates the moves to the next tile for each tile. Withouth using world wraping. Currently only works for even sized maps.

### move-to-next-tile.py
This script calculates the moves to the next tile on the fly. Always follows the same path.

### navi-to-next-tile.py
This script pre-calculates the moves to the next tile for each tile. Always follows the same path.
