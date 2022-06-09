# リスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)


r = [i for i in t if i % 2 ==0]
print(r)


r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

## 読みにくいので、forがネストするような場合は
## 基本的には上の書き方をする
r = [ i * j for i in t for j in t2]
print(r)
