pub fn quicksort(array: &mut [i32]) -> &mut [i32] {
    if array.len() <= 1 {
        return array;
    }
    let pivot = array.len() - 1;
    let mut i = 0;
    for j in 0..pivot {
        if array[j] < array[pivot] {
            array.swap(i, j);
            i += 1;
        }
    }
    array.swap(pivot, i);
    let (left, right) = array.split_at_mut(i);
    let right = &mut right[1..];

    quicksort(left);
    quicksort(right);
    array
}

#[cfg(test)]
mod quicksort {
    use crate::sorting::quicksort::quicksort;
    use rand::{thread_rng, Rng};
    use std::time::Instant;
    #[test]
    fn test_quicksort() {
        let mut rng = thread_rng();
        for _ in 0..100 {
            let mut unsorted = (0..5000)
                .map(|_| rng.gen_range(0..5000))
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
                "quicksort: rust_elapsed: {:?}, our_elapsed: {:?}",
                rust_elapsed, our_elapsed,
            );
        }
    }
}
