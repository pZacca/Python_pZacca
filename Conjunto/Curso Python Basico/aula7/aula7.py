nome = 'Pedro Henrique'  # string
idade = 20  # int
altura = 1.75  # float
e_maior = idade >= 18  # bool // Expressão booleana, True = maior de idade // False = Menor de idade
peso = 75
imc = 0

print('Nome: ', nome, '\nIdade: ', idade, '\nAltura: ', altura, '\nÉ maior de idade: ', e_maior)
imc = peso / altura ** 2

# F Strings
print(f'{nome} tem {idade} anos de idade, seu IMC é {imc:.2f}.')
print('{} tem {} anos de idade e seu imc é {:.2f}.'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é {2:.2f}.'.format(nome, idade, imc))
print('{a} tem {b} anos de idade e seu imc é {c:.2f}.'.format(a=nome, b=idade, c=imc))

'''
formatação de f strings
{var:.2f} -> 2 casas após a vírgula
'''

'''
Em uma linguagem de tipagem dinâmica e forte, o próprio interpretador determina o tipo de um valor quando criado.
É possível modificar um valor interpretado de um tipo para outro realizando um "Type Cast" (ou cast) em alguns casos,
mas o interpretador não fará isso por você.
'''
