# Variables
# Assignment via =
n = 300
print(n)
n = 500
print(n)
a = b = c = 100
print(a, b, c)
# You do not need to declare a variable type!
# Almost everything in Python is an object, so you create an object and assign a pointer to the var
print(type(n))
# Because of this, assignments are by reference, they point to the same object
m = n
print(id(n))
print(id(m))

