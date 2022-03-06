"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista_de_lista # str
* Enumerate - Enumerar elementos da lista_de_lista # iteráveis
"""
string = "O Brasil Brasil é o o o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

# lista_1 == ['O', 'Brasil', 'Brasil', 'é', 'o', 'país', 'do', 'futebol,', 'o', 'Brasil', 'é', 'penta.']
# lista_2 == ['O Brasil Brasil é o o o país do futebol', ' o Brasil é penta.']

palavra = ''
contagem = 0

for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'"{palavra}" é a palavra que apareceu mais vezes, foram {contagem}x.')
