'''
Kullanıcıya şifresine soralım. Şifresinde;
- 1 küçük harf 
- 1 büyük harf 
- 1 sayı olmalı
- boşluk olmamalı
- en az 8 karakter olmalı

Koşullara uygun şifre girilirse Başarıyla oluşturuldu diyelim.
Değilse hatayı yazdıralım ve tekrar soralım.
'''

# while loop
# boolean keywords
# input()
# len()
# print()
# str.isspace()
# if condition
# relational operators
# for loop
# str.islower()
# str.isdecimal()
# str.isupper()
# break

while True:
    password = input('Please enter your password: ')

    if len(password) < 8:
        print('Your password too short')
    else:
        decimal = lower = upper = False
        for char in password:
            if char.isspace():
                print('You cant use whitespace')
                break
            
            if char.isdecimal():
                decimal = True
            
            if char.islower():
                lower = True

            if char.isupper():
                upper = True

        if decimal and upper and lower:
            print('Your password is accepted')
            break
        else:
            print('You must use one lower, one upper and one digit.')

'''
Output:

Please enter your password: Emre Çevik
You cant use whitespace
You must use one lower, one upper and one digit.
Please enter your password: 1234!Python
Your password is accepted
'''