# リストのコピー
i = [ 1, 2, 3, 4, 5]
j = i
# print('i=',i)
# print('j=',j)
j[0] = 100
print('i=',i)
print('j=',j)

print('#########################')
x = [ 1, 2, 3, 4, 5]
y = x.copy()
# y = x[:] ※こっちは分かりにくいかなぁ
# print('x=',x)
# print('y=',y)
x[0] = 100
print('x=',x)
print('y=',y)

print('#########################')
# 値渡しと参照渡し
X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(X)
print(Y)

X = ['a','b']
Y = X
print(id(X))
print(id(Y))
print(X)
print(Y)
