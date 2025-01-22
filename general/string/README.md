# String

This folder contains functions that are useful for manipulating strings.

## Functions

### `join.py`
This file contains a function that joins a list of strings into a single string with a given separator.
```python
strings = ["a", "b", "c"]
separator = ", "
joined_string = join(strings, separator) # "a, b, c"
```

### `string.py`
This file contains a function that converts a number into a string. Optionally, you can pass the number of decimal places as a second argument. The default is 4 decimal places.
```python
number = 42.751554
string = string(number) # "42.7515"

string = string(number, 2) # "42.75"
```

## `strtime.py`
This file contains a function that returns a time string for the given number of seconds, displayed as mm:ss.xx.
```python
seconds = 75
time_string = strtime(seconds) # "  1:15.00"
```
