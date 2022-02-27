'''
Entrada de dados - Aula 3
'''

#  nome = input("Qual o seu nome? ")
#  print(f'O nome do usuário é {nome}, e o tipo de variável que armazena essa informação é {type(nome)}.')

'''
#  No caso, o Luiz fez desta forma
nome = input("Qual o seu nome? ")
print(f'O nome do usuário é {nome}, e o tipo de variável que armazena essa informação é'
      f'{type(nome)}.')
'''

'''
input sempre recebe em string, mesmo que sejam só números
'''
'''
idade = input('Qual sua idade? ')
nome = input("Qual o seu nome? ")
#  print() pula uma linha
idade = int(idade)
print()

print(type(idade))
ano_nasc = 2022 - idade
#  print(f'O usuário se chama {nome}, tem {idade} anos e nasceu em {ano_nasc}.')

#  O professor fez desta forma:
print(f'O usuário se chama {nome}, '
      f'tem {idade} anos e '
      f'nasceu em {ano_nasc}.')
'''

#  Calculadora
'''
num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

num_1 = int(num_1)
num_2 = int(num_2)

result = num_1 + num_2

print(result)
'''

#  Método melhor

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))

result = num_1 + num_2
print(result)