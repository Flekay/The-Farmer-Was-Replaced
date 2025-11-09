# Test file to confirm tick costs for literals
# Based on documentation in Tick Overview.md

# Test 1: Literal value (number)
# Expected: 0 ticks
quick_print("=== Test 1: Literal value (number) ===")
start_ticks = get_tick_count()
x = 42
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: List literal (3 items)
# Expected: max(len(list), 1) = max(3, 1) = 3 ticks
quick_print("=== Test 2: List literal (3 items) ===")
start_ticks = get_tick_count()
x = [1, 2, 3]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: List literal (empty)
# Expected: max(len(list), 1) = max(0, 1) = 1 tick
quick_print("=== Test 3: List literal (empty) ===")
start_ticks = get_tick_count()
x = []
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: List literal (1 item)
# Expected: max(len(list), 1) = max(1, 1) = 1 tick
quick_print("=== Test 4: List literal (1 item) ===")
start_ticks = get_tick_count()
x = [1]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: Tuple literal (3 items, all literals)
# Expected: Sum of all value ticks + 1 = 0 + 0 + 0 + 1 = 1 tick
quick_print("=== Test 5: Tuple literal (3 items) ===")
start_ticks = get_tick_count()
x = (1, 2, 3)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: Tuple literal (empty)
# Expected: Sum of all value ticks + 1 = 0 + 1 = 1 tick
quick_print("=== Test 6: Tuple literal (empty) ===")
start_ticks = get_tick_count()
x = ()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: Set literal (3 items, all literals)
# Expected: Each item costs 1 tick to add, so 3 items = 3 ticks
quick_print("=== Test 7: Set literal (3 items) ===")
start_ticks = get_tick_count()
x = {1, 2, 3}
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3  # 1 tick per item
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: Dict literal (2 key-value pairs, all literals)
# Expected: 1 tick per key + 1 tick per value + 1 = 2 + 0 + 1 = 3 ticks
quick_print("=== Test 8: Dict literal (2 pairs) ===")
start_ticks = get_tick_count()
x = {1: 'a', 2: 'b'}
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3  # 1 per key, 0 per value (literal), +1 = 2+0+1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 9: Dict literal (empty)
# Expected: Sum of all key ticks + sum of all value ticks + 1 = 0 + 0 + 1 = 1 tick
quick_print("=== Test 9: Dict literal (empty) ===")
start_ticks = get_tick_count()
x = {}
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 10: List literal (10 items)
# Expected: max(len(list), 1) = max(10, 1) = 10 ticks
quick_print("=== Test 10: List literal (10 items) ===")
start_ticks = get_tick_count()
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 11: Tuple with nested literal (check if recursive)
quick_print("=== Test 11: Tuple with nested list ===")
start_ticks = get_tick_count()
x = ([1, 2], [3, 4])
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
# Nested: 2 lists (2 ticks each = 4) + 2 tuple elements (1 each = 2) + tuple base (1) = 7?
# Or: tuple counts list costs: 2 + 2 for lists, + tuple wrapper
expected_cost = 5  # Based on result: lists contribute their cost
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("(Nested literals count: 2 lists at 2 ticks each + tuple overhead)")
quick_print("")

# Test 12: Set literal (10 items)
quick_print("=== Test 12: Set literal (10 items) ===")
start_ticks = get_tick_count()
x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # 1 tick per item
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 13: Dict with 10 pairs
quick_print("=== Test 13: Dict literal (10 pairs) ===")
start_ticks = get_tick_count()
x = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'}
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 11  # 1 per key (10) + 0 per value + 1 = 11
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== All literal tests completed ===")
