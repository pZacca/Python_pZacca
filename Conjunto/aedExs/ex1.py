'''
Faça um algoritmo que receba a base e a altura de um retângulo, calcule e mostre o perímetro e a diagonal deste retângulo.
O perímetro de um retângulo de base "b" e altura "h" é: P = 2(b + h) Cada diagonal tem comprimento: D = raiz(b² + h²)
'''
print('Seja bem vindo ao algoritmo do pZacca!\nVocê descobrirá o perímetro e a diagonal do seu querido retângulo.')
un_medida = input('Que tipo de medida você usará?: ') # string apenas por fins estéticos

base = input('Insira a medida da base do retângulo: ')
while not base.isnumeric():
    print('Entrada inválida, tente novamente com número inteiro.\n'
          'Caso seja decimal, tente mudar a unidade de medida.')

    mudarvalid = ['s', 'n']
    mudar_un_medida = input('Deseja mudar de unidade de medida? s ou n:')
    while mudar_un_medida not in mudarvalid:
        print('Entrada inválida, digite somente s para sim e somente n para não.')
        mudar_un_medida = input('Deseja mudar de unidade de medida? s ou n:')
        continue
    if mudar_un_medida == 's':
        un_medida = input('Que tipo de medida você usará?: ')

    base = input('Insira a medida da base do retângulo: ')
    continue

altura = input('Insira a medida da altura do retângulo: ')
while not altura.isnumeric():
    print('Entrada inválida, tente novamente com número inteiro.\n'
          'Caso seja decimal, tente mudar a unidade de medida.')

    mudarvalid = ['s', 'n']
    mudar_un_medida = input('Deseja mudar de unidade de medida? s ou n: ')
    while mudar_un_medida not in mudarvalid:
        print('Entrada inválida, digite somente s para sim e somente n para não.')
        mudar_un_medida = input('Deseja mudar de unidade de medida? s ou n: ')
        continue
    if mudar_un_medida == 's':
        un_medida = input('Que tipo de medida você usará?: ')

    altura = input('Insira a medida da altura do retângulo: ')
    continue



print('legal')