# Esse código valida um CPF.
# Caso seja inválido, o código
# pede para tentar novamente.
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
        elif cpf[0]*9 == cpf[:9]:
            print('Seu CPF não é válido, tente novamente.')
            continue
        else:
            break

    i = 0

    for n, m in enumerate(range(10, 1, -1)):
        i += int(cpf[n]) * m  # Soma o resultado de todas as multiplicações realizadas.

    dig_1 = 0 if 11 - (i%11) > 9 else 11 - (i%11)
    cpf_novo = cpf[:9] + str(dig_1)
    i = 0

    for n, m in enumerate(range(11, 1, -1)):
        i += int(cpf_novo[n]) * m  # Usa do novo dígito calculado para descobrir o último.

    dig_2 = 0 if 11 - (i%11) > 9 else 11 - (i%11)
    cpf_novo = cpf_novo + str(dig_2)

    if not cpf_novo == cpf:  # Verificador de validade do CPF. Se válido, fim, se não, recomeça.
        print('Seu CPF não é valido, tente novamente.\n')
        continue
    else:
        print('Seu CPF é valido!')
        break
