def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)  # Assume all numbers are prime initially
    prime[0] = prime[1] = False  # 0 and 1 are not prime

    p = 2  # Start with the smallest prime number

    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes = []
    for i in range(2, n + 1):
        if prime[i] == True:
            primes.append(i)

    return primes
        