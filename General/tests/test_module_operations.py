# Test file to confirm tick costs for module imports and attribute operations
# Based on documentation in Tick Overview.md
#
# Prerequisites: test_helper_module.py must exist with attributes: data, fn

# Test 1: Module import
# Expected: 0 ticks
quick_print("=== Test 1: Module import ===")
start_ticks = get_tick_count()
import test_helper_module
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: Module attribute write
# Expected: 0 ticks
quick_print("=== Test 2: Module attribute write ===")
start_ticks = get_tick_count()
test_helper_module.data = 42
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: Module attribute read
# Expected: 0 ticks
quick_print("=== Test 3: Module attribute read ===")
start_ticks = get_tick_count()
x = test_helper_module.data
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: Write function to module attribute
# Expected: 0 ticks
quick_print("=== Test 4: Write function to module attribute ===")
start_ticks = get_tick_count()
test_helper_module.fn = get_tick_count
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: Call function through module attribute
# Expected: 0 ticks (same as direct call)
quick_print("=== Test 5: Call function through module attribute ===")
start_ticks = get_tick_count()
test_helper_module.fn()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: Store module in variable
# Expected: 0 ticks
quick_print("=== Test 6: Store module in variable ===")
start_ticks = get_tick_count()
dynamic_module = test_helper_module
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: Read attribute through dynamic module
# Expected: 0 ticks
quick_print("=== Test 7: Read attribute through dynamic module ===")
test_helper_module.data = 42
dynamic_module = test_helper_module
start_ticks = get_tick_count()
x = dynamic_module.data
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: Write attribute through dynamic module
# Expected: 1 tick ⚠️ CRITICAL: Dynamic write costs 1 tick!
quick_print("=== Test 8: Write attribute through dynamic module ===")
dynamic_module = test_helper_module
start_ticks = get_tick_count()
dynamic_module.data = 99
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks (IMPORTANT!)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 9: Call function through dynamic module
# Expected: 0 ticks (same as direct call)
quick_print("=== Test 9: Call function through dynamic module ===")
test_helper_module.fn = get_tick_count
dynamic_module = test_helper_module
start_ticks = get_tick_count()
dynamic_module.fn()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 10: Multiple attribute writes through dynamic module
# Expected: 2 ticks (1 per write)
quick_print("=== Test 10: Multiple writes through dynamic module ===")
dynamic_module = test_helper_module
start_ticks = get_tick_count()
dynamic_module.data = 1
dynamic_module.fn = get_tick_count
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2
quick_print("Expected:", expected_cost, "ticks (1 per write)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: Multiple module attribute reads
# Expected: ? ticks
quick_print("=== Test 8: Multiple module attribute reads ===")
start_ticks = get_tick_count()
a = test_helper_module.data
b = test_helper_module.fn
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 9: Expensive function through module (West.move)
# Expected: ? ticks (should be 200 if no overhead)
quick_print("=== Test 9: Expensive function through module ===")
test_helper_module.fn = West.move
start_ticks = get_tick_count()
test_helper_module.fn()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("Expected: 200 ticks if no overhead")
quick_print("")

# Test 15: Compare direct vs dynamic module function call
# Expected: Should be equal
quick_print("=== Test 15: Direct vs dynamic function call ===")
test_helper_module.fn = get_tick_count
dynamic_module = test_helper_module
# Direct through module
start_direct = get_tick_count()
test_helper_module.fn()
end_direct = get_tick_count()
direct_cost = end_direct - start_direct
# Through dynamic module
start_dynamic = get_tick_count()
dynamic_module.fn()
end_dynamic = get_tick_count()
dynamic_cost = end_dynamic - start_dynamic
quick_print("Direct module call:", direct_cost, "ticks")
quick_print("Dynamic module call:", dynamic_cost, "ticks")
quick_print("Pass:", direct_cost == dynamic_cost)
quick_print("")

# Test 16: Deeply nested dynamic module access
# Expected: 0 ticks (reading is always free)
quick_print("=== Test 16: Deeply nested dynamic access ===")
test_helper_module.data = 42
m = test_helper_module
m2 = m
m3 = m2
start_ticks = get_tick_count()
x = m3.data
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 17: User-defined function direct call
# Expected: 0 ticks
quick_print("=== Test 17: User-defined function direct call ===")
def my_user_func():
	return 42

start_ticks = get_tick_count()
result = my_user_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 18: User-defined function through module attribute
# Expected: ? ticks
quick_print("=== Test 18: User-defined function through module.func() ===")
test_helper_module.user_func = my_user_func
start_ticks = get_tick_count()
result = test_helper_module.user_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 19: User-defined function through dynamic module
# Expected: ? ticks
quick_print("=== Test 19: User-defined function through dynamic module ===")
test_helper_module.user_func = my_user_func
dynamic_module = test_helper_module
start_ticks = get_tick_count()
result = dynamic_module.user_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 20: Compare system vs user function through module
quick_print("=== Test 20: System vs User function through module ===")
# System function through module
test_helper_module.sys_func = get_tick_count
start_ticks = get_tick_count()
test_helper_module.sys_func()
end_ticks = get_tick_count()
system_cost = end_ticks - start_ticks
# User function through module
test_helper_module.user_func = my_user_func
start_ticks = get_tick_count()
test_helper_module.user_func()
end_ticks = get_tick_count()
user_cost = end_ticks - start_ticks
quick_print("System function through module:", system_cost, "ticks")
quick_print("User function through module:", user_cost, "ticks")
quick_print("Difference:", user_cost - system_cost, "ticks")
quick_print("")

# Test 21: Compare system vs user function through dynamic module
quick_print("=== Test 21: System vs User function through dynamic module ===")
dynamic_module = test_helper_module
# System function through dynamic module
test_helper_module.sys_func = get_tick_count
start_ticks = get_tick_count()
dynamic_module.sys_func()
end_ticks = get_tick_count()
system_cost = end_ticks - start_ticks
# User function through dynamic module
test_helper_module.user_func = my_user_func
start_ticks = get_tick_count()
dynamic_module.user_func()
end_ticks = get_tick_count()
user_cost = end_ticks - start_ticks
quick_print("System function through dynamic module:", system_cost, "ticks")
quick_print("User function through dynamic module:", user_cost, "ticks")
quick_print("Difference:", user_cost - system_cost, "ticks")
quick_print("")

# Test 22: Direct call to native module function
quick_print("=== Test 22: Direct call to native module function ===")
start_ticks = get_tick_count()
result = test_helper_module.native_user_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 23: Direct call through dynamic module to native function
quick_print("=== Test 23: Dynamic module call to native function ===")
dynamic_module = test_helper_module
start_ticks = get_tick_count()
result = dynamic_module.native_user_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 24: Compare native vs stored function
quick_print("=== Test 24: Native vs Stored function comparison ===")
# Native function in module
start_ticks = get_tick_count()
test_helper_module.native_user_func()
end_ticks = get_tick_count()
native_cost = end_ticks - start_ticks
# Stored function in module attribute
test_helper_module.user_func = my_user_func
start_ticks = get_tick_count()
test_helper_module.user_func()
end_ticks = get_tick_count()
stored_cost = end_ticks - start_ticks
quick_print("Native function (defined in module):", native_cost, "ticks")
quick_print("Stored function (assigned to module.attr):", stored_cost, "ticks")
quick_print("Are they equal?:", native_cost == stored_cost)
quick_print("")

# Test 25: Dynamic module with stored function
quick_print("=== Test 25: Dynamic module with stored function ===")
test_helper_module.user_func = my_user_func
dynamic_module = test_helper_module
start_ticks = get_tick_count()
result = dynamic_module.user_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("dynamic_module.stored_func():", actual_cost, "ticks")
quick_print("")

# Test 26: All four combinations
quick_print("=== Test 26: All combinations summary ===")
# 1. Static module, native function
start_ticks = get_tick_count()
test_helper_module.native_user_func()
end_ticks = get_tick_count()
static_native = end_ticks - start_ticks

# 2. Static module, stored function
test_helper_module.user_func = my_user_func
start_ticks = get_tick_count()
test_helper_module.user_func()
end_ticks = get_tick_count()
static_stored = end_ticks - start_ticks

# 3. Dynamic module, native function
dynamic_module = test_helper_module
start_ticks = get_tick_count()
dynamic_module.native_user_func()
end_ticks = get_tick_count()
dynamic_native = end_ticks - start_ticks

# 4. Dynamic module, stored function
start_ticks = get_tick_count()
dynamic_module.user_func()
end_ticks = get_tick_count()
dynamic_stored = end_ticks - start_ticks

quick_print("module.native_func():", static_native, "ticks")
quick_print("module.stored_func():", static_stored, "ticks")
quick_print("dynamic_module.native_func():", dynamic_native, "ticks")
quick_print("dynamic_module.stored_func():", dynamic_stored, "ticks")
quick_print("")
