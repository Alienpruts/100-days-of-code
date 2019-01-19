# Functions in Python
# def <functionname>:
#   <statements>

def matrix_mul(a, b):
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]


a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]

print(matrix_mul(a, b))


# Scope in function
# vars in function are in the local scope
# vars outside of functione are in the global scope
# vars in the local scope are NOT availabe in the local scope, but globals ARE available in the local scop
def my_function():
    test = 1
    print(test)


test = 0
my_function()
print(test)


# The scopes can be 'nested', following the same rules in each scope
def outer():
    test = 1  # Try commenting out this line to see that test would be global value 0

    def inner():
        test = 2  # Commenting this would see test = 1, because it would take the NEAREST global (which is test=1)
        print('inner: ', test)

    inner()
    print('outer: ', test)


test = 0
outer()
print('global: ', test)


# Local and nonlocal
# We can define vars in each namespace, but cannot actually modify them outside of the scope
# Nonlocal
def outer2():
    # nonlocal test # This would not work, nonlocal only works on enclosing scopes, not on global
    test = 1

    def inner2():
        # nonlocal test  # bind test to the nearest scope, so test = 1 in outer gets overwritten
        test = 2
        print('inner: ', test)

    inner2()
    print('outer: ', test)


test = 0
outer2()
print('global: ', test)


# Global

def outer3():
    test = 1

    def inner3():
        global test  # The same idea as nonlocal, but binds directly to the global scope, so test in global gets overwritten
        test = 2
        print('inner: ', test)

    inner3()
    print('outer: ', test)


test = 0
outer3()
print('global: ', test)


# Input parameters
# assigns an object to a local variable name
def func(y):
    # y is a local scope var that points to the SAME object as x outside the func
    print(id(y))
    print(y)


x = 3
print(id(x))
func(x)


# assignments to argument names do not affect the caller

def func2(x):
    x = 7  # define a local var, not changing the global one


func2(x)
print(x)

# changing a mutable DOES affect the caller
x = [1, 2, 3]
print(x)


def func3(x):
    x[1] = 4567  # this WILL affect the caller


func3(x)
print(x)


# keyword arguments
def keyword(a, b, c):
    print(a, b, c)


keyword(a=1, c=2, b=3)  # Here the order does not matter, they are matched by key


# default values
def default(a, b=4, c=88):
    print(a, b, c)


default(1)
default(b=5, a=7, c=9)
default(42, c=9)


# Variable positional arguments
# You can define a parameter is not beeing of a fixed number of arguments
def minimum(*n):
    print(n)  # n is a Tuple

    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)


minimum(1, 3, -7, 9)
minimum(33, 2456, -1, 5676567, 56)
minimum()


# Using * in a function calls means you unpack the values of the tuple, and are effectively
# calling the function with the elements themselves (so unpacking(a, b, c, d))
def unpacking(*args):
    print(args)


values = (1, 3, -7, 9)

unpacking(values)
unpacking(*values)


# Variable keyword arguments
# By adding ** in front of a dictionary as argument in function, the arguments is a dictionary wth keywords instread of a tuple
def dictionary(**kwargs):
    print(kwargs)


dictionary(a=1, b=42)
dictionary(**dict(a=1, b=42))
dictionary(**{'a': 1, 'b': 42})


# What is the value of being able to add variable amount of parameters?
# for example : a database connection function
def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }

    print(conn_params)


connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='test', pwd='gandalf')


# Keyword only arguments
# The keyword part MUST be called
# Not much used.
def kwo(*a, c):
    print(a, c)


kwo(1, 2, 3, c=7)
kwo(c=4)


# Watch out for mutable defaults!!!!
# every operation on the defaults will be kept on subsequent function calls!!!
def mutable(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))  # This will affect default value of a!
    b[len(a)] = len(a)  # This will affect default value of b!


mutable()
mutable()
# this in interesting : introduce one parameter that doesn't use a default
mutable(a=[1, 2, 3], b={'B': 1})
mutable()


# Return values
# In Python you can return almost anything you want.
# Since you can return a tuple, you are not restricted to 1 return value
# By default, a function returns None

def returns():
    pass


returns()  # The return value is not collected and is lost
a = returns()
print(a)


def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(2, n):
        result *= k
    return result


print(factorial(5))


# Multiple return values using tuples
def moddiv(a, b):
    return a // b, a % b


print(moddiv(20, 7))


# Final considerations on functions:
# - They should do one thing (Single Responsibility)
# - They should be small
# - They should not contain too many input parameters
# - They should be consistent in their return values
# - They shouldn't have side effects


# SPecial type : Recursive functions
def factorial_recursive(n):
    if n in (0, 1):
        return 1
    return factorial_recursive(n - 1) * n


print(factorial_recursive(5))


# Special type : Anonymous functions
# are called Lambda in Python

def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))


print(get_multiples_of_five(30))

adder_lambda = lambda a, b: a + b
print(adder_lambda('test', 'ing'))

to_upper_lambda = lambda s: s.upper()
print(to_upper_lambda('testing'))

# Importing objects (functions)
# You can import functions and modules using
# - import <module_name>
# - from <module_name> import <function_name>
