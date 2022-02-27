# DESEMPACOTAMENTO
# Dois métodos que chegam ao mesmo resultado,
# sendo o segundo mais otimizado,
# principalmente para maiores listas.

lista = [
    [0, 'joao'],
    [1, 'maria'],
    [2, 'pedrao']
]

for indice, nome in lista:
    print(indice, nome)


print('\n########\n')


lista = ['joao', 'maria', 'pedrao']

for indice, nome in enumerate(lista):
    print(indice, nome)