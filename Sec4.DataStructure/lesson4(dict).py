# 辞書型
d = {'x': 10, 'y': 20 }
print(type(d))
print(d['x'])
print(d['y'])
d['x'] = 100
print(d)
d['x'] = 'XXXX'
d['z'] = 200
print(d)

d2 = dict( a=10, b=20)
print(d2)


# 辞書型のメソッド
d = {'x': 10, 'y': 20 }

print(d.keys())
print(d.values())
d2 = {'x': 1000, 'z': 500 }
d.update(d2)
print(d)
print(d.get('x'))
print(d.get('j'))

d.pop('x')
print(d)
del d['y']
print(d)
d.clear()
print(d)

d = {'x': 10, 'y': 20 }
print('x' in d )
print('a' in d )

# 辞書型は参照渡し
print('*****x=yとした場合*****')
x = {'a': 1}
y = x
y['a'] = 1000
print(id(x))
print(id(y))
print('x→',x )
print('y→',y)

print('*****x.copyとした場合*****')
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(id(x))
print(id(y))
print('x→',x )
print('y→',y)
