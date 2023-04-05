def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = len(array) - 1
    i = 0
    for j in range(pivot):
        if array[j] < array[pivot]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[pivot], array[i] = array[i], array[pivot]
    left = quickSort(array[:i])
    right = quickSort(array[i+1:])
    return left + [array[i]] + right

