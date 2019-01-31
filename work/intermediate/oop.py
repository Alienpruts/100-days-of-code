# Object Oriented Programmming in Python.

# In Python, everything is already an Object

# Classes:

class Simplest():
    pass


print(type(Simplest))

simp = Simplest()
print(type(simp))
print(type(simp) == Simplest)


class Person():
    species = 'Human'


print(Person.species)

# You can dynamically add properties to a Class
Person.alive = True
print(Person.alive)

# You even inherit the dynamically created properties!
man = Person()
print(man.species)
print(man.alive)

Person.alive = False
print(man.alive)

man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)


# Attribute Shadowing
# This means that, if an attribute is not found, Python will go down the inheritance chain
# until it find is, or runs out of search domain
class Point():
    x = 10
    y = 7


p = Point()
print(p.x)
print(p.y)

# This will have no effect on the class itself
p.x = 12
print(p.x)
print(Point.x)

# We delete one attribute and then search for it, it will go to the class itself
del p.x
print(p.x)

p.z = 3
print(p.z)


# print(Point.z) # This will throw an AttributeError

# self
class Square():
    side = 8

    def area(self):
        return self.side ** 2


sq = Square()
print(sq.area())
print(Square.area(sq))


class Price():
    def final_price(self, vat, discount=0):
        """Returns Price after applying vat and fixed discount"""
        return (self.net_price * (100 + vat) / 100) - discount


p1 = Price()
p1.net_price = 100
print(Price.final_price(p1, 20, 10))
print(p1.final_price(20, 10))


# Initializing an instance (constructor)
# In Python this is called an initializer, since it works on already created instance
# Is a magic method, run right after object is created
class Rectangle():
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def area(self):
        return self.sideA * self.sideB


r1 = Rectangle(10, 4)
print(r1.sideA, r1.sideB)
print(r1.area())

r2 = Rectangle(7, 3)
print(r2.area())


# Inheritance and composition
# Inheritance : object Is A relation
# Composition : object Has A relation

class Engine():
    def start(self):
        pass

    def stop(self):
        pass


class ElectricEngine(Engine):  # Inherits
    pass


class V8Engine(Engine):  # Inherits
    pass


class Car():
    engine_cls = Engine  # property must be of class Engine

    def __init__(self):
        self.engine = self.engine_cls()  # Composed of an Engine. Here we create an instance, see the ()

    def start(self):
        print(
            'Starting engine {0} for car {1}.... Vroom!'.format(
                self.engine.__class__.__name__,
                self.__class__.__name__
            )
        )
        self.engine.start()

    def stop(self):
        self.engine.stop()


class RaceCar(Car):  # Inherits
    engine_cls = V8Engine  # Is composed of


class CityCar(Car):  # Inherits
    engine_cls = ElectricEngine  # Is composed of


class F1Car(RaceCar):  # Inherits from RaceCar AND Car
    engine_cls = V8Engine  # Is composed of


car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]

for automobile in cars:
    automobile.start()

cars2 = [(car, 'car'), (racecar, 'racecar'), (f1car, 'f1car')]
car_classes = [Car, RaceCar, F1Car]

for vehicle, car_name in cars2:
    for class_ in car_classes:
        belongs = isinstance(vehicle, class_)
        msg = 'is a' if belongs else 'is not a'
        print(car_name, msg, class_.__name__)


# Accesing a base class from within a class
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages


class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages)
        self.format_ = format_


# We can do even better, because now Book class is tied to Ebook class
# We can use super(), which is a proxy that delegates method calls to a parent class.
# Beauty is that we decouple Book from Ebook

class Ebook2(Book):
    def __init__(self, title, publisher, pages, format_):
        super().__init__(title, publisher, pages)
        self.format_ = format_


# Multiple Inheritance

class Shape:
    geometric_type = 'Generic Shape'

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:
    def plot(self, ratio, topleft):
        # Code logic
        print('Plotting at {}, ratio {} .'.format(topleft, ratio))


class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'


class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side


class RegularHexaGon(RegularPolygon):
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)


class Square(RegularPolygon):
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side


hexagon = RegularHexaGon(10)
print(hexagon.area())
print(hexagon.get_geometric_type())
hexagon.plot(0.8, (75, 77))

square = Square(12)
print(square.area())
print(square.get_geometric_type())
square.plot(0.93, (74, 75))

