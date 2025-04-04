# Built-ins

This folder contains useful built-in functions and constants.

## Functions

### `copy.py`
Creates a shallow copy of an object.
```python
shallow_copy = copy([1, 2, 3])
quick_print(shallow_copy)  # [1, 2, 3]
```

### `deepcopy.py`
Returns a deep copy of an object.
```python
original = {1: [1, 2, 3]}
copied = deepcopy(original)
quick_print(copied)  # {1: [1, 2, 3]}
```

### `help.py`
Prints a help message for a module.
```python
import math
help(math)
```

### `uniqid.py`
Generates a unique identifier.
```python
unique_id = uniqid()
quick_print(unique_id)  # 1
```

### `raise.py`
Raises an exception with a message.
```python
raise("This is an error message.")
```

### `enumerate.py`
Returns an iterator that generates tuples of indices and values.
```python
for index, value in enumerate([1, 2, 3]):
    quick_print(index, value)  # 0 1, 1 2, 2 3
```
