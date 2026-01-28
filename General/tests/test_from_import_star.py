# Test file for `from module import *` tick costs and zero-ticking techniques
# Based on Discord comment about static function definitions

quick_print("=== from module import * Tests ===")
quick_print("")

# Test 1: First `from module import *`
quick_print("=== Test 1: First from module import * ===")
start_ticks = get_tick_count()
from test_helper_module import *
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("First import * cost:", actual_cost, "ticks")
quick_print("")

# Test 2: Second `from module import *` (should be 0 ticks according to comment)
quick_print("=== Test 2: Second from module import * ===")
start_ticks = get_tick_count()
from test_helper_module import *
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Second import * cost:", actual_cost, "ticks")
quick_print("")

# Test 3: Third `from module import *`
quick_print("=== Test 3: Third from module import * ===")
start_ticks = get_tick_count()
from test_helper_module import *
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Third import * cost:", actual_cost, "ticks")
quick_print("")

# Test 4: Call imported function before override
quick_print("=== Test 4: Call native_user_func after import * ===")
start_ticks = get_tick_count()
result = native_user_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Cost:", actual_cost, "ticks")
quick_print("Result:", result)
quick_print("")

# Test 5: Override function with get_tick_count
quick_print("=== Test 5: Override native_user_func with get_tick_count ===")
start_ticks = get_tick_count()
native_user_func = get_tick_count
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Override cost:", actual_cost, "ticks")
quick_print("")

# Test 6: Call overridden function
quick_print("=== Test 6: Call overridden native_user_func ===")
start_ticks = get_tick_count()
result = native_user_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Cost:", actual_cost, "ticks")
quick_print("Result type check - is it tick count?:", result > 0)
quick_print("")

# Test 7: Re-import to restore function
quick_print("=== Test 7: Re-import * to restore function ===")
start_ticks = get_tick_count()
from test_helper_module import *
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Re-import cost:", actual_cost, "ticks")
quick_print("")

# Test 8: Call restored function
quick_print("=== Test 8: Call restored native_user_func ===")
start_ticks = get_tick_count()
result = native_user_func()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Cost:", actual_cost, "ticks")
quick_print("Result:", result)
quick_print("")

# Test 9: Compare regular import vs from import *
quick_print("=== Test 9: Compare regular import vs from import * ===")
# Regular import
start_ticks = get_tick_count()
import test_helper_module
end_ticks = get_tick_count()
regular_cost = end_ticks - start_ticks
# from import * (should be free after first time)
start_ticks = get_tick_count()
from test_helper_module import *
end_ticks = get_tick_count()
star_cost = end_ticks - start_ticks
quick_print("Regular import:", regular_cost, "ticks")
quick_print("from import * (repeated):", star_cost, "ticks")
quick_print("")

# Test 10: Multiple function overrides
quick_print("=== Test 10: Multiple function overrides ===")
from test_helper_module import native_user_func, another_func
# Call both before override
start_ticks = get_tick_count()
native_user_func()
another_func()
end_ticks = get_tick_count()
before_cost = end_ticks - start_ticks
quick_print("Both functions before override:", before_cost, "ticks")
# Override both
native_user_func = get_tick_count
another_func = get_tick_count
# Call both after override
start_ticks = get_tick_count()
native_user_func()
another_func()
end_ticks = get_tick_count()
after_cost = end_ticks - start_ticks
quick_print("Both functions after override:", after_cost, "ticks")
quick_print("Savings:", before_cost - after_cost, "ticks")
quick_print("")

# Test 11: Override with different system functions
quick_print("=== Test 11: Override with different system functions ===")
from test_helper_module import native_user_func
# Override with get_pos_x
native_user_func = get_pos_x
start_ticks = get_tick_count()
result = native_user_func()
end_ticks = get_tick_count()
quick_print("Override with get_pos_x cost:", end_ticks - start_ticks, "ticks")
# Override with harvest (should fail but only cost 1 tick)
native_user_func = harvest
start_ticks = get_tick_count()
try_result = native_user_func()
end_ticks = get_tick_count()
quick_print("Override with harvest cost:", end_ticks - start_ticks, "ticks")
