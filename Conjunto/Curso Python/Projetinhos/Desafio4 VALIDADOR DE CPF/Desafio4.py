"""
CPF = 168.995.350-90
---------------------------------
1 * 10 = 10           #    1 * 11 = 11
6 * 9 = 54            #    6 * 10 = 60
8 * 8 = 64            #    8 *  9 = 72
9 * 7 = 63            #    9 *  8 = 72
9 * 6 = 54            #    9 *  7 = 63
5 * 5 = 25            #    5 *  6 = 30
3 * 4 = 12            #    3 *  5 = 15
5 * 3 = 15            #    5 *  4 = 20
0 * 2 = 0             #    0 *  3 = 0
                      # -> 0 *  2 = 0
        297           #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

print('Seja bem-vindo ao validador de CPF! Será que o seu é válido mesmo?\n')
while True:
    while True:  # Validando as entradas para verificar se o CPF contém exatos 11 e apenas dígitos.
        cpf = input('Insira seu CPF (apenas números): ')
        if not cpf.isnumeric():
            print('Favor digitar apenas números.\n')
            continue
        elif not len(cpf) == 11:
            print('O CPF deve conter 11 dígitos.\n')
            continue
        else:
            break

    i = 0
    for n, m in enumerate(range(10, 1, -1)):
        i += int(cpf[n])*m

    dig_1 = 0 if 11-(i%11)>9 else 11-(i%11)
    cpfnovo = cpf[0:9] + str(dig_1)

    i = 0
    for n, m in enumerate(range(11, 1, -1)):
        i += int(cpfnovo[n]) * m

    dig_2 = 0 if 11-(i%11)>9 else 11-(i%11)
    cpfnovo = cpfnovo + str(dig_2)

    if not cpfnovo == cpf:
        print('Seu CPF não é valido, tente novamente.\n')
        continue
    else:
        print('Seu CPF é valido!')
        break
