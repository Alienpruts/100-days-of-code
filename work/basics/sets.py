# Sets
# Data type
# - Unordered
# - Elements are unique
# - Mutable, but the elements themselves are not

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
print(x)
x = set(('foo', 'bar', 'baz', 'qux'))
print(x)
# Strings are iterable!
# Order is NOT preserved!
x = set('Bertrand')
print(x)
x = {'a', 'b', 'c', 'd'}
print(x)
# When using the {}, the elements themselves are preserved, even if Iterable
x = {'foo'}
y = set('foo')
print(x, y)
# Empty set is falsy
print(bool(set()))

# len returns the number of elements in a set
print(len(x))
print('f' in y)

# Operations on a set
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1 | x2)  # Both operands must be sets
print(x1.union(x2))  # Second operand can be any iterable

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

print(a.union(b, c, d))

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1.intersection(x2))
print(x1 & x2)

print(x1.difference(x2))
print(x1 - x2)

print(x1.symmetric_difference(x2))
print(x1 ^ x2)

print(x1.isdisjoint(x2))
print(x1.isdisjoint(x2 - {'baz'}))

x1 = {'foo', 'bar', 'baz'}
print(x1.issubset({'foo', 'bar', 'baz', 'qux', 'quux'}))
x2 = {'baz', 'qux', 'quux'}
print(x1 <= x2)

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1 |= x2
print(x1)
x1.update(['corge', 'garply'])
print(x1)

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1 &= x2
print(x1)
x1.intersection_update(['baz', 'qux'])
print(x1)

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1 -= x2
print(x1)
x1.difference_update(['foo', 'bar', 'qux'])
print(x1)

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1 ^= x2
print(x1)
x1.symmetric_difference_update(['qux', 'corge'])
print(x1)

x1 = {'foo', 'bar', 'baz'}
x1.add('qux')
print(x1)

x1.remove('qux')
print(x1)
x1.discard('test') # Difference with remove is that discard does not raise exception

x1.pop() # WATCH IT! This removes a RANDOM element from the list!!
print(x1)

x1.clear()
print(len(x1))

# A special type is frozenset : difference is that it is immutable
x = frozenset(['foo', 'bar', 'baz'])
print(x)

# Only methods that DONT modify the frozenset will work
print(x & {'baz', 'qux', 'quux'})


