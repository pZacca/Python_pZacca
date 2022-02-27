while True:
    print()
    num_1 = input('Digite um numero: ')
    operador = input('Digite o operador: ')
    num_2 = input('Digite outro numero: ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Valor inválido')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)
    # + - / * ^
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '^':
        print(num_1 ** num_2)
    else:
        print('Digite um operador válido')
