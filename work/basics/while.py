# While loops (Indefinite Iteration)

# while <expe>:
#   <statements>

n = 5
while n > 0:
    n -= 1
    print(n)

n = 0
while n > 0:
    n -= 1
    print('This will never run')

a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))

# Break and Continue
# Break : terminate the loop immediately and continue to the next statement

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)

# Continue : termine the CURRENT loop iteration and continue to the top of the loop.

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)

# While loops have an optional ELSE clause
# This clause contains statements that will be run when the loop finishes.
# The clause will ONLY be reached when loop exits naturally, so no break statements!
# while <expr>:
#   <statements>
# else :
#   <statements>

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
else:
    print('Loop done!')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
else:
    print('Loop done!')

a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

i = 0
while i < len(a):
    if a[i] == s:
        # Processing for item found
        break
    i += 1
else:
    # Processing for item not found
    print(s, 'not found in list.')

# Infinite loops
# Loops that do not have their condition changed in the loop body - run forever.
# Can be useful to call a break instead of changing the loop condition

a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop(-1))

# This construct can be used for multiple break statements : instead of writing one long
# and complicated if condition, let the loop run and break at each specific condition
# while True:
#     if <expr1>:  # One condition for loop termination
#         break
#     ...
#     if <expr2>:  # Another termination condition
#         break
#     ...
#     if <expr3>:  # Yet another
#         break

# While loops can be nested
# Remember that break / continue statements apply to the NEAREST enclosing loop:

a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))

# One liners
# Statements on one liners are separated w-by a ;
# However, this is discouraged!
n = 5
while n > 0: n -= 1; print(n)

