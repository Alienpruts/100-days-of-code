# Functions and scopes

def helloWorld():
    print("You are in Hello World function")


helloWorld()


# Arguments can be passed, if none are given, TypeError
def func(passArgument):
    print("Argument was :", passArgument)


str = "Hello all"
func(str)


# Return types
def sum(a, b):
    return a + b


print("Result of sum of 10 and 5 is : ", sum(10, 5))


# Default arguments

def info(name, age=50):
    print("Name : ", name)
    print("Age : ", age)


info('Bert', 37)
info('John')


# Variable length arguments.
# Gives ability to pass in any number of arguments, if needed
def variable_argument(var1, *vari):
    print("Output is : ", var1)
    for var in vari:
        print(var)


variable_argument(60)
variable_argument(100, 99, 98, 97)


# Key value pair as variable length argument
def infocity(**var):
    print(var)
    for key, value in var.items():
        print("%s == %s" % (key, value))


infocity(name="l4w", age=20, city="Los Angeles")
infocity(name="John", age=45, city="London", sex="male", medals=0)


# Pass by reference - Pass by Value
# By reference : mem addres is passed and operation is performed on data at that address
# By value : operation is done on passed value and THEN stored at mem address
# default : BY REFERENCE
def pass_red(list1):
    list1.extend([23, 89])
    print('List inside function : ', list1)


list = [12, 67, 90]
print('List before function : ', list)
pass_red(list)
print("List after function : ", list)

def pass_value(list):
    list.extend([1000000000])
    print("List inside function : ", list)

print('List before function : ', list)
pass_value(list)
print('List after function : ', list)
