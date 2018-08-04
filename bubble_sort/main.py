def bubble_sort(arr):
    for i in range(len(arr) - 2, 0, -1):
        print i
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print arr


def bubble_sort_fast(arr):
    cmpcount, swapcount = 0, 0
    n = 0
    while n < len(arr) - 1:
        cmpcount += 1
        if arr[n] > arr[n + 1]:
            swapcount += 1
            arr[n], arr[n+1] = arr[n+1], arr[n]
            n = 0
        else:
            n = n + 1
    print arr, cmpcount, swapcount

bubble_sort_fast([111,33,5555,77,93,999])