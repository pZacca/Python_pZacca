"""
While / Else
contadores
acumuladores
"""

# Calcula quantos números pares há até certo número, com exceção do zero.
'''
num = int(input('insira o numero: '))
contador = 1
qtd_par = 0

while contador <= num:
    contador += 1
    if contador % 2 == 0:
        qtd_par += 1
print()
print(f'até {num} (incluindo o {num}) tem {qtd_par} par(es) com exceção do zero.')
'''

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Chegamos no else')

# else só será executado quando o laço for falso, caso
# saia do laço de outra forma, o else não é executado.