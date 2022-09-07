'''
Group Elements of Same Indices
'''

# function
# list
# arithmetic operators
# for loop
# len()
# range()
# list.append()

inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputLists = []
index = 0

for i in range(len(inputLists[0])):
    outputLists.append([])
    for j in range(len(inputLists)):
        outputLists[index].append(inputLists[j][ index])
    index = index + 1

print(outputLists)
# Output : [[10, 40, 70], [20, 50, 80], [30, 60, 90]]

# --------------------------------------
'''
Find Missing Number using Python
'''

# function
# list
# arithmetic operators
# for loop
# len()
# set()
# range()
# list.append()
# if condition
# membership operators

def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, length + 1):
        if i not in numbers:
            output.append(i)
    return output

listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9]
print(findMissingNumbers(listOfNumbers))



# --------------------------------------


'''
Index of the Maximum Value in a List
'''

# function
# list
# arithmetic operators
# while loop
# relational operators
# len()
# if condition

def maximum(x):
    maximum_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] > x[maximum_index]:
            maximum_index = current_index
        current_index = current_index + 1
    return maximum_index
a = [23, 76, 45, 20, 70, 65, 15, 54]
print(maximum(a))

# --------------------------------------

'''
Index of the Minimum Value in a List
'''

# function
# list
# arithmetic operators
# while loop
# relational operators
# len()
# if condition

def minimum(x):
    minimum_index = 0
    current_index = 1
    while current_index < len(x):
        if x[current_index] < x[minimum_index]:
            minimum_index = current_index
        current_index = current_index + 1
    return minimum_index
a = [23, 76, 45, 20, 70, 65, 15, 54]
print(minimum(a))

# --------------------------------------
'''
İki listede birbirinden benzersiz olanları listeyen fonksiyon [1,2,3] ve [1,2,4] -> [3]
'''

# list
# functions
# for loop
# list.append()
# if condition
# membership operators

list1 = [1, 2, 3]
list2 = [1, 2, 4]

def difference(data_1, data_2):
    diff = []
    for item in data_1:
        if item not in data_2:
            diff.append(item)

    return diff

print(difference(list1, list2))




# --------------------------------------
'''
İki listedeki benzersiz olanları listeleyen fonksiyon  [1,2,3] ve [1,2,4] -> [3, 4]
'''

# list
# functions
# for loop
# if condition
# list.append()
# membership operators

list1 = [1, 2, 3]
list2 = [1, 2, 4]

def symmetric_difference(data_1, data_2):
    diff = []
    for item in data_1:
        if item not in data_2:
            diff.append(item)

    for item in data_2:
        if item not in data_1:
            diff.append(item)

    return diff

print(symmetric_difference(list1, list2))




# --------------------------------------

'''
Listeyi tersine çeviren kodu yazınız

for ile de yapalım
'''

# function
# list
# list.reverse()
# list.copy()

data = ['paris', 'istanbul', 'Newyork', 'berlin']

def list_reverse(data):
    new = data.copy()
    new.reverse()

    return new

print(list_reverse(data))
# --------------------------------------

# function
# list
# list slicing

def list_reverse(data):
    return data[::-1]

print(list_reverse(data))



# --------------------------------------
'''
Bir fonksiyon yazalım ve bu fonksiyon parametre olarak girilen 
sayıların ortalamasını alsın
'''

# functions
# *args
# sum()
# len()
# arithmetic operators

def my_avg(*numbers):
    return sum(numbers) / len(numbers)

my_avg(3,5,7,10) 



# --------------------------------------
'''
İki listedeki aynı olan elemanları yazdıran fonksiyon
'''

# list
# functions
# for loop
# if condition
# list.append()
# membership operators

data1 = [1, 2, 5, 10]
data2 = [2, 4, 10, 20]

def same_items(data1, data2):
    new = []
    for item in data1:
        if item in data2:
            new.append(item)

    return new

same_items(data1, data2)

