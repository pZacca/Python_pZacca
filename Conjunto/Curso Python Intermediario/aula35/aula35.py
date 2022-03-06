'''
Dicionários
'''
# Lista gera um índice, no dicionário VOCÊ gera o índice (chamado chave).
# Dicionário é uma estrutura de dados que suporta um par de chave ("índice") e valor.
d1 = {
    'um' : 'Primeiro valor',  # Só valores imutáveis podem ser chave
    'dois' : 'Segundo valor',
    'tres' : 'Terceiro valor'
}

for k, v in d1.items():
    print(k, '->', v)

"""
del d1['um']  # Apaga a chave 'um' de d1.
d1.update({'quatro' : 'Quarto valor'})  # Insere a chave 'quatro' em d1.
d1['cinco'] = 'Quinto valor'  # Insere a chave 'cinco' em d1.
"""

'''
print(d1)
print('um' in d1)  # equivale a -> print('um' in d1.keys())
print('Primeiro valor' in d1.values())
print(len(d1))
'''