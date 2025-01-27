# Typing Functions

This folder contains functions for determining variable types or converting them.

## Functions

### `int.py`
Converts a string or float to an integer.

```python
x = 3.14
int_value = int(x)
quick_print(int_value) # 3
```

### `isinstance.py`
Checks if a variable is of a certain type.

```python
x = 1
x_is_number = isinstance(x, 'number')
quick_print(x_is_number) # True
```


### `type.py`
Determines the type of a variable.

```python
x = 1
x_type = type(x)
quick_print(x_type) # 'number'
```
