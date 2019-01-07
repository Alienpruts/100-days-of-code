# Pyhton lists are mutable, as opposed to tuples
avengers = ['hulk', 'iron-man', 'Captain', 'Thor']

# Just like Tuples, a list can be unpacked
a, b, c, d = avengers
print(a)
print(b)
print(c)
print(d)

# List operations
# Accessing lists is like an array
print(avengers[1])
# Slicing is the same as with tuples
print(avengers[1:3])
print(avengers[:2])
print(avengers[:])
print(avengers[2:])
print(avengers[0:4:2])
# Updating a list = assigning new value to a list index
print(avengers[2])
avengers[2] = "Captain America"
print(avengers[2])
# Deleting from a list : del. You can also use splicing.
print(avengers[:])
del avengers[1]
print(avengers[:])
del avengers[0:2]
print(avengers[:])

# Addition of two lists : + operator. The original lists are preserved
avengers = ['hulk', 'iron-man', 'Captain', 'Thor']
avengers2 = ['Vision', 'sam']
print(avengers + avengers2)
# Multiplication of lists : * operator. The original lists are preseved
new_avengers2 = avengers2 * 2
print(new_avengers2)
print(id(new_avengers2[0]))
print(id(new_avengers2[2]))

# In operator to check if a value is between the list values
if 'iron-man' in avengers:
    print('yes')
if 'Vision' in avengers:
    print('yes')
else:
    print('no')

# List functions
# len : return the number of items in the list
print(len(avengers))
# max : return the item in the list with the highest value. The same extra rules apply
# here as well as with the tuples
list1 = [1, 2, 3, 4, 510]
print(max(list1))
# min : return the item in the list with the lowest value. See max
# list : convert a sequence to a list
tup1 = ('a', 'c', 'b')
list1 = list(tup1)
print(list1)
name = 'Bertrand'
print(list(name))
# sorted : return a new sorted list. Entering a Tuple to be sorted automatically converts it
# to a list
list1 = [1, 6, 3, -2, 13, 5]
print(sorted(list1))
print(sorted(tup1))
print(type(sorted(tup1)))

# List methods
avengers = []
# append : append an item to a list
avengers.append('Captain-America')
avengers.append('Iron-man')
print(avengers)
# extend : extend a list with another list. This is different than the + operator since the original lists
# are NOT preserved
avengers.extend(avengers2)
print(avengers)
list1.extend(name)
print(list1)
avengers.extend(tup1)
print(avengers)
# count : returns number of occurences of [search] in a list
name = list(name)
print(name.count('r'))
# index : find the index of [search] in a list. Only returns index of first occurrence
print(avengers.index('Iron-man'))
# insert : insert a new item at a specified index
avengers.insert(0, 'The-Incredible-Bertrand')
print(avengers)
# remove : removes an item from a list. Only remove the first occurrence
avengers.remove('The-Incredible-Bertrand')
print(avengers)
# pop : removes the last item from the list and returns that item. Also on index nr
print(avengers.pop())
print(avengers.pop())
print(avengers.pop())
print(avengers.pop(2))
print(avengers)
# sort : sort the values in a list
avengers.sort()
print(avengers)
avengers.sort(reverse=True)
print(avengers)
# complex example using key parameter of sort
list_of_tuples = [("a", 4), ("b", 1), ("v", 5), ("f", 2)]
print(list_of_tuples)


def fun1(x):
    return x[1]


list_of_tuples.sort(key=fun1)
print(list_of_tuples)
# example of sorting based on condition : the cmp argument (compare)
list1 = [10, 9, 3, 7, 2, 1, 23, 1, 561, 1, 1, 96, 1]
print(list1)


# comparison between two values. If return is negative : sorting is ascending, if positive, soring is descending
# we want to perform sorting, but have all the 1's on the right side of the variable
def cmp1(x, y):
    if x == 1 or y == 1:
        c = y - x
    else:
        c = x - y
    return c


# This will only work in Python2, cmp key has been removed in Python3
# https://docs.python.org/3/howto/sorting.html
# list1.sort(cmp=cmp1)
print(list1)
# reverse : reverses all items of a list
avengers.reverse()
print(avengers)

# List comprehensions
list1 = list(range(2, 7))
list2 = []
print(list1)
for each in list1:
    list2.append(each * each)

print(list2)
# By using comprehension we can shorten this to 1 line
print([each * each for each in list1])

list2 = []
for each in list1:
    if each % 2 == 0:
        list2.append(each * each)

print(list2)
# oneliner using comprehension
print([each * each for each in list1 if each % 2 == 0])

# Exercises
# get the [search] from the special list
list1 = ["abc", [2, 3, ("mohit", "the avengers")], 1, 2, 3]
search = "the avengers"
print(list1[1][2][1])

# with for loop, sort list based on sum of the values of the tuples
list2 = [(1, 5), (9, 0), (12, 3), (5, 4), (13, 6), (1, 1)]


def cmp2(x, y):
    return sum(x) - sum(y)


# This will only work in Python2, cmp key has been removed in Python3
# https://docs.python.org/3/howto/sorting.html
# list2.sort(cmp=cmp2)
# print(list2)

# return the indices of all the 1 elements
list3 = [1, 2, 4, 5, 1, 1, 4, 1, 56]
solution = []
for key, each in enumerate(list3):
    if each == 1:
        solution.append(key)

print(solution)

# with List comprehension
print([key for key, each in enumerate(list3) if each == 1])
