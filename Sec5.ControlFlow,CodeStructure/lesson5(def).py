import math

# 関数定義
def say_something():
    print('hi')

say_something()
f = say_something
f()
print(type(f))
print('###############')
# 戻り値
def calc_tax():
    price = 100
    tax_rate = 1.1
    total_price = math.floor(price * tax_rate)
    return total_price

result = calc_tax()
print(result)
print('###############')
# 引数
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'yellow':
        return 'banana'
    else:
        return "Don't exist"

result = what_is_this('yellow')
result = what_is_this('green')
print(result)
