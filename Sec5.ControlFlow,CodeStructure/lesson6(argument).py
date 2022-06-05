def menu(entree,drink,dessert):
    print('entree → ',entree)
    print('drink → ',drink)
    print('dessert → ',dessert)

menu('beef','coffee','ice')

# キーワード引数
menu(drink='coffee',dessert='pudding',entree='fish')

# デフォルト引数
def family(father='Ken',mother='Judy'):
    print('father → ',father)
    print('mother → ',mother)

family()
family(father='Cony')

# デフォルト引数の注意点
# ## デフォルト引数にリストやDicを置くとバグにつながるので控える
# def test_func(x, l=[]):
#     l.append(x)
#     return l

# y = [1,2,3]
# r = test_func(100, y)
# print(r)

# r = test_func(100)
# print(r)

# r = test_func(100)
# print(r)

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

