# Test file to confirm tick costs for arithmetic operators
# Based on documentation in Tick Overview.md

# Test 1: + on numbers
# Expected: 1 tick
quick_print("=== Test 1: + on numbers ===")
start_ticks = get_tick_count()
result = 5 + 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: + on lists
# Expected: len(list1) + len(list2) = 3 + 2 = 5 ticks
quick_print("=== Test 2: + on lists ===")
list1 = [1, 2, 3]
list2 = [4, 5]
start_ticks = get_tick_count()
result = list1 + list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # 3 + 2
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: + on strings
# Expected: len(str1) + len(str2) = 5 + 5 = 10 ticks
quick_print("=== Test 3: + on strings ===")
str1 = "hello"
str2 = "world"
start_ticks = get_tick_count()
result = str1 + str2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # 5 + 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: + on tuples
# Expected: len(tuple1) + len(tuple2) = 2 + 3 = 5 ticks
quick_print("=== Test 4: + on tuples ===")
tuple1 = (1, 2)
tuple2 = (3, 4, 5)
start_ticks = get_tick_count()
result = tuple1 + tuple2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # 2 + 3
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: - (subtraction)
# Expected: 1 tick
quick_print("=== Test 5: - (subtraction) ===")
start_ticks = get_tick_count()
result = 10 - 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: * (multiplication)
# Expected: 1 tick
quick_print("=== Test 6: * (multiplication) ===")
start_ticks = get_tick_count()
result = 5 * 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: / (division)
# Expected: 1 tick
quick_print("=== Test 7: / (division) ===")
start_ticks = get_tick_count()
result = 10 / 2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: % (modulo)
# Expected: 1 tick
quick_print("=== Test 8: % (modulo) ===")
start_ticks = get_tick_count()
result = 10 % 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 9: ** (power)
# Expected: 1 tick
quick_print("=== Test 9: ** (power) ===")
start_ticks = get_tick_count()
result = 2 ** 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 10: + on empty lists
# Expected: len(list1) + len(list2) = 0 + 0 = 0 ticks
quick_print("=== Test 10: + on empty lists ===")
list1 = []
list2 = []
start_ticks = get_tick_count()
result = list1 + list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 11: + on empty list and non-empty list
# Expected: len(list1) + len(list2) = 0 + 3 = 3 ticks
quick_print("=== Test 11: + on empty + non-empty lists ===")
list1 = []
list2 = [1, 2, 3]
start_ticks = get_tick_count()
result = list1 + list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 12: + on empty strings
# Expected: len(str1) + len(str2) = 0 + 0 = 0 ticks
quick_print("=== Test 12: + on empty strings ===")
str1 = ""
str2 = ""
start_ticks = get_tick_count()
result = str1 + str2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 0
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== All arithmetic operator tests completed ===")
