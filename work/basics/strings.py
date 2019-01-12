# Strings and Characters
# + :  String addition
s = 'foo'
t = 'bar'
u = 'baz'
print(s + t)
print(s + t + u)
# * : String multiplication with int operand
s = 'foo.'
print(s * 4)
print(4 * s)
# This is also possible (result : empty string)
print(s * -4)

# In operator : [searchterm] in string
print('foo' in 'That is food on the table!')
print('bar' not in 'That is food on the table!')

# String functions
# chr() : converts integer to character
# ord() : converts character to integer
# len() : resturns length of a string
# str() : returns a string respresentation of an object
print(ord('a'))
print(chr(1234))
print(len('hsjkhqkdhuibfkfbjklfbkjflk'))
print(str(3 + 29), type(str(49.2)))

# String indexing
# Strings can be represented like an array of characters
s = 'foobar'
print(s[0])
print(s[len(s) - 1])
# Also negative indexes means starting from reverse
print(s[-2])
print(s[-len(s)])
# Slicing is possible [start : stop : interval] (interval also named Stride in Python)
print(s[2:4])
print(s[:4])
print(s[3:])
print(s[:4] + s[4:])
print(s[-5:-2])
print(s[1:4])
print(s[-5:-2] == s[1:4])
print(s[0:6:2])
print(s[1:6:2])
s = '12345' * 5
print(s[::5])
print(s[4::5])
s = 'foobar'
print(s[5:0:-2])
# This is a common way of reversing a string
s = 'If Comrade Napoleon says it, it must be right'
print(s[::-1])

# Formatted String Literal
# Since Python 3.6, nicknamed f-string
# Extensive String formatting and operations : https://realpython.com/python-f-strings/
n = 25
m = 25
prod = n * m
print(f'The product of {n} and {m} is {prod}')

# Strings are immutable, as are the other literal data types! You cannot change them, only make copies and change those
s = 'foobar'
print(s.replace('b', 'x'))
print(s[:3] + 'b' + s[4:])

# String methods
# capitalize() : capitalize string
s = 'foO BaR BAZ quX'
print(s.capitalize())
# lower() : lowercase string
print(s.lower())
# swapcase() : swap case  of string
print(s.swapcase())
# title() : coverts string to title case (capitalize every word in string)
print(s.title())
# upper() : uppercase string
print(s.upper())
# count() : count occurences of [search] in string with [search], [start], [stop]
print(s.count('oO', 0, 10))
# endswith() : returns if string ends with [search], also with [start], [stop]
print('foobar'.endswith('bar', 0, 4))
# find() : search [search] in string, also with [start], [end], return first index of occurence of -1 if not found
print(s.find('oO'))
# index() : search [search] in string, also with [start], [end]
# indentical to find(), but this one raises Exception
print(s.index('oO'))
# rfind() : identical to find, but starting at the end
print('foo bar foo baz foo qux'.rfind('foo'))
# rindex() : identical to index, but starting at the end
print('foo bar foo baz foo qux'.rindex('foo'))
# startswitch() : returns if string ends with [search], also with [start], [end]
print('foobar'.startswith('foo'))
# isalnum() : returns if string consists of alphanumeric characters
print('foobar'.isalnum())
print('foobar&'.isalnum())
# isalpha() : returns if string consists of alphabetic characters
print('foobar'.isalpha())
print('foobar2'.isalpha())
# isdigit() : returns if string consists of digits
print('123'.isdigit())
print('123abc'.isdigit())
# islower() : returns if string is in lowercase
print('foobar'.islower())
print('fooBar'.islower())
# isprintable() : returns if string consists entirely of printable characters
print('a b c'.isprintable())
print('a\tb'.isprintable())
# isspace() : returns if string consists of whitespace characers
print(' \t \n'.isspace())
print(('   a   ').isspace())
# istitle() : returns if string is in Title case
print('This Is Good'.istitle())
print('This is Good'.istitle())
# center() : centers string in a [length] string, with [padding_character]
print('foobar'.center(20, '-'))

# The rest of them : https://realpython.com/python-strings/






