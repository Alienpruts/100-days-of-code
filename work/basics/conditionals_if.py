# Conditional Statements

# If
# if <expr>:
#   <statement>
# else:
#   <statement>

x = 0
y = 5

if x < y:
    print('yes')

if y < x:
    print('yes')

if x:
    print('yes')

if y:
    print('yes')

if x or y:
    print('yes')

if x and y:
    print('yes')

if 'aul' in 'grault':
    print('yes')

if 'quux' in ['foo', 'bar', 'baz']:
    print('yes')

if 'foo' in ['foo', 'bar', 'baz']:
    print('Expression was true')
    print('We are now in suite')
    print('.....')
    print('Done')
print('After conditional')

if 'foo' in ['foo', 'bar', 'baz']:
    print('Outer condition is true')

    if 10 > 20:
        print('Inner condition 1')

    print('Between inner conditions')

    if 10 < 20:
        print('Inner condition 2')

    print('End of outer condition')
print('After outer condition')

x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

# Tip : length elif statement can mostly be rewritter with another data structure
names = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
    'Arnold': 'Hello Arnold'
}

print(names.get('Joe', "I don't know who you are!"))

print(names.get('Rick', "I don't know who you are!"))

# Ternary operators are also supported
# <expr1> if <conditional> else <expr2>
raining = False
print("Let's go the the", 'beach' if not raining else 'library')

age = 12
s = 'minor' if age < 21 else 'adult'
print(s)

a = 10
b = 20
m = a if a > b else b
print(m)

# Beware of precedence!
x = y = 40
z1 = 1 + x if x > y else y + 2
z2 = 1 + (x if x > y else y) + 2
print(z1)
print(z2)

# The Conditional in a ternary can also be nested, like a long elif statement block
x = 2
s = ('foo' if (x == 1) else
     'bar' if (x == 2) else
     'baz' if (x == 3) else
     'qux' if (x == 4) else
     'quux'
     )

print(s)

# Pass keyword
# Like a empty body statement {}, this allows you to pass the block of statements
if  True:
    pass

print('foo');
