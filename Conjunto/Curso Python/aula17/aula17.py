"""
while em Python
utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos: entender condições e operadores
"""
"""

while True:  #loop infinito
    ...
    
"""

"""
i = 0
while i < 10:
    if i == 3:
        i += 1
        continue
#  como tirar uma execução de um laço
#  break <- PARA um laço quando encontrado
    print(f'foi {i} vez')
    i += 1
print('over')
"""

# Nota do estudante:
# Se por um acaso alguém estiver a ler esse código ou os demais postados,
# saibam que notei somente agora que cometia um erro de norma do
# Python, dava dois espaços a partir da cerquilha, não dois espaços antes
# da cerquilha xD peço perdão.

i = 0
x = 0  # coluna
while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'{x}, {y}, {i}')
        y += 1
        i += 1

    x += 1  # x = x + 1


print('x, y, nº de exec.')
print(f'Total de execuções: {i}')
