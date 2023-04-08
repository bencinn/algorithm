pub fn selectionsort(mut array: Vec<i32>) -> Vec<i32> {
    for i in 0..array.len() {
        let mut minimum_index = i;
        for j in i + 1..array.len() {
            if array[j] < array[minimum_index] {
                minimum_index = j;
            }
        }
        array.swap(minimum_index, i)
    }
    array
}

#[cfg(test)]
mod selectionsort {
    use crate::sorting::selectionsort::selectionsort;
    use rand::{thread_rng, Rng};
    use std::time::Instant;
    #[test]
    fn test_selectionsort() {
        let mut rng = thread_rng();
        for _ in 0..100 {
            let mut unsorted = (0..10).map(|_| rng.gen_range(0..10)).collect::<Vec<i32>>();
            let mut sorted = unsorted.clone();
            let rust_now = Instant::now();
            unsorted.sort();
            let rust_elapsed = rust_now.elapsed();
            let our_now = Instant::now();
            sorted = selectionsort(sorted.clone());
            let our_elapsed = our_now.elapsed();
            assert_eq!(&sorted, &unsorted);
            println!(
                "quicksort: rust_elapsed: {:?}, our_elapsed: {:?}",
                rust_elapsed, our_elapsed,
            );
        }
    }
}
