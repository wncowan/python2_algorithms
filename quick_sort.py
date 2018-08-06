def quick_sort(_list):
    
    if len(_list) == 1:
        return _list
    elif _list == []:
        return []
    else:
        pivot = _list[0]
        left = []
        right = []

        for i in range(1, len(_list)):
            if _list[i] < pivot:
                left.append(_list[i])
            else:
                right.append(_list[i])
        pivot = [pivot]
        return quick_sort(left) + pivot + quick_sort(right)
    
print quick_sort([447, 8, 15, 71, 23, 21, 7, 99, 201])

#quick_sort([44, 8, 15, 71, 23, 21, 7, 99])
#pivot = 44
#left = [8, 15, 23, 21, 7]
#right = [71, 99]

#quick_sort([8, 15, 23, 21, 7]) + [44] + quick_sort([71, 99])

#quick_sort([8, 15, 23, 21, 7])
#pivot = 8
#left = [7]
#right = [15, 23, 21]

#quick_sort([7]) + [8] + quick_sort([15, 23, 21])

#quick_sort([7]) returns [7] because base case is satisfied

#quick_sort([7]) + [8] + quick_sort([15, 23, 21]) becomes
#[7] + [8] + quick_sort([15, 23, 21])

#quick_sort([15, 23, 21])
#pivot = 15
#left = []
#right = [23, 21]

#quick_sort([]) + [15] + quick_sort([23, 21])
#quick_sort([]) returns []
#[] + [15] + quick_sort([23, 21])

#quick_sort([23, 21])
#pivot = 23
#left = [21]
#right = []

#quick_sort([21]) + [23] + quick_sort([])
#[21] + [23] + []

#quick_sort([]) + [15] + quick_sort([23, 21]) becomes
#[15, 21, 23]

#so way back to the beginning 
#quick_sort([8, 15, 23, 21, 7]) + [44] + quick_sort([71, 99]) becomes
#[7, 8, 15, 21, 23] + [44] + quick_sort([71, 99])

# quick_sort([71, 99])
#pivot = 71
#left = []
#right = [99]

#quick_sort([]) + [71] + quick_sort([99]) becomes
#[71, 99]

#finally: [7, 8, 15, 21, 23, 44, 71, 99]












