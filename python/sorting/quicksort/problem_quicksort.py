# Problem 1: Given an array of integers and a target value, write a function to determine if there exists a pair of elements in the array whose sum is equal to the target value. 

import quicksort

def P1(arr, target):
    if (len(arr) < 2):
        return False
    sortedArr = quicksort.quickSort(arr)
    print(sortedArr)
    pointerOne = 0
    pointerTwo = len(arr) - 1
    while (pointerOne < pointerTwo):
        if (sortedArr[pointerOne] + sortedArr[pointerTwo] == target):
            return True
        else:
            if (sortedArr[pointerOne] + sortedArr[pointerTwo] > target):
                pointerTwo-=1
            else:
                pointerOne+=1
            if pointerOne >= pointerTwo:
                return False
    return False
