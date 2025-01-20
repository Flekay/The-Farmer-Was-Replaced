# Dictionary Functions

This folder contains functions that are useful for manipulating dictionaries.

## Functions

### `copy.py`
Creates a shallow copy of a dictionary.
```python
old_dict = {'a': 1, 'b': 2}
new_dict = copy(old_dict)
new_dict['a'] = 3

quick_print(old_dict['a']) # 1
quick_print(new_dict['a']) # 3
```

### `deep_copy.py`
Creates a deep copy of a dictionary up to a specified depth.
```python
old_dict = {'a': {'b': 1}}
new_dict = deep_copy(old_dict, 1)
new_dict['a']['b'] = 2

quick_print(old_dict['a']['b']) # 1
quick_print(new_dict['a']['b']) # 2
```

### `filter.py`
Filters a dictionary based on a predicate function.
```python
def is_even(value):
	return value % 2 == 0

dictionary = {'a': 1, 'b': 2, 'c': 3}
filtered = filter(dictionary, is_even)

quick_print(filtered) # {'b': 2}
```

### `get.py`
Gets the value for a specified key with an optional default.
```python
dictionary = {'a': 1, 'b': 2}
example1 = get(dictionary, 'a')
example2 = get(dictionary, 'c', 'default')

quick_print(example1) # 1
quick_print(example2) # 'default'
```

### `items.py`
Retrieves all key-value pairs from a dictionary.
```python
dictionary = {'a': 1, 'b': 2}
items = dictionary_items(dictionary)

quick_print(items) # [('a', 1), ('b', 2)]
```

### `keys.py`
Retrieves all the keys from a dictionary and returns them as a list.
```python
dictionary = {'a': 1, 'b': 2}
keys = keys(dictionary)

quick_print(keys) # ['a', 'b']
```

### `merge.py`
Merges two dictionaries into one.
```python
left = {'a': 1}
right = {'b': 2}
merged = merge(left, right)

quick_print(merged) # {'a': 1, 'b': 2}
```

### `set.py`
Sets a key-value pair in a dictionary.
```python
dictionary = {'a': 1}
set(dictionary, 'b', 2)

quick_print(dictionary) # {'a': 1, 'b': 2}
```

### `values.py`
Retrieves all the values from a dictionary and returns them as a list.
```python
dictionary = {'a': 1, 'b': 2}
values = values(dictionary)

quick_print(values) # [1, 2]
```
