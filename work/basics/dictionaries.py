# Dictionaries
# Composite data type
# Shares a lot with lists :
# - Mutable
# - Dynamic (can grow and shrink as needed)
# - Nestable
# They differ mainly in the way they are accessed:
# - Lists can be accessed via index, while dictionaries can be accessed via keys
MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}
print(MLB_team)
print(type(MLB_team))
team = dict([
    ('team1', 'rocks'),
    ('team2', 'tuples'),
    ('team3', 'dicts')
])
print(team)
print(type(team))
team = dict(
    team1='rocks',
    team2='tuples',
    team3='dicts'
)
print(team)
print(type(team))

print(MLB_team['Minnesota'])
print(MLB_team['Boston'])
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)
del (MLB_team['Colorado'])
print(MLB_team)
numbers = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
}
print(numbers[1])  # This is not a numerical index, rather a key

# In fact, almost any type can be used as a key!

# There are however, restrictions:
# - a key must be unique in the dictionary
# - a key must be of an immutable type (a Tuple can be a key, but not a list nor another dictionary)

# Methods and functions
print(0 in numbers)
print(len(MLB_team))

numbers.clear()
print(len(numbers))

print(MLB_team.get('Milwaukee'))
print(MLB_team.get('Bruges', 'Defaults'))

print(MLB_team.items())

print(MLB_team.keys())
print(MLB_team.values())

print(MLB_team.pop('Minnesota'))

print(MLB_team.popitem())

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
print(d1)
print(d2)
d1.update(d2)
print(d1)
