# Random
This directory contains functions that simulate python's built-in random module.

### `choice.py`
This file contains a function that randomly selects an element from a list.
```python
list_of_elements = [1, 2, 3, 4, 5]
random_element = choice(list_of_elements) # 3
```

### `choices.py`
This file contains a function that returns k random elements from a list with replacement. Optionally supports weighted selection.
```python
population = [1, 2, 3, 4, 5]
# Elements with higher weights are more likely to be chosen
weights = None # All elements have equal weight
weights = [10, 1, 1, 1, 1]  # First element is 10x more likely to be selected
k = 3
chosen = choices(population, weights, k) # [1, 1, 3]
```

### `randomint.py`
This file contains a function that generates a random integer between two given numbers.
```python
lower_bound = 1
upper_bound = 10
random_integer = randomint(lower_bound, upper_bound) # 5
```

### `sample.py`
This file contains a function that returns k unique random elements from a list.
```python
population = [1, 2, 3, 4, 5]
k = 3
samples = sample(population, k) # [4, 1, 3]
```

### `shuffle.py`
This file contains a function that randomly shuffles a list in-place.
```python
my_list = [1, 2, 3, 4, 5]
shuffle(my_list) # [3, 1, 5, 2, 4]
```
