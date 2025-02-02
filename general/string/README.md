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

## `find.py`
This file contains a function that finds the first occurrence of a substring in a string. It returns the index of the first character of the substring in the string.
```python
string = "hello world"
substring = "world"
index = find(string, substring) # 6
```

## `replace.py`
This file contains a function that replaces all occurrences of a substring in a string with another substring.
```python
string = "hello world"
old_substring = "world"
new_substring = "there"
new_string = replace(string, old_substring, new_substring) # "hello there"
```

## `split.py`
This file contains a function that splits a string into a list of substrings based on a separator.
```python
string = "a, b, c"
separator = ", "
substrings = split(string, separator) # ["a", "b", "c"]
```

## `strip.py`
This file contains a function that removes leading and trailing whitespace from a string.
```python
string = "  hello world  "
stripped_string = strip(string) # "hello world"
```

## `rstrip.py`
This file contains a function that removes trailing whitespace from a string.
```python
string = "  hello world  "
right_stripped_string = rstrip(string) # "  hello world"
```

## `lstrip.py`
This file contains a function that removes leading whitespace from a string.
```python
string = "  hello world  "
left_stripped_string = lstrip(string) # "hello world  "
```

## `zfill.py`
This file contains a function that pads a string with zeros on the left until it reaches the specified length.
```python
string = "42"
padded_string = zfill(string, 5) # "00042"
```
