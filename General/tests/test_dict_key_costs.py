# Test file to confirm tick costs for dictionary operations with different key types
# Based on documentation in Tick Overview.md

quick_print("=== Dictionary Key Cost Tests ===")
quick_print("")

# Test 1: Dict indexing with simple integer key (read)
# Expected: 1 tick for indexing
quick_print("=== Test 1: Dict[int] read ===")
d = {1: 'a', 2: 'b', 3: 'c'}
start_ticks = get_tick_count()
value = d[2]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 2: Dict assignment with simple integer key
# Expected: 1 tick for indexing + 0 ticks for assignment = 1 tick total
quick_print("=== Test 2: Dict[int] assignment ===")
d = {1: 'a', 2: 'b', 3: 'c'}
start_ticks = get_tick_count()
d[2] = 'x'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
expected_cost = 1
quick_print("Expected:", expected_cost, "ticks (1 for indexing + 0 for assignment)")
quick_print("Actual:", actual_cost, "ticks")
quick_print("Pass:", actual_cost == expected_cost)
quick_print("")

# Test 3: Dict indexing with short string key (read)
# Expected: ? ticks (need to measure)
quick_print("=== Test 3: Dict[short string 'a'] read ===")
d = {'a': 1, 'b': 2, 'c': 3}
start_ticks = get_tick_count()
value = d['a']
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 4: Dict indexing with medium string key (read)
# Expected: ? ticks (need to measure)
quick_print("=== Test 4: Dict[medium string 'hello'] read ===")
d = {'hello': 1, 'world': 2, 'test': 3}
start_ticks = get_tick_count()
value = d['hello']
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 5: Dict indexing with long string key (read)
# Expected: ? ticks (need to measure)
quick_print("=== Test 5: Dict[long string] read ===")
long_key = "this_is_a_very_long_key_name_to_test_performance"
d = {long_key: 1, 'other': 2}
start_ticks = get_tick_count()
value = d[long_key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Key length:", len(long_key), "chars")
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 6: Dict indexing with tuple key (2 elements, read)
# Expected: ? ticks (need to measure)
quick_print("=== Test 6: Dict[tuple (2 elements)] read ===")
d = {(1, 2): 'a', (3, 4): 'b', (5, 6): 'c'}
start_ticks = get_tick_count()
value = d[(3, 4)]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 7: Dict indexing with tuple key (3 elements, read)
# Expected: ? ticks (need to measure)
quick_print("=== Test 7: Dict[tuple (3 elements)] read ===")
d = {(1, 2, 3): 'a', (4, 5, 6): 'b', (7, 8, 9): 'c'}
start_ticks = get_tick_count()
value = d[(4, 5, 6)]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 8: Dict indexing with tuple key (5 elements, read)
# Expected: ? ticks (need to measure)
quick_print("=== Test 8: Dict[tuple (5 elements)] read ===")
d = {(1, 2, 3, 4, 5): 'a', (6, 7, 8, 9, 10): 'b'}
start_ticks = get_tick_count()
value = d[(1, 2, 3, 4, 5)]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 9: Dict assignment with short string key
# Expected: ? ticks (need to measure)
quick_print("=== Test 9: Dict[short string 'a'] assignment ===")
d = {'a': 1, 'b': 2, 'c': 3}
start_ticks = get_tick_count()
d['a'] = 99
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 10: Dict assignment with medium string key
# Expected: ? ticks (need to measure)
quick_print("=== Test 10: Dict[medium string 'hello'] assignment ===")
d = {'hello': 1, 'world': 2, 'test': 3}
start_ticks = get_tick_count()
d['hello'] = 99
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 11: Dict assignment with long string key
# Expected: ? ticks (need to measure)
quick_print("=== Test 11: Dict[long string] assignment ===")
long_key = "this_is_a_very_long_key_name_to_test_performance"
d = {long_key: 1, 'other': 2}
start_ticks = get_tick_count()
d[long_key] = 99
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Key length:", len(long_key), "chars")
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 12: Dict assignment with tuple key (2 elements)
# Expected: ? ticks (need to measure)
quick_print("=== Test 12: Dict[tuple (2 elements)] assignment ===")
d = {(1, 2): 'a', (3, 4): 'b', (5, 6): 'c'}
start_ticks = get_tick_count()
d[(3, 4)] = 'x'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 13: Dict assignment with tuple key (3 elements)
# Expected: ? ticks (need to measure)
quick_print("=== Test 13: Dict[tuple (3 elements)] assignment ===")
d = {(1, 2, 3): 'a', (4, 5, 6): 'b', (7, 8, 9): 'c'}
start_ticks = get_tick_count()
d[(4, 5, 6)] = 'x'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 14: Dict assignment with tuple key (5 elements)
# Expected: ? ticks (need to measure)
quick_print("=== Test 14: Dict[tuple (5 elements)] assignment ===")
d = {(1, 2, 3, 4, 5): 'a', (6, 7, 8, 9, 10): 'b'}
start_ticks = get_tick_count()
d[(1, 2, 3, 4, 5)] = 'x'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 15: Dict assignment with new key (int)
# Expected: ? ticks (need to measure - might differ from existing key)
quick_print("=== Test 15: Dict[int] assignment (new key) ===")
d = {1: 'a', 2: 'b', 3: 'c'}
start_ticks = get_tick_count()
d[99] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 16: Dict assignment with new string key
# Expected: ? ticks (need to measure)
quick_print("=== Test 16: Dict[string] assignment (new key) ===")
d = {'a': 1, 'b': 2, 'c': 3}
start_ticks = get_tick_count()
d['newkey'] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 17: Dict assignment with new tuple key
# Expected: ? ticks (need to measure)
quick_print("=== Test 17: Dict[tuple] assignment (new key) ===")
d = {(1, 2): 'a', (3, 4): 'b'}
start_ticks = get_tick_count()
d[(99, 100)] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 18: String keys of varying lengths (read)
quick_print("=== Test 18: String key length comparison (read) ===")
# Length 1
key = 'a'
d = {key: 'value', 'other': 'data'}
start_ticks = get_tick_count()
value = d[key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 1 char:", actual_cost, "ticks")

# Length 5
key = 'abcde'
d = {key: 'value', 'other': 'data'}
start_ticks = get_tick_count()
value = d[key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 5 chars:", actual_cost, "ticks")

# Length 10
key = 'abcdefghij'
d = {key: 'value', 'other': 'data'}
start_ticks = get_tick_count()
value = d[key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 10 chars:", actual_cost, "ticks")

# Length 20
key = 'abcdefghijklmnopqrst'
d = {key: 'value', 'other': 'data'}
start_ticks = get_tick_count()
value = d[key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 20 chars:", actual_cost, "ticks")

# Length 50
key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV'
d = {key: 'value', 'other': 'data'}
start_ticks = get_tick_count()
value = d[key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 50 chars:", actual_cost, "ticks")
quick_print("")

# Test 19: Tuple key length comparison (read)
quick_print("=== Test 19: Tuple key length comparison (read) ===")
# Length 1
key = (0,)
d = {key: 'value', (999,): 'other'}
start_ticks = get_tick_count()
value = d[key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 1 element:", actual_cost, "ticks")

# Length 2
key = (0, 1)
d = {key: 'value', (999,): 'other'}
start_ticks = get_tick_count()
value = d[key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 2 elements:", actual_cost, "ticks")

# Length 3
key = (0, 1, 2)
d = {key: 'value', (999,): 'other'}
start_ticks = get_tick_count()
value = d[key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 3 elements:", actual_cost, "ticks")

# Length 5
key = (0, 1, 2, 3, 4)
d = {key: 'value', (999,): 'other'}
start_ticks = get_tick_count()
value = d[key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 5 elements:", actual_cost, "ticks")

# Length 10
key = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
d = {key: 'value', (999,): 'other'}
start_ticks = get_tick_count()
value = d[key]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 10 elements:", actual_cost, "ticks")
quick_print("")

# Test 20: String keys of varying lengths (assignment)
quick_print("=== Test 20: String key length comparison (assignment) ===")
# Length 1
key = 'a'
d = {key: 'value', 'other': 'data'}
start_ticks = get_tick_count()
d[key] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 1 char:", actual_cost, "ticks")

# Length 5
key = 'abcde'
d = {key: 'value', 'other': 'data'}
start_ticks = get_tick_count()
d[key] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 5 chars:", actual_cost, "ticks")

# Length 10
key = 'abcdefghij'
d = {key: 'value', 'other': 'data'}
start_ticks = get_tick_count()
d[key] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 10 chars:", actual_cost, "ticks")

# Length 20
key = 'abcdefghijklmnopqrst'
d = {key: 'value', 'other': 'data'}
start_ticks = get_tick_count()
d[key] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 20 chars:", actual_cost, "ticks")

# Length 50
key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV'
d = {key: 'value', 'other': 'data'}
start_ticks = get_tick_count()
d[key] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 50 chars:", actual_cost, "ticks")
quick_print("")

# Test 21: Tuple key length comparison (assignment)
quick_print("=== Test 21: Tuple key length comparison (assignment) ===")
# Length 1
key = (0,)
d = {key: 'value', (999,): 'other'}
start_ticks = get_tick_count()
d[key] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 1 element:", actual_cost, "ticks")

# Length 2
# Test 22: List indexing with integer (read)
quick_print("=== Test 22: List[int] read ===")
lst = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
value = lst[2]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 23: List assignment with integer (write)
quick_print("=== Test 23: List[int] assignment ===")
lst = [10, 20, 30, 40, 50]
start_ticks = get_tick_count()
lst[2] = 99
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks (1 for indexing + 0 for assignment)")
quick_print("")

# Test 24: String indexing (read)
quick_print("=== Test 24: String[int] read ===")
s = "hello world"
start_ticks = get_tick_count()
value = s[5]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 25: Tuple indexing (read)
quick_print("=== Test 25: Tuple[int] read ===")
t = (10, 20, 30, 40, 50)
start_ticks = get_tick_count()
value = t[2]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 26: Nested dict indexing (read)
quick_print("=== Test 26: Dict[int][int] nested read ===")
d = {1: {10: 'a', 20: 'b'}, 2: {30: 'c', 40: 'd'}}
start_ticks = get_tick_count()
value = d[1][20]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks (should be 2 indexing operations)")
quick_print("")

# Test 27: Nested dict assignment
quick_print("=== Test 27: Dict[int][int] nested assignment ===")
d = {1: {10: 'a', 20: 'b'}, 2: {30: 'c', 40: 'd'}}
start_ticks = get_tick_count()
d[1][20] = 'x'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks (1 for outer indexing + 1 for inner indexing + 0 for assignment)")
quick_print("")

# Test 28: List of lists indexing (read)
quick_print("=== Test 28: List[int][int] nested read ===")
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
start_ticks = get_tick_count()
value = lst[1][2]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 29: List of lists assignment
quick_print("=== Test 29: List[int][int] nested assignment ===")
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
start_ticks = get_tick_count()
lst[1][2] = 99
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks")
quick_print("")

# Test 30: Dict with nested tuple key
quick_print("=== Test 30: Dict[(int, int)] with nested tuple value access ===")
d = {(1, 2): [10, 20, 30], (3, 4): [40, 50, 60]}
start_ticks = get_tick_count()
value = d[(1, 2)][1]
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Actual:", actual_cost, "ticks (tuple key indexing + list indexing)")
quick_print("")

key = (0, 1)
d = {key: 'value', (999,): 'other'}
start_ticks = get_tick_count()
d[key] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 2 elements:", actual_cost, "ticks")

# Length 3
key = (0, 1, 2)
d = {key: 'value', (999,): 'other'}
start_ticks = get_tick_count()
d[key] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 3 elements:", actual_cost, "ticks")

# Length 5
key = (0, 1, 2, 3, 4)
d = {key: 'value', (999,): 'other'}
start_ticks = get_tick_count()
d[key] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 5 elements:", actual_cost, "ticks")

# Length 10
key = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
d = {key: 'value', (999,): 'other'}
start_ticks = get_tick_count()
d[key] = 'new'
end_ticks = get_tick_count()
actual_cost = end_ticks - start_ticks
quick_print("Length 10 elements:", actual_cost, "ticks")
quick_print("")

quick_print("=== All dictionary key cost tests completed ===")
