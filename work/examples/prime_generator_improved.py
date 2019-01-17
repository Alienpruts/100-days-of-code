primes = []
limit = 100
for n in range(2, limit + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else: # this block will only be reached when for loop is NOT interrupted by break
        primes.append(n)

print(primes)
