# Control statements
password = input("Please enter password : ")
if password == "MI16":
    print("welcome Mr Bond")
else:
    print('Access denied!')

num = float(input("Enter a number"))

if num > 4:
    letter = 'A'
elif num > 3:
    letter = 'B'
elif num > 2:
    letter = 'C'
else:
    letter = 'D'

print('The letter is ', letter)

# Loops
# Definite
for var in range(4):
    print(var)

product = 1
for count in range(1, 5):
    product = product * count
    print(product)

for each in 'BERTRAND':
    print(each)

# Indefinite
checking_acc = 5678143
num = int(input('Enter the account number: '))
while num != checking_acc:
    print('Wrong number')
    num = int(input("Enter the account number: "))

# You can use while loops to make them Definite
sum = 0
for counter in range(1, 10):
    sum = sum + counter
    print(sum)
    print('\n')
sum = 0
counter = 1

while (counter < 10):
    sum = sum + counter
    print(sum)
    counter = counter + 1

# You can break out of loops
sum = 0
while True:
    data = int(input("Enter the data or press 0 to quit"))
    if data == 0:
        break
    sum = sum + data
print("Sum of all entered numbers is : ", sum)

# Also : break can be used in control flows
list = [1, 2, 3, 4]
search = 3
for each in list:
    if each == search:
        break
    print(each)

# Nested loops
list1 = ["London", "Paris", "New York", "Berlin"]
for each in list1:
    str1 = each
    for s in str1:
        if s == "o":
            break
        print(s)
    print("\n")

# Continue and Pass statements
# Continue : skip current iteration and start with the next one

search = 3
for each in list:
    if each == search:
        continue
    print(each)

# Pass : a continue statement to have empty bodies : do nothing, but you need something
def fun():
    pass

for each in 'Australia':
    pass
