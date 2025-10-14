# Math

This folder contains functions that are useful for performing mathematical operations.

## Functions

### `ceil.py`
This file contains a function that rounds a number up to the nearest integer.
```python
number = 3.14
rounded_up = ceil(number) # 4
```

### `divmod.py`
This file contains a function that returns the quotient and remainder of dividing two numbers.
```python
dividend = 10
divisor = 3
quotient, remainder = divmod(dividend, divisor) # quotient: 3, remainder: 1
```

### `floor.py`
This file contains a function that rounds a number down to the nearest integer.
```python
number = 3.14
rounded_down = floor(number) # 3
```

### `isclose.py`
This file contains a function that checks if two numbers are close to each other. This is useful for comparing floating point numbers.
```python
number1 = 1
number2 = 1.000000001
close = isclose(number1, number2) # True
```

### `ln.py`
This file contains a function that calculates the natural logarithm of a number.
```python
number = 2.71828
natural_logarithm = ln(number) # 1
```

### `log.py`
This file contains a function that calculates the logarithm of a number with a given base.
```python
number = 100
base = 10
logarithm = log(number, base) # 2
```

### `pow.py`
This file contains a function that raises a number to a given power.
```python
number = 2
power = 3
result = pow(number, power) # 8
```

### `root.py`
This file contains a function that calculates the nth root of a number.
```python
number = 8
root = 3
result = root(number, root) # 2
```

### `round.py`
This file contains a function that rounds a number to a given number of decimal places.
```python
number = 3.14159
decimal_places = 2
rounded_number = round(number, decimal_places) # 3.14
```

### `sign.py`
This file contains a function that returns the sign of a number.
```python
positive_number = 5
negative_number = -3
zero_number = 0
sign_positive = sign(positive_number) # 1
sign_negative = sign(negative_number) # -1
sign_zero = sign(zero_number) # 0
```

### `sqrt.py`
This file contains a function that calculates the square root of a number.
```python
number = 9
square_root = sqrt(number) # 3
```

### `truncate.py`
This file contains a function that truncates a number to a given number of decimal places.
```python
number = 3.14159
decimal_places = 2
truncated_number = truncate(number, decimal_places) # 3.14
```
