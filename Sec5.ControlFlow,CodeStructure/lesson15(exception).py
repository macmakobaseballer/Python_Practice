# 例外処理
from sympy import pde_separate_add


l = [1, 2, 3]
i = 5

# del[l]

try:
    l[0]
except IndexError as ex:
    print("IndexError:{}".format(ex))
except NameError as ex:
    print("NameError:{}".format(ex))
## except以外の処理を実行する
else:
    print('Done')
## try except等しても必ず実行する→finally
finally:
    print('clean up')


# 独自例外
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE','orange','banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is error:', exc)
