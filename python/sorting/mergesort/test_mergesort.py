import mergesort
import problem_mergesort as problem

import random
import timeit

# Test the speed

def test_sorting_functions():
    k = 100
    n = 500
    arr = [random.randint(1, 1000) for _ in range(k)]

    # test quickSort()
    quickSort_time = timeit.timeit(lambda: mergesort.mergeSort(arr.copy()), number=n)
    quick_sorted = mergesort.mergeSort(arr.copy())

    # test sorted()
    sorted_time = timeit.timeit(lambda: sorted(arr.copy()), number=n)
    python_sorted = sorted(arr.copy())

    print(f"quickSort() time for k={k}, n={n}: {quickSort_time:.6f}")
    print(f"sorted() time for k={k}, n={n}: {sorted_time:.6f}")
    assert quick_sorted == python_sorted

# Problem 1: Given an array of integers, find the nth smallest element in the array.

def test_problemOne():
    assert problem.P1([3, 7, 1, 4, 8], 3) == 4
    assert problem.P1([3, 7, 1, 4, 8], 1) == 1
    assert problem.P1([3, 7, 1, 4, 8], 5) == 8
    assert problem.P1([3], 1) == 3
    assert problem.P1([1, 1, 1, 1, 1], 3) == 1

# Problem 2: Given an array of integers, return the array sorted in non-decreasing order.

def test_problemTwo():
    assert problem.P2([3, 7, 1, 4, 8]) == [1, 3, 4, 7, 8]
    assert problem.P2([3, 7, 1, 4, 8, 0]) == [0, 1, 3, 4, 7, 8]
    assert problem.P2([3]) == [3]
    assert problem.P2([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]

# Problem 3: Given two sorted arrays, merge them into a single sorted array.

def test_problemThree():
    assert problem.P3([1, 3, 5, 7], [2, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert problem.P3([1, 3, 5], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 8, 10]
    assert problem.P3([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert problem.P3([1, 1, 1], [1, 1, 1]) == [1, 1, 1, 1, 1, 1]
