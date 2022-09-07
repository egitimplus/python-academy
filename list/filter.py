'''
Filter a list
'''

# Filter list by first characters

# function
# list
# for loop
# str.startswith()
# list.append()
# relational operators

data = ['apple', 'apricot', 'blueberry', 'apple', 'Apple', 
        'apricot', 'blueberry', 'cherry', 'Banana', 'applE']

def filter_list(char, data):
    new = []
    for item in data:
        #item.startswith(char)
        if item[0] == char:
                new.append(item)
    return new

print(filter_list('b', data))
# Output : ['blueberry', 'blueberry']

# --------------------------------------

# Filter list by first characters (case insensitive) and remove duplicate items.

# function
# list
# for loop
# str.startswith()
# list.append()
# str.lower()
# relational operators

def filter_list(char, data):
    new = []
    for item in data:
    
        item_lower = item.lower()
        #item.startswith(char)
        if item_lower[0] == char:
            if item_lower not in new:
                new.append(item_lower)
    return new
    
print(filter_list('b', data))
# Output: ['blueberry', 'banana']

# --------------------------------------

# Filter list by last characters (case insensitive) and remove duplicate items.

# function
# list
# for loop
# str.endswith()
# list.append()
# relational operators

def filter_list(char, data):
    new = []
    for item in data:
        item_lower = item.lower()
        #item.endswith(char)
        if item_lower[-1] == char:
            if item_lower not in new:
                new.append(item_lower)

    return new

print(filter_list('y', data))
# Output: ['blueberry', 'cherry']

# --------------------------------------

'''
Sequential Search
'''
# filter
# bool
# for loop
# relational operators
# function

def sequential_search(list_, n):
    found = False
    for i in list_:
        if i == n:
            found = True
            break
    return found

numbers = [1, 3, 5, 10, 20]
print(sequential_search(numbers, 3))
# True