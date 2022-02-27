# Caro leitor do meu humilde código, até a linha 28 são apenas anotações da aula,
# desconsidere-as para análise do restante do código. Obrigado =]

"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#           0    1    2    3    4
# lista = ['A', 'B', 'C', 'D', 'E']
#          -5   -4   -3   -2   -1

'''
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# lista[0:5] = 'Qualquer outra coisa.'

print(lista[::-1])
'''

'''
l2 = ['String', True, 10, -20.5]

for elem in l2:
    print(f'O tipo de {elem} é {type(elem)}')
'''

secreto = 'perfume'
digitadas = []
chances = 5

print('Sejas bem-vindo ao descubra a palavra! Tens 5 chances, boa sorte.')
while True:

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue


    if letra in secreto:
        print(f'\nTas a chegar perto, não, gajo? "{letra}" está contido na palavra secreta.')
        digitadas.append(letra)
    else:
        chances -= 1
        if chances == 0:
            print('Que pena, suas chances acabaram. Você perdeu.')
            break
        print(f'\nNah gajo, "{letra}" não está contido na palavra secreta. Restam-te {chances} tentativas!')

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns, puto! Descobriste a palavra secreta! Como sabias que era {secreto_temporario}?')
        break
    else:
        print(f'Ora pois, continue tentando para descobrir os asteríscos de {secreto_temporario}\n')
