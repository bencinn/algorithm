fn heapify(vector: &mut Vec<i32>, i: usize, n: usize) {
    let left = 2 * i;
    let right = 2 * i + 1;
    let mut largest = i;
    if left < n && vector[left] > vector[largest] {
        largest = left;
    }
    if right < n && vector[right] > vector[largest] {
        largest = right;
    }
    if largest != i {
        vector.swap(i, largest);
        heapify(vector, largest, n);
    }
}

fn heapsort(vector: &mut Vec<i32>) -> &mut Vec<i32> {
    let n = vector.len();
    for i in (0..=n / 2).rev() {
        heapify(vector, i, n);
    }
    for i in (1..n).rev() {
        vector.swap(0, i);
        heapify(vector, 0, i);
    }
    vector
}

#[cfg(test)]
mod heapsort {
    use crate::sorting::quicksort::quicksort;
    use rand::{thread_rng, Rng};
    use std::time::Instant;
    #[test]
    fn test_heapsort() {
        let mut rng = thread_rng();
        for _ in 0..100 {
            let mut unsorted = (0..100)
                .map(|_| rng.gen_range(0..100))
                .collect::<Vec<i32>>();
            let mut sorted = unsorted.clone();
            let rust_now = Instant::now();
            unsorted.sort();
            let rust_elapsed = rust_now.elapsed();
            let our_now = Instant::now();
            quicksort(&mut sorted);
            let our_elapsed = our_now.elapsed();
            assert_eq!(&sorted, &unsorted);
            println!(
                "heapsort: rust_elapsed: {:?}, our_elapsed: {:?}",
                rust_elapsed, our_elapsed,
            );
        }
    }
}
