def bubbleSort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        unsortedlen = len(array) - i
        for j in range(0, unsortedlen):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
