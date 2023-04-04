def mergeArray(left, right, result):
    if len(left) == 0:
        return result + right
    elif len(right) == 0:
        return result + left
    if left[0] <= right[0]:
        result.append(left[0])
        left.pop(0)
    elif left[0] > right[0]:
        result.append(right[0])
        right.pop(0)
    return mergeArray(left, right, result)

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return mergeArray(left, right, [])
