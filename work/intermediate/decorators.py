# Decorators in Python

# Each time you repeat something, you should ask yourself if you can put it in a function

from time import sleep, time


def f():
    sleep(.3)


def g():
    sleep(.5)


t = time()
f()
print('f took: ', time() - t)

t = time()
g()
print('g took: ', time() - t)


# This is repetition! We can easily encapsulate the timing mechanism in a function to call

def f2():
    sleep(.3)


def g2():
    sleep(.5)


def measure(func):
    t = time()
    func()
    print(func.__name__, 'took : ', time() - t)


measure(f2)
measure(g2)


# What if we need to pass arguments to the function we measure?

def f3(sleep_time=0.1):
    sleep(sleep_time)


def measure2(func, *args, **kwargs):  # functionname, variable arguments, keyword variable arguments
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took :', time() - t)


measure2(f3, sleep_time=0.3)  # kwargs
measure2(f3, 0.2)  # args


# We can push this a bit further!
# We want the timing behavior built in to the f function
def f4(sleep_time=0.1):
    sleep(sleep_time)


def measure3(func):  # measure is the decorator
    def wrapper(*args, **kwargs):  # wrapper is the ... wrapper
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took :', time() - t)

    return wrapper


f = measure3(f4)  # We decorate the function with the wrapper. We are in effect calling the wrapper

f(0.2)
f(sleep_time=0.3)
print(f.__name__)


# The decorator pattern is so widely used in Python, it has its own syntax
# Prepend the decorator function with #<func_name>
def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper


@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


print(get_text("John"))

# So we rewrite the measurment of time using docorators
# we use wraps from functools module, because we want to retain all information about our original function.
# Since we wrapped it, we would lose that information
from functools import wraps


def measure4(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took : ', time() - t)

    return wrapper


@measure4
def f5(sleep_time=0.1):
    """I'm a cat. I love to sleep"""
    sleep(sleep_time)


f5 = measure4(f5(0.3))
print(f5.__name__, ':', f5.__doc__)


# Another example : decorator that prints error message if result of function is over treshold

def measure5(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took : ', time() - t)
        return result

    return wrapper


def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print('Result is too big ({0}). Max allowed is 100.'.format(result))
        return result

    return wrapper


@measure5
@max_result
def cube(n):
    return n ** 3


print(cube(2))
print(cube(5))


# A decorator factory
# Example : decorate the max_result so that we can do it with different tresholds, without
# writing a decorator for each treshold
def max_result2(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print('Result is too big ({0}). Max allowed is {1}.'.format(result, threshold))
            return result

        return wrapper

    return decorator


@max_result2(75)
def cube2(n):
    return n ** 3

print(cube2(5))

@max_result2(150)
def cube3(n):
    return n ** 3

print(cube3(3))

