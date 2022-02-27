"""
2.1) Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#  Nota do dev:
#  Entendo que números negativos inteiros são dados como falsos,
#  porém,a proposta do exercício não pede a inclusão dos mesmos.

num = input('Digite um número inteiro para saber se é par ou impar: ')

if num.isdigit():
    num = int(num)

    if num % 2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é ímpar')
else:
    print('Número não inteiro.')
