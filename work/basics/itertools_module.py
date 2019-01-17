# Small introduction to Itertools module
# Gives access to three broad categories of iterators

# Infinite iterators
from itertools import count

for n in count(5, 5):
    if n > 20:
        break
    print(n, end=', ')

# Iterators terminating on the shortest input sequence
# Using compress you would get
# compress('ABC', (1, 0, 1) would result in 'AC', because they correspond to the 1's
# Think of it like a sieve of an array.
from itertools import compress

data = range(20)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))
print('\n')
print(odd_selector)
print(even_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)

# Combinatoric generators
# For example : permutations
from itertools import permutations
print(list(permutations('ABC')))
