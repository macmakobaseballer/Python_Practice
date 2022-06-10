# whileループ
count = 0

while count < 5 :
  print(count)
  count += 1
print('###############')
count = 0
while True:
  if count >= 5 :
    break
  print(count)
  count += 1
print('###############')
# while else文
count = 0
while count < 5 :
  print(count)
  count += 1
else:
  print('done')
print('###############')
# whileの文中でbreakするとelseの中身は処理されず終了
count = 0
while count < 5 :
  if count == 2 :
    break
  print(count)
  count += 1
else:
  print('done')
print('###############')
# input関数
while True:
  word = input('Enter:')
  num = int(word)
  if num == 10:
    break
  print('next')
