# Bucket Sort
# requires the insertion_sort function
# since lists are passed by reference, this function modifies the original list
def bucket_sort(list):
    if len(list) == 0:
        return []
    min_value = min(list)
    max_value = max(list)

    # Number of buckets
    n = len(list)
    bucket_range = (max_value - min_value) // n + 1
    buckets = []
    for i in range(n):
        buckets.append([])

    # Put array elements in different buckets
    for num in list:
        index = (num - min_value) // bucket_range
        buckets[index].append(num)

    # Sort individual buckets using insertion sort
    for bucket in buckets:
        insertion_sort(bucket)

    # Concatenate all buckets into arr[]
    index = 0
    for bucket in buckets:
        for num in bucket:
            list[index] = num
            index += 1
    return list
