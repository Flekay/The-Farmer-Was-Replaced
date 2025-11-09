# Test file to confirm tick costs for assignment operators
# Based on documentation in Tick Overview.md

# Test 1: = (assignment)
# Expected: 0 ticks
quick_print("=== Test 1: = (assignment) ===")
start_ticks = get_tick_count()
x = 5
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: +=
# Expected: 1 tick
quick_print("=== Test 2: += ===")
x = 5
start_ticks = get_tick_count()
x += 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: -=
# Expected: 1 tick
quick_print("=== Test 3: -= ===")
x = 5
start_ticks = get_tick_count()
x -= 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: *=
# Expected: 1 tick
quick_print("=== Test 4: *= ===")
x = 5
start_ticks = get_tick_count()
x *= 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: /=
# Expected: 1 tick
quick_print("=== Test 5: /= ===")
x = 10
start_ticks = get_tick_count()
x /= 2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: %=
# Expected: 1 tick
quick_print("=== Test 6: %= ===")
x = 10
start_ticks = get_tick_count()
x %= 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: **= (not available in game)
# Note: **= operator is not implemented and throws an error
quick_print("=== Test 7: **= (not available) ===")
quick_print("**= operator is not implemented in the game")
quick_print("Skipping test")
quick_print("")

quick_print("=== All assignment operator tests completed ===")
