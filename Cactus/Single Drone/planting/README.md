# Planting Algorithms

This directory contains planting scripts used to grow cactus. These algorithms differ in complexity and include sorting mechanisms to manage cactus placement.

## Functions

### 1. `simple_planting.py`
A straightforward planting method that plants cactus without any extra sorting steps. It simply plants cactus in a grid pattern and measures each spot.

### 2. `plant_and_sort.py`
This algorithm not only plants cactus but also performs a two-round swapping procedure to sort the cactus based on their measurements. It takes into account measurements from multiple directions to ensure proper order.

### 3. `movement_pattern.py` no example yet
An advanced planting path to maximize sorts while planting. There are hundreds of possible movement patterns and i still haven't found the optimal one.

### 4. `replanting.py` no example yet
Another advanced planting strategy is to replant cactus that are way too high or too low for their position. e.g. a 9 on (0,0) takes longer to swap to the correct position than just replanting.

### 5. `hardcoding.py` no example yet
A final optimization step is to hardcode the planting function. This obviously is only nessessary if you want to squeeze out the last few ticks.

## Important Notes
- I already explained the additional planting steps on discord, but i don't have simple implementations of them yet. I will add them in the future when i have time and motivation.
