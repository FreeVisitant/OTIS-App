# Problem C.1: Learn to Code, Please, I Implore You

## Description

This program finds the number of ordered pairs of prime numbers \((p, q)\) such that when \(N = p^2 + q^3\) is written in decimal, each digit from 0 to 9 appears exactly once.

## Methods

1. **`sieve_of_eratosthenes(limit)`**: Uses the Sieve of Eratosthenes algorithm to generate prime numbers up to a given limit.

2. **`is_valid_number(n)`**: Checks if a number contains exactly 10 digits and if each digit from 0 to 9 appears exactly once.

3. **`count_valid_pairs()`**: Calculates \(N = p^2 + q^3\) for each pair of prime numbers \((p, q)\). If \(N\) is valid according to `is_valid_number(n)`, it counts as a valid pair.

4. **`is_prime(num)`**: Checks if the number is prime. This function is used to verify that the result is 10 times a prime number.

## How to Run

1. **Run the Program**:
   ```sh
   python mainprog.py
   ```

2. **Run Unit Tests**:
   ```sh
   python tests.py
   ```

## Notes

- The code has been tested to work with Python 2.7.16. 