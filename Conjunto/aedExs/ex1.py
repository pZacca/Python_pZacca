'''
Faça um algoritmo que receba a base e a altura de um retângulo, calcule e mostre o perímetro e a diagonal deste retângulo.
O perímetro de um retângulo de base "b" e altura "h" é: P = 2(b + h) Cada diagonal tem comprimento: D = raiz(b² + h²)
'''
executar = True

while executar:
    print('\nSeja bem vindo ao algoritmo E1L do pZacca!\nVocê descobrirá o perímetro e a diagonal do seu querido '
          'retângulo.')
    un_medida = input('\nQue tipo de medida você usará?: ') # string apenas por fins estéticos

    base = input('Insira a medida da base do retângulo: ')
    while not base.isnumeric():
        print('Entrada inválida, tente novamente com número inteiro.\n'
              'Caso seja decimal, tente mudar a unidade de medida.')

        mudarvalid = ['s', 'n']
        mudar_un_medida = input('Deseja mudar de unidade de medida? s ou n:')
        while mudar_un_medida.lower() not in mudarvalid:
            print('Entrada inválida, digite somente s para sim e somente n para não.')
            mudar_un_medida = input('Deseja mudar de unidade de medida? s ou n:')
            continue
        if mudar_un_medida.lower() == 's':
            un_medida = input('Que tipo de medida você usará?: ')

        base = input('Insira a medida da base do retângulo: ')
        continue
    base = int(base)

    altura = input('Insira a medida da altura do retângulo: ')
    while not altura.isnumeric():
        print('Entrada inválida, tente novamente com número inteiro.\n'
              'Caso seja decimal, tente mudar a unidade de medida.')

        mudarvalid = ['s', 'n']
        mudar_un_medida = input('Deseja mudar de unidade de medida? s ou n: ')
        while mudar_un_medida.lower() not in mudarvalid:
            print('Entrada inválida, digite somente s para sim e somente n para não.')
            mudar_un_medida = input('Deseja mudar de unidade de medida? s ou n: ')
            continue

        if mudar_un_medida.lower() == 's':
            un_medida = input('Que tipo de medida você usará?: ')

        altura = input('Insira a medida da altura do retângulo: ')
        continue
    altura = int(altura)

    perimetro = (base + altura) * 2
    diagonal = (base**2 + altura**2)**0.5

    print(f'\nBase: {base}{un_medida}\n'
          f'Altura: {altura}{un_medida}\n'
          f'Perimetro: {perimetro:.2f}{un_medida}\n'
          f'Diagonal: {diagonal:.2f}{un_medida}\n')

    executar = input('Deseja executar novamente? s ou n: ')
    mudarvalid = ['s', 'n']
    while executar.lower() not in mudarvalid:
        print('Entrada inválida, digite somente s para sim e somente n para não.')
        executar = input('Deseja executar novamente? s ou n: ')
        continue
    if executar.lower() == 's':
        continue
    elif executar.lower() == 'n':
        print('\nObrigado por usar meu código! pZacca <3')
        break
    else:
        safe = input('Não era pra isso aq tá acontecendo irmão...')
