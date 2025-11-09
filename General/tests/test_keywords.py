# Test file to confirm tick costs for keywords
# Based on documentation in Tick Overview.md

# Test 1: pass
# Expected: 1 tick
quick_print("=== Test 1: pass ===")
start_ticks = get_tick_count()
pass
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: def
# Expected: 1 tick
quick_print("=== Test 2: def ===")
start_ticks = get_tick_count()
def test_func():
	pass
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: return
# Expected: 0 ticks
quick_print("=== Test 3: return ===")
def return_test():
	start = get_tick_count()
	return get_tick_count() - start

actual_cost = return_test()
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: break
# Expected: 0 ticks
quick_print("=== Test 4: break ===")
start_ticks = get_tick_count()
for i in range(10):
	if i == 0:
		before_break = get_tick_count()
		break
after_break = get_tick_count()
actual_cost = after_break - before_break
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: continue
# Expected: 0 ticks (continue itself)
# Test by comparing two identical loops: one with continue, one with pass
quick_print("=== Test 5: continue ===")

# Loop with continue (executes continue 2 times)
start1 = get_tick_count()
for i in range(3):
	if i < 2:
		continue
end1 = get_tick_count()
continue_loop_cost = end1 - start1

# Loop with pass (executes pass 2 times in same structure)
start2 = get_tick_count()
for i in range(3):
	if i < 2:
		pass
end2 = get_tick_count()
pass_loop_cost = end2 - start2

# Difference should be: 2 * (pass_cost - continue_cost) = 2 * (1 - 0) = 2
actual_cost = pass_loop_cost - continue_loop_cost
expected_cost = 2  # pass executes 2 times at 1 tick each, continue at 0 ticks
quick_print("Expected difference (pass - continue):", expected_cost, "ticks")
quick_print("Actual difference:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("(Confirms continue = 0 ticks, pass = 1 tick)")
quick_print("")

# Test 6: global
# Expected: 0 ticks
quick_print("=== Test 6: global ===")
global_var = 5
def global_test():
	start = get_tick_count()
	global global_var
	return get_tick_count() - start

actual_cost = global_test()
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== All keyword tests completed ===")
