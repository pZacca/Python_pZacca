'''
Tipos de dados

str - string                 -> 'assim' / "assim"
int - inteiro                -> 123456 / -10 / 0 / -15000
float - real/ponto flutuante -> 10.50 / 1.5 / -10.10 / -50.94 / 0.0
bool - booleano/lógico       -> True / False
'''

print('Pedro', type('Pedro'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))
print(bool(''))  # retorna falso, string vazia

# Nome: string
print('Pedro', type('Pedro'))

# Idade: int
print(20, type(20))

# Altura: float
print(1.75, type(1.75))

# É maior de idade 10 > 20
print(20 > 18, type(20 > 18))