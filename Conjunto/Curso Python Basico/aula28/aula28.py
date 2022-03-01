"""
Expresssão condicional com operador OR
"""

# while True:
#     nome = input('Digite seu nome: ')
#
#     if nome:
#         print(nome)
#         break
#     else:
#         print('Você não digitou nada.')
#         continue


# nome = input('Digite seu nome: ')
# print(nome or None or False or 0 or 'Você não digitou nada!' or 'Isso n vai ser impresso pq ja achou um verdadeiro')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Pedro'

variavel = a or b or c or d or e or f or g
print(variavel)

variavel2 = a or b or c or d or e or g or f
print(variavel2)