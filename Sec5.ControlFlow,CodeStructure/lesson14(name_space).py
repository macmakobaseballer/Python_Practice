"""
Test test py doc
"""

animal = 'cat'

def f():
    # print(animal)
    animal = 'dog'
    print('local:', animal)

f()
print('global:',animal)

## 関数内でglobal変数を書き換える
def f2():
    """
    Test test func doc
    """
    global animal
    animal= 'dog'
    print('local:',animal)
    print(f2.__doc__)
    print(f2.__name__)
    print('local:',locals())
    

f2()
print('global:', animal)
print('global:',__doc__)
print('global:',__name__)
# print('global:', globals())

