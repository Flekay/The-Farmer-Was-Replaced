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
- `**=`: 1 tick

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


### Arithmetic operators
- `+`
	- On lists, strings, and tuples: `len(list1) + len(list2) + 1` ticks
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
		- Item does not exist: `len(list)` + 1 ticks

	- On set: 2 ticks
	- On dict: 2 ticks

### Methods
- `.add()`: 1 tick
- `.append()`: 1 tick
- `.insert()`: `len(list) - insertion_index + 1` ticks
- `.remove()`
	- On list: `indexof(item)` + 1 ticks (this is probably a bug, it should be `len(list) - indexof(item)` ticks to account for shifting)
	- On set: 1 tick
- `.ptick()`
	- On list: `len(list) - idx` + 1 ticks (note that idx defaults to `len(list)`)
	- On dict: 1 tick

- Indexing with a value: 1 tick
- Indexing with a slice: number of items in slice + 1 ticks

## Literals
- Literal value: 0 ticks

- Dict: Sum of all key ticks + sum of all value ticks + 1
- List: `max(len(list), 1)` ticks
- Set: Sum of all value ticks + 1
- Tuple: Sum of all value ticks + 1

## Keywords
- `break`: 0 ticks
- `continue`: 0 ticks
- `def`: 1 tick
- `pass`: 1 tick
- `return`: 0 ticks
- `import`: 0 ticks
- `from`: 0 ticks
- `global`: 0 ticks

## Control Flow
- `if`: 1 tick
- `elif`: 0 ticks
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
- `min()`: # of comparisons (this is recursive), minimum 1 tick
- `max()`: # of comparisons (this is recursive), minimum 1 tick

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
	- Args: `len(args)` ticks
- `min()`: # of comparisons (this is recursive)
- `max()`: # of comparisons (this is recursive)
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
