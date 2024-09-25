## Unary Operators
- `not`: ops(operand) + 1
- `-`: ops(operand) + 1
- `+`: ops(operand) + 1

## Binary Operators
### Assignment
- `=`: 1 per assigned value + 1 base

### Enum access
- `.`: 1 op
### Logical Operators
(all comparison operators are recursive)
- `==`: # of checks + 1 ops
- `!=`: # of checks + 1 ops
- `>=`: # of comparisons + 1 ops
- `<=`: # of comparisons + 1 ops
- `>`: # of comparisons + 1 ops
- `<`: # of comparisons + 1 ops
- `and`: 1 op
- `or`: 1 op
- `not`: operand ops + 1 ops


### Arithmetic Operators
- `+`
  - On lists, strings, and tuples: `len(list1) + len(list2) + 1` ops
  - On numbers: 1 op

- `-`: 1 op
- `*`: 1 op
- `/`: 1 op
- `%`: 1 op
- `**`: 1 op

## Collection Operators
- `in`
  - On lists & tuples
    - Item exists: `indexof(item)` + 1 ops
    - Item does not exist: `len(list)` + 1 ops

  - On set: 2 ops
  - On dict: 2 ops

### Methods
- `.add()`: 1 op
- `.append()`: 1 op
- `.insert()`: `len(list) - insertion_index + 1` ops
- `.remove()`
  - On list: `indexof(item)` + 1 ops (this is probably a bug, it should be `len(list) - indexof(item)` ops to account for shifting)
  - On set: 1 op
- `.pop()`
  - On list: `len(list) - idx` + 1 ops (note that idx defaults to `len(list)`)
  - On dict: 1 op

- Indexing with a value: 1 op
- Indexing with a slice: number of items in slice + 1 ops

## Literals
- Literal value: 1op

- Dict: Sum of all key ops + sum of all value ops + 1
- List: Sum of all value ops + 1
- Set: Sum of all value ops + 1
- Tuple: Sum of all value ops + 1

## Keywords
- `break`: 1 op
- `continue`: 1 op
- `def`: 1 op
- `pass`: 1 op
- `return`: returned value ops + 1

## Control Flow
- `if`: 0 op
- `elif`: 0 op
- `else`: 0 op
- `for`: 0 op
- `while`: 0 op

## Builtin Functions
### Arithmetic Functions
- `abs()`: 1 op
- `random()`: 1 op
- `min()`: # of comparisons (this is recursive)
- `max()`: # of comparisons (this is recursive)

### Farm Functions
- `can_harvest()`: 1 op
- `clear()`: 200 ops
- `get_companion()`: 1 op
- `get_entity_type()`: 1 op
- `get_ground_type()`: 1 op
- `get_water()`: 1 op
- `harvest()`
  - Success: 200 ops
  - Fail: 1 op
- `measure()`: 1 op
- `plant()`
  - Success: 200 ops
  - Fail: 1 op
- `swap()`
  - Success: 200 ops
  - Fail: 1 op
- `till()`: 200 ops

### API Functions
- `get_cost()`: 1 op
- `get_world_size()`: 1 op
- `num_items()`: 1 op
- `num_unlocked()`: 1 op
- `timed_reset()`: 200 ops
- `trade()`:
  - Success: 200 ops
  - Fail: 1 op
- `unlock()`:
  - Suscess: 200 ops
  - Fail: 1 op

### Drone Functions
- `get_pos_x()`: 1 op
- `get_pos_y()`: 1 op
- `move()`
  - Success: 200 ops
  - Fail: 1 op
- `use_item()`
  - Success: 200 ops
  - Fail: 1 op

### Debug Functions
- `get_tick_count()`: 1 op
- `get_time()`: 1 op
- `quick_print()`: 1 op
- `set_execution_speed()`: 200 ops
- `set_farm_size()`: 200 ops

### Collections
- `dict()`
  - No args: 1 op
  - Args: `2 * len(args) + 1` ops
- `len()`: 1 op
- `list()`
  - No args: 1 op
  - Args: `len(args) + 1` ops
- `min()`: # of comparisons (this is recursive)
- `max()`: # of comparisons (this is recursive)
- `range()`: 1 op
- `set()`
  - no args: 1 op
  - args: `len(args) + 1` ops


## Exceptions:
- `print()`: 1 second, regardless of speed
- `do_a_flip()`: 1 second, regardless of speed
