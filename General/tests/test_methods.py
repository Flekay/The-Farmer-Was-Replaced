# Test file to confirm tick costs for collection methods
# Based on documentation in Tick Overview.md

# Test 1: .add() on set
# Expected: 1 tick
quick_print("=== Test 1: .add() on set ===")
test_set = {1, 2, 3, 4, 5}
start_ticks = get_tick_count()
test_set.add(6)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: .append() on list
# Expected: 1 tick
quick_print("=== Test 2: .append() on list ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
test_list.append(6)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: .insert() on list (at beginning)
# Expected: len(list) - insertion_index + 2 = 5 - 0 + 2 = 7 ticks
quick_print("=== Test 3: .insert() at index 0 ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
test_list.insert(0, 99)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 7  # len(list) - 0 + 2 = 7
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: .insert() on list (at middle)
# Expected: len(list) - insertion_index + 2 = 5 - 2 + 2 = 5 ticks
quick_print("=== Test 4: .insert() at index 2 ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
test_list.insert(2, 99)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # len(list) - 2 + 2 = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: .insert() on list (at end)
# Expected: len(list) - insertion_index + 2 = 5 - 5 + 2 = 2 ticks
quick_print("=== Test 5: .insert() at end (index 5) ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
test_list.insert(5, 99)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # len(list) - 5 + 2 = 2
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: .remove() on list (item at beginning)
# Expected: len(list) = 5 ticks
quick_print("=== Test 6: .remove() from list (item at index 0) ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
test_list.remove(1)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # len(list) = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: .remove() on list (item at middle)
# Expected: len(list) = 5 ticks
quick_print("=== Test 7: .remove() from list (item at index 2) ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
test_list.remove(3)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # len(list) = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: .remove() on list (item at end)
# Expected: len(list) = 5 ticks
quick_print("=== Test 8: .remove() from list (item at index 4) ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
test_list.remove(5)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # len(list) = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 9: .remove() on set
# Expected: 1 tick
quick_print("=== Test 9: .remove() from set ===")
test_set = {1, 2, 3, 4, 5}
start_ticks = get_tick_count()
test_set.remove(3)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 10: .pop() on list (no index - default to end)
# Expected: len(list) - idx, where idx defaults to len(list)
# So: 5 - 5 = 0, but minimum is 1 tick
quick_print("=== Test 10: .pop() from list (no index) ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
test_list.pop()
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # max(len(list) - len(list), 1) = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 11: .pop() on list (at index 0)
# Expected: len(list) - idx = 5 - 0 = 5 ticks
quick_print("=== Test 11: .pop() from list (index 0) ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
test_list.pop(0)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # len(list) - 0 = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 12: .pop() on list (at index 2)
# Expected: len(list) - idx = 5 - 2 = 3 ticks
quick_print("=== Test 12: .pop() from list (index 2) ===")
test_list = [1, 2, 3, 4, 5]
start_ticks = get_tick_count()
test_list.pop(2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3  # len(list) - 2 = 3
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 13: .pop() on dict
# Expected: 1 tick
quick_print("=== Test 13: .pop() from dict ===")
test_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
start_ticks = get_tick_count()
test_dict.pop(3)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Additional verification tests for .insert() with different list sizes
quick_print("=== Test 14: .insert() on list of length 3 at index 0 ===")
test_list = [1, 2, 3]
start_ticks = get_tick_count()
test_list.insert(0, 99)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # 3 - 0 + 2 = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== Test 15: .insert() on list of length 3 at index 1 ===")
test_list = [1, 2, 3]
start_ticks = get_tick_count()
test_list.insert(1, 99)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 4  # 3 - 1 + 2 = 4
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== Test 16: .insert() on list of length 10 at index 5 ===")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
test_list.insert(5, 99)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 7  # 10 - 5 + 2 = 7
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Additional verification tests for .remove() with different list sizes
quick_print("=== Test 17: .remove() from list of length 3 (item at index 0) ===")
test_list = [1, 2, 3]
start_ticks = get_tick_count()
test_list.remove(1)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3  # len(list) = 3
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== Test 18: .remove() from list of length 3 (item at index 1) ===")
test_list = [1, 2, 3]
start_ticks = get_tick_count()
test_list.remove(2)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3  # len(list) = 3
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== Test 19: .remove() from list of length 3 (item at index 2) ===")
test_list = [1, 2, 3]
start_ticks = get_tick_count()
test_list.remove(3)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3  # len(list) = 3
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== Test 20: .remove() from list of length 10 (item at index 0) ===")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
test_list.remove(1)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # len(list) = 10
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== Test 21: .remove() from list of length 10 (item at index 5) ===")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
test_list.remove(6)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # len(list) = 10
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== Test 22: .remove() from list of length 10 (item at index 9) ===")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
test_list.remove(10)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10  # len(list) = 10
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== All method tests completed ===")
