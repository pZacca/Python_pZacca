"""
Funções (def) em Python - *args **kwargs -
"""

'''
def func(a1, a2, a3, a4, a5, a6=None):  # Com 'None', o a6 deixa de ser obrigatório para a função executar.
    print(a1, a2, a3, a4, a5, a6)
    return a5, a6


var = func(1, 2, 3, 4, 5, a6='oi')
print(var)
print(var[0])
print(var[1])
print(var[0], var[1])
'''

# 'args' é uma convenção
# assim como 'kwargs'
# kwargs = keyword args

def func(*args, **kwargs):
    print(args)
    nome = kwargs.get('nome')
    idade = kwargs.get('idade')
    print(nome, idade)


lista = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
func(*lista, *lista2, nome ='Pedro', idade = 20)


# print(*lista)  # Desempacotamento de lista.
# print(*lista, sep='-')  # Desempacotamento de lista com separador.