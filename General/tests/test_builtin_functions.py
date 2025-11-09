# Test file to confirm tick costs for builtin functions
# Based on documentation in Tick Overview.md
#
# RECURSIVE COMPARISONS EXPLAINED:
# When comparing complex types like lists or tuples, the game compares
# element-by-element recursively. This means:
# - min([1,3], [2,4]) compares each element: 1 vs 2, then 3 vs 4
# - The cost includes both the base comparison cost AND the cost of
#   comparing the elements inside
# - Nested structures are compared deeply: ((1,2), (3,4)) vs ((1,2), (3,5))
# - This applies to min(), max(), ==, !=, <, >, <=, >= operators
# - Example costs (WITHOUT list creation overhead):
#   * min([1,3], [2,4]) = 6 ticks (2 args + 4 comparisons)
#   * min([1,2], [3,4], [5,6]) = 9 ticks (3 args + 6 comparisons)
#   * min([1,2,3,4,5], [1,2,3,4,6]) = 13 ticks (must compare all 5 elements)
#   * min([1...10], [1...11]) = 23 ticks (10-element comparison)
#   * The formula max(len(items), 1) applies to the top-level count,
#     but recursive comparison adds overhead based on the data being compared

# Test 1: abs()
# Expected: 1 tick
quick_print("=== Test 1: abs() ===")
start_ticks = get_tick_count()
result = abs(-5)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: len()
# Expected: 1 tick
quick_print("=== Test 2: len() ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
result = len(test_list)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: range()
# Expected: 1 tick
quick_print("=== Test 3: range() ===")
start_ticks = get_tick_count()
result = range(10)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: list() with no args
# Expected: 1 tick
quick_print("=== Test 4: list() with no args ===")
start_ticks = get_tick_count()
result = list()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: list() with args
# Expected: len(args) + 1 ticks
quick_print("=== Test 5: list() with args (5 items) ===")
test_tuple = (1, 2, 3, 4, 5)
start_ticks = get_tick_count()
result = list(test_tuple)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 6  # 5 + 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: set() with no args
# Expected: 1 tick
quick_print("=== Test 6: set() with no args ===")
start_ticks = get_tick_count()
result = set()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: set() with args
# Expected: len(args) + 1 ticks
quick_print("=== Test 7: set() with args (5 items) ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
result = set(test_list)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 6  # 5 + 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: dict() with no args
# Expected: 1 tick
quick_print("=== Test 8: dict() with no args ===")
start_ticks = get_tick_count()
result = dict()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 9: min() on list
# Expected: max(len(items), 1) = max(5, 1) = 5 ticks
# Note: test_list is pre-created, so only min() cost is measured
quick_print("=== Test 9: min() on list (5 items) ===")
test_list = [5, 2, 8, 1, 9]
start_ticks = get_tick_count()
result = min(test_list)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # max(5, 1)
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 10: max() on list
# Expected: max(len(items), 1) = max(5, 1) = 5 ticks
# Note: test_list is pre-created, so only max() cost is measured
quick_print("=== Test 10: max() on list (5 items) ===")
test_list = [5, 2, 8, 1, 9]
start_ticks = get_tick_count()
result = max(test_list)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # max(5, 1)
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 11: min() with 1 item
# Expected: 1 tick for list creation + 1 tick for min() = 2 ticks
# Note: [5] costs 1 tick to create, min() on 1 item costs max(1,1)=1 tick
quick_print("=== Test 11: min() with 1 item ===")
start_ticks = get_tick_count()
result = min([5])
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # 1 for [5] creation + 1 for min()
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 12: max() with 1 item
# Expected: 1 tick for list creation + 1 tick for max() = 2 ticks
# Note: [5] costs 1 tick to create, max() on 1 item costs max(1,1)=1 tick
quick_print("=== Test 12: max() with 1 item ===")
start_ticks = get_tick_count()
result = max([5])
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # 1 for [5] creation + 1 for max()
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 13: list() with empty iterable
# Expected: len(args) + 1 = 0 + 1 = 1 tick
quick_print("=== Test 13: list() with empty iterable ===")
test_tuple = ()
start_ticks = get_tick_count()
result = list(test_tuple)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # 0 + 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 14: set() with empty iterable
quick_print("=== Test 14: set() with empty iterable ===")
test_list = []
start_ticks = get_tick_count()
result = set(test_list)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # len(args) + 1 = 0 + 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 15: min() with 10 items
# Expected: max(len(items), 1) = max(10, 1) = 10 ticks
# Note: test_list is pre-created, so only min() cost is measured
quick_print("=== Test 15: min() with 10 items ===")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
result = min(test_list)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # max(10, 1)
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 16: max() with 10 items
# Expected: max(len(items), 1) = max(10, 1) = 10 ticks
# Note: test_list is pre-created, so only max() cost is measured
quick_print("=== Test 16: max() with 10 items ===")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
result = max(test_list)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # max(10, 1)
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 17: list() with 10 items
# Expected: len(args) + 1 = 10 + 1 = 11 ticks
quick_print("=== Test 17: list() with 10 items ===")
test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
start_ticks = get_tick_count()
result = list(test_tuple)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 11  # 10 + 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 18: set() with 10 items
quick_print("=== Test 18: set() with 10 items ===")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
result = set(test_list)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 11  # 10 + 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 19: min() with multiple arguments (not a list)
# Note: Direct arguments, no list creation overhead
quick_print("=== Test 19: min() with multiple number arguments ===")
start_ticks = get_tick_count()
result = min(5, 2, 8, 1, 9)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
# 5 arguments, expected: max(5, 1) = 5 ticks
expected_cost = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 20: max() with multiple arguments (not a list)
# Note: Direct arguments, no list creation overhead
quick_print("=== Test 20: max() with multiple number arguments ===")
start_ticks = get_tick_count()
result = max(5, 2, 8, 1, 9)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
# 5 arguments, expected: max(5, 1) = 5 ticks
expected_cost = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 21: min() with list arguments (recursive comparison)
quick_print("=== Test 21: min() with list arguments ===")
list1 = [1, 3]
list2 = [2, 4]
start_ticks = get_tick_count()
result = min(list1, list2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 6  # Recursive: 2 args (base) + comparing 2 lists with 2 items each
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 22: max() with list arguments (recursive comparison)
quick_print("=== Test 22: max() with list arguments ===")
list1 = [1, 3]
list2 = [2, 4]
start_ticks = get_tick_count()
result = max(list1, list2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 6  # Recursive: 2 args (base) + comparing 2 lists with 2 items each
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 23: min() with 3 list arguments
quick_print("=== Test 23: min() with 3 list arguments ===")
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
start_ticks = get_tick_count()
result = min(list1, list2, list3)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 9  # Recursive: 3 args (base) + comparing 3 lists with 2 items each
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 24: min() with 2 arguments
# Note: Direct arguments, no list creation overhead
quick_print("=== Test 24: min() with 2 number arguments ===")
start_ticks = get_tick_count()
result = min(5, 3)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # max(2, 1) = 2
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 25: min() with longer lists (recursive comparison)
# Demonstrates that comparison dives into list elements
# Pattern: 2 args (base) + recursive comparison of 5-element lists
quick_print("=== Test 25: min() with longer lists (5 items each) ===")
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 6]
start_ticks = get_tick_count()
result = min(list1, list2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 13  # Must compare all 5 elements to find difference
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 26: max() with nested tuples (deeply recursive)
# Shows recursion goes multiple levels deep
quick_print("=== Test 26: max() with nested tuples ===")
tuple1 = (1, 2)
tuple2 = (1, 3)
start_ticks = get_tick_count()
result = max(tuple1, tuple2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 7  # 2 args + recursive comparison of 2-element tuples
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 27: min() with different length lists
# Shorter list is "less than" longer when prefixes match
quick_print("=== Test 27: min() with different length lists ===")
list1 = [1, 2, 3]
list2 = [1, 2]
start_ticks = get_tick_count()
result = min(list1, list2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 7  # Compare elements until length difference found
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 28: min() with 4 list arguments
# 4 lists with 2 items each
quick_print("=== Test 28: min() with 4 list arguments ===")
list1 = [5, 6]
list2 = [3, 4]
list3 = [7, 8]
list4 = [1, 2]
start_ticks = get_tick_count()
result = min(list1, list2, list3, list4)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 12  # 4 args + recursive comparisons
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 29: max() with lists of different lengths (complex)
# 3 lists of varying lengths (1, 2, 3 items)
quick_print("=== Test 29: max() with variable length lists ===")
list1 = [1]
list2 = [1, 2]
list3 = [1, 2, 3]
start_ticks = get_tick_count()
result = max(list1, list2, list3)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 7  # Comparisons of variable length lists
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 30: min() with lists containing same values
# Must compare all elements to determine equality
quick_print("=== Test 30: min() with identical lists ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
start_ticks = get_tick_count()
result = min(list1, list2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 8  # Full comparison of identical 3-element lists
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 31: max() with single-element lists (many args)
# 10 arguments, each list has 1 element
quick_print("=== Test 31: max() with many single-element lists ===")
list1 = [1]
list2 = [2]
list3 = [3]
list4 = [4]
list5 = [5]
list6 = [6]
list7 = [7]
list8 = [8]
list9 = [9]
list10 = [10]
start_ticks = get_tick_count()
result = max(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 29  # 10 args + recursive comparisons of single-element lists
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 32: min() with longer lists (10 elements each)
# 2 lists of 10 elements each, differ only at end
quick_print("=== Test 32: min() with long lists (10 elements each) ===")
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,11]
start_ticks = get_tick_count()
result = min(list1, list2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 23  # Must check all 10 elements to find difference
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 33: min() mixing numbers and single-item lists
# 3 arguments, mix of list and tuple types
quick_print("=== Test 33: min() with mix of lists and tuples ===")
list1 = [1, 5]
tuple1 = (2, 3)
list2 = [1, 4]
start_ticks = get_tick_count()
result = min(list1, tuple1, list2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # 3 args with 2-element collections each
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 34: max() with empty lists
# Empty list vs non-empty list
# Result: 2 ticks (base cost for 2 args)
quick_print("=== Test 34: max() comparing empty and non-empty lists ===")
list1 = []
list2 = [1]
start_ticks = get_tick_count()
result = max(list1, list2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 35: min() with 3 longer lists
# 3 lists of 5 elements each
quick_print("=== Test 35: min() with 3 longer lists (5 elements) ===")
list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]
list3 = [3,4,5,6,7]
start_ticks = get_tick_count()
result = min(list1, list2, list3)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 12  # 3 args + recursive comparisons of 5-element lists
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== All builtin function tests completed ===")
