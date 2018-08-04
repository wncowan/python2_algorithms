def insertion_sort(arr):
    print arr
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print arr

insertion_sort([6,2,9,0,4,3,7,1])

#start with first value. if one of the next values is less than first value, 
#then move the entire array in between it and first value forward one, 
# and insert the lesser value in front of the first value