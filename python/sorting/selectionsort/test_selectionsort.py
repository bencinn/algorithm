import selectionsort

import random
import timeit

def test_sorting_functions():
    k = 100
    n = 500
    arr = [random.randint(1, 1000) for _ in range(k)]

    # test selectionSort()
    selectionSort_time = timeit.timeit(lambda: selectionsort.selectionSort(arr.copy()), number=n)
    selection_sorted = selectionsort.selectionSort(arr.copy())

    # test sorted()
    sorted_time = timeit.timeit(lambda: sorted(arr.copy()), number=n)
    python_sorted = sorted(arr.copy())

    print(f"selectionSort() time for k={k}, n={n}: {selectionSort_time:.6f}")
    print(f"sorted() time for k={k}, n={n}: {sorted_time:.6f}")
    assert selection_sorted == python_sorted

