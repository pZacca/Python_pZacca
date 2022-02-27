"""
For / Else em Python
"""
# .startswith
# .lower().startswith('')

variavel = ['Pedro Henrique', ' Joãozinho', 'Maria']

for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        print('Existe uma palavra que começa com J.')
        break
else:
    print('Não exite uma palavra que começa com J.')
