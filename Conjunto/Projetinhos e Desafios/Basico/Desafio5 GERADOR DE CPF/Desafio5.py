# Algoritmo gerador de CPFs válidos com fins acadêmicos.
from random import randint

print('\nSeja bem vindo ao gerador de CPF válido!\nO que você pretende fazer com isso..?')

while True:
    while True:
        cpf = str(randint(1, 999999998))  # Gera um número aleatório de nove dígitos, evitando o 0 e o 999999999 pois repetições são inválidas.
        if cpf[0] * 9 == cpf:  # Verificador de sequências repetidas, se for repetido, o número é gerado novamente.
            continue
        else:
            break

    cpf = '{:0>9}'.format(cpf)  # Caso o número tenha um ou mais dígitos começados com 0, o número é formatado para não perder as casas vazias.
    i = 0

    for n, m in enumerate(range(10, 1, -1)):
        i += int(cpf[n]) * m  # Soma o resultado de todas as multiplicações realizadas.

    dig_1 = 0 if 11 - (i%11) > 9 else 11 - (i%11)
    cpf_novo = cpf + str(dig_1)
    i = 0

    for n, m in enumerate(range(11, 1, -1)):
        i += int(cpf_novo[n]) * m  # Usa do novo dígito calculado para calcular o último.

    dig_2 = 0 if 11 - (i%11) > 9 else 11 - (i%11)
    cpf_novo = cpf_novo + str(dig_2)
    print(f'\nCPF válido: {cpf_novo[:3]}.{cpf_novo[3:6]}.{cpf_novo[6:9]}-{cpf_novo[9:11]}\n')
    executar = input('Deseja gerar um novo CPF? [S]im ou [N]ão: ')
    resp_valida = ['s', 'n']

    while executar.lower() not in resp_valida:
        print('Entrada inválida, digite somente s para sim e somente n para não.\n')
        executar = input('Deseja executar novamente? [S]im ou [N]ão: ')
        continue
    if executar.lower() == 's':
        continue
    else:
        print('\nObrigado por usar meu código! pZacca <3')
        break
