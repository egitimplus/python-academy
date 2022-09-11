'''
Bir fonksiyon yazalım bu fonksiyon bir metindeki boş karakletleri _ ile değiştirsin.
'''

# functions
# str.replace()

def replace_whitespace(text):
    return text.replace(' ', '')

print(replace_whitespace('He ll o     World'))
# Output: HelloWorld