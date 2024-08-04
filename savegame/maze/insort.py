def insort(list, item):
    lo = 0
    hi = len(list)
    while lo < hi:
        mid = (lo + hi) // 2
        if list[mid] < item:
            lo = mid + 1
        else:
            hi = mid
    list.insert(lo, item)