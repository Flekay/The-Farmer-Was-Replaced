# General
This folder contains nice-to-have functions and commonly used python functions that are not natively available in the game.

## average.py
This file contains a function that calculates the average of a given list of numbers.
```python
list_of_numbers = [1, 2, 3, 4, 5]
average = average(list_of_numbers) # 3
```

## bell-curve.py
This file contains a function that prints an ASCII bell curve in the console based on a given list of numbers.
Optionally, you can pass the width and height of the bell curve as a second and third argument.
```python
list_of_numbers = [1, 2, 3, 4, 5]
bell_curve(list_of_numbers)

height = 10
width = 50
bell_curve(list_of_numbers, height, width)
```

## ceil.py
This file contains a function that rounds a number up to the nearest integer.
```python
number = 3.14
rounded_up = ceil(number) # 4
```

## floor.py
This file contains a function that rounds a number down to the nearest integer.
```python
number = 3.14
rounded_down = floor(number) # 3
```

## insort.py
This file contains a function that inserts a number into a sorted list while keeping the list sorted.
```python
sorted_list = [1, 2, 3, 5, 6]
insort(sorted_list, 4) # [1, 2, 3, 4, 5, 6]
```

## int.py
This file contains a function that converts a number into an integer.
```python
number = 3.14
integer = int(number) # 3
```

## is_sorted.py
This file contains a function that checks if a list is sorted in ascending order.
```python
sorted_list = [1, 2, 3, 4, 5]
is_sorted(sorted_list) # True
```

## ln.py
This file contains a function that calculates the natural logarithm of a number.
```python
number = 2.71828
natural_logarithm = ln(number) # 1
```

## log.py
This file contains a function that calculates the logarithm of a number with a given base.
```python
number = 100
base = 10
logarithm = log(number, base) # 2
```

## mean.py
This file contains a function that calculates the mean of a given list of numbers.
```python
list_of_numbers = [1, 2, 3, 4, 5]
mean = mean(list_of_numbers) # 3
```

## median.py
This file contains a function that calculates the median of a given list of numbers.
```python
list_of_numbers = [1, 2, 3, 4, 5]
median = median(list_of_numbers) # 3
```

## ops.py
This file contains a function that calculates the number of operations the drone can perform in one second.
```python
operations_per_second = ops() # 16800
```

## pow.py
This file contains a function that raises a number to a given power.
```python
number = 2
power = 3
result = pow(number, power) # 8
```

## randomint.py
This file contains a function that generates a random integer between two given numbers.
```python
lower_bound = 1
upper_bound = 10
random_integer = randomint(lower_bound, upper_bound) # 5
```

## reversed.py
This file contains a function that reverses the order of elements in a list.
```python
list_of_numbers = [1, 2, 3, 4, 5]
reversed_list = reversed(list_of_numbers) # [5, 4, 3, 2, 1]
```

## root.py
This file contains a function that calculates the nth root of a number.
```python
number = 8
root = 3
result = root(number, root) # 2
```

## round.py
This file contains a function that rounds a number to a given number of decimal places.
```python
number = 3.14159
decimal_places = 2
rounded_number = round(number, decimal_places) # 3.14
```

## sleep_ops.py
This file contains a function that pauses the execution of the script for a given number of operations. Minimum 13 operations. Needs to be warmed up before use :/
```python
operations = 100
sleep_ops(operations) # script pauses for 100 operations
```

## sleep.py
This file contains a function that pauses the execution of the script for a given number of seconds.
```python
seconds = 5
sleep(seconds) # script pauses for 5 seconds
```

## sorted.py
This file contains a function that returns a sorted list of elements. It does not modify the original list. It uses a custom bucket sort algorithm.
```python
list_of_numbers = [5, 4, 3, 2, 1]
sorted_list = sorted(list_of_numbers) # [1, 2, 3, 4, 5]
```

## sqrt.py
This file contains a function that calculates the square root of a number.
```python
number = 9
square_root = sqrt(number) # 3
```

## str.py
This file contains a function that converts a number into a string. Optionally, you can pass the number of decimal places as a second argument. The default is 4 decimal places.
```python
number = 42.751554
string = str(number) # "42.7515"

string = str(number, 2) # "42.75"
```

## sum.py
This file contains a function that calculates the sum of a given list of numbers.
```python
list_of_numbers = [1, 2, 3, 4, 5]
sum_of_numbers = sum(list_of_numbers) # 15
```

## time-series.py WIP
This file contains a function that prints an ASCII time series graph in the console based on a given list of numbers.
Optionally, you can pass the width and height of the time series as a second and third argument.

## tuncate.py
This file contains a function that truncates a number to a given number of decimal places.
```python
number = 3.14159
decimal_places = 2
truncated_number = truncate(number, decimal_places) # 3.14
```
