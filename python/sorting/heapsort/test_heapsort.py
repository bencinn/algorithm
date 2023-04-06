import heapsort

import random
import timeit

def test_sorting_functions():
    k = 10000
    n = 500
    arr = [random.randint(1, 1000) for _ in range(k)]

    # test quickSort()
    heapSort_time = timeit.timeit(lambda: heapsort.heapSort(arr.copy()), number=n)
    heap_sorted = heapsort.heapSort(arr.copy())

    # test sorted()
    sorted_time = timeit.timeit(lambda: sorted(arr.copy()), number=n)
    python_sorted = sorted(arr.copy())

    print(f"quickSort() time for k={k}, n={n}: {heapSort_time:.6f}")
    print(f"sorted() time for k={k}, n={n}: {sorted_time:.6f}")
    assert heap_sorted == python_sorted

