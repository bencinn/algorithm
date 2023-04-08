import bubblesort

import random
import timeit

# Test the speed

def test_sorting_functions():
    k = 100
    n = 500
    arr = [random.randint(1, 1000) for _ in range(k)]

    # test insertionSort()
    insertionSort_time = timeit.timeit(lambda: bubblesort.bubbleSort(arr.copy()), number=n)
    insertion_sorted = bubblesort.bubbleSort(arr.copy())

    # test sorted()
    sorted_time = timeit.timeit(lambda: sorted(arr.copy()), number=n)
    python_sorted = sorted(arr.copy())

    print(f"insertionSort() time for k={k}, n={n}: {insertionSort_time:.6f}")
    print(f"sorted() time for k={k}, n={n}: {sorted_time:.6f}")
    assert insertion_sorted == python_sorted
