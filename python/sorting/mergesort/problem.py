import mergesort

# Problem 1: Given an array of integers, find the nth smallest element in the array.

def P1(arr, n):
    return mergesort.mergeSort(arr)[n-1]

# Problem 2: Given an array of integers, return the array sorted in non-decreasing order.

def P2(arr):
    return mergesort.mergeSort(arr)

# Problem 3: Given two sorted arrays, merge them into a single sorted array.

def P3(arr1, arr2):
    return mergesort.mergeArray(arr1, arr2, [])

# Problem 4: Given an array of integers, find the number of inversions in the array. An inversion is a pair of indices (i, j) where i < j and arr[i] > arr[j].

def P4mergeArray(l, r, result):
    invCount = 0
    if len(l) == 0:
        return result + r, invCount
    elif len(r) == 0:
        return result + l, invCount
    if l[0] <= r[0]:
        result.append(l[0])
        l.pop(0)
    else:
        result.append(r[0])
        r.pop(0)
        invCount += len(l)
    merged, more_inv = P4mergeArray(l, r, result)
    invCount += more_inv
    return merged, invCount

def P4mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    leftSide = arr[:mid]
    rightSide = arr[mid:]
    leftSide, left_inv = P4mergeSort(leftSide)
    rightSide, right_inv = P4mergeSort(rightSide)
    merged, merge_inv = P4mergeArray(leftSide, rightSide, [])
    inv = left_inv + right_inv + merge_inv
    return merged, inv

def P4(arr):
    _, invcount = P4mergeSort(arr)
    return invcount
