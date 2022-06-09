# 辞書内包表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'soda', 'coke']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)


# 集合内包表記
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10)}
