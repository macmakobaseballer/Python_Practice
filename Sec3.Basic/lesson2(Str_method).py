# 文字列のメソッド

greet = 'My name is Mako.How are you?'

print(greet)

is_start = greet.startswith('My')
print(is_start)
is_start = greet.startswith('You')
print(is_start)

print(greet.find('Mako'))
print(greet.count('Mako'))
print(greet.capitalize())
print(greet.title())
print(greet.upper())
print(greet.lower())
print(greet.replace('Mako', 'Risa'))

# 文字の代入
print('My name is {0} {1}'.format('Makoto','Yamaguchi'))
print('My name is {first_name} {last_name}'
      .format(first_name='Makoto', last_name='Yamaguchi'))

first_name = 'Makoto'
last_name= 'Yamaguchi'
print(f'My name is {first_name} {last_name}.' )
