# Basic data types is Python


# Integer
# In Python3, there is no limit to how long an integer can be, bar your system memory
print(123456789123456789123456789 + 1)
# A sequence of decimal digits is a decimal number
print(10)

# You can prepend strings to convert to other base numbers
# 0b / 0B : binary (base 2)
# 0o / 0O : Octal (base 8)
# 0x / 0X : Hexadecimal (base 16)
print(0b10)
print(0o10)
print(0x10)

# However, they are all derived from int class
print(type(0b10))
print(type(0o10))
print(type(0x10))


# Floating point numbers
# Values with a decimal point. You can use character 'e' or 'E' for scientific notation
# These values are represented as 64 double-precision, max value = 1.8 x 10^308
# Closest nonzero number can be to zero is 5.0 x 10^-324
# Remember : floating numbers do have precision problems!!!!
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(type(.4e7))
print(4.2e-4)

# complex numbers : <real part> + <imaginary part>j
print(2+3j)
print(type(2+3j))


# Strings
# As with integers, they can be as large as your system memory
print("I am a string")
print(type("I am a string"))
# Strings can have escaoe sequences
print('This string has a \' character')
print('a\
      b\
      c')
# Examples:
# \a : ASCII Bell character
# \b : ASCII Backspace character
# \f : ASCII Formfeed character
# \n : ASCII Linefeed character
# \N{name} : Character from Unicode with {name}
# \r : ASCII Carriage Return character
# \t : ASCII Horzontal Tab character
# \uxxxx : Unicode character with 16 bit hexa value
# \Uxxxxxx : Unicode character with 32 bit hexa value
# \v : ASCII Vertical Tab character
# \ooo : Character with octal value ooo
# \xhh : Character with hax value xx
print('foo\tbar')
print('a\141\x61')
print('a\nb')
print('\u2192 \N{rightwards arrow}')
# By preceding strings with character r or R, you indicate that escaoe sequences are to be displayes
print(r'foo\nbar')
print(R'foo\nbar')
# Triple quoted strings : so you do not have to escape all quotes. Also used for multilines
print('''This string has ' and " quotes''')
print('''Yesh, this is a 
        multiline string, 
        quite funny, I know''')


# Boolean
print(True)
print(False)
