def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p] == True:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit + 1) if is_prime[p]]
    return prime_numbers

def is_valid_number(n):
    digits = str(n)
    return len(digits) == 10 and set(digits) == set("0123456789")

def count_valid_pairs():
    limit = 100000 
    primes = sieve_of_eratosthenes(limit)
    count = 0
    valid_pairs = []

    for p in primes:
        p_squared = p * p
        for q in primes:
            q_cubed = q * q * q
            N = p_squared + q_cubed
            if is_valid_number(N):
                count += 1
                valid_pairs.append((p, q, N))
                print("Valid pair found: (p, q) = (%d, %d), N = %d" % (p, q, N))
    
    return count, valid_pairs

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    result, valid_pairs = count_valid_pairs()
    print("Total number of valid pairs: %d" % result)
    
    if result % 10 == 0 and is_prime(result // 10):
        print("The result is 10 times a prime number.")
    else:
        print("The result does not meet the expected criteria.")

    return result, valid_pairs

if __name__ == "__main__":
    main()
