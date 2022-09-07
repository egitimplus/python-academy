'''
Counting Item Occurrences 
'''

data = ['John','Kelly', 'Peter', 'Moses', 'peter']

# function
# dict
# list
# for loop
# str.lower()
# if conditions
# arithmetic operators

def count_items(data):
    new = {}
    for item in data:
        item_lower = item.lower()
        if item_lower in new:
            new[item_lower] = new[item_lower] + 1
        else:
            new[item_lower] = 1
    return new

print(count_items(data))
# Output : {'john': 1, 'kelly': 1, 'peter': 2, 'moses': 1}

# --------------------------------------

# function
# collections.defaultdict
# for
# artihmetic operators
# dict

from collections import defaultdict

def count_items(data):
    new = defaultdict(int)

    for item in data:
        new[item.lower()] += 1

    return dict(new)
    
print(count_items(data))
# Output : {'john': 1, 'kelly': 1, 'peter': 2, 'moses': 1}

# --------------------------------------
'''
The Counter() class will return a dictionary of how many times each item appears in an iterable. 
'''
# collections.Counter
# function

from collections import Counter

def count_item(value, data):
    count_value = Counter(data).get(value)
    return count_value

print(count_item('Peter', data))
# Output: 1

# --------------------------------------

# function
# for
# if conditions
# artihmetic operators
# dict

def count_item(value, data):
    count = 0
    for name in data:
        if name.lower() == value.lower():
            count +=1
    return count

print(count_item('Peter', data))
# Output: 2

# --------------------------------------
'''
Most Repeated Item
'''

# list
# dict
# for loop
# str.lower()
# arithmetic operators
# if conditions
# sorted
# lambda functions

data = ['new', 'bold', 'apple', 'yes', 'apple', 'bold', 'new', 'apple']

def most_repeat(data):
    new = {}
    for item in data:
        item_lower = item.lower()
        if item in new:
            new[item_lower] += 1
        else:
            new[item_lower] = 1

    return sorted(new, key=lambda x: x[1], reverse=True)[0]

print(most_repeat(data))
# Output: apple