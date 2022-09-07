'''
Group Elements of Same Indices
'''

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





# --------------------------------------





# --------------------------------------
