# for文
num_list = [ 1, 2, 3, 4, 5]

# whileの場合
i=0
while i < len(num_list):
    print(num_list[i])
    i += 1

# forループでの表記
for i in num_list:
    print(i)

for s in 'abcde':
    print(s)

# continue文
for fruits in ['apple','orange','banana','grape']:
    if fruits == 'banana':
        continue
    print(fruits)

# for else文
for fruits in ['apple','orange','banana','grape']:
    print(fruits)
else:
    print('I ate all!!')
