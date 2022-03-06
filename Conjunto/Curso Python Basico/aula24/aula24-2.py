# enumerate == enumera cada iteração do for
# desempacotamento == extrair valores dentro de uma lista_de_lista

lista1 = [
    ['joao', 'maria', 'pedrao'],  # 0
    ['enzo', 'valentina', 'valentim'],  # 1
    ['cristiano', 'marta', 'puskas']  # 2
]

# Imprime tuplas
# for v1 in enumerate(lista1):
#     print(v1)

# Imprime o desempacotamento
# for v1, v2 in enumerate(lista1):
#     print(v1, v2)

# Desempacota com variáveis e imprime os dois valores
# for v1 in enumerate(lista1):
#     valor_enumerado, minha_lista = v1
#     print(valor_enumerado, minha_lista)

# Desempacota com variáveis e imprime a lista_de_lista sem os índices
# for v1 in enumerate(lista1):
#     valor_enumerado, minha_lista = v1
#     print(minha_lista)

for v1 in enumerate(lista1):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista  # desempacotamento do desempacotamento
    print(nome1, nome3)

'''
enumerada = list(enumerate(lista1))
print(enumerada[0][0])
'''
'''
[
    (0, ['joao', 'maria', 'pedrao']),
    (1, ['enzo', 'valentina', 'valentim']),
    (2, ['cristiano', 'marta', 'puskas'])
]
'''
'''
i = 0
for n in lista1:
    print(lista1[i])
    i += 1
'''