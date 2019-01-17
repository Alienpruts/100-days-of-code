primes = []
limit = 100

for n in range(2, limit + 1):
    is_prime = True
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break  # Breaks out of CURRENT loop, continues to the next statement
    if is_prime:  #
        primes.append(n)

print(primes)
