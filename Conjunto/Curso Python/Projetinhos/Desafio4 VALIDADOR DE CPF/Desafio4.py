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


'''
# Método realizado pelo professor. Mais linhas, porém mais leveza no código.
print('Seja bem-vindo ao validador de CPF! Será que o seu é válido mesmo?\n')

while True:
    while True:
        cpf = input('Insira seu CPF (apenas números): ')
        
        if not cpf.isnumeric():
            print('Favor digitar apenas números.\n')
            continue
        elif not len(cpf) == 11:
            print('O CPF deve conter 11 dígitos.\n')
            continue
        else:
            break           
            
    novocpf = cpf[:-2]
    reverso = 10
    total = 0
    
    for index in range(19):
        if index > 8:
            index -= 9
            
        total += int(novocpf[index]) * reverso
        reverso -= 1
        
        if reverso < 2:
            reverso = 11
            d = 11 - (total%11)
            
            if d > 9:
                d = 0
                
            total = 0
            novocpf += str(d)
            
    if cpf == novocpf:
        print('Seu CPF é valido!')
        break
    else:
        print('Seu CPF não é valido, tente novamente.\n')
        continue
        
'''
