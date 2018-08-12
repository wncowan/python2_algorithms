def binary_search(arr, key, start, end):
    print arr
    print "start", start
    print "end", end
    if end - start < 0:
        return False
    else:
        midpoint = start + (end - start) // 2
        print "arr[midpoint]", arr[midpoint]
        print "midpoint", midpoint
        if arr[midpoint] < key:
            return binary_search(arr, key, midpoint+1, end)
        elif arr[midpoint] > key:
            return binary_search(arr, key, start, midpoint-1)
        else:
            return midpoint


alist = [-90, -18 , 17, 23, 29, 77, 120, 250, 450]
print binary_search(alist, 79, 0 , len(alist))