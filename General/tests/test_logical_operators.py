# Test file to confirm tick costs for logical operators
# Based on documentation in Tick Overview.md
#
# RECURSIVE COMPARISONS EXPLAINED:
# All comparison operators (==, !=, <, >, <=, >=) use recursive comparisons
# when comparing complex types like lists, tuples, or nested structures.
#
# This means the cost is not just 1 tick - it includes comparing all elements:
# - [1,2,3] == [1,2,3] compares each element: 1==1, 2==2, 3==3
# - [[1,2],[3,4]] == [[1,2],[3,4]] recursively compares nested lists
# - The comparison stops early if a difference is found (lexicographic)
# - Different length lists: [1,2,3] < [1,2,3,4] compares prefix first
#
# Base cost is documented as 1 tick, but recursive overhead adds significantly
# to the actual cost when comparing collections.

# Test 1: == (equality)
# Expected: 1 tick
quick_print("=== Test 1: == (equality) ===")
start_ticks = get_tick_count()
result = 5 == 5
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: != (not equal)
# Expected: 1 tick
quick_print("=== Test 2: != (not equal) ===")
start_ticks = get_tick_count()
result = 5 != 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: >= (greater than or equal)
# Expected: 1 tick
quick_print("=== Test 3: >= (greater than or equal) ===")
start_ticks = get_tick_count()
result = 5 >= 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: <= (less than or equal)
# Expected: 1 tick
quick_print("=== Test 4: <= (less than or equal) ===")
start_ticks = get_tick_count()
result = 3 <= 5
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: > (greater than)
# Expected: 1 tick
quick_print("=== Test 5: > (greater than) ===")
start_ticks = get_tick_count()
result = 5 > 3
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: < (less than)
# Expected: 1 tick
quick_print("=== Test 6: < (less than) ===")
start_ticks = get_tick_count()
result = 3 < 5
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: and (logical and)
# Expected: 1 tick
quick_print("=== Test 7: and (logical and) ===")
start_ticks = get_tick_count()
result = True and True
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: or (logical or)
# Expected: 1 tick
quick_print("=== Test 8: or (logical or) ===")
start_ticks = get_tick_count()
result = True or False
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 9: Short-circuit evaluation for 'and' (first False)
quick_print("=== Test 9: 'and' short-circuit (first False) ===")
start_ticks = get_tick_count()
result = False and True
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 10: Short-circuit evaluation for 'or' (first True)
quick_print("=== Test 10: 'or' short-circuit (first True) ===")
start_ticks = get_tick_count()
result = True or False
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 11: Comparison with lists (recursive)
quick_print("=== Test 11: == with lists ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
start_ticks = get_tick_count()
result = list1 == list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
# Should be recursive, so more than 1 tick expected
quick_print("Actual:", actual_cost, "ticks (testing if recursive)")
quick_print("")

# Test 12: == with longer lists (recursive comparison)
quick_print("=== Test 12: == with longer lists (10 elements) ===")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
result = list1 == list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks (recursive)")
quick_print("")

# Test 13: != with lists that differ at end
quick_print("=== Test 13: != with lists differing at end ===")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
start_ticks = get_tick_count()
result = list1 != list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks (must check all elements)")
quick_print("")

# Test 14: < with lists (lexicographic comparison)
quick_print("=== Test 14: < with lists (lexicographic) ===")
list1 = [1, 2, 3]
list2 = [1, 2, 4]
start_ticks = get_tick_count()
result = list1 < list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 15: > with lists of different lengths
quick_print("=== Test 15: > with different length lists ===")
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3]
start_ticks = get_tick_count()
result = list1 > list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 16: <= with tuples (recursive)
quick_print("=== Test 16: <= with tuples ===")
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 6)
start_ticks = get_tick_count()
result = tuple1 <= tuple2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 17: >= with nested lists (deeply recursive)
quick_print("=== Test 17: == with nested lists ===")
list1 = [[1, 2], [3, 4]]
list2 = [[1, 2], [3, 4]]
start_ticks = get_tick_count()
result = list1 == list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks (nested recursion)")
quick_print("")

# Test 18: != with nested lists differing deeply
quick_print("=== Test 18: != with nested lists (deep difference) ===")
list1 = [[1, 2], [3, 4]]
list2 = [[1, 2], [3, 5]]
start_ticks = get_tick_count()
result = list1 != list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 19: == with empty vs non-empty lists
quick_print("=== Test 19: == empty vs non-empty list ===")
list1 = []
list2 = [1]
start_ticks = get_tick_count()
result = list1 == list2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 20: < with tuples (many elements)
quick_print("=== Test 20: < with long tuples (10 elements) ===")
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 11)
start_ticks = get_tick_count()
result = tuple1 < tuple2
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

quick_print("=== All logical operator tests completed ===")
