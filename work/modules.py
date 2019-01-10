# Modules and packages

# Modules : code files meant to be used by other programs
# Import with as : import module in SAME directory, as  = alias
# Import specific function :
# from module1 import sum1
import module1 as md

# dir : view contents of inmported package
print(dir(md))
x = 12
y = 34

print('The sum is : ', md.sum1(x, y))
print('The multiple is : ', md.mul1(x, y))
