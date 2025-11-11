## Unary operators
- `not`: 0 ticks
- `-`: 0 ticks
- `+`: 0 ticks

## Binary operators
### Assignment
- `=`: 0 ticks
- `+=`: 1 tick
- `-=`: 1 tick
- `*=`: 1 tick
- `/=`: 1 tick
- `%=`: 1 tick
- `**=`: Not implemented

### Enum access
- `.`: 0 ticks

### Logical operators
(all comparison operators are recursive)
- `==`: 1 ticks
- `!=`: 1 ticks
- `>=`: 1 ticks
- `<=`: 1 ticks
- `>`: 1 ticks
- `<`: 1 ticks
- `and`: 1 tick
- `or`: 1 tick
- `not`: 0 ticks

**Note on Recursive Comparisons:** When comparing complex types (lists, tuples), comparisons are element-by-element. The base cost is 1 tick, but comparing collections adds overhead proportional to the elements compared. See tests in `General/tests/test_builtin_functions.py` for examples.


### Arithmetic operators
- `+`
	- On lists, strings, and tuples: `len(list1) + len(list2)` ticks
	- On numbers: 1 tick

- `-`: 1 tick
- `*`: 1 tick
- `/`: 1 tick
- `%`: 1 tick
- `**`: 1 tick

## Collection operators
- `in`
	- On lists & tuples
		- Item exists: `indexof(item)` + 1 ticks
		- Item does not exist: `len(list)` ticks
	- On strings: `len(string)` ticks (regardless of whether char exists or position)
	- On set: 1 tick
	- On dict: 1 tick

### Methods
- `.add()`: 1 tick
- `.append()`: 1 tick
- `.insert()`: `len(list) - insertion_index + 2` ticks
- `.remove()`
	- On list: `len(list)` ticks
	- On set: 1 tick
- `.pop()`
	- On list: `max(len(list) - idx, 1)` ticks
	- On dict: 1 tick

- Indexing with a value: 1 tick
- Indexing with a slice: `max(number of items in slice, 1)` ticks

## Literals
- Number: 0 ticks
- String: 0 ticks
- Boolean: 0 ticks
- None: 0 ticks
- Dict
	- `{}`: 1 tick
	- `{k1: v1, k2: v2}`: `len(keys) + 1` ticks
	- `dict()`: 1 tick
	- `dict(args)`: `2 * len(args) + 1` ticks
	- `d[key]` (indexing): 1 tick
	- `d[key] = value` (assignment): 0 ticks
	- `.pop(key)`: 1 tick
- List
	- `[]`: 1 tick
	- `[1, 2, 3]`: `max(len(list), 1)` ticks
	- `list()`: 1 tick
	- `list(args)`: `len(args) + 1` ticks
	- `lst[idx]` (indexing): 1 tick
	- `lst[idx] = value` (assignment): 0 ticks
	- `.append(item)`: 1 tick
	- `.insert(idx, item)`: `len(list) - idx + 2` ticks
	- `.remove(item)`: `len(list)` ticks
	- `.pop(idx)`: `max(len(list) - idx, 1)` ticks
- Set
	- `{1, 2, 3}`: `len(set)` ticks
	- `set()`: 1 tick
	- `set(args)`: `len(args) + 1` ticks
	- `.add(item)`: 1 tick
	- `.remove(item)`: 1 tick
- Tuple
	- `()`: 1 tick
	- `(1, 2, 3)`: `sum(value_costs) + 1` ticks

## Keywords
- `break`: 0 ticks
- `continue`: 0 ticks
- `def`: 1 tick
- `pass`: 1 tick
- `return`: 0 ticks
- `import`: 0 ticks
- `from`: 0 ticks
- `global`: 0 ticks

## Functions
- `def function_name():` (definition): 1 tick
- `function_name()` (direct call): 0 ticks
- `variable()` (indirect call through variable): 1 tick
- `return`: 0 ticks
- `pass`: 1 tick
- `lambda`: not implemented
- `*args`: not implemented
- `**kwargs`: not implemented
- `yield`: not implemented
- `async`: not implemented
- `await`: not implemented

## Control Flow
- `if`: 1 tick
- `elif`: 1 tick
- `else`: 0 ticks
- `for`:
	- Initialization: 1 tick
	- Each iteration: 0 ticks
- `while`:
	- Initialization: 1 tick
	- Each iteration: 0 ticks

## Builtin Functions
### Arithmetic Functions
- `abs()`: 1 tick
- `random()`: 1 tick
- `min()`: `max(len(items), 1)` ticks (recursive comparisons - see note below)
- `max()`: `max(len(items), 1)` ticks (recursive comparisons - see note below)

**Note on Recursive Comparisons:** When comparing complex types (lists, tuples), the actual cost includes recursive element-by-element comparison. Examples: `min([1,3], [2,4])` = 6 ticks, `min([1,2], [3,4], [5,6])` = 9 ticks. The cost scales with both the number of arguments and the elements being compared.

### Farm Functions
- `can_harvest()`: 1 tick
- `clear()`: 200 ticks
- `get_companion()`: 1 tick
- `get_entity_type()`: 1 tick
- `get_ground_type()`: 1 tick
- `get_water()`: 1 tick
- `harvest()`
	- Success: 200 ticks
	- Fail: 1 tick
- `measure()`: 1 tick
- `plant()`
	- Success: 200 ticks
	- Fail: 1 tick
- `swap()`
	- Success: 200 ticks
	- Fail: 1 tick
- `till()`: 200 ticks

### API Functions
- `get_cost()`: 1 tick
- `get_world_size()`: 1 tick
- `num_items()`: 1 tick
- `num_unlocked()`: 1 tick
- `unlock()`:
	- Success: 200 ticks
	- Fail: 1 tick

### Drone Functions
- `get_pos_x()`: 1 tick
- `get_pos_y()`: 1 tick
- `move()`
	- Success: 200 ticks
	- Success (with Dinosaur Hat): 400 ticks, reduced by 3% (rounded down) for each apple picked up
	- Fail: 1 tick
- `can_move()`: 1 tick
- `use_item()`
	- Success: 200 ticks
	- Fail: 1 tick

### Debug Functions
- `get_tick_count()`: 0 ticks
- `get_time()`: 0 ticks
- `quick_print()`: 0 ticks
- `set_execution_speed()`: 200 ticks
- `set_farm_size()`: 200 ticks

### Collections
- `dict()`
	- No args: 1 tick
	- Args: `2 * len(args) + 1` ticks
- `len()`: 1 tick
- `list()`
	- No args: 1 tick
	- Args: `len(args) + 1` ticks
- `min()`: `max(len(items), 1)` ticks (recursive comparisons - see note in Arithmetic Functions)
- `max()`: `max(len(items), 1)` ticks (recursive comparisons - see note in Arithmetic Functions)
- `range()`: 1 tick
- `set()`
	- no args: 1 tick
	- args: `len(args) + 1` ticks

## Data Types
### Dictionaries

## Exceptions:
- `print()`: 1 second, regardless of speed
- `do_a_flip()`: 1 second, regardless of speed
- `pet_the_piggy()`: 1 second, regardless of speed
