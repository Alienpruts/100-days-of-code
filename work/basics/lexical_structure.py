# Lexical structure of a Python program

# Statements are executed line per line until the end (or until a fatal error occurs)

# In other languages, you can split a long statement and the interpreter will not care
# However, in Python, a newline is considered an end of statement, so you have to split :
# - implicitely (preferred) : use () [] {} to surround your statements across lines
# - explicitely : use \ at the end of the broken statement part ( NO whitspace AFTER \)

x = (
        1 + 2
        + 3 + 4
        + 5 + 6
)
print(x)
print(
    'foo',
    'bar',
    'baz'
)
t = (
    'a', 'b',
    'c', 'd'
)

print(t)

d = {
    'a': 1,
    'b': 2
}
print(d)

x1 = {
    'foo',
    'bar',
    'baz'
}
print(x1)

a = [
    'foo', 'bar',
    'baz', 'qux'
]
print(a)
print(a[
          1
      ])
print(a[
      0:2
      ])
print(d[
          'b'
      ])

a = [
    [
        ['foo', 'bar'],
        [1, 2, 3]
    ],
    {1, 3, 5},
    {
        'a': 1,
        'b': 2
    }
]

print(a)

# Explicit

s = \
    'Hello World'
print(s)

x = 1 + 2 \
    + 3 + 4 \
    + 5 + 6
print(x)

# Multiple statements per line
# Can be done via ; . This is frowned upon however!
x = 1; y = 2; z = 3
print(x); print(y); print(z)

# Better version:
x, y, z = 1, 2, 3
print(x, y, z, sep='\n')

# Comments
# Can be placed at start of line for complete line comment
# Or after a statement for a partial comment
# As you can see, there is no multiline comment for Python.

# Indentation
# Leading whitespace is normally ignored in most languages
# Not in Python : indentation is used to group statements




