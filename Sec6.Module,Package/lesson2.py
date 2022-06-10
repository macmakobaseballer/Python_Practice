# import lesson2_package.utils
from lesson2_package.tools import utils
## 階層構造となっているpackageのインポート
from lesson2_package.talk import human
from lesson2_package.talk import animal

# __init__.pyに__all__ = ['human']等を定義すれば可能
# from lesson2_package.talk import *

##　関数からの読み込みは好まれていない
## from lesson2_package.utils import say_twice

r = utils.say_twice('hello')

## 関数からの読み込みは好まれていない
## r = say_twice('hello')
print(r)

print(animal.sing())
print(animal.cry())


print(human.sing())
print(human.cry())

