# 集合型
a = { 1, 1, 2 ,2, 3, 3, 3, 4, 6, 6, 6, 7}
print(a)

b = { 1, 2, 2, 3, 3, 5}
print(b)
print(a-b)
print(b-a)
print(a&b)
print(a|b)
print(a^b)
print('###############')
# 集合のメソッド
s = { 1, 2, 3, 4, 5}
# s[0] エラー
s.add(6)
print(s)
s.remove(6)
print(s)
s.clear()
print(s)
print('###############')
#　集合の使い所
my_friends = { 'a', 'c', 'd', 'f' }
A_friends = { 'e' , 'f', 'g' }

print(my_friends & A_friends)

fruits = ['apple','orange','banana','banana','orange']
kind = set(fruits)
print(kind)
