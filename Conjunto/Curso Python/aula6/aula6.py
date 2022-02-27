# Variáveis
'''
Iniciar com letra, pode conter números, separar _, letras minúsculas
'''
# Operador de atribuição "="


# Inicialização de variáveis
nome = 'Pedro Henrique'  # string
idade = 20  # int
altura = 1.75  # float
e_maior = idade >= 18  # bool // Expressão booleana, True = maior de idade // False = Menor de idade
peso = 75
imc = 0

print('Nome: ', nome, '\nIdade: ', idade, '\nAltura: ', altura, '\nÉ maior de idade: ', e_maior)

# Cálculo de IMC
# Peso (kg) / Altura*Altura (m)
imc = peso / altura ** 2

print('\nO IMC de', nome, 'é: ', imc, '\n')

print('Abaixo do peso     ->  < 18.5')
print('Peso normal        ->  18.5 - 24.9')
print('Sobrepeso          ->  25 - 29.9')
print('Obesidade Grau I   ->  30 - 34.9')
print('Obesidade Grau II  ->  35 - 39.9')
print('Obesidade Grau III ->  >= 40')




# Python -> Linguagem de tipagem dinâmica

