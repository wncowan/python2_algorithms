
def selection_sort(arr):
    for i in range(0, len(arr)):
        print "looping through this:", arr[i:]
        min_val = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
        print "min val from this loop", min_val
        swap_i = arr.index(min_val)
        print "swap_i", swap_i
        arr[i], arr[swap_i] = arr[swap_i], arr[i]
        print "array after swap", arr



selection_sort([6,2,9,1,7,3,5,4])