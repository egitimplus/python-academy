'''
Listede ilk ve son elemanı sıfır yapan kodu yazınız
'''

# list

cities = ['paris', 'istanbul', 'Newyork', 'berlin']

cities[0] = 0
cities[-1] = 0

# cities[0], cities[-1] = 0, 0

# --------------------------------------

'''
Listedeki ilk ve son elemanın yerini değiştiren kodu yazınız
'''

# list

first = cities[0]
last = cities[-1]

cities[0] = last
cities[-1] = first

# cities[0], cities[-1] = cities[-1], cities[0]

# --------------------------------------
'''
Listedeki ilk ve son elemanı silen kodu
'''
# list
# del

del cities[0]
del cities[-1]

cities

# --------------------------------------
