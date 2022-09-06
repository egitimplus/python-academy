# Sum of numbers in the list

numbers = [1, '2', 5, '7', 11, 15]

# list
# function
# for loop
# int()
# arithmetic operators

def sum_numbers(data):
  sum = 0
  for number in data:
    sum += int(number)

  return sum

print(sum_numbers(numbers))

# --------------------------------------

# list
# function
# for loop
# int()
# sum()

def sum_numbers(data):
  new = []
  for number in data:
    new.append(int(number))

  return sum(new)

print(sum_numbers(numbers))

# --------------------------------------

# list comprehension
# int()
# sum()
def sum_numbers(data):
  result = sum([int(item) for item in data])
  return result
  
print(sum_numbers(numbers))

# --------------------------------------

# map()
# function
# lambda function
# sum()
# int()
def sum_numbers(data):
  result = sum(map(lambda x: int(x), data))
  return result
  
print(sum_numbers(numbers))

# --------------------------------------

# reduce()
# function
# lambda
# int()
# arithmetic operators

from functools import reduce

def sum_numbers(data):
  result = reduce(lambda x, y: int(x) + int(y), data)
  return result
  
print(sum_numbers(numbers))

# --------------------------------------
# if non-number characters

numbers = ['1', 2, '5', '7', '11', 15, 'bla']

# list
# function
# if condition
# for loop
# str()
# str.isdecimal()
# int()
# list.append()

def sum_numbers(data):
  new = []
  for number in data:
    if str(number).isdecimal():
      new.append(int(number))

  return sum(new)

print(sum_numbers(numbers))
