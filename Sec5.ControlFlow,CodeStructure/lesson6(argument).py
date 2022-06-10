def menu(entree,drink,dessert):
    print('entree → ',entree)
    print('drink → ',drink)
    print('dessert → ',dessert)

menu('beef','coffee','ice')
print('###############')
# キーワード引数
menu(drink='coffee',dessert='pudding',entree='fish')
print('###############')
# デフォルト引数
def family(father='Ken',mother='Judy'):
    print('father → ',father)
    print('mother → ',mother)

family()
family(father='Cony')
print('###############')
# デフォルト引数の注意点
# ## デフォルト引数にリストやDicを置くとバグにつながるので控える
def test_func(x, l=[]):
    l.append(x)
    return l

y = [1,2,3]
r = test_func(100, y)
print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)
print('###############')
## 解決策
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(100)
print(r)
print('###############')
#　位置引数のタプル化
def say_something(word,*args):
    print(word)
    for arg in args:
        print(arg)

say_something('Hi','Mike','Nancy')
print('###############')
## あまり使わない
# t = ('Mike','Nancy')
# say_something('Hi!', *t )

# キーワード引数による辞書化
def menu(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)

# menu(entree='beef',drink='wine')

d = {
    'entree': 'beef',
    'drink': 'wine',
    'dessert':'tiramisu'
}
menu(**d)

print('###############')
def menu2(food,*args,**kwargs):
    print(food)
    print(args)
    print(kwargs)

menu2('banana','apple','orange',entree='beef',drink='coffee')
