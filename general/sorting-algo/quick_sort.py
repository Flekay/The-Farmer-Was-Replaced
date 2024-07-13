# Quick Sort
# since resuls are returned, the original list is not modified
def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    left = []
    middle = []
    right = []
    for x in list:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left) + middle + quick_sort(right)
