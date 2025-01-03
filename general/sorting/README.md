# Sorting Algorithms

This folder contains various sorting algorithm implementations. Note that these are general-purpose list sorting algorithms and are not related to the cacti sorting algorithms used elsewhere in the project.

## Implemented Algorithms

- **Bubble Sort**: A simple comparison-based sorting algorithm
- **Bucket Sort**: Distribution-based sorting for uniform data distribution
- **Cocktail Sort**: Bidirectional bubble sort variant
- **Comb Sort**: Improvement over bubble sort using gap sequence
- **Counting Sort**: Integer sorting algorithm using counting of objects
- **Gnome Sort**: Simple sorting algorithm similar to insertion sort
- **Heap Sort**: Comparison-based sort using a binary heap
- **Insertion Sort**: Simple sorting algorithm building final array one item at a time
- **Merge Sort**: Divide-and-conquer algorithm using merging of sorted subarrays
- **Quick Sort**: Efficient, in-place sorting algorithm using partitioning
- **Radix Sort**: Non-comparative integer sorting algorithm
- **Selection Sort**: In-place comparison sort
- **Shell Sort**: Optimization of insertion sort

## Performance Testing

The `sorting-performance.py` script tests each algorithm against various test cases:
- Original test case
- Already sorted arrays
- Reverse sorted arrays
- Arrays with identical elements
- Empty lists
- Single element arrays
- Mixed positive and negative numbers
- Floating point numbers
- Arrays with duplicate elements
- Large reverse sorted lists
- Large random lists

## Benchmark Results

See `sorting-results.md` for detailed performance metrics of each algorithm across all test cases. Notable observations:

- Quick Sort and Shell Sort perform consistently well across different scenarios
- Radix Sort fails with floating point and negative numbers
- Bubble Sort and Gnome Sort show poor performance on large datasets
- Merge Sort and Heap Sort maintain reliable performance regardless of input

## Important Notes
- `bucket_sort` is used for the `sorted.py` function found in the `general` folder
- Some algorithms modify the original array while others create a new sorted array
- Radix Sort only works with non-negative integers
