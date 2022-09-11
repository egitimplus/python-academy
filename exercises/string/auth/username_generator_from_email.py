'''
Kullanıcının kayıt formuna yazdığı email adresinden kullanıcı adı oluşturan bir 
fonksiyon yazacağız. @ işaretinden önceki kısmı kullanıcı adı olacak. 
'''

# function
# str.count()
# str.split()
# if condition
# relational operators
# str indexing

def create_user_from_email(email):

    if email.count(' ') > 0:
        return 'You dont use whitespaces'

    if email.count('@') > 1:
        return 'You must only one @'
    
    if email.count('@') == 0:
        return 'You must use one @'

    if email[-1] == '@' or email[0] == '@':
        return 'You must use @ in the middle'

    split_email = email.split('@')

    if split_email[1].count('.') == 0:
        return 'You must use . for domain'

    if split_email[1][-1] == '.' or split_email[1][0] == '.':
        return 'You must use . in the middle'

    return split_email[0]

print(create_user_from_email('emrecevik@sas.ss'))
# Output: emrecevik