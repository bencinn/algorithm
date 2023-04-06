import insertionsort

import random
import timeit

# Test the speed

def test_sorting_functions():
    k = 100
    n = 500
    arr = [random.randint(1, 1000) for _ in range(k)]

    # test quickSort()
    quickSort_time = timeit.timeit(lambda: insertionsort.insertionSort(arr.copy()), number=n)
    quick_sorted = insertionsort.insertionSort(arr.copy())

    # test sorted()
    sorted_time = timeit.timeit(lambda: sorted(arr.copy()), number=n)
    python_sorted = sorted(arr.copy())

    print(f"quickSort() time for k={k}, n={n}: {quickSort_time:.6f}")
    print(f"sorted() time for k={k}, n={n}: {sorted_time:.6f}")
    assert quick_sorted == python_sorted
