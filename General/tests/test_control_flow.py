# Test file to confirm tick costs for control flow
# Based on documentation in Tick Overview.md

# Test 1: if statement
# Expected: 1 tick
quick_print("=== Test 1: if statement ===")
start_ticks = get_tick_count()
if True:
	end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: elif statement
# Expected: 1 tick for elif condition check
quick_print("=== Test 2: elif statement ===")
start_ticks = get_tick_count()
if False:
	pass
elif True:
	end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
# if costs 1 tick, elif costs 1 tick (for condition), total is 2
expected_cost = 2
quick_print("Expected:", expected_cost, "ticks (if + elif)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: else statement
# Expected: 0 ticks
quick_print("=== Test 3: else statement ===")
start_ticks = get_tick_count()
if False:
	pass
else:
	end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
# if costs 1 tick, else costs 0, so total is 1
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks (if + else)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: for loop initialization
# Expected: 1 tick (for initialization)
quick_print("=== Test 4: for loop initialization ===")
start_ticks = get_tick_count()
for i in range(0):
	pass
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
# range(0) costs 1 tick, for init costs 1 tick = 2 ticks total
expected_cost = 2
quick_print("Expected:", expected_cost, "ticks (range + for init)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: for loop iteration
# Expected: 0 ticks per iteration
quick_print("=== Test 5: for loop iteration ===")
tick_before_loop = get_tick_count()
for i in range(1):
	tick_in_first_iteration = get_tick_count()
	break
# range(1) = 1 tick, for init = 1 tick, iteration = 0 ticks
actual_cost = tick_in_first_iteration - tick_before_loop
expected_cost = 2
quick_print("Expected:", expected_cost, "ticks (range + for init + iteration)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: while loop initialization
# Expected: 1 tick
quick_print("=== Test 6: while loop initialization ===")
counter = 0
start_ticks = get_tick_count()
while counter < 0:
	pass
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
# while init costs 1 tick, comparison costs 1 tick = 2 ticks
expected_cost = 2
quick_print("Expected:", expected_cost, "ticks (while init + comparison)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: while loop iteration
# Expected: 0 ticks per iteration
quick_print("=== Test 7: while loop iteration ===")
counter = 0
tick_before_loop = get_tick_count()
while counter < 1:
	tick_in_first_iteration = get_tick_count()
	break
# while init = 1 tick, comparison = 1 tick, iteration = 0 ticks
actual_cost = tick_in_first_iteration - tick_before_loop
expected_cost = 2
quick_print("Expected:", expected_cost, "ticks (while init + comparison + iteration)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: Multiple iterations cost
quick_print("=== Test 8: for loop with 5 iterations ===")
tick_before_loop = get_tick_count()
iteration_ticks = []
for i in range(5):
	iteration_ticks.append(get_tick_count())
tick_after_loop = get_tick_count()
# Check if each iteration costs 0 ticks
if len(iteration_ticks) >= 2:
	first_iter_cost = iteration_ticks[0] - tick_before_loop
	second_iter_cost = iteration_ticks[1] - iteration_ticks[0]
	quick_print("First iteration from start:", first_iter_cost, "ticks")
	quick_print("Second iteration cost:", second_iter_cost, "ticks")
quick_print("")

# Test 9: Nested if statements
quick_print("=== Test 9: Nested if statements ===")
start_ticks = get_tick_count()
if True:
	if True:
		end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # 2 if statements, each costs 1 tick
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== All control flow tests completed ===")
