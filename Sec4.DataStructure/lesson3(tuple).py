# タプル
t = (1,2,3,4,1,2)
#print(help(tuple))
print('############')
t = ([1,2,3,4],[1,2,3,4])
#t[0] = 100
t[0][0] = 100
print(t)
print('############')
t = 1, 2, 3, 4
print(type(t))
t = 1,
print(type(t))
t = (1)
print(type(t))
t = ('test')
print(type(t))
print('############')
tuple_add = ( 1, 2, 3) + ( 4, 5, 6)
print(tuple_add)
print('############')
# タプルのアンパッキング
num_tuple = ( 10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)
print('############')
min , max = 0, 100
print(min, max)
max = 1500
print(min, max)
print('############')
i = 10
j = 20
print(i, j)
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

