# Operaters and Expressions

# Operators
# Arithmetic
# + / - (unary) : Unary positive / negative
# + + - (binary) : Addition - Subtraction
# * : Multiplication
# / : Division
# % : Modulo
# // : Floor division (Integer division)
# ** : Exponentiation
a = 4
b = 3
print(+a)
print(-b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

# Result of Division is always a float
print(type(a / b))

# Comparison
# == : Equal to
# != : Not Equal to
# < : Less than
# <= : Less than or Equal to
# > : Greater than
# >= : Greater than or Equal to
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

# Comparison on floating point numbers can be dodgy because of floating point precision
x = 1.1 + 2.2
print(x == 3.3)
# You can solve this problem by introducing a tolerance for comparison
tolerance = 0.00000001
print(abs(x - 3.3) < tolerance)

# Logical operators
# not : the opposite
# or : if one is true, the whole expression is true
# and : if all are true, the whole expression is true
x = 5
print(x < 10 or callable(x))
print(x < 0 or callable(x))
print(x < 10 and callable(x))
print(x < 100 and callable(len))
# Objects and expressions are not equal to True or False, but can be evaluated as such
# These values evaluate to Falsy
# - Boolean False
# - any numerical zero value
# - empty string
# - object of data type which is empty
# - special value None
# You can test for 'thruthiness' with bool() function
print(bool(0), bool(0.0), bool(0 + 0 + 0j))
print(bool(''), bool(""), bool(""""""))
print(bool([]))
print(bool(None))

x = 3
bool(x)
print(not x)

x = 0.0
bool(x)
print(not x)

x = 3
y = 4
print(x or y)

# This will result in 4.4, because x evaluates to False (0.0)
x = 0.0
y = 4.4
print(x or y)

x = 3
y = 4
print(x and y)

# This will result in 0.0, because 0.0 evaluates to false, so the whole expression evaluates to false
x = 0.0
y = 4.4
print(x and y)

# Compound Logical expressions and Short-Circuit Evaluation
# Short-circuit evaluation : if one of the conditions is false, the rest of the conditions are never checked
# or : true if one if the conditions is true, so if one is true, the rest is not evaluated
# and : true if all conditions is true, so if one is false, the rest is not evaluated
# This allows for some idiomatic patterns
a = 3
b = 1
print((b / a) > 0)
# However : a might be zero !!!!
# You can short-circuit on the first condition being that it should not be zero, and the faulty expression will not be executed!
a = 0
print(a != 0 and (b / a) > 0)

# Another idiom is the default value selection
# if string is empty, the default_value is selected
string = 'foo bar'
default_value = 'default value'
s = string or default_value
print(s)
string = ''
s = string or default_value
print(s)

z = 100
# Chained operators
# First expression : y will be evaluated one
# Second expression : y will be evaluated twice
print(x < y <= z)
print(x < y and y <= z)

# This might have big repercussions if used with functions (especially those that modify data)
# x < funct() <= z
# x < funct() and funct() <=z

# Bitwise operators
# Treat operands as sequences of binary digits and operate on them bit by bit
# & : bitwise AND (1 if all are 1, otherwise 0
# | : bitwise OR (1 if one is 1, otherwise 0)
# ~ : bitwise NEGATION (1 is 0, 0 is 1)
# ^ : bitwise XOR ( 1 if bits in the operand are different, 0 if they are the same)
# >> : bit shift right (each bit is shifted right n places)
# << : bit shift left (each bit is shifted left n places)
print('0b{:04b}'.format(0b1100 & 0b1010))
print('0b{:04b}'.format(0b1100 | 0b1010))
print('0b{:04b}'.format(0b1100 ^ 0b1010))
print('0b{:04b}'.format(0b1100 >> 2))
print('0b{:04b}'.format(0b0011 << 2))

# Identity operators
x = 1001
y = 1000 +1
print(x, y)
# Check on Equality
print(x == y)
# Check if same identity
print(x is y)
print(x is not y)
print(id(x))
print(id(y))

# Operator precedence
# From lowest to highest
# OR AND NOT (Comparison and identity) | ^ & (bit shifts) (+ -) (* / // %) (+x -x ~x) **
