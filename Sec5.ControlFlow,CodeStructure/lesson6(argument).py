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
