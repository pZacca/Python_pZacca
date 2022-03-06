"""
Desempacotamento de listas em Python
"""

lista = ['Alan', 'Curie', 'Tesla', 213, 123.2, 'ss']

primeiro_lista, segundo_lista, *_ = lista  # o asterisco '*' na declaração de uma variável
#                                                    aparentemente cria como uma lista_de_lista

print(_)  # -> ['Tesla', 213, 123.2, 'ss']
# _ significa para os devs que será um resto de lista_de_lista não usado

"""
primeiro_lista, segundo_lista, *resto_pro_fim_lista
primeiro_lista, *resto_lista, ultimo_lista
*resto_lista, penultimo_lista, ultimo_lista
"""

