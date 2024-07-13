# Insertion Sort
# since lists are passed by reference, this function modifies the original list
def insertion_sort(list):
    for i in range(1, len(list)):
        a = list[i]
        j = i - 1
        while j >= 0 and a < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = a
    return list
