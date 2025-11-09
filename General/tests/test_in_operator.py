# Test file to confirm tick costs for the 'in' operator on different collection types
# Based on documentation in Tick Overview.md

# Test 1: 'in' operator on lists (item exists)
# Expected: indexof(item) + 1 ticks
quick_print("=== Test 1: 'in' on list (item exists) ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
result = 3 in test_list  # Item at index 2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3  # indexof(3) = 2, so 2 + 1 = 3
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: 'in' operator on lists (item does not exist)
# Expected: len(list) ticks
quick_print("=== Test 2: 'in' on list (item not exists) ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
result = 99 in test_list
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # len(list) = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: 'in' operator on tuples (item exists)
# Expected: indexof(item) + 1 ticks
quick_print("=== Test 3: 'in' on tuple (item exists) ===")
test_tuple = (1, 2, 3, 4, 5)
start_ticks = get_tick_count()
result = 4 in test_tuple  # Item at index 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 4  # indexof(4) = 3, so 3 + 1 = 4
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: 'in' operator on tuples (item does not exist)
# Expected: len(tuple) ticks
quick_print("=== Test 4: 'in' on tuple (item not exists) ===")
test_tuple = (1, 2, 3, 4, 5)
start_ticks = get_tick_count()
result = 99 in test_tuple
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # len(tuple) = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: 'in' operator on sets (item exists)
# Expected: 1 tick
quick_print("=== Test 5: 'in' on set (item exists) ===")
test_set = {1, 2, 3, 4, 5}
start_ticks = get_tick_count()
result = 3 in test_set
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: 'in' operator on sets (item does not exist)
# Expected: 1 tick
quick_print("=== Test 6: 'in' on set (item not exists) ===")
test_set = {1, 2, 3, 4, 5}
start_ticks = get_tick_count()
result = 99 in test_set
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: 'in' operator on dicts (key exists)
# Expected: 1 tick
quick_print("=== Test 7: 'in' on dict (key exists) ===")
test_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
start_ticks = get_tick_count()
result = 3 in test_dict
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: 'in' operator on dicts (key does not exist)
# Expected: 1 tick
quick_print("=== Test 8: 'in' on dict (key not exists) ===")
test_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
start_ticks = get_tick_count()
result = 99 in test_dict
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 9: Edge case - 'in' on list with item at index 0
# Expected: indexof(item) + 1 = 0 + 1 = 1 tick
quick_print("=== Test 9: 'in' on list (item at index 0) ===")
test_list = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
result = 10 in test_list  # Item at index 0
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # indexof(10) = 0, so 0 + 1 = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 10: Edge case - 'in' on list with item at last index
# Expected: indexof(item) + 1 = 4 + 1 = 5 ticks
quick_print("=== Test 10: Edge case - 'in' on list with item at last index ===")
test_list = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
result = 50 in test_list  # Item at index 4
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # indexof(50) = 4, so 4 + 1 = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 11: 'in' on large list (item exists at middle)
quick_print("=== Test 11: 'in' on large list (10 items, item at index 5) ===")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
result = 6 in test_list  # Item at index 5
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 6  # indexof(6) = 5, so 5 + 1 = 6
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 12: 'in' on large list (item not exists)
quick_print("=== Test 12: 'in' on large list (10 items, item not exists) ===")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
result = 99 in test_list
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # len(list) = 10
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 13: 'in' on empty list
quick_print("=== Test 13: 'in' on empty list ===")
test_list = []
start_ticks = get_tick_count()
result = 1 in test_list
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0  # len(list) = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 14: 'in' on string
quick_print("=== Test 14: 'in' on string (char exists) ===")
test_str = "hello"
start_ticks = get_tick_count()
result = 'e' in test_str  # Char at index 1
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # Strings cost len(string) regardless of position
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 15: 'in' on string (char not exists)
quick_print("=== Test 15: 'in' on string (char not exists) ===")
test_str = "hello"
start_ticks = get_tick_count()
result = 'z' in test_str
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # len(str) = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 16: 'in' on string (char at index 0)
quick_print("=== Test 16: 'in' on string (char at index 0) ===")
test_str = "hello"
start_ticks = get_tick_count()
result = 'h' in test_str
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # Should still cost len(string)
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 17: 'in' on string (char at last index)
quick_print("=== Test 17: 'in' on string (char at last index) ===")
test_str = "hello"
start_ticks = get_tick_count()
result = 'o' in test_str  # Last character
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # Should still cost len(string)
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 18: 'in' on longer string (10 chars)
quick_print("=== Test 18: 'in' on longer string (10 chars) ===")
test_str = "helloworld"
start_ticks = get_tick_count()
result = 'w' in test_str  # At index 5
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # len(string) = 10
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 19: 'in' on longer string (char not exists)
quick_print("=== Test 19: 'in' on longer string (char not exists) ===")
test_str = "helloworld"
start_ticks = get_tick_count()
result = 'z' in test_str
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # len(string) = 10
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 20: 'in' on empty string
quick_print("=== Test 20: 'in' on empty string ===")
test_str = ""
start_ticks = get_tick_count()
result = 'a' in test_str
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0  # len(string) = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 21: 'in' on single character string (exists)
quick_print("=== Test 21: 'in' on single char string (exists) ===")
test_str = "a"
start_ticks = get_tick_count()
result = 'a' in test_str
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # len(string) = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 22: 'in' on single character string (not exists)
quick_print("=== Test 22: 'in' on single char string (not exists) ===")
test_str = "a"
start_ticks = get_tick_count()
result = 'b' in test_str
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # len(string) = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== All tests completed ===")
