nome = input('digite seu nome: ')
#  nome_formatado = '{:#^20}'.format(nome)
#  ou
#  nome_formatado = f'{nome:#^20}'
#  ou melhor,
nome_formatado = '{n:#^20}'.format(n=nome)
print(nome_formatado)
print(len(nome))
print(len(nome_formatado))

'''
nome = nome.ljust(20, '#')
print(nome)
'''

'''
Observação do estudante:
Ao formatar uma string colocando caracteres para o preenchimento de determinada quantidade de vetores,
percebe-se que ao determinar uma quantidade a mais do que a da string, o caractere que sobra é adicionado
a direita, ao final da string formatada.
'''

print(nome.lower())  #  Tudo maiúsculo
print(nome.upper())  #  Tudo minúsculo
print(nome.title())  #  Primeiras letras maiúsculas (definidas por espaço)

