"""
Funções (def) em Python - return - Aula 16 (Parte 2)
"""
def funcao(var):
    return var  # Última linha a ser executada.
    print('Isso nunca será executado.')

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor')