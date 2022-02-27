"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
'''
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
#  print('{:.2f}'.format(divisao))
#  ou
print(f'{divisao:.2f}')
'''
nome1 = ' Pedro Henrique '
print(f'{nome1:-^50}')
nome2 = 'Pedro Henrique'
print(f'{nome2:-^50}')


num1 = 1
print(f'{num1:0>10}')

num2 = 1150
print(f'{num2:0>10.2f}')

#  print(f'{num2:f}')

print(len(nome1))

nome1_form = '{:#^20}'.format(nome1)
print(nome1_form)