# The Method Resolution Order
# The order in which base classes are searched for a member during lookup of properties
# and methods. Simply put, it is an algorithm that drives the search.
# You can see what the mro is for any given class / object.
print(square.__class__.__mro__)
print(Square.__mro__)


# Demo of why this could be important
class A:
    label = 'a'


class B:
    # label = 'b' #commented to test what label will be returned
    pass


class C(A):
    label = 'c'


class D(B, C):
    pass


d = D()
print(d.label)
print(d.__class__.__mro__)


# Static methods

class String:
    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        # Only allow letter and numbers
        s = ''.join(c for c in s if c.isalnum())
        if case_insensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c - 1]:
                return False
            return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())


print(String.is_palindrome('Radar', case_insensitive=False))
print(String.is_palindrome('A nut for a jar of tuna'))
print(String.is_palindrome('Never Odd, Or Even'))
print(String.is_palindrome('In Girum Imus Nocte Et Consumimur Igni'))

print(String.get_unique_words('I love em, I really do'))


# Class Methods
# These take a special argument, the object itself. It then performs the method associated
# with it. The cls keyword refers to the class itself.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # These two class methods are factories : we want to be able to instantiate a
    # Point from coordinates, but also by passing a tuple or another Point instance
    @classmethod
    def from_tuple(cls, coords):
        return cls(*coords)

    @classmethod
    def from_point(cls, point):
        return cls(point.x, point.y)


p = Point.from_tuple((3, 7))
print(p.x, p.y)
q = Point.from_point(p)
print(q.x, q.y)


# Use cases : splitting static methods
# They are named with a _ to indicate these should not be called from outside of the class

class String2:

    @classmethod
    def is_palindrome(cls, s, case_insensitive=True):
        s = cls._strip_strings(s)
        if case_insensitive:
            s = s.lower()
        return cls._is_palindrome(s)

    @staticmethod
    def _strip_strings(s):
        return ''.join(c for c in s if c.isalnum())

    @staticmethod
    def _is_palindrome(s):
        for c in range(len(s) // 2):
            if s[c] != s[-c - 1]:
                return False
            return True


print(String2.is_palindrome('A nut for a jar of tuna'))
print(String2.is_palindrome('A nut for a jar of beans'))


# Private methods
# In Python, we do not have visibility modifiers, everything is supposedly public
# Therefore, we rely on Name Mangling
# _ means it is private
# Example of how this can turn out bad

class X:
    def __init__(self, factor):
        # self._factor = factor # Fix for overwriting factor
        self.__factor = factor

    def op1(self):
        # print('Op1 with factor {}...'.format(self._factor))
        print('Op1 with factor {}...'.format(self.__factor))


class Y(X):
    def op2(self, factor):
        # self._factor = factor # Fix for overwriting factor
        self.__factor = factor
        # print('Op2 with factor {}...'.format(self._factor))
        print('Op2 with factor {}...'.format(self.__factor))


obj = Y(100)
obj.op1()
obj.op2(42)
obj.op1()  # This is BAD !!!!! But is fixed with Name Mangling (__)

print(obj.__dict__.keys())


# Property decorator
# Yuo can use the name of a mthod as if it was a data attrubue (like age on Person)

class Person:
    def __init__(self, age):
        self.age = age  # this is free to modify!


class PersonWithAccessors:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')


class PersonPythonic:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')


person = PersonPythonic(39)
print(person.age) # Accessing as if a property, but actually calling @property def age
person.age = 42 # Setting not directly, but via @age.setter property decorator
print(person.age)
#person.age(200) # Will raise ValueError


# Operator Overloading
# To give an operator a meaning according to the context it is used.
# a + with numbers means addition, with strings it means concatenation

class Weird:
    def __init__(self, s):
        self._s = s

    def __len__(self):
        return len(self._s)

    def __bool__(self):
        return '42' in self._s

weird = Weird('Hello! I am 9 years old')
print(len(weird))
print(bool(weird))

weird2 = Weird('Hello! I am 42 years old')
print(len(weird2))
print(bool(weird2))

# Polymorfism
# Provisioning a single interface for entities of different types
# A car has engine.start(). We can call this regardless of what engine it is.
# In Python, there are no interfaces, nothing prevents yiu to call a method on an object




