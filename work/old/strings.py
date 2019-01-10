import ctypes

# Strings are immutable in memory. Reassignment of variable puts in other memory location
name = 'Bert'
print(id(name))
name = 'Bertrand'
print(id(name))

# Getting memory values at specific location
print(ctypes.cast(id(name), ctypes.py_object).value)

# Length of a string
print(len(name))

# Accessing string at location
# -1 = last character
# -len = first character (counting in reverse)
print(name[3])
print(name[-1])
print(name[-len(name)])

# String Slicing
print(name[0:3])
print(name[:3])
print(name[4:])
print(name[4:len(name)])
print(name[::2])
print(name[::-1])

# String methods
# count : count occurences of [search] in [sub]-string
print(name.count('e'))
print(name.count('r'))
print(name.count('r', 4, len(name)))
# find : find first index of [search] in [sub]-string
print(name.find("trand"))
print(name.find("e"))
# lower : put string in lowercase. Original str is preserved, unless overwritten
print(name.lower())
print(name)
# upper : put string in uppercase. Original str is preserved, unless overwritten
print(name.upper())
print(name)
# swapcase : swap cases of str. Original str is preserved, unless overwritten
print(name.swapcase())
print(name)
# capitalize : Capitalize string. Origin str is preserved, unless overwritten
print(name.lower().capitalize())
print(name)
# title : Capitalize strings consisting of multiple words. Orginal str is preserved, unless overwritten
multiple = "This is not true, your honor!"
print(multiple.title())
print(multiple)
# rstrip : remove unwanted characters from the right side of the string. Space is default character
print(name.rstrip('nd'))
# lstrip : remove unwanted characters from the left side of the string. Space is default character
print(name.lstrip('Be'))
# split : split a string in multiple parts. Supply character to split on (space by default), and number of occurences
test = "27-12-2016"
print(test.split("-"))
print(test.split("-", 1))
print(test.rsplit("-", 1))
# ljust : justify text from the left side. Provide length and a padding character (space by default)
print(name.ljust(30, "#"))
# rjust : justify text from the right side. Provide length and a padding character (space by default)
print(name.rjust(30, '#'))
# center : justify text from the center of the text. Provide length and a padding character (space by default)
print(name.center(30, '#'))
# zfill : justify text with zeroes (good for binary numbers or bank accounts). Shorthand for rjust() with 0 as padding
print(name.zfill(30))
# replace : replace [search] with [replace], [number_of_times]
print(name.replace("trand", "trando", 1))
# join : join elements of a tuple (array) in a string. Format : [separator].join([list])
test = ['Bert', 'rand']
print("".join(test))
print(" | ".join(test))
# endswith : returns if a string ends with [search]. Also [begin, end] is possible at the end
print(name.endswith("rand"))
print(name.endswith('rond'))
print(name.endswith('rand', 0,4))
# startswith : see above, but searching from the start of the string
print(name.startswith('Bert'))
print(name.startswith('Burt'))
print(name.startswith('Bert', 5, len(name)))
# isalpha : returns if string only contains letter. NOT EVEN SPACES are allowed.
print(name.isalpha())
# isdigit : returns if string only contains numbers.
print(name.isdigit())
# isspace : returns if string only contains spaces
print(name.isspace())
# istitle : returns if string is in Title case
print(name.istitle())
# islower : returns if string is in Lower case
print(name.islower())
# isUpper : returns if string is in Upper case
print(name.isupper())

# String functions
# min : find the ASCII character with the lowest index nr
print(min(name))
# max : find the ASCII character with the highest index
print(max(name))
# str : convert a type to STRING datatype
test = 123
print(type(test))
test = str(test)
print(type(test))
test = [1, 2]
print(type(test))
test = str(test)
print(type(test))
# in operator can be used to search for [search] in string, coupled with an if statement
if "tra" in name:
    print("Yes")

# Tuples : sequences of heterogeneous data types sort of an array
tup1 = (1, 2, 3, 4.6, "Hello", "a")
print(tup1)
tup2 = 1, 2, 3
print(tup2)
print(type(tup2))
# Like arrays, getting data from a particular index requires [x] notation. Negative values indicate reverse order
print(tup1[2])
print(tup1[-1])
# You can also use range notation [start:end] - NON INCLUSIVE
print(tup1[1:3])
print(tup1[:3])
print(tup1[1:])

# unpacking of tuples
a, b, c = tup2
print(a)
print(b)
print(c)

# len : return total number of items in the tuple
print(len(tup1))
# max : return highest integer item of the tuple. Only works on integer and / or float based tuples in Python3
print(max(tup2))
# If strings are compared, only the first character is taken into account. Tiebreaker : next character, and so on
tuple3 = ['ash', 'beta', 'zeta']
print(max(tuple3))
# min : return lowest integer item of the tuple. See max
# tuple : convert to tuple data type
print(tuple(name))
# del : delete tuple
del tup1
# print(tup1)

# + : addition of tuples
tup1 = (1, 2, 3)
tup2 = ('four', 'five', 'six')
print(tup1 + tup2)
# * : multiplication of tuples
print(tup2 * 2)
print(tup1 * 2)

# Exercises
# Get domain from URL
position = 2
wwwposition = 0
url = 'http://www.thapar.edu/index.php/about-us/mission'

list = url.split('/')
domain = list[position].split('.')
del domain[wwwposition]
print('Domain is: \n')
print('.'.join(domain))

# Create URL from tuple
parts = ('www', 'thapar', 'edu', 'index', 'php', 'about-us', 'mission')
print('Constructed URL is : \n')
print(parts[0] + '.' + parts[1] + '.' + parts[2] + '/' + parts[3] + '.' + parts[4] + '/' + parts[5] + '/' + parts[6])
