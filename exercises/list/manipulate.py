'''
Listede ilk ve son elemanı sıfır yapan kodu yazınız
'''

# function
# list
# list indexing

data = ['paris', 'istanbul', 'Newyork', 'berlin']

data[0] = 0
data[-1] = 0

# --------------------------------------

'''
Listede ilk ve son elemanı sıfır yapan kodu yazınız
'''

# function
# list
# list indexing

data[0], data[-1] = 0, 0

# --------------------------------------

'''
Listedeki ilk ve son elemanın yerini değiştiren kodu yazınız
'''

# function
# list 
# list indexing

first = data[0]
last = data[-1]

data[0] = last
data[-1] = first

# --------------------------------------

'''
Listedeki ilk ve son elemanın yerini değiştiren kodu yazınız
'''

# function
# list
# list indexing

data[0], data[-1] = data[-1], data[0]

# --------------------------------------
'''
Listedeki ilk ve son elemanı silen kodu
'''
# function
# list
# list indexing
# del

del data[0]
del data[-1]

data

