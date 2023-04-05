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
