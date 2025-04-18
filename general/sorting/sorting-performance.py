# /general/sorting/*
from bubble_sort import *
from bucket_sort import *
from cocktail_sort import *
from comb_sort import *
from counting_sort import *
from gnome_sort import *
from heap_sort import *
from insertion_sort import *
from merge_sort import *
from quick_sort import *
from radix_sort import *
from selection_sort import *
from shell_sort import *

# /libraries/random.py
from random import randint
# /libraries/list.py
from list import is_sorted

sorting_functions = {
	"Bubble Sort": bubble_sort,
	"Bucket Sort": bucket_sort,
	"Cocktail Sort": cocktail_sort,
	"Comb Sort": comb_sort,
	"Counting Sort": counting_sort,
	"Gnome Sort": gnome_sort,
	"Heap Sort": heap_sort,
	"Insertion Sort": insertion_sort,
	"Merge Sort": merge_sort,
	"Quick Sort": quick_sort,
	"Radix Sort": radix_sort,
	"Selection Sort": selection_sort,
	"Shell Sort": shell_sort,
}
test_cases = {
	"Original test case": [3, 6, 8, 10, 1, 2, 1, 4, 5, 7],
	"Already sorted": [1, 2, 3, 4, 5, 6, 7, 8, 10],
	"Reverse sorted": [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
	"All elements the same": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	"Empty list": [],
	"Single element": [42],
	"Mixed positive and negative": [10, -1, 3, 9, -4, 0, 6, 4, -5, -2, 8, 7, 1, -3, 5, 2],
	"Floating point numbers": [3.14, 2.71, 1.41, 0.58, 1.61, 2.72, 1.41, 1.73],
	"Duplicate elements": [99, 99, 98, 97, 98, 99, 97, 98, 97, 99],
	"Large reverse sorted list": list(range(100, 0, -1)),
	# "Large random list": [randint(1, 1000) for _ in range(100)],
}
arr = []
for i in range(100):
	arr.append(randint(1, 1000))
test_cases["Large random list"] = arr

quick_print("# Sorting performance")
for algo in sorting_functions:
	quick_print("*********************************")
	quick_print("##", algo)
	quick_print("*********************************")
	for case in test_cases:
		list_copy = list(test_cases[case])
		ops = get_tick_count()

		sorted_arr = sorting_functions[algo](list_copy)

		ops = get_tick_count() - ops
		if sorted_arr == None:
			sorted_arr = list_copy
		if is_sorted(sorted_arr):
			quick_print(case, "passed successfully in **", ops, "** ops  <br/>")
		else:
			quick_print(case, "**failed**")
	quick_print("\n")
