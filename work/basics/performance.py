# How can we be more efficient with Collections in Python

# map(<func>, Iterable, ....)
# Map function : apply function to every element of the Iterable(s)
# Very useful, because the colletion and Iterable(s) do NOT need to be of same length
# Whichever runs out of elements first, the function just yields the results
test = map(lambda *a: a, range(3))
print(list(test))
print(list(map(lambda *a: a, range(3), 'abc')))
print(list(map(lambda *a: a, range(3), 'abc', range(4, 7))))
print(list(map(lambda *a: a, (), 'abc')))
print(list(map(lambda *a: a, (1, 2), 'abc')))
print(list(map(lambda *a: a, (1, 2, 3, 4), 'abc')))

# Use case : Schartzian Transform
# No longer used, but good trick in the early days of Python where sorting did not provide
# key functions.
# We want to sort in descending order by sum of credits accumulated by students
students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]


def decorate(student):
    # create a 2-tuple (sum of credits, student) from student dict
    # we 'decorate' the student with the sum data
    return sum(student['credits'].values()), student


def undecorate(decorated_student):
    # we remove the sum data from the decorated student
    return decorated_student[1]


students = sorted(map(decorate, students), reverse=True)
students = list(map(undecorate, students))

print(students)

# Zip function
# Similar to an array_merge in PHP (sort of).
# zip(*Iterables) returns an Iterator of Tuples, were the nth Tuple contains the nth
# element of each Iterable. If one of the Iterables runs out, the function ends
grades = [18, 23, 30, 27, 15, 9, 22]
avgs = [22, 21, 29, 24, 18, 18, 24]
print(list(zip(grades, avgs)))

# This is in fact the same as
print(list(map(lambda *a: a, grades, avgs)))

# Example : calculate the maximum value of each element of a group of lists
a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]

maxs = map(lambda n: max(*n), zip(a, b, c))
print(list(maxs))

# Filter function
# Works the same as an array_filter function in PHP
# filter(<function>, Iterable)
# Feed a function to every element of the Iterable, if it returns True, it gets in the filtered results

test = [2, 5, 8, 0, 0, 1, 0]
print(list(filter(None, test)))  # This will filter out the 0's, because their value is Falsy
print(list(filter(lambda x: x, test)))  # Since we return the value as is, same result as previous example
print(list(filter(lambda x: x > 4, test)))

# Comprehensions
# List function : a quick way of making a list
# Example : calculate a list with the square of the first 10 natural numbers
squares = []
for n in range(10):
    squares.append(n ** 2)

print(list(squares))

# Previous example works, but is a bit cluncky and not really the Python way

squares = map(lambda n: n ** 2, range(10))
print(list(squares))

# The oneliner above is the Python way of doing so. However the preferred way is
# by using comprehension
print([n ** 2 for n in range(10)])

# Another example : filter out the odd squares. We do it first with map and filter
sq1 = list(filter(lambda n: not n % 2, map(lambda n: n ** 2, range(10))))
print(sq1)

# Now with comprehension
sq2 = [n ** 2 for n in range(10) if not n % 2]
# Read it like this : give me all squares [n ** 2] for n between 0 and 9 if n is even
print(sq2)

# You can have nested comprehensions
items = 'ABCDE'
pairs = []
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))

print(pairs)

# But you could do this with a nested comprehension too
pairs: [(items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))]

print(pairs)

# Dict comprehensions
# You can use dictionaries in comprehensions
from string import ascii_lowercase

lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
print(lettermap)

lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
print(lettermap)

# Set comprehensions
word = 'Hello'
letters1 = set(c for c in word)
letters2 = {c for c in word}
print(letters1)
print(letters2)
print(letters2 == letters1)


# Generators
# Generator Functions : similar function as in PHP
# Generator Expressions : very similar to comprehensions, but return object instead of lists

# Generator Functions : like normal functions but instead of returning all results at once, you
# can yield one value, save their state, be paused, and when called upon again, they can resume their work
# Example :

def get_squares(n):
    return [x ** 2 for x in range(n)]


print(get_squares(10))


def get_squares_gen(n):
    for x in range(n):
        yield x ** 2  # YIELD the result, do not return it


print(list(get_squares_gen(10)))

# The result will be the samee, however, functione collects all results and returns the list, while the generator
# yields the results and waits for a next call. The print / list statements do that automatically

squares = get_squares_gen(10)
print(squares)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


# The next method is actually __next__() call, the Iterator magic method

# print(next(squares)) # This line will raise StopIteration exception - end of Iterator reached!

# This is for instanced how a for loop works :
# for x in range(y) = call next on Iterator range(y) until StopIteration is raised.

# The HUGE advantage of genearots is that they allow us to work with huge numbers where a normal function could not
# calculate them all and return, for instance factorial, where factorial of 10 would be do-able, but 20 would be impossibly
# huge. If you enter a stop condition (a return, or a break), you can prevent this and still get results

def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q ** k
        if result <= 100000000:  # this is the stop condition, prevents overflow
            yield result
        else:
            return
        k += 1


for n in geometric_progression(2, 5):
    print(n)

# Generators have , apart from next, the following methods
# - Send : communicate a value back to the Generator
# - throw : raise an exception within the Generator
# - close : close the Generator
# Send:

stop = False


def counter(start=0):
    n = start
    # while True: # normal Generator style
    while not stop:  # an extra check to be able to stop the Generator
        yield n
        n += 1


c = counter()
print(next(c))
print(next(c))
stop = True


# print(next(c))  # Because of stop = True, Iterator will raise StopIterator Exception

# HOWEVER : reliance on external variable is not good - use send

def counter_2(start=0):
    n = start
    while True:
        result = yield n
        print(type(result), result)
        if result == 'Q':
            break
        n += 1


c2 = counter_2()
print(next(c2))
print(c2.send('WOW'))
print(next(c2))


# print(c2.send('Q')) # This will halt the Generaotr, but also throw an Exception - commented out


# Yield from : yield from subiterator.
# Allows for advanced stuff
def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2


for n in print_squares(2, 5):
    print(n)


# That was normal generator function. Now with Yield From
def print_squares2(start, end):
    yield from (n ** 2 for n in range(start, end))


for n in print_squares2(2, 5):
    print(n)
