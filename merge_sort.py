def merge(list1, list2):
    print "merge called", list1, list2
    sorted_list = []
    reps = len(list1) + len(list2)
    for i in range(0, reps):
        if list1 == []:
            sorted_list.append(list2[0])
        elif list2 == []:
            sorted_list.append(list1[0])
        elif list1[0] < list2[0]:
            sorted_list.append(list1[0])
            list1.pop(0)
        else:
            sorted_list.append(list2[0])
            list2.pop(0)
    print "sorted_list", sorted_list
    return sorted_list

def merge_sort(_list):
    print _list
    if len(_list) < 2:
        print "got here"
        return _list
    else:
        return merge(merge_sort(_list[0:len(_list)/2]), merge_sort(_list[len(_list)/2:]))

print merge_sort([8, 23, 15, 89, 42, 16, 99, 27])

# [8,23] a sorted list is returned
# merge([8], [23])
# merge(merge_sort([8]), merge_sort([23])) ---when merge_sort input is 1 element, it returns that input. Other wise it will keep splitting the input.
# merge(merge_sort([8, 23]), merge_sort([15, 89]))
# merge(merge_sort([8, 23, 15, 89]), merge_sort([42, 16, 99, 27]))
# merge_sort([8, 23, 15, 89, 42, 16, 99, 27])

# [15,89] a sorted list is returned
# merge([15], [89])
# merge(merge_sort([15]), merge_sort([89])) ---when merge_sort input is 1 element, it returns that input. Other wise it will keep splitting the input.
# merge([8, 23], merge_sort([15, 89]))
# merge(merge_sort([8, 23, 15, 89]), merge_sort([42, 16, 99, 27]))
# merge_sort([8, 23, 15, 89, 42, 16, 99, 27])

# [8, 15, 23, 89] sorted lit returned
# merge([8, 23], [15, 89])
# merge(merge_sort([8, 23, 15, 89]), merge_sort([42, 16, 99, 27]))
# merge_sort([8, 23, 15, 89, 42, 16, 99, 27])

# [16,42] a sorted list is returned
# merge([42], [16])
# merge(merge_sort([42]), merge_sort([16])) ---when merge_sort input is 1 element, it returns that input. Other wise it will keep splitting the input.
# merge(merge_sort([42, 16]), merge_sort([99, 27]))
# merge([8, 15, 23, 89], merge_sort([42, 16, 99, 27]))
# merge_sort([8, 23, 15, 89, 42, 16, 99, 27])

# [27,99] a sorted list is returned
# merge([99], [27])
# merge(merge_sort([99]), merge_sort([27])) ---when merge_sort input is 1 element, it returns that input. Other wise it will keep splitting the input.
# merge([16, 42], merge_sort([99, 27]))
# merge([8, 15, 23, 89], merge_sort([42, 16, 99, 27]))
# merge_sort([8, 23, 15, 89, 42, 16, 99, 27])

# [16, 27, 42, 99] a sorted lit is return
# merge([16, 42], [27, 99])
# merge([8, 15, 23, 89], merge_sort([42, 16, 99, 27]))
# merge_sort([8, 23, 15, 89, 42, 16, 99, 27])

# [8, 15, 16, 23, 27, 42, 89, 99] sorted list is returned
# merge([8, 15, 23, 89], [16, 27, 42, 99])
# merge_sort([8, 23, 15, 89, 42, 16, 99, 27])