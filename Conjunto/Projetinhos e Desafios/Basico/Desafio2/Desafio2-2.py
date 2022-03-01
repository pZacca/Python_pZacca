"""
2.2) Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite as horas (0-23) para receber a devida saudação: ')

if hora.isdigit():
    hora = int(hora)
    if 11 >= hora:
        #  Não validei valores menores que 0 por não haver necessidade, .isdigit já descarta valores negativos
        print('Bom dia!')
    elif 17 >= hora:
        print('Boa tarde!')
    elif 23 >= hora:
        print('Boa noite!')
    else:
        print('Digite um horário entre 0 e 23')
else:
    print('Digite um horário válido.')
