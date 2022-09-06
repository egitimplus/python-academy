'''
Get unique values from a list
''' 

# list
# functions
# for loop
# if conditions
# list.count()
# list.append()

def unique_list(data):
    new = []
    for item in data:
        if not new.count(item):
            new.append(item)

    return new

print(unique_list(data))

# list()
# set()

unique_list = list(set(data))
print(unique_list)