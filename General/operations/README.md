# Operations

This folder contains functions that are useful for controlling the number of operations the drone can perform in a given time frame.

## Functions

### `ops.py`
This file contains a function that calculates the number of operations the drone can perform in one second.
```python
operations_per_second = ops() # 16800
```

### `sleep_ops.py`
This file contains a function that pauses the execution of the script for a given number of operations. Minimum 3 operations.
```python
operations = 100
sleep_ops(operations) # script pauses for 100 operations
```

### `sleep.py`
This file contains a function that pauses the execution of the script for a given number of seconds.
```python
seconds = 5
sleep(seconds) # script pauses for 5 seconds
```
