import unittest
from mainprog import main, sieve_of_eratosthenes, is_valid_number, count_valid_pairs, is_prime

class TestMainCode(unittest.TestCase):

    def test_prime_generation(self):
        primes = sieve_of_eratosthenes(30)
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(primes, expected_primes)

    def test_valid_number(self):
        valid_number = 1573049628
        invalid_number = 123456789
        self.assertTrue(is_valid_number(valid_number))
        self.assertFalse(is_valid_number(invalid_number))

    def test_count_valid_pairs(self):
        result, valid_pairs = count_valid_pairs()
        self.assertGreater(result, 0)
        self.assertTrue(result % 10 == 0 and is_prime(result // 10))

    def test_main_function(self):
        result, valid_pairs = main()
        self.assertGreater(result, 0)
        self.assertTrue(result % 10 == 0 and is_prime(result // 10))
        for p, q, N in valid_pairs:
            self.assertTrue(is_valid_number(N))

if __name__ == "__main__":
    unittest.main()
