# リストの操作メソッド
n = [1,2,3,4,5,6,7,8,9,10]
print(n)
n.append(11)
print(n)
n.insert(0,0)
print(n)
n.pop()
print(n)
n.pop(0)
print(n)
del n[0]
print(n)
del n
n = [ 1, 2, 2, 2, 3]
print(n)
n.remove(2)
print(n)
n.remove(2)
n.remove(2)
print(n)

a = [ 1, 2, 3, 4, 5]
b = [ 6, 7, 8, 9, 10]
print(a,b)
x = a + b
print(x)
a += b
print(a)
x = [ 1, 2, 3, 4, 5]
y = [ 6, 7, 8, 9, 10]
x.extend(y)


r = [ 1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3 ,3 ))

print(r.count(3))

if 5 in r:
  print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)


s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

# print(help(list))
