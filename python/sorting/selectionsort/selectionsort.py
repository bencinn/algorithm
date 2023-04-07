def selectionSort(arr):
    for i in range(len(arr)):
        minimumIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minimumIndex]:
                minimumIndex = j
        arr[minimumIndex], arr[i] = arr[i], arr[minimumIndex]
    return arr
