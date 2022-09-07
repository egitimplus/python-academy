'''
Get unique values from a list
''' 

data = ['apple', 'apricot', 'blueberry', 'apple', 'Apple', 
        'apricot', 'blueberry', 'cherry', 'Banana', 'applE']

# list
# function
# for loop
# if conditions
# list.count()
# list.append()
# str.lower()

def unique_list(data):
    new = []
    for item in data:
        if not new.count(item.lower()):
            new.append(item.lower())

    return new

print(unique_list(data))
# Output : ['apple', 'apricot', 'blueberry', 'cherry', 'banana']

# list()
# set()
# function
# str.lower()
# set comprehension

def unique_list(data):
    return list(set(i.lower() for i in data))
    
print(unique_list(data))
# Output : ['apricot', 'blueberry', 'banana', 'apple', 'cherry']
