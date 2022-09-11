'''
Bir listedeki mail adreslerinin doğru olup olmadığını kontrol eden ve doğru olanları
döndüren fonksiyonu yazalım.

Koşullar:

- içerisinde @ geçmeli ve başta/sonda olmamalı
- sadece bir tane @ olmalı
- içerisinde . olmalı ve en sonda olmamalı
'''

# list
# function
# for loop
# if condition
# str.count()
# str.startswith()
# str.endswith()
# str.split()
# list.append()
# boolean operators
# relational operators
# str indexing

def check_emails(emails):
    new = []
    for email in emails: 
        if email.count('@') == 1:
            if not email.startswith('@') and not email.endswith('@'):
                parts = email.split('@')
                if parts[1].count('.') > 0:
                    if not parts[1].startswith('.') and not parts[1].endswith('.'):
                        new.append(email)

        
    return new


data = [
    'adam.com',
    'adam@.adam.com',
    'adam@adam.com.',
    'adam@adam.com'
    ]

print(check_emails(data))
# Output: ['adam@adam.com']