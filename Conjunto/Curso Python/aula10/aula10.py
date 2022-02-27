'''
Operadores Relacionais
==  Igual
>   Maior que
>=  Maior ou igual a
<   Menor que
<=  Menor ou igual a
!=  Diferente de
'''
'''
num1 = 2
num2 = 2

expbool = num1 != num2

print(expbool)
'''

'''
print('Avaliador de permissão para comprar bebida.')
legalidade = 18
idade = int(input('Qual sua idade? '))
nome = input('Qual seu nome? ')
if idade>=legalidade:
    print(f'{nome}, você pode comprar bebida!')
else:
    print(f'{nome}, você não pode comprar bebida.')
'''


idade_menor = 20 #  muito jovem
idade_maior = 30 #  passou da idade

idade = int(input('Qual sua idade? '))
nome = input('Qual seu nome? ')
if idade<idade_menor:
    print(f'{nome}, você é muito jovem para o empréstimo.')
elif idade>idade_maior:
    print(f'{nome}, você passou da idade para o empréstimo.')
else:
    print(f'{nome}, você está qualificado para o empréstimo!')
