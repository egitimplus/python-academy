'''
Bir fonksiyon yazalım bu fonksiyon eğer argüman olarak gönderilen kelime
tersten de aynı şekilde ise True değilse False döndürsün. 
'''

# functions
# if condition
# relational operators
# boolean keywords

def palindrome(word):
    if word == word[::-1]:
        return True

    return False

print(palindrome('kabak'))
# Output: True