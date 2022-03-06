'''
2) Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o valor da funcao2
executada. Faça a funcao1 executar duas funções que recebam um número diferente de argumentos.
'''
def f_mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def funcao2(idade):
    return f'Você tem {idade} anos.'


def funcao3(nome, sobrenome):
    return f'Bom dia, {nome} {sobrenome}!'


executando = f_mestre(funcao2, idade=20)
executando2 = f_mestre(funcao3, 'Pedro', sobrenome='Zaccaria')
print(executando)
print(executando2)
