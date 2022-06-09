# ラムダ
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def capita_func(word):
#     return word.capitalize()
## lamdaを用いてシンプルに書くと・・・
## capita_func = lambda word: word.capitalize()

## change_words(l, capita_func)
## さらにシンプルに
change_words(l, lambda word: word.capitalize())
print('#####################')
change_words(l, lambda word: word.lower())
