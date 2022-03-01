"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

'''
i = 0
for n in range(0, 10, 2):
    i += 1
    print(n)
print(f'foram {i} exec')
'''

'''
for n in range(100):
    if n % 8 == 0:
        print(n)
'''

'''
Propriedade matemática:
for n in range(0, 100, 8):
identifica os múltiplos de 8 até 100
'''


texto = 'Python'
nova_string = ''

# continue -> pula para o próximo laço
# break    -> termina o laço

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)