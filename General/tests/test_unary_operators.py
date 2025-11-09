# Test file to confirm tick costs for unary operators
# Based on documentation in Tick Overview.md

# Test 1: not operator
# Expected: 0 ticks
quick_print("=== Test 1: not operator ===")
start_ticks = get_tick_count()
result = not True
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: unary minus (-)
# Expected: 0 ticks
quick_print("=== Test 2: unary minus (-) ===")
start_ticks = get_tick_count()
result = -5
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: unary plus (+)
# Expected: 0 ticks
quick_print("=== Test 3: unary plus (+) ===")
start_ticks = get_tick_count()
result = +5
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== All unary operator tests completed ===")
