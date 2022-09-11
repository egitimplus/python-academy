'''
Bir fonksiyon yazalım. BU fonksiyon içerisine gönderilen cümledeki büyük 
harfleri küçük, küçük harfleri büyük yapsın
'''

# functions
# for loop
# if conditions
# str.islower()
# str.upper()
# str.lower()
# arithmetic operators

def swapcase(text):
    new_text = ''
    for letter in text:
        if letter.islower():
            new_text += letter.upper()
        else:
            new_text += letter.lower()

    return new_text

print(swapcase('HeLLoWorLD!!-+'))
# Output: hEllOwORld!!-+

# --------------------------------------

# functions
# text.swapcase()

def swapcase(text):
    return text.swapcase()

print(swapcase('HeLLoWorLD!!-+'))
# Output: hEllOwORld!!-+