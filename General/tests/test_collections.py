# Test collection creation, indexing, assignment, and methods
# Based on documentation in Tick Overview.md

# Test 1: Dict empty literal
quick_print("=== Test 1: Dict empty literal {} ===")
start = get_tick_count()
d = {}
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "ticks")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 2: Dict literal 2 keys
quick_print("=== Test 2: Dict literal {1:'a', 2:'b'} ===")
start = get_tick_count()
d = {1: 'a', 2: 'b'}
end = get_tick_count()
actual = end - start
expected = 3  # len(keys) + 1 = 2 + 1
quick_print("Expected:", expected, "ticks (len(keys) + 1)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 3: Dict literal 5 keys
quick_print("=== Test 3: Dict literal 5 keys ===")
start = get_tick_count()
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
end = get_tick_count()
actual = end - start
expected = 6  # len(keys) + 1 = 5 + 1
quick_print("Expected:", expected, "ticks (len(keys) + 1)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 4: Dict constructor empty
quick_print("=== Test 4: dict() ===")
start = get_tick_count()
d = dict()
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "ticks")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 5: Dict constructor with args
quick_print("=== Test 5: dict(args) with 3 tuples ===")
args = [(1, 'a'), (2, 'b'), (3, 'c')]
start = get_tick_count()
d = dict(args)
end = get_tick_count()
actual = end - start
expected = 7  # 2 * len(args) + 1 = 2 * 3 + 1
quick_print("Expected:", expected, "ticks (2 * len(args) + 1)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 6: Dict indexing
quick_print("=== Test 6: d[key] indexing ===")
d = {1: 'a', 2: 'b', 3: 'c'}
start = get_tick_count()
value = d[2]
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 7: Dict assignment (indexing + assignment)
quick_print("=== Test 7: d[key] = value ===")
d = {1: 'a', 2: 'b', 3: 'c'}
start = get_tick_count()
d[2] = 'x'
end = get_tick_count()
actual = end - start
expected = 1  # 1 tick for indexing, 0 for assignment
quick_print("Expected:", expected, "tick (indexing only, assignment = 0)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 8: Dict pop
quick_print("=== Test 8: d.pop(key) ===")
d = {1: 'a', 2: 'b', 3: 'c'}
start = get_tick_count()
d.pop(2)
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 9: List empty literal
quick_print("=== Test 9: List empty literal [] ===")
start = get_tick_count()
lst = []
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 10: List literal 3 items
quick_print("=== Test 10: List literal [1,2,3] ===")
start = get_tick_count()
lst = [1, 2, 3]
end = get_tick_count()
actual = end - start
expected = 3  # max(len, 1) = max(3, 1)
quick_print("Expected:", expected, "ticks (max(len, 1))")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 11: List literal 10 items
quick_print("=== Test 11: List literal 10 items ===")
start = get_tick_count()
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
end = get_tick_count()
actual = end - start
expected = 10  # max(len, 1) = max(10, 1)
quick_print("Expected:", expected, "ticks (max(len, 1))")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 12: List constructor empty
quick_print("=== Test 12: list() ===")
start = get_tick_count()
lst = list()
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 13: List constructor with args
quick_print("=== Test 13: list(args) with 5 items ===")
args = [1, 2, 3, 4, 5]
start = get_tick_count()
lst = list(args)
end = get_tick_count()
actual = end - start
expected = 6  # len(args) + 1 = 5 + 1
quick_print("Expected:", expected, "ticks (len(args) + 1)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 14: List indexing
quick_print("=== Test 14: lst[idx] indexing ===")
lst = [1, 2, 3, 4, 5]
start = get_tick_count()
value = lst[2]
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 15: List assignment
quick_print("=== Test 15: lst[idx] = value ===")
lst = [1, 2, 3, 4, 5]
start = get_tick_count()
lst[2] = 99
end = get_tick_count()
actual = end - start
expected = 1  # 1 tick for indexing, 0 for assignment
quick_print("Expected:", expected, "tick (indexing only, assignment = 0)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 16: List append
quick_print("=== Test 16: lst.append() ===")
lst = [1, 2, 3]
start = get_tick_count()
lst.append(4)
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 17: List insert at start
quick_print("=== Test 17: lst.insert(0, item) ===")
lst = [1, 2, 3, 4, 5]
start = get_tick_count()
lst.insert(0, 99)
end = get_tick_count()
actual = end - start
expected = 7  # len(list) - idx + 2 = 5 - 0 + 2
quick_print("Expected:", expected, "ticks (len - idx + 2)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 18: List insert at middle
quick_print("=== Test 18: lst.insert(2, item) ===")
lst = [1, 2, 3, 4, 5]
start = get_tick_count()
lst.insert(2, 99)
end = get_tick_count()
actual = end - start
expected = 5  # len(list) - idx + 2 = 5 - 2 + 2
quick_print("Expected:", expected, "ticks (len - idx + 2)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 19: List insert at end
quick_print("=== Test 19: lst.insert(5, item) ===")
lst = [1, 2, 3, 4, 5]
start = get_tick_count()
lst.insert(5, 99)
end = get_tick_count()
actual = end - start
expected = 2  # len(list) - idx + 2 = 5 - 5 + 2
quick_print("Expected:", expected, "ticks (len - idx + 2)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 20: List remove
quick_print("=== Test 20: lst.remove(item) ===")
lst = [1, 2, 3, 4, 5]
start = get_tick_count()
lst.remove(3)
end = get_tick_count()
actual = end - start
expected = 5  # len(list)
quick_print("Expected:", expected, "ticks (len(list))")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 21: List pop from end
quick_print("=== Test 21: lst.pop() from end ===")
lst = [1, 2, 3, 4, 5]
start = get_tick_count()
lst.pop()
end = get_tick_count()
actual = end - start
expected = 1  # max(5 - 4, 1) = 1
quick_print("Expected:", expected, "tick (max(len - idx, 1))")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 22: List pop from start
quick_print("=== Test 22: lst.pop(0) from start ===")
lst = [1, 2, 3, 4, 5]
start = get_tick_count()
lst.pop(0)
end = get_tick_count()
actual = end - start
expected = 5  # max(5 - 0, 1) = 5
quick_print("Expected:", expected, "ticks (max(len - idx, 1))")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 23: List pop from middle
quick_print("=== Test 23: lst.pop(2) from middle ===")
lst = [1, 2, 3, 4, 5]
start = get_tick_count()
lst.pop(2)
end = get_tick_count()
actual = end - start
expected = 3  # max(5 - 2, 1) = 3
quick_print("Expected:", expected, "ticks (max(len - idx, 1))")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 24: Set literal 3 items
quick_print("=== Test 24: Set literal {1,2,3} ===")
start = get_tick_count()
s = {1, 2, 3}
end = get_tick_count()
actual = end - start
expected = 3  # len(set)
quick_print("Expected:", expected, "ticks (len(set))")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 25: Set literal 7 items
quick_print("=== Test 25: Set literal 7 items ===")
start = get_tick_count()
s = {1, 2, 3, 4, 5, 6, 7}
end = get_tick_count()
actual = end - start
expected = 7  # len(set)
quick_print("Expected:", expected, "ticks (len(set))")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 26: Set constructor empty
quick_print("=== Test 26: set() ===")
start = get_tick_count()
s = set()
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 27: Set constructor with args
quick_print("=== Test 27: set(args) with 4 items ===")
args = [1, 2, 3, 4]
start = get_tick_count()
s = set(args)
end = get_tick_count()
actual = end - start
expected = 5  # len(args) + 1 = 4 + 1
quick_print("Expected:", expected, "ticks (len(args) + 1)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 28: Set add
quick_print("=== Test 28: s.add(item) ===")
s = {1, 2, 3}
start = get_tick_count()
s.add(4)
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 29: Set remove
quick_print("=== Test 29: s.remove(item) ===")
s = {1, 2, 3}
start = get_tick_count()
s.remove(2)
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 30: Tuple empty literal
quick_print("=== Test 30: Tuple empty literal () ===")
start = get_tick_count()
t = ()
end = get_tick_count()
actual = end - start
expected = 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 31: Tuple literal 3 numbers
quick_print("=== Test 31: Tuple literal (1,2,3) ===")
start = get_tick_count()
t = (1, 2, 3)
end = get_tick_count()
actual = end - start
expected = 1  # sum(value_costs) + 1 = 0 + 0 + 0 + 1
quick_print("Expected:", expected, "tick (numbers are 0 cost)")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 32: Tuple with nested list
quick_print("=== Test 32: Tuple (lst, 5) ===")
lst = [1, 2, 3]
start = get_tick_count()
t = (lst, 5)
end = get_tick_count()
actual = end - start
expected = 1  # sum(value_costs) + 1 = 0 + 0 + 1
quick_print("Expected:", expected, "tick")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

# Test 33: Scalar literals
quick_print("=== Test 33: Scalar literals (number, string, bool, None) ===")
start = get_tick_count()
n = 42
s = "hello"
b = True
none = None
end = get_tick_count()
actual = end - start
expected = 0
quick_print("Expected:", expected, "ticks")
quick_print("Actual:", actual, "ticks")
quick_print("Pass:", actual == expected)
quick_print("")

quick_print("=== All collection tests completed ===")
