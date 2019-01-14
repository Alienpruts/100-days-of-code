# Lists and Tuples

# Lists are a collection of arbitrary objects.
a = ['foo', 'bar', 'baz', 'qux']
print(a)

# They are Ordered : the order in which they enter the list is maintained
print([1, 2, 3, 4] == [4, 3, 2, 1])
# They can contain Arbitrary objects : there is no rule telling all elemnts should be of the same time
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(a)
import math


def foo():
    pass


a = [int, len, foo, math]
print(a)

# They can be accessed by Index : like arrays. Keep in mind that Slicing also works. (See Strings)
# However, slicing has one difference here : returns a new object that is a copy
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[0])
print(a[2])
print(a[:4:2])
print(a[:] is a) # You would think they are the same

# They can be Nested : a list can exist in a list
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x)
print(x[0])
print(x[1])
print(x[1][0])
print(x[1][1][0])

# They are Mutable : elements can be added, deleted, shifted and moved
print(a)
a[2] = 10
a[-1] = 20
del a[3]
print(a)
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)
b = ['grault', 'garply']
a += b
print(a)
# Remember that strings are iterables too !
a += 'string'
print(a)
a += ['string']
print(a)
a.append(123)
print(a)
a.extend([1, 2, 3])
print(a)
a.insert(3, 3.14159)
print(a)
a.remove('foo')
print(a)
x = a.pop(-3)
print(a)
print(x)

# They are Dynamic : they grow and shrink as needed
# See examples above, since they already illustrate that point

# Tuples
# Another type of ordered list.
# They are identical to lists, except for :
#   - Defined by parentheses, instread of square brackets
#   - They are immutable

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[3])
print(t[1::2])

# Every aspect of lists are also usable on Tuples
# WHy use them?
#   - Execution time is smaller
#   - Immutable state
#   - Can be used in Dictionaries (to be seen later)
a = 'foo'
b = 42
x = a, 3.14, b
print(x)
print(type(x))

# There is however one curiosity with Tuples
t = (1, 2, 3, 4, 5)
print(t, ' is a ', type(t))
t = (2)
print('but a single element ', print(t), 'becomes a ', type(t))
# That is because ..... it interprets it as an operator with precedence (), so it is one element of its type
# Should you really want to define a singleton tuple, use trailing comma
print((2,))
print(type((2,)))

# You can unpack tuples to variables
t = ('foo', 'bar', 'baz', 'qux')
print(t)
(s1, s2, s3, s4) = t
print(s1)
print(s2)
print(s3)
print(s4)

# One curiosity of this is that you can swap two vars without requiring a temp var, like in other languages
a = 'foo'
b = 'bar'
print(a, b)
a, b = b, a
print(a, b)
