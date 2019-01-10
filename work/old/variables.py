# Variable assignment
city = 'London'
money = 100.75
count = 4

a = b = c = 1

# Data Types
# Int + Long Int
print(123242354)
print(1437529862683132453262536536573658733583156 * 100000000000000000000000000000000000000000000000000000000000000000)

# Floats
print(5.46)
# Scientific notation
print(5.46e8)
print(5.46e-2)
# Complex numbers
print(complex(4, 9))
print(5 + 9j)
# Boolean
print(3 < 4)
print(3 > 4)
print(3 == 4)
# String
print('Hello World')


# Converting to ASCII
print(ord("A"))
print(chr(66))

# Arithmetic operators (in precedence order)
# ** : Exponent
# * : Multiplication
# / : Division
# % : Modulus Division
# + : Addition
# - : Substraction

# Mixed Mode Arithmetic (Only in Python2 ?
# Operations involving integer and floating point numbers will result in float type result
print(11 / 2)
print(11 / 2.0)

# Type conversion is handled by functions
print(int(4.77))
print(float(12))
print(str(900))

# Comparison operators (standard)
# Short circuit evaluation is used - if only one of the conditions evaluates to false, the
# others won't be evaluated!
print((10 < 11 <= 12) == (10 < 11) and (11 <= 12))
# Because 12 < 5 == false, the next comparison is not evaluated
print(12 < 5 < "John")
# This one will fail on the other hand
#print("John" > 5 > 12)

# Variants of assignment operators
# += : addition
# -= : subtraction
# *= : Multiplication
# /= : Division
# **= : Exponent

# Bitwise operators
# | Binary OR
# & Binary AND
# ~ Binary XOR
# ^ Binary complement operation
# << Left Shift operator
# >> Right Shift operator
x = 240
y = 1
print(x | y)
print(x & y)
print(x << 2)
print(x >> 2)
print(~x)

# Logical operators (standard and, or, not)

# Membership operators
# in : true if operand is found in sequence
# not in : true if operand is not found in sequence
str1 = 'John'
print('o' in str1)
print('k' in str1)
print('a' not in str1)

# Identity operators
# is : true if two vars point to the same object
# is not : true if two vars do not point to the same object
x = 10
y = 10
print(id(x))
print(id(y))
print(x is y)
x = [1, 2, 3]
y = [1, 2, 3]
print(id(x))
print(id(y))
print(x is y)
print(x == y)




