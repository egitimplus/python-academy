'''
Bir fonksiyon yazalım bu fonksiyon içerisine gönderilen metinde kaç tane farklı
kelime ve harf olduğunu tespit etsin.
'''  

# function
# len()
# set()
# str.split()
# str.replace()

def count_words_chars(text):
    word_count = len(set(text.split()))
    letter_count = len(set(text.replace(' ', '')))

    return word_count, letter_count

print(count_words_chars('Hello this funcion works!'))
# Output : (4, 16)

# --------------------------------------

'''
Bİr fonksiyon yazalım bu fonksiyon bir cümledeki sesli harfleri bulsun ve
bu harflerin sayıları çarpsın

Benim adım emre ya sen?
2 x 2 x 2 x 1 x 1 = 8

Örneği geliştirelim kelime içerisinde büyük harf varsa çarpmasın
2 x 2 x 1 x 1 = 4
'''

# function
# str.split()
# for loop
# if condition
# artihmetic operators
# relational operators
# membership operators

def multiply_vowels(text):
    vowels = "AaEeIiOoUu"
    words = text.split()

    vowel_multiply = 1
    for word in words:
        vowel_count = 0
        for letter in word:
            if letter in vowels:
                vowel_count += 1
        if vowel_count > 0:
            vowel_multiply *= vowel_count

    return vowel_multiply


print(multiply_vowels('Hello my name is Alexander.'))
# Output: 16