'''
Bir kullanıcı formu olduğunu düşünelim kullanıcı şifresini girdiğinde (12345)
ona şifrenizi girdiniz 5 karakter ('*****') uzunluğunda diye ekrana yazdıralım
'''

# function
# input()
# f string
# len()
# arithmetic operators

def password_count():
    password = input('Please enter password: ')
    password_count = len(password)

    return password_count

pass_count = password_count()
print(f'Your password is {pass_count} ({pass_count * "*"}) characters long.')

'''
Output:

Please enter password: 123456
Your password is 6 (******) characters long.
'''