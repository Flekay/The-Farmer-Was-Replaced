# Cactus
This is a collection of cactus scripts that are used to farm cactus.

## Functions

### `shear_sort.py`
from @acters

Implements a shear sort algorithm. The script rearranges cactus elements in a grid-like structure by performing alternating row and column sorts, adapting parallel sorting ideas for efficiently ordering your cactus.

#### how to use:
```python
clear()
from simple_planting import simple_planting # Or any other planting function
from shear_sort import shear_sort

shear_sort(simple_planting())
harvest()
```

### `gradient_bubble_sort.py`
from @acters

Uses a gradient-enhanced bubble sort. This script gradually improves the order of cactus placement by repeatedly sweeping through the data with incremental adjustments, resulting in a more efficient sorting process compared to the standard bubble sort.

#### how to use:
```python
clear()
from simple_planting import simple_planting # Or any other planting function
from gradient_bubble_sort import gradient_bubble_sort

gradient_bubble_sort(simple_planting())
harvest()
```

### `heapify.py`
from @mika

Organizes cacti using a heap sort approach. The script builds a heap from the cactus collection and then rearranges it by applying the heapify process over a range of coordinates, ensuring a structured and efficient sort based on spatial positions.

#### how to use:
```python
clear()
from navi_to_deltalist import move_to # Or any other movement function
from simple_planting import simple_planting # Or any other planting function
from heapify import heapify, rectCoords

cacti = simple_planting()
for x, y in rectCoords():
	move_to(x, y)
	heapify(cacti, x, y)
harvest()
```

### `insertion_sort.py`
from @SwedishChef

Applies an insertion sort method to sequentially build a sorted array of cacti. This script inserts each cactus in the right order relative to the already sorted portion, making it ideal for collections that are nearly in order.

#### how to use:
```python
clear()
from simple_planting import simple_planting # Or any other planting function
from insertion_sort import insertion_sort

insertion_sort(simple_planting())
harvest()
```

### `oneshot.py`
A unique replating algorithm that continuously replant cacti until all have the same measurement. This approach bypasses traditional sorting by aiming for uniformity through iterative adjustments. It will be updated in future versions to incorporate a constant cactus growth time.

### `naive_bubble_sort.py`
Implements a naive bubble sort algorithm that repeatedly swaps the entire field without skipping already sorted cacti.

#### how to use:
```python
clear()
from simple_planting import simple_planting # Or any other planting function
from naive_bubble_sort import naive_bubble_sort

naive_bubble_sort(simple_planting())
harvest()
```

### `naive_cocktail_sort.py`
Could also be called a naive 2-way bubble sort.
Implements a naive cocktail sort algorithm that repeatedly swaps the entire field in 2 directions without skipping already sorted cacti.

#### how to use:
```python
clear()
from simple_planting import simple_planting # Or any other planting function
from naive_cocktail_sort import naive_cocktail_sort

naive_cocktail_sort(simple_planting())
harvest()
```

### `naive_4_way_bubble_sort.py`
Could also be called a naive 2-way cocktail sort.
A 2D bubble sort variant that applies full grid passes in four traversal
directions — left-to-right, right-to-left, top-to-bottom, and bottom-to-top.
It cycles through these directions in order to reduce directional bias.

#### how to use:
```python
clear()
from simple_planting import simple_planting # Or any other planting function
from naive_4_way_bubble_sort import naive_4_way_bubble_sort

naive_4_way_bubble_sort(simple_planting())
harvest()
```

## Cactus Leaderboard (10x10)
Optimal planting can vary for each script, so the leaderboard is based on the `/cactus/planting/simple_planting.py` script. This is to ensure a fair comparison across all scripts and only compare raw sorting speed.

| file                                | min       | max       | avg       |
| ----------------------------------- | --------- | --------- | --------- |
| gradient_bubble_sort.py             |  11.2305s |  15.0240s |  12.9877s |
| insertion_sort.py                   |  11.6708s |  15.0012s |  13.3787s |
| heapify.py                          |  12.0650s |  16.3983s |  14.2171s |
| naive_4_way_bubble_sort.py          |  12.2437s |  18.4504s |  14.5890s |
| naive_cocktail_sort.py              |  12.4747s |  17.4745s |  14.6087s |
| shear_sort.py                       |  14.1361s |  18.8177s |  16.4155s |
| naive_bubble_sort.py                |  13.8212s |  19.3854s |  16.7880s |
| oneshot.py                          |  20.1245s |  32.6655s |  25.6584s |

## Important Notes
- `insertion_sort.py` is a simple and unoptimized version of the current #1 script. That's why it is not the fastest on this leaderboard.
- `shear_sort.py` is not optimized at all.
- `oneshot.py` will be updated in future versions to incorporate a constant cactus growth time.
