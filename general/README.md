# General
This folder contains nice-to-have functions that don't fit in any other category.

## str.py
This file contains the default `str()` function that is commonly used by the community to get a more precise string representation of a number.

### str(number, precision = 4)
Returns a string representation of the number with the specified precision.
mostly used for debugging purposes like this:
```python
start_time = get_time()
# do something
quick_print("Time taken:", str(get_time() - start_time), "seconds")
```

## sleep.py
This file contains the `sleep()` function. This function is used to pause the program for a specified amount of time.

### sleep(seconds)
Pauses the program for the specified amount of time. This is useful to prevent the program from running too fast. Sike, you never want to slow down your program.