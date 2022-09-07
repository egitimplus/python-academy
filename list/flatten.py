'''
Flatten a nested list
'''

# list
# function
# for loop
# list.append()

data = [[1,2,5,4],[3,2,5,4],[4,5]]

def list_flatten(data):
    new = []
    for item in data:
        for i in item:
            new.append(i)

    return new

print(list_flatten(data))
# Output : [1, 2, 5, 4, 3, 2, 5, 4, 4, 5]

# --------------------------------------

# list
# function
# itertools module

import itertools

def list_flatten(data):
    flat_list = list(itertools.chain.from_iterable(data))
    return flat_list
    
print(list_flatten(data))
# Output : [1, 2, 5, 4, 3, 2, 5, 4, 4, 5]

# --------------------------------------

# list comprehension
# function

def list_flatten(data):
    flat_list= [i for j in data for i in j]
    return flat_list
    
print(list_flatten(data))
# Output : [1, 2, 5, 4, 3, 2, 5, 4, 4, 5]

# --------------------------------------

# flatten multi-nested data

# list
# function
# if conditions
# recursive functions
# arithmetic operators

data = [[[1,2]], [3,4], [5, [6, 7]]]

def list_flatten_recursive(data):
    
    if data == []:
        return data
    
    if type(data[0]) == list:
        return list_flatten_recursive(data[0]) + list_flatten_recursive(data[1:])

    return data[:1] + list_flatten_recursive(data[1:])

print(list_flatten_recursive(data))
# Output : [1, 2, 3, 4, 5, 6, 7]