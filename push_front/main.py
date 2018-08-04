def push_to_front(arr, val):
    arr.append(0)
    for i in range(len(arr)-2, -1, -1):
        print i
        arr[i], arr[i+1] = arr[i+1], arr[i]
    arr[0] = val
    print arr
    return arr

push_to_front([1,2,3,4,5,6,7], 666)

