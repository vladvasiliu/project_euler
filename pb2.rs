// https://projecteuler.net/problem=2
//
// Even Fibonacci numbers
use std::mem::replace;

struct Fibonacci {
    curr: uint,
    next: uint,
}

impl Iterator<uint> for Fibonacci {
    fn next(&mut self) -> Option<uint> {
        let new_next = self.curr + self.next;
        let new_curr = replace(&mut self.next, new_next);
        Some(replace(&mut self.curr, new_curr))
    }
}

fn main() {
    let mut fib = Fibonacci {curr: 1, next: 2};
    let mut sum = 0;

    loop {
        let next = fib.next().unwrap();
        if next < 4_000_000 {
            if next % 2 == 0 {
                sum += next;
            }
        } else {
            break;
        }
    }

    println!("sum: {}", sum);
}
