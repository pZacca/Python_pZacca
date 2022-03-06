'''
1) Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne
o valor da funcao2 executada.
'''


def funcao2():
    var = 'show'
    return var


def mestre(arg):
    return arg()


executando = mestre(funcao1)
print(executando)
