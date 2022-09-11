'''
Username Generator

Kullanıcının kayıt formuna yazadığı isim ve soyisimden kullanıcı adı 
oluşturan bir fonksiyon yazacağız.

Eğer o kullanıcı adı varsa sonuna 1 ekleyeceğiz. Eğer sonunda kullandığımız
sayıda varsa 2, 3 diye olmayana kadar ilerleyeceğiz.

Boş karakterler silinecektir.
'''

user_data = [
    'adamsmith',
    'johnwick'
]

# list
# function
# input()
# while loop
# str.replace()
# str.lower()
# if condition
# boolean keywords
# relational operators
# boolean operators
# membership operators
# list.append()
# str()
# arithmetic operators

def user_info(data):
    name = input('Please enter name: ')
    surname = input('Please enter surname: ')

    username = name.replace(' ', '').lower() + surname.replace(' ', '').lower()
    
    i = 0
    while True:        
        username = username if i == 0 else username + str(i)
        
        if username not in data:    
            data.append(username)
            return username
        i = i + 1

    return username

print(user_info(user_data))

'''
Output:

Please enter name: Adam
Please enter surname: Smith
adamsmith1

'''
