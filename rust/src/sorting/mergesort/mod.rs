fn merge_vec(left: &mut Vec<i32>, right: &mut Vec<i32>) -> Vec<i32> {
    let mut result: Vec<i32> = Vec::new();
    while left.len() != 0 && right.len() != 0 {
        if left[0] <= right[0] {
            let drained: Vec<_> = left.drain(0..1).collect();
            result.extend(drained);
        } else {
            let drained: Vec<_> = right.drain(0..1).collect();
            result.extend(drained);
        }
    }
    if left.len() == 0 {
        result.append(right);
    } else {
        result.append(left);
    }
    result
}

pub fn mergesort(vector: &mut Vec<i32>) -> &mut Vec<i32> {
    if vector.len() == 1 {
        return vector;
    }
    let center = vector.len() / 2;
    let mut binding = vector.drain(0..center).collect();
    let left = mergesort(&mut binding);
    let right = mergesort(vector);
    let merged = merge_vec(left, right);
    vector.clear();
    vector.extend(merged);
    vector
}

#[cfg(test)]
mod mergesort {
    use crate::sorting::mergesort::mergesort;
    use rand::{thread_rng, Rng};
    use std::time::Instant;
    #[test]
    fn test_mergesort() {
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
            mergesort(&mut sorted);
            let our_elapsed = our_now.elapsed();
            assert_eq!(&sorted, &unsorted);
            println!(
                "mergesort: rust_elapsed: {:?}, our_elapsed: {:?}",
                rust_elapsed, our_elapsed,
            );
        }
    }
}
