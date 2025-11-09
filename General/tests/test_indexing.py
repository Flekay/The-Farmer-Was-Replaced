# Test file to confirm tick costs for indexing operations
# Based on documentation in Tick Overview.md

# Test 1: Indexing with a value (list)
# Expected: 1 tick
quick_print("=== Test 1: Indexing list with value ===")
test_list = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
value = test_list[2]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: Indexing with a value (tuple)
# Expected: 1 tick
quick_print("=== Test 2: Indexing tuple with value ===")
test_tuple = (10, 20, 30, 40, 50)
start_ticks = get_tick_count()
value = test_tuple[2]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: Indexing with a value (dict)
# Expected: 1 tick
quick_print("=== Test 3: Indexing dict with key ===")
test_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
start_ticks = get_tick_count()
value = test_dict[3]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 4: Slicing list (2 items)
# Expected: max(number of items in slice, 1) = max(2, 1) = 2 ticks
quick_print("=== Test 4: Slicing list (2 items) ===")
test_list = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
slice_result = test_list[1:3]  # Gets [20, 30]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # 2 items
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 5: Slicing list (1 item)
# Expected: max(number of items in slice, 1) = max(1, 1) = 1 tick
quick_print("=== Test 5: Slicing list (1 item) ===")
test_list = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
slice_result = test_list[2:3]  # Gets [30]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # 1 item
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 6: Slicing list (all items)
# Expected: max(number of items in slice, 1) = max(5, 1) = 5 ticks
quick_print("=== Test 6: Slicing list (all items) ===")
test_list = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
slice_result = test_list[:]  # Gets all items
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5  # 5 items
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 7: Slicing list (0 items)
# Expected: max(number of items in slice, 1) = max(0, 1) = 1 tick
quick_print("=== Test 7: Slicing list (0 items) ===")
test_list = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
slice_result = test_list[2:2]  # Gets []
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1  # max(0, 1) = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 8: Slicing tuple (3 items)
# Expected: max(number of items in slice, 1) = max(3, 1) = 3 ticks
quick_print("=== Test 8: Slicing tuple (3 items) ===")
test_tuple = (10, 20, 30, 40, 50)
start_ticks = get_tick_count()
slice_result = test_tuple[1:4]  # Gets (20, 30, 40)
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3  # 3 items
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 9: Slicing with step (every other item)
# Expected: max(number of items in slice, 1) = max(3, 1) = 3 ticks
quick_print("=== Test 9: Slicing list with step (3 items) ===")
test_list = [10, 20, 30, 40, 50, 60]
start_ticks = get_tick_count()
slice_result = test_list[::2]  # Gets [10, 30, 50]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 3  # 3 items
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 10: Negative indexing
# Expected: 1 tick
quick_print("=== Test 10: Negative indexing ===")
test_list = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
value = test_list[-1]  # Gets last item
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 11: Slicing large list (10 items)
quick_print("=== Test 11: Slicing list (10 items) ===")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_ticks = get_tick_count()
slice_result = test_list[:]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 10
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 12: Negative slicing
quick_print("=== Test 12: Negative slicing ===")
test_list = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
slice_result = test_list[-3:-1]  # Gets [30, 40]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 2  # 2 items
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 13: Indexing string
quick_print("=== Test 13: Indexing string ===")
test_str = "hello"
start_ticks = get_tick_count()
value = test_str[2]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 14: Slicing string
quick_print("=== Test 14: Slicing string (5 chars) ===")
test_str = "hello world"
start_ticks = get_tick_count()
slice_result = test_str[0:5]  # "hello"
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 5
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

quick_print("=== All indexing tests completed ===")
