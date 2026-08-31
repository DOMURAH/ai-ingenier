def quick_short(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[(len(array) - 1) // 2]
        less = [i for i in array[1:] if i < pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quick_short(less) + [pivot] + quick_short(greater)
    
tableau = [45,12,56,98,1]
print(quick_short(tableau))