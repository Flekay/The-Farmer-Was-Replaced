# Movement
This folder contains movement related functions. These functions are used to move the player to a specific position or to the next tile in the path. The prefix `move` is used for functions that calculate the movement on the fly, while the prefix `navi` is used for functions that calculate the movement beforehand. 


## Benchmark

### benchmark-destination.py | move to a specific position
| file                        | setup time | ops per bench | ops per move |
| --------------------------- | ---------- | ------------- | ------------ |
| navi-to-pos.py              | 69.4154s   |  539          |  3.2865      |
| navi-to.py                  | 0.0806s    |  869          |  5.2987      |
| move-to.py                  | 0s         | 1769          | 10.7865      |

### benchmark-loop.py | traverse the map
| file                        | setup time | ops per map |
| --------------------------- | ---------- | ----------- |
| navi-map.py                 | 0.0944s    | 301         |
| move-to-next-tile.py inline | 0s         | 903         |
| navi-to-next-tile.py        | 0.0090s    | 903         |
| move-to-next-tile.py        | 0s         | 1003        |