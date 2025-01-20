# List

This folder contains functions that are useful for manipulating strings.

## Functions

### `average.py`
This file contains a function that calculates the average of a given list of numbers.
```python
list_of_numbers = [1, 2, 3, 4, 5]
average = average(list_of_numbers) # 3
```

### `copy_list.py`
This file contains a function that creates a copy of a list.
```python
list_of_numbers = [1, 2, 3, 4, 5]
copied_list = copy_list(list_of_numbers) # [1, 2, 3, 4, 5]
```

### `deep_copy_list.py`
This file contains a function that creates a deep copy of a list. Requires a depth parameter to specify the level of depth to copy and all nested lists need to be of the same depth.
```python
list_of_numbers = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
deep_copied_list = deep_copy_list(list_of_numbers, 1) # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
```

### `insort.py`
This file contains a function that inserts a number into a sorted list while keeping the list sorted.
```python
sorted_list = [1, 2, 3, 5, 6]
insort(sorted_list, 4) # [1, 2, 3, 4, 5, 6]
```

### `is_sorted.py`
This file contains a function that checks if a list is sorted in ascending order.
```python
sorted_list = [1, 2, 3, 4, 5]
is_sorted(sorted_list) # True
```

### `mean.py`
This file contains a function that calculates the mean of a given list of numbers.
```python
list_of_numbers = [1, 2, 3, 4, 5]
mean = mean(list_of_numbers) # 3
```

### `median.py`
This file contains a function that calculates the median of a given list of numbers.
```python
list_of_numbers = [1, 2, 3, 4, 5]
median = median(list_of_numbers) # 3
```

### `reversed.py`
This file contains a function that reverses the order of elements in a list.
```python
list_of_numbers = [1, 2, 3, 4, 5]
reversed_list = reversed(list_of_numbers) # [5, 4, 3, 2, 1]
```

### `sorted.py`
This file contains a function that returns a sorted list of elements. It does not modify the original list. It uses a custom bucket sort algorithm.
```python
list_of_numbers = [5, 4, 3, 2, 1]
sorted_list = sorted(list_of_numbers) # [1, 2, 3, 4, 5]
```

### `sum.py`
This file contains a function that calculates the sum of a given list of numbers.
```python
list_of_numbers = [1, 2, 3, 4, 5]
sum_of_numbers = sum(list_of_numbers) # 15
```

### `zip.py`
This file contains a function that zips two or more lists together.
```python
lists_to_zip = [
	[1,2,3],
	['a','b','c'],
	[True,False,True]
]
zipped = zip(lists_to_zip)  # [(1,'a',True), (2,'b',False), (3,'c',True)]
```
