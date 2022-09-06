'''
Sorting lists
'''

# sorting list ascending

# list.sort()

data = ['paris', 'istanbul', 'Newyork', 'berlin']

def sort_list(data):
    new = data.copy()
    new.sort()
    return new

print(sort_list(data))

# --------------------------------------

# sorting list ascending (fix uppercase char problem)

# list comprehension
# str.lower()
# list.sort()

def sort_list(data):
    new = [item.lower() for item in data]
    new.sort()
    return new
    
print(sort_list(data))

# --------------------------------------

# sorting list ascending with key parameter 

# list.sort()
# lambda functions
# str.lower() 

def sort_list(data):
    new = data.copy()
    new.sort(key=lambda x: x.lower())
    return new
    
print(sort_list(data))

# --------------------------------------

# sorting list descending

# list.sort()
# lambda functions
# str.lower()

def sort_list(data):
    new = data.copy()
    new.sort(key=lambda x: x.lower(), reverse=True)

    return new
    
print(sort_list(data))
# --------------------------------------

# sorting list with sorted method.

# list
# sorted()
# str.lower()
# lambda functions

def sort_list(data):
    new = sorted(data, key=lambda x: x.lower(), reverse=True)
    return new
    
print(sort_list(data))
# --------------------------------------

# sorting list by number of characters

# list.sort()
# len()

def sort_list(data):
    new = data.copy()
    new.sort(key=len)

    return new
    
print(sort_list(data))

# --------------------------------------

# list.sort()
# lambda functions
# len()

# sorting list by number of characters
def sort_list(data):
    new = data.copy()
    new.sort(key=lambda x: len(x))
    return new
    
print(sort_list(data))

# --------------------------------------

# sorting list by second word

# list
# list.sort()
# str.split()

data = [
    'Adam Smith',
    'Alex Mors',
    'Mina Moore',
    'Arya Stark',
    'Ban Ate'
]

def sort_list(data):
    new = data.copy()
    new.sort(key=lambda x: x.split()[1])
    return new
    
print(sort_list(data))

# --------------------------------------

# sorting list ascending but zeros at the end.

# list
# function
# for loop
# sorted()
# if conditions
# list.append()
# range()
# len()
# arithmetic operators

data = [24, 0, 35, 0, 41, 11, 8]

def sorted_list(data):
    new = []
    for item in sorted(data):
        if item != 0:
            new.append(item)

    zero_count = len(data) - len(new)
    if zero_count > 0:
        for i in range(zero_count):
            new.append(0)
    return new

print(sorted_list(data))