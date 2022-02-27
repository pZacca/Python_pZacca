
'''
num1 = input('Digite um num: ')
print(type(num1))
if type(num1) != int:
    print('fez merda1')
else:
    num2 = input('Digite um num: ')

if type(num2) != int:
    print('fez merda2')
else:
    soma = num1 + num2
    print(f'A soma de {num1} e {num2} resulta em {soma}')
'''

#  isnumeric
#  isdigit
#  isdecimal

num1 = input('Digite um num: ')
num2 = input('Digite um num: ')

if num1.isdecimal() and num2.isdecimal():
    num1 = int(num1)
    num2 = int(num2)
    soma = num1 + num2
    print(f'O resultado da soma de {num1} e {num2} é: {soma}.')
else:
    print('Você digitou errado.')

#  Solução para validar floats também
#  https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py
