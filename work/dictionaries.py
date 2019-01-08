# Dictionary : Sequence of key value pairs, seperated by comma's
port = {22: "ssh", 23: "Telnet", 53: "DNS", 80: "HTTP"}
print(port)

# Dictionary keys cannot be changed
# Keys must be unique
# Is an unordered collection

# Operations:
# Accessing a value : array notation
print(port[80])
# Updating a value
port[23] = "SMTP"
print(port)
port[23] = 'Telnet'
print(port)
# adding a new item to the dictionary
port[110] = "POP"
print(port)
# del : delete an item from the dictionary
del port[80]
print(port)
# you can delete an entire dictionary that way
# del port
# print(port)

# Dictionary functions
# len : returns number of items in dict
print(len(port))
# str : convert dict to a string
print(type(port))
print(type(str(port)))
# max : returns key with the highest worth
print(max(port))
# min : returns key with the lowest worth
print(min(port))
# dict : convert the list / tuple to a dict
port2 = [[80, "http"], [20, "ftp"], [23, "telnet"], [443, "https"], [53, "DNS"]]
print(type(port2))
port2 = dict(port2)
print(type(port2))
# in : check for existence of [search] among the KEYS of a dictionary
#key = int(input("Enter a key:"))
key = 23
if key in port:
    print("Yes")
else:
    print("No")

# Dictionary methods
# copy : create a copy of an existing dict
# with copy the result is a NEW dict, while copying with assignent (a = b) they will be the same
# this is important because a change in the original will NOT be reflected in the copy!
# Be careful about this !
avengers = {'iron-man': "Tony", "CA": "Steve", "BW": "Natasha"}
avengers2 = avengers.copy()
avengers3 = avengers
print(avengers2)
avengers["Spectacular-Bertrand"] = "Bertrand"
print(avengers)
print(avengers2)
print(avengers3)
# get : returns the VALUE of a given key. You can extend with a custom message
print(avengers.get("iron-man", 'not found'))
print(avengers.get("iron-girl", 'not found'))
# setdefault : the same is get, however, if not found it will add it with a default value
print(avengers.setdefault("iron-man", "not found"))
print(avengers.setdefault("iron-girl", "Not found"))
print(avengers)
# has_key : check if a KEY exists in dictionary, ONLY in Python2. Python3 prefers in operator
#print(avengers.has_key("iron-man"))
# keys : returns all KEYS of a dictionary
print(avengers.keys())
print(type(avengers.keys()))
# values : returns all VALUES of a dictionary
print(avengers.values())
print(type(avengers.values()))
# update : updates one dictionary with the contents of another dictionary
# be careful : if KEY exists in both dict, it will be overwritten
newavengers = {"Bearman": "Bert"}
avengers.update(newavengers)
print(avengers)
# items : return key-value pairs of the dictionary
print(avengers.items())
# clear : clear the contents of the dictionary
avengers.clear()
print(avengers)

# For loops with dictionaries
for each in port:
    print(each)

for key, value in port.items():
    print(key,' : ', value)

# In Python 2
# items method is memory intensive, espcially with large data sets
# for that, we can use iteritems
# In Python 3 items method is iterable, so iteritems is no longer needed
#for key, value in port.iteritems():
    #print(key," : ", value)


list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]

dict1 = {}

# TODO : exercises
