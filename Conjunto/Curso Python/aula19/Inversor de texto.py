# Algoritmo para testar meu conhecimento em iteração de strings
# Função: inverter de trás para frente uma string de n caracteres

inverter = input('Insira a frase a ser invertida: ')
# i -> contador
i = 0
invertido = ''

while i < len(inverter):
    i += 1
    invertido += inverter[-i]

print(f'Frase original: "{inverter}"\nFrase invertida: "{invertido}"')
