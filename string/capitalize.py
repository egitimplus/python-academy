'''
Bir fonksiyon yazalım. BU fonksiyon içerisine gönderilen cümledeki her 
kelimenin ilk harfini büyük diğerlerini küçük yapsın
'''

# function
# str.capitalize()

def capitalize(text):
    return text.capitalize()

capitalize('this Text sHow')
# Output: 'This text show'

# --------------------------------------

# function
# arithmetic operators
# string indexing
# str.upper()
# str.lower()

def capitalize(text):
    return text[0].upper() + text[1:].lower()


print(capitalize('this Text sHow'))
# Output: 'This text show'