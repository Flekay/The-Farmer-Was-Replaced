# Test file to confirm tick costs for function-related operations
# Based on documentation in Tick Overview.md

# Test 1: Function definition (def)
# Expected: 1 tick
quick_print("=== Test 1: Function definition (def) ===")
start_ticks = get_tick_count()
def simple_function():
	pass
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: Function call (no parameters, no return)
# Expected: 0 ticks for call itself
quick_print("=== Test 2: Function call (no params, no return) ===")
def no_op():
	pass

start_ticks = get_tick_count()
no_op()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # Only the pass statement costs 1 tick
quick_print("Expected:", expected_cost, "ticks (pass inside)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: Function call with parameters
# Expected: 0 ticks for call, parameters are just evaluated
quick_print("=== Test 3: Function call with parameters ===")
def add(a, b):
	return a + b

x = 5
y = 3
start_ticks = get_tick_count()
result = add(x, y)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # Only the addition (a + b) costs 1 tick
quick_print("Expected:", expected_cost, "ticks (addition only)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: Function with return value
# Expected: 0 ticks for return itself
quick_print("=== Test 4: Return statement ===")
def return_value():
	start = get_tick_count()
	return get_tick_count() - start

actual_cost = return_value()
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: Function call overhead (empty function body with return)
# Expected: 0 ticks total (return costs 0)
quick_print("=== Test 5: Empty function with return ===")
def empty_return():
	return

start_ticks = get_tick_count()
empty_return()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: Multiple function definitions
# Expected: 1 tick per def
quick_print("=== Test 6: Multiple function definitions ===")
start_ticks = get_tick_count()
def func1():
	pass
def func2():
	pass
def func3():
	pass
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3  # 3 def statements, 1 tick each
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: Function with default parameters
# Expected: 1 tick for def
quick_print("=== Test 7: Function with default parameters ===")
start_ticks = get_tick_count()
def func_with_defaults(a=1, b=2):
	pass
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: Function call with default parameters (using defaults)
# Expected: Just the cost of pass (1 tick)
quick_print("=== Test 8: Call with default parameters ===")
def func_defaults(a=5, b=10):
	pass

start_ticks = get_tick_count()
func_defaults()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # Only pass costs 1 tick
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 9: Function call with default parameters (overriding defaults)
# Expected: Just the cost of pass (1 tick)
quick_print("=== Test 9: Call overriding default parameters ===")
def func_override(a=5, b=10):
	pass

start_ticks = get_tick_count()
func_override(3, 7)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # Only pass costs 1 tick
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 10: Nested function definition
# Expected: 1 tick for outer def
quick_print("=== Test 10: Nested function definition ===")
start_ticks = get_tick_count()
def outer():
	def inner():
		pass
	return inner
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # Only outer def costs 1 tick
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 11: Calling function that defines another function
# Expected: 1 tick for inner def + 0 for return
quick_print("=== Test 11: Call function that defines nested function ===")
def outer_func():
	def inner_func():
		pass
	return inner_func

start_ticks = get_tick_count()
result = outer_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # Inner def costs 1 tick, return costs 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 12: Recursive function call
# Expected: Cost of operations inside
quick_print("=== Test 12: Recursive function (simple) ===")
def countdown(n):
	if n <= 0:
		return 0
	return countdown(n - 1)

start_ticks = get_tick_count()
result = countdown(3)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
# Each call: if (1) + comparison (1) + subtraction (1) or return (0)
# countdown(3): if(1) + compare(1) + subtract(1) + call
# countdown(2): if(1) + compare(1) + subtract(1) + call
# countdown(1): if(1) + compare(1) + subtract(1) + call
# countdown(0): if(1) + compare(1) + return(0)
# Total: 4 * (if + compare) + 3 * subtract = 4*2 + 3 = 11 ticks
expected_cost = 11
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 13: Dynamic function assignment
# Expected: 0 ticks (assigning function reference)
quick_print("=== Test 13: Dynamic function assignment ===")
def original_func():
	return 5

start_ticks = get_tick_count()
dynamic_func = original_func
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0  # Assignment is 0 ticks
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 14: Calling dynamically assigned function
# Expected: 1 tick for function call
quick_print("=== Test 14: Calling dynamically assigned function ===")
def func_to_assign():
	return 10

assigned_func = func_to_assign
start_ticks = get_tick_count()
result = assigned_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # Function call costs 1 tick
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 15: Reassigning function dynamically
# Expected: 0 ticks per assignment
quick_print("=== Test 15: Reassigning function dynamically ===")
def func_a():
	return 1

def func_b():
	return 2

dynamic = func_a
start_ticks = get_tick_count()
dynamic = func_b
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0  # Assignment is 0 ticks
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 16: Function with multiple statements
# Expected: Sum of all statement costs
quick_print("=== Test 16: Function with multiple statements ===")
def multi_statement():
	x = 5  # assignment: 0 ticks
	y = 10  # assignment: 0 ticks
	z = x + y  # addition: 1 tick, assignment: 0 ticks
	return z  # return: 0 ticks

start_ticks = get_tick_count()
result = multi_statement()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # Only the addition costs ticks
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 17: Global keyword
# Expected: 0 ticks
quick_print("=== Test 16: Global keyword ===")
global_var = 0
def use_global():
	start = get_tick_count()
	global global_var
	return get_tick_count() - start

actual_cost = use_global()
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 17: Function modifying global variable
# Expected: Cost of operations (assignment = 0, += = 1)
quick_print("=== Test 17: Modifying global variable ===")
counter = 0
def increment_counter():
	global counter
	counter += 1

start_ticks = get_tick_count()
increment_counter()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # += costs 1 tick
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 18: Storing function in list
# Expected: 1 tick for list creation
quick_print("=== Test 18: Storing function in list ===")
def my_func():
	return 42

start_ticks = get_tick_count()
func_list = [my_func]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # List with 1 item = max(1, 1) = 1 tick
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 19: Calling function from list
# Expected: 1 tick for indexing + 1 tick for call = 2 ticks
quick_print("=== Test 19: Calling function from list ===")
def stored_func():
	return 99

functions = [stored_func]
start_ticks = get_tick_count()
result = functions[0]()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # 1 tick for indexing functions[0], 1 tick for call
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 20: Storing function in dict
# Expected: 2 ticks for dict creation (1 key + 0 value + 1)
quick_print("=== Test 20: Storing function in dict ===")
def dict_func():
	return 123

start_ticks = get_tick_count()
func_dict = {'key': dict_func}
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # len(keys) + 1 = 1 + 1 = 2
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 21: Calling function from dict
# Expected: 1 tick for dict indexing + 1 tick for call = 2 ticks
quick_print("=== Test 21: Calling function from dict ===")
def dict_stored_func():
	return 456

func_map = {'action': dict_stored_func}
start_ticks = get_tick_count()
result = func_map['action']()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # 1 tick for dict indexing, 1 tick for call
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 22: Conditional function selection
# Expected: Cost of if + assignment
quick_print("=== Test 22: Conditional function selection ===")
def func_true():
	return 1

def func_false():
	return 0

condition = True
start_ticks = get_tick_count()
if condition:
	selected = func_true
else:
	selected = func_false
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # if costs 1 tick, assignment costs 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 23: Returning function from function
# Expected: 1 tick for inner def + 0 for return
quick_print("=== Test 23: Returning function from function ===")
def function_factory():
	def created_func():
		return 777
	return created_func

start_ticks = get_tick_count()
new_func = function_factory()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # Inner def costs 1, return costs 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 24: Calling returned function
# Expected: 1 tick for call + 1 tick for addition = 2 ticks
quick_print("=== Test 24: Calling returned function ===")
def make_adder(n):
	def adder(x):
		return x + n
	return adder

add_5 = make_adder(5)
start_ticks = get_tick_count()
result = add_5(10)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # 1 tick for call + 1 tick for x + n
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 25: Reassigning global function from within function
# Expected: 0 ticks for assignment
quick_print("=== Test 25: Reassigning global function ===")
def original_behavior():
	return 100

def new_behavior():
	return 200

active_function = original_behavior

def switch_function():
	global active_function
	active_function = new_behavior

start_ticks = get_tick_count()
switch_function()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0  # Assignment costs 0 ticks
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 26: Calling dynamically reassigned global function
# Expected: 1 tick for function call
quick_print("=== Test 26: Calling dynamically reassigned global function ===")
def func_version_1():
	return 1

def func_version_2():
	return 2

current_func = func_version_1

def swap_to_version_2():
	global current_func
	current_func = func_version_2

swap_to_version_2()
start_ticks = get_tick_count()
result = current_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # Function call costs 1 tick
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 27: Multiple function reassignments in one function
# Expected: 0 ticks per assignment
quick_print("=== Test 27: Multiple global function reassignments ===")
def strategy_a():
	return 10

def strategy_b():
	return 20

def strategy_c():
	return 30

strategy = strategy_a

def change_all_strategies():
	global strategy
	strategy = strategy_b
	strategy = strategy_c

start_ticks = get_tick_count()
change_all_strategies()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0  # 2 assignments, each costs 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 28: Conditional function reassignment with global
# Expected: 1 tick for if, 0 for assignment
quick_print("=== Test 28: Conditional global function reassignment ===")
def mode_easy():
	return 1

def mode_hard():
	return 10

game_mode = mode_easy

def set_difficulty(hard):
	global game_mode
	if hard:
		game_mode = mode_hard
	else:
		game_mode = mode_easy

start_ticks = get_tick_count()
set_difficulty(True)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # if costs 1 tick, assignment costs 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 29: Function that reassigns another global function
# Expected: 0 ticks for assignments
quick_print("=== Test 29: Function reassigning other global function ===")
def handler_default():
	return 0

def handler_custom():
	return 1

event_handler = handler_default
other_handler = handler_default

def update_handlers():
	global event_handler
	global other_handler
	event_handler = handler_custom
	other_handler = handler_custom

start_ticks = get_tick_count()
update_handlers()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0  # 2 assignments, each 0 ticks
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 30: Reassign function then call it immediately
# Expected: 0 for assignment + cost of called function
# Test 30: Reassign and call immediately
# Expected: 0 for assignment + 1 for call + 1 for addition = 2 ticks
quick_print("=== Test 30: Reassign and call immediately ===")
def compute_v1():
	return 5 + 5

def compute_v2():
	return 10 + 10

compute = compute_v1

def switch_and_compute():
	global compute
	compute = compute_v2
	return compute()

start_ticks = get_tick_count()
result = switch_and_compute()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # Assignment 0 + call 1 + addition 1 + return 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== All function tests completed ===")
