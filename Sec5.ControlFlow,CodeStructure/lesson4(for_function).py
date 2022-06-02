# range関数
for i in range(2,10,3):
    print(i)
## inedexの番号は使わないということが明示的にわかる
for _ in range(10):
    print('hello')


# enumerate関数
i = 0
for i, fruits in enumerate(['apple','banana','orange']):
    print(i,fruits)


# zip関数
days = ['Mon','Tue','Wed']
fruits = ['apple','banana','orange']
drinks = ['coffee','tea','beer']

## rangeで表記すると
# for i in range (len(days)):
#     print(days[i],fruits[i],drinks[i])

for day, fruit, drink in zip(days,fruits,drinks):
    print(day,fruit,drink)

# 辞書型の出力
d = {'x': 100, 'y': 200}

print(d.items())
for k,v in d.items():
    print(k,':',v)
