import quicksort
import problem_quicksort as problem

import random
import timeit

# Test the speed

def test_sorting_functions():
    k = 100
    n = 500
    arr = [random.randint(1, 1000) for _ in range(k)]

    # test quickSort()
    quickSort_time = timeit.timeit(lambda: quicksort.quickSort(arr.copy()), number=n)
    quick_sorted = quicksort.quickSort(arr.copy())

    # test sorted()
    sorted_time = timeit.timeit(lambda: sorted(arr.copy()), number=n)
    python_sorted = sorted(arr.copy())

    print(f"quickSort() time for k={k}, n={n}: {quickSort_time:.6f}")
    print(f"sorted() time for k={k}, n={n}: {sorted_time:.6f}")
    assert quick_sorted == python_sorted

# Problem 1: Given an array of integers and a target value, write a function to determine if there exists a pair of elements in the array whose sum is equal to the target value.

def test_problemOne():
    assert problem.P1([1, 2, 3, 4, 5], 9) == True
    assert problem.P1([1, 2, 3, 4, 5], 10) == False
    assert problem.P1([], 0) == False
    assert problem.P1([1], 1) == False
    assert problem.P1([1, 2], 3) == True
    assert problem.P1([-5, -2, 0, 3, 7], 2) == True
    assert problem.P1([1, 2, 3, 4, 5, 5], 10) == True
    assert problem.P1([1, 2, -3, 4, -1], 0) == True
